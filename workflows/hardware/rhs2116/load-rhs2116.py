# Import necessary packages
import numpy as np
import matplotlib.pyplot as plt

# Parameters
suffix = 0              # Change to match file names' suffix
plot_num_channels = 10  # Number of channels to plot

# Constants
ac_uV_multiplier = 0.195
ac_offset = 32768
dc_uV_multiplier = -19.23
dc_offset = 512
num_channels = 32

# Load acquisition session data
dt = {'names': ('time', 'acq_clk_hz', 'block_read_sz', 'block_write_sz'),
      'formats': ('datetime64[us]', 'u4', 'u4', 'u4')}
meta = np.genfromtxt(f'/content/drive/MyDrive/rhs2116/start-time_{suffix}.csv', delimiter=',', dtype=dt, skip_header=1)
print(f"Recording was started at {meta['time']} GMT")
print(f'Acquisition clock rate was {meta["acq_clk_hz"] / 1e6 } MHz')

# Load RHS2116 clock data
time = np.fromfile(f'/content/drive/MyDrive/rhs2116/rhs2116-clock_{suffix}.raw', dtype=np.uint64) / meta['acq_clk_hz']

# Load and scale RHS2116 ac data
ac = np.reshape(np.fromfile(f'/content/drive/MyDrive/rhs2116/rhs2116-ac_{suffix}.raw', dtype=np.uint16), (-1, num_channels))
ac_scaled = (ac.astype(np.float32) - ac_offset) * ac_uV_multiplier

# Load and scale RHS2116 dc data
dc = np.reshape(np.fromfile(f'/content/drive/MyDrive/rhs2116/rhs2116-dc_{suffix}.raw', dtype=np.uint16), (-1, num_channels))
dc_scaled = (dc.astype(np.float32) - dc_offset) * dc_uV_multiplier

# Plot time series
fig = plt.figure()

# Plot RHS2116 AC data
plt.subplot(211)
plt.plot(time, ac_scaled[:,0:plot_num_channels])
plt.xlabel('Time (seconds)')
plt.ylabel('Voltage (µV)')
plt.title('RHS2116 AC Data')

# Plot RHS2116 DC data
plt.subplot(212)
plt.plot(time, dc_scaled[:,0:plot_num_channels])
plt.xlabel('Time (seconds)')
plt.ylabel('Voltage (µV)')
plt.title('RHS2116 DC Data')

plt.tight_layout()
plt.show()