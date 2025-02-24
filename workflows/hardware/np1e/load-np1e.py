# Import necessary packages
import numpy as np
import matplotlib.pyplot as plt
import spikeinterface.extractors as se
import probeinterface
import probeinterface.plotting

# Parameters
suffix = 0              # Change to match file names' suffix
plot_num_channels = 10  # Number of channels to plot
ap_gain = 1000          # Change to the ap band gain used
lfp_gain = 50           # Change to the lfp band gain used

# Constants
fs_hz_ap = 30e3
fs_hz_lfp = fs_hz_ap / 12
sample_offset = 512
sample_gain = 1171.875
num_channels = 384

# Load acquisition session data
dt = {'names': ('time', 'acq_clk_hz', 'block_read_sz', 'block_write_sz'),
      'formats': ('datetime64[us]', 'u4', 'u4', 'u4')}
meta = np.genfromtxt(f'/content/drive/MyDrive/np1e/start-time_{suffix}.csv', delimiter=',', dtype=dt, skip_header=1)
print(f'Recording was started at {meta["time"]} GMT')
print(f'Acquisition clock rate was {meta["acq_clk_hz"] / 1e6 } MHz')

# Load Neuropixels 1.0 AP clock data
ap_time = np.fromfile(f'/content/drive/MyDrive/np1e/np1-clock_{suffix}.raw', dtype=np.uint64).astype(np.double) / meta['acq_clk_hz']

# Load and scale Neuropixels 1.0 AP data
gain_to_uV_ap = sample_gain / ap_gain
offset_to_uV_ap = -sample_offset * gain_to_uV_ap
ap_rec = se.read_binary(f'/content/drive/MyDrive/np1e/np1-spike_{suffix}.raw',
                        sampling_frequency=fs_hz_ap,
                        dtype=np.uint16,
                        num_channels=num_channels,
                        gain_to_uV=gain_to_uV_ap,
                        offset_to_uV=offset_to_uV_ap)
ap_scaled = ap_rec.get_traces(return_scaled=True, channel_ids=np.arange(plot_num_channels))

# Load Neuropixels 1.0 LFP clock data. The LFP is sampled every at 1/12th the rate of AP data
lfp_time = ap_time[::12]

# Load and scale Neuropixels 1.0 LFP data
gain_to_uV_lfp = sample_gain / lfp_gain
offset_to_uV_lfp = -sample_offset * gain_to_uV_lfp
lfp_rec = se.read_binary(f'/content/drive/MyDrive/np1e/np1-lfp_{suffix}.raw',
                         sampling_frequency=fs_hz_lfp,
                         dtype=np.uint16,
                         num_channels=num_channels,
                         gain_to_uV=gain_to_uV_lfp,
                         offset_to_uV=offset_to_uV_lfp)
lfp_scaled = lfp_rec.get_traces(return_scaled=True, channel_ids=np.arange(plot_num_channels))

# Load BNO055 data
dt = {'names': ('clock', 'euler', 'quat', 'is_quat_id', 'accel', 'grav', 'temp'),
      'formats': ('u8', '(1,3)f8', '(1,4)f8', '?', '(1,3)f8', '(1,3)f8', 'f8')}
bno055 = np.genfromtxt(f'/content/drive/MyDrive/np1e/bno055_{suffix}.csv', delimiter=',', dtype=dt)

# BNO055 time data
bno055_time = bno055['clock'] / meta['acq_clk_hz']

# Plot time series
fig = plt.figure(figsize=(12, 10))

# Plot scaled Neuropixels 1.0 AP data
plt.subplot(611)
plt.plot(ap_time, ap_scaled)
plt.xlabel('Time (seconds)')
plt.ylabel('µV')
plt.title('AP Band Voltage')

# Plot scaled Neuropixels 1.0 LFP data
plt.subplot(612)
plt.plot(lfp_time, lfp_scaled)
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
plt.show()