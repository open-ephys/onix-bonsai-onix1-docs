# Import necessary packages
import os
import numpy as np
import matplotlib.pyplot as plt
import spikeinterface.extractors as se
import probeinterface
import probeinterface.plotting

# Parameters
suffix = 0                                                 # Change to match file names' suffix
data_directory = 'C:/Users/open-ephys/Documents/data/np2e' # Change to match files' directory
plot_num_channels = 10                                     # Number of channels to plot

# Constants
fs_hz = 30e3
gain_to_uV = 3.05176
offset_to_uV = -2048 * gain_to_uV
num_channels = 384

# Load acquisition session data
dt = {'names': ('time', 'acq_clk_hz', 'block_read_sz', 'block_write_sz'),
      'formats': ('datetime64[us]', 'u4', 'u4', 'u4')}
meta = np.genfromtxt(os.path.join(data_directory, f'start-time_{suffix}.csv'), delimiter=',', dtype=dt, skip_header=1)
print(f'Recording was started at {meta["time"]} GMT')
print(f'Acquisition clock rate was {meta["acq_clk_hz"] / 1e6 } MHz')

# Load Neuropixels 2.0 clock data
rec_time = np.fromfile(os.path.join(data_directory, f'np2-a-clock_{suffix}.raw'), dtype=np.uint64).astype(np.double) / meta['acq_clk_hz']

# Load and scale Neuropixels 2.0 ephys data
rec = se.read_binary(os.path.join(data_directory, f'np2-a-ephys_{suffix}.raw'),
                     sampling_frequency=fs_hz,
                     dtype=np.uint16,
                     num_channels=num_channels,
                     gain_to_uV=gain_to_uV,
                     offset_to_uV=offset_to_uV)
rec_scaled = rec.get_traces(return_scaled=True, channel_ids=np.arange(plot_num_channels))

# Load BNO055 data
dt = {'names': ('clock', 'euler', 'quat', 'is_quat_id', 'accel', 'grav', 'temp'),
      'formats': ('u8', '(1,3)f8', '(1,4)f8', '?', '(1,3)f8', '(1,3)f8', 'f8')}
bno055 = np.genfromtxt(os.path.join(data_directory, f'bno055_{suffix}.csv'), delimiter=',', dtype=dt)

# BNO055 time data
bno055_time = bno055['clock'] / meta['acq_clk_hz']

# Plot time series
fig = plt.figure(figsize=(12, 8))

# Plot scaled Neuropixels 2.0 data
plt.subplot(511)
plt.plot(rec_time, rec_scaled)
plt.xlabel('Time (seconds)')
plt.ylabel('µV')
plt.title('Neuropixels 2.0 Voltage')

# Plot BNO055 data
plt.subplot(512)
plt.plot(bno055_time, bno055['euler'].squeeze())
plt.ylabel('degrees')
plt.title('Euler Angles')
plt.legend(['Yaw', 'Pitch', 'Roll'])

plt.subplot(513)
plt.plot(bno055_time, bno055['quat'].squeeze())
plt.xlabel('Time (seconds)')
plt.title('Quaternion')
plt.legend(['X', 'Y', 'Z', 'W'])

plt.subplot(514)
plt.plot(bno055_time, bno055['accel'].squeeze())
plt.xlabel('Time (seconds)')
plt.ylabel('m/s\u00b2')
plt.title('Linear Acceleration')
plt.legend(['X', 'Y', 'Z'])

plt.subplot(515)
plt.plot(bno055_time, bno055['grav'].squeeze())
plt.xlabel('Time (seconds)')
plt.ylabel('m/s\u00b2')
plt.title('Gravity Vector')
plt.legend(['X', 'Y', 'Z'])

fig.tight_layout()

# Load and plot Neuropixels 2.0 probeinterface probe group
np2_config = probeinterface.io.read_probeinterface(os.path.join(data_directory, 'np2-config.json'))
probeinterface.plotting.plot_probegroup(np2_config, show_channel_on_click=True)

plt.show()