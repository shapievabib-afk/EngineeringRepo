import matplotlib.pyplot as plt

def plt_voltage_vs_time(time, voltage, max_voltage):
    plt.figure(figsize=(10, 6))
    plt.plot(time, voltage)
    plt.ylabel("Voltage")
    plt.xlabel("Time")

def plot_sampling_period_hist(time):
    old_time = time
    sampling_period = time - old_time
    plt.figure(figsize=(10, 6))
    plt.hist(sampling_period)
    plt.xlim(0, 0.06)
    plt.grid(True)

    plt.show()

    #part if cod that is needed to fix
    
