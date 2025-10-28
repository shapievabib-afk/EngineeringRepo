import matplotlib.pyplot as plt

def plt_voltage_vs_time(time, voltage, max_voltage):
    plt.figure(figsize=(10, 6))
    plt.plot(time, voltage)
    plt.xlabel("Voltage")
    plt.ylabel("Time")

    plt.show()

    #part if cod that is needed to fix
    
