import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

plt.figure(figsize=(10, 5))

SPVI_file=open('/home/cc/output/SPVI_time_process/tracking_time_V202.txt','r')
SPVI_timestamps=list()
SPVI_process_time=list()


ORB_file=open('/home/cc/output/ORB_process_time/ORB_perimage_process_time_V202.txt','r')
ORB_timestamps=list()
ORB_process_time=list()


OKVIS_file=open('/home/cc/output/okvis_process_time/OKVIS_process_time_V202.txt','r')
OKVIS_timestamps=list()
OKVIS_process_time=list()
resample_OKVIS_process_time=list()

#get SPVI-SLAM data
for c in SPVI_file.read().splitlines():

        c_array=c.split(" ")
        SPVI_timestamps.append(float(c_array[0]))
        SPVI_process_time.append(float(c_array[1]))

#get ORB-SLAM2 data
for c in ORB_file.read().splitlines():
        c_array=c.split(" ")
        ORB_timestamps.append(float(c_array[0]))
        ORB_process_time.append(float(c_array[1]))

#get OKVIS data
for c in OKVIS_file.read().splitlines():
        c_array=c.split(" ")
        OKVIS_timestamps.append(float(c_array[0]))
#       OKVIS_process_time.append(min(float(c_array[1]),450))
#        if float(c_array[1]) >500.0:
#           OKVIS_process_time.append(float(c_array[1])/2.0)
#        else:
        OKVIS_process_time.append(float(c_array[1]))
#print(SPVI_process_time)


SPVI_file.close()
ORB_file.close()
OKVIS_file.close()

#print(SPVI_timestamps,SPVI_process_time)

#time=np.linspace(0.05,  (len(SPVI_process_time))/20.0, num=len(SPVI_process_time))
Frame=np.linspace(1,  len(SPVI_process_time), num=len(SPVI_process_time))

plt.plot(Frame, ORB_process_time, marker="+",label='ORB-SLAM2', linewidth=1)
plt.plot(Frame, OKVIS_process_time,marker="+", label='OKVIS', linewidth=1)
plt.plot(Frame, SPVI_process_time, marker="+",label='SPVI-SLAM', linewidth=1)

plt.xlim(0, len(SPVI_process_time))
#plt.ylim(0, max(ORB_timestamps)*2)
plt.ylim(0, max(OKVIS_process_time)+20)
plt.xlabel("Frame")
plt.ylabel("Time(ms)")



plt.legend(loc='best')

plt.rcParams['figure.dpi'] = 300 #Resolution
plt.tight_layout()
#plt.grid()  #grid
plt.savefig('process_time_compare_V202.png')
plt.show()
