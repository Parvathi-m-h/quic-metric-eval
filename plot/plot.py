import matplotlib.pyplot as plt
import csv

#Throughput vs time taken
with open("plotData1gQUIC.csv") as filein:
    reader = csv.reader(filein, skipinitialspace = True)
    throughput, time = zip(*reader)
plt.plot(time, throughput, 'bd-', label = "gQUIC")

with open("plotData1mvfst.csv") as filein:
    reader = csv.reader(filein, skipinitialspace = True)
    throughput, time = zip(*reader)
plt.plot(time, throughput, 'yd-', label = "mvfst")
plt.xlabel('Time taken(seconds)')
plt.ylabel('Throughput(Mbps)')
plt.legend()
plt.ylim(0,80)
plt.show()


#Throughput vs Time taken(with 2% packet loss):
with open("plotData2gQUIC.csv") as filein:
    reader = csv.reader(filein, skipinitialspace = True)
    throughput, time = zip(*reader)
plt.plot(time, throughput, 'pink',label = "gQUIC")

with open("plotData2mvfst.csv") as filein:
    reader = csv.reader(filein, skipinitialspace = True)
    throughput, time = zip(*reader)
plt.plot(time, throughput, 'aqua', label = "mvfst")
plt.xlabel('Time taken(seconds)')
plt.ylabel('Throughput(Mbps)')
plt.legend()
plt.ylim(0,80)
plt.show()

#Latency / Data(Mb) for  gQUIC vs. Mvfst:
with open("plotData3gQUIC.csv") as filein:
    reader = csv.reader(filein, skipinitialspace = True)
    quic, data = zip(*reader)
plt.plot(data, quic, 'blueviolet',label="gQUIC", linewidth='3')

with open("plotData3mvfst.csv") as filein:
    reader = csv.reader(filein, skipinitialspace = True)
    mvfst, data = zip(*reader)
plt.plot(data, mvfst, 'teal', label= "Mvfst", linewidth='3')
plt.xlabel('Data (Mb)')
plt.ylabel('latency (Milliseconds)')
plt.legend()
plt.ylim(0,200)
plt.show()

#Latency / Mb of Data- gQUIC vs. Mvfst with 2% Packet Loss:
with open("plotData4gQUIC.csv") as filein:
    reader = csv.reader(filein, skipinitialspace = True)
    quic, data = zip(*reader)
plt.plot(data, quic, 'darkorange', label="gQUIC", linewidth='3')


with open("plotData4mvfst.csv") as filein:
    reader = csv.reader(filein, skipinitialspace = True)
    mvfst, data = zip(*reader)

plt.plot(data, mvfst, 'palevioletred', label= "Mvfst", linewidth='3')
plt.xlabel('Data (Mb)')
plt.ylabel('Latency with packet loss (Milliseconds)')
plt.legend()
plt.ylim(0,200)
plt.show()

#Latency / Mb of Data- gQUIC vs. Mvfst with 10 ms Network Delay:
with open("plotData5gQUIC.csv") as filein:
    reader = csv.reader(filein, skipinitialspace = True)
    quic, data = zip(*reader)
plt.plot(data, quic,'teal', label="gQUIC", linewidth='3')


with open("plotData5mvfst.csv") as filein:
    reader = csv.reader(filein, skipinitialspace = True)
    mvfst, data = zip(*reader)
plt.plot(data, mvfst,'lime', label= "Mvfst", linewidth='3')
plt.xlabel('Data (Mb)')
plt.ylabel('Latency with network delay (Milliseconds)')
plt.legend()
plt.ylim(0,200)
plt.show()