import numpy as np
import matplotlib.pyplot as plt

# Load data from neuropixels board tutorial workflow
suffix = '4'; # Change to match file names' suffix
np_ap_gain = 1000 # Change to the AP band gain used
np_lfp_gain = 50 # Change to the lfp band gain used

plt.close('all')

#%% Metadata
dt = {'names': ('time', 'acq_clk_hz', 'block_read_sz', 'block_write_sz'),
      'formats': ('datetime64[us]', 'u4', 'u4', 'u4')}
meta = np.genfromtxt('start-time_' + suffix + '.csv', delimiter=',', dtype=dt, skip_header=1)
print(f"Recording was started at {meta['time']} GMT")

#%% Hardware FIFO buffer use
dt = {'names': ('clock', 'bytes', 'percent'),
      'formats': ('u8', 'u4', 'f8')}
memory_use = np.genfromtxt('memory-use_' + suffix + '.csv', delimiter=',', dtype=dt)

plt.figure()
plt.plot(memory_use['clock'] / meta['acq_clk_hz'], memory_use['percent'])
plt.xlabel("time (sec)")
plt.ylabel("FIFO used (%)")


#%% Neuropixels 1.0
start_t = 9.0 # when to start plotting data (seconds)
dur = 1.0 # duration of data to plot
plot_channel_offset_uV = 100 # Vertical offset between each channel in the time series

npx = {}
npx['spike_time'] = np.fromfile('np1-clock_' + suffix + '.raw', dtype=np.uint64) / meta['acq_clk_hz']
npx['spike'] = np.reshape(np.fromfile('np1-spike_' + suffix + '.raw', dtype=np.uint16), (-1, 384))

npx['lfp_time'] = npx['spike_time'][::12] # 12 spike samples per lfp sample
npx['lfp'] = np.reshape(np.fromfile('np1-lfp_' + suffix + '.raw', dtype=np.uint16), (-1, 384))

# Make arrays for plotting
b = np.bitwise_and(npx['spike_time'] >= start_t, npx['spike_time'] < start_t + dur)
spike_time = npx['spike_time'][b]
spike_wave = npx['spike'][b, :].astype(np.double)
b = np.bitwise_and(npx['lfp_time'] >= start_t, npx['lfp_time'] < start_t + dur)
lfp_time = npx['lfp_time'][b]
lfp_wave = npx['lfp'][b, :].astype(np.double)

# Convert to uV and offset each channel by some plot_channel_offset_uV 
ap_uV_per_lsb = 1e6 * 1.2 / 1024 / np_ap_gain
lfp_uV_per_lsb = 1e6 * 1.2 / 1024 / np_lfp_gain
spike_wave = (spike_wave - 512) * ap_uV_per_lsb + np.arange(spike_wave.shape[1])[None, :] * plot_channel_offset_uV
lfp_wave =  (lfp_wave - 512) * lfp_uV_per_lsb + np.arange(lfp_wave.shape[1])[None, :] * plot_channel_offset_uV

plt.figure()
plt.subplot(121)
plt.plot(spike_time, spike_wave, 'k', linewidth=0.25)
plt.tick_params(axis='y', which='both', left=False, right=False, labelleft=False) 
plt.xlabel("time (sec)")
plt.ylabel("channel")
plt.title('Spike Band')

plt.subplot(122)
plt.plot(lfp_time, lfp_wave, 'k', linewidth=0.25)
plt.tick_params(axis='y', which='both', left=False, right=False, labelleft=False) 
plt.xlabel("time (sec)")
plt.ylabel("channel")
plt.title('LFP Band')

#%% Bno055
dt = {'names': ('clock', 'euler', 'quat', 'is_quat_id', 'accel', 'grav', 'temp'),
      'formats': ('u8', '(1,3)f8', '(1,4)f8', '?', '(1,3)f8', '(1,3)f8', 'f8')}
bno055 = np.genfromtxt('bno055_' + suffix + '.csv', delimiter=',', dtype=dt)

bno055_time = bno055['clock'] / meta['acq_clk_hz']

plt.figure()
plt.subplot(231)
plt.plot(bno055_time, bno055['euler'].squeeze())
plt.xlabel("time (sec)")
plt.ylabel("angle (deg.)")
plt.ylim(-185, 365)
plt.legend(['yaw', 'pitch', 'roll'])
plt.title('Euler')

plt.subplot(232)
plt.plot(bno055_time, bno055['quat'].squeeze())
plt.xlabel("time (sec)")
plt.ylim(-1.1, 1.1)
plt.legend(['X', 'Y', 'Z', 'W'])
plt.title('Quaternion')

plt.subplot(233)
plt.plot(bno055_time, bno055['accel'].squeeze())
plt.xlabel("time (sec)")
plt.ylabel("accel. (m/s^2)")
plt.legend(['X', 'Y', 'Z'])
plt.title('Lin. Accel.')

plt.subplot(234)
plt.plot(bno055_time, bno055['grav'].squeeze())
plt.xlabel("time (sec)")
plt.ylabel("accel. (m/s^2)")
plt.legend(['X', 'Y', 'Z'])
plt.title('Gravity Vec.')

plt.subplot(235)
plt.plot(bno055_time, bno055['temp'].squeeze())
plt.xlabel("time (sec)")
plt.ylabel("temp. (deg. C)")
plt.title('Headstage Temp.')
