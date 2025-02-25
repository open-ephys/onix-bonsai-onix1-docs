# Import necessary packages
import os
import numpy as np
import matplotlib.pyplot as plt
import spikeinterface.extractors as se
import probeinterface
import probeinterface.plotting

#%% Set parameters for loading data

suffix = 0                                                 # Change to match filenames' suffix
data_directory = 'C:/Users/open-ephys/Documents/data/np1e' # Change to match files' directory
plot_num_channels = 10                                     # Number of channels to plot
ap_gain = 1000                                             # Change to the ap band gain used
lfp_gain = 50                                              # Change to the lfp band gain used

# Neuropixels 1.0 constants
fs_hz_ap = 30e3
fs_hz_lfp = fs_hz_ap / 12
sample_offset = 512
sample_gain = 1171.875
num_channels = 384

#%%  Load acquisition session data

dt = {'names': ('time', 'acq_clk_hz', 'block_read_sz', 'block_write_sz'),
      'formats': ('datetime64[us]', 'u4', 'u4', 'u4')}
meta = np.genfromtxt(os.path.join(data_directory, f'start-time_{suffix}.csv'), delimiter=',', dtype=dt, skip_header=1)
print(f'Recording was started at {meta["time"]} GMT')
print(f'Acquisition clock rate was {meta["acq_clk_hz"] / 1e6 } MHz')

#%% Load Neuropixels 1.0 probe data

np1 = {}

# Load Neuropixels 1.0 AP clock data and convert clock cycles to seconds
np1['ap_time'] = np.fromfile(os.path.join(data_directory, f'np1-clock_{suffix}.raw'), dtype=np.uint64).astype(np.double) / meta['acq_clk_hz']

# Load and scale Neuropixels 1.0 AP data
gain_to_uV_ap = sample_gain / ap_gain
offset_to_uV_ap = -sample_offset * gain_to_uV_ap
ap_rec = se.read_binary(os.path.join(data_directory, f'np1-spike_{suffix}.raw'),
                        sampling_frequency=fs_hz_ap,
                        dtype=np.uint16,
                        num_channels=num_channels,
                        gain_to_uV=gain_to_uV_ap,
                        offset_to_uV=offset_to_uV_ap)
np1['ap_uV'] = ap_rec.get_traces(return_scaled=True, channel_ids=np.arange(plot_num_channels))

# Load Neuropixels 1.0 LFP clock data. The LFP is sampled every at 1/12th the rate of AP data
np1['lfp_time'] = np1['ap_time'][::12]

# Load and scale Neuropixels 1.0 LFP data
gain_to_uV_lfp = sample_gain / lfp_gain
offset_to_uV_lfp = -sample_offset * gain_to_uV_lfp
lfp_rec = se.read_binary(os.path.join(data_directory, f'np1-lfp_{suffix}.raw'),
                         sampling_frequency=fs_hz_lfp,
                         dtype=np.uint16,
                         num_channels=num_channels,
                         gain_to_uV=gain_to_uV_lfp,
                         offset_to_uV=offset_to_uV_lfp)
np1['lfp_uV'] = lfp_rec.get_traces(return_scaled=True, channel_ids=np.arange(plot_num_channels))

#%% Load BNO055 data

dt = {'names': ('clock', 'euler', 'quat', 'is_quat_id', 'accel', 'grav', 'temp'),
      'formats': ('u8', '(1,3)f8', '(1,4)f8', '?', '(1,3)f8', '(1,3)f8', 'f8')}
bno055 = np.genfromtxt(os.path.join(data_directory, f'bno055_{suffix}.csv'), delimiter=',', dtype=dt)

# Convert clock cycles to seconds
bno055_time = bno055['clock'] / meta['acq_clk_hz']

#%% Plot time series

fig = plt.figure(figsize=(12, 8))

# Plot scaled Neuropixels 1.0 AP data
plt.subplot(611)
plt.plot(np1['ap_time'], np1['ap_uV'])
plt.xlabel('Time (seconds)')
plt.ylabel('µV')
plt.title('AP Band Voltage')

# Plot scaled Neuropixels 1.0 LFP data
plt.subplot(612)
plt.plot(np1['lfp_time'], np1['lfp_uV'])
plt.xlabel('Time (seconds)')
plt.ylabel('µV')
plt.title('LFP Band Voltage')

# Plot BNO055 data
plt.subplot(613)
plt.plot(bno055_time, bno055['euler'].squeeze())
plt.xlabel('Time (seconds)')
plt.ylabel('degrees')
plt.title('Euler Angles')
plt.legend(['Yaw', 'Pitch', 'Roll'])

plt.subplot(614)
plt.plot(bno055_time, bno055['quat'].squeeze())
plt.xlabel('Time (seconds)')
plt.title('Quaternion')
plt.legend(['X', 'Y', 'Z', 'W'])

plt.subplot(615)
plt.plot(bno055_time, bno055['accel'].squeeze())
plt.xlabel('Time (seconds)')
plt.ylabel('m/s\u00b2')
plt.title('Linear Acceleration')
plt.legend(['X', 'Y', 'Z'])

plt.subplot(616)
plt.plot(bno055_time, bno055['grav'].squeeze())
plt.xlabel('Time (seconds)')
plt.ylabel('m/s\u00b2')
plt.title('Gravity Vector')
plt.legend(['X', 'Y', 'Z'])

fig.tight_layout()

#%% Load and plot Neuropixels 1.0 probeinterface probe group

fig = plt.figure(figsize=(3, 8))
fig.add_subplot()
np1_config = probeinterface.io.read_probeinterface(os.path.join(data_directory, f'np1-config.json'))
probeinterface.plotting.plot_probegroup(np1_config, show_channel_on_click=True, ax=fig.axes[0])

plt.show()