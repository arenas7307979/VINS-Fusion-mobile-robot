import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

plt.figure(figsize=(10, 5))

FB_file=open('/home/cc/output/FB_tracking_time_MH01.txt','r')
FB_timestamps=list()
FB_process_time=list()


of_file=open('/home/cc/output/of_tracking_time_MH01.txt','r')
of_timestamps=list()
of_process_time=list()



#get Foward_Back optical data
for c in FB_file.read().splitlines():

        c_array=c.split(" ")
        FB_timestamps.append(float(c_array[0]))
        FB_process_time.append(float(c_array[1]))

#get original optical flow data
for c in of_file.read().splitlines():
        c_array=c.split(" ")
        of_timestamps.append(float(c_array[0]))
        of_process_time.append(float(c_array[1]))

FB_file.close()
of_file.close()


Frame=np.linspace(1,  len(FB_process_time), num=len(FB_process_time))

print(np.mean(FB_process_time))
print(np.mean(of_process_time))
plt.plot(Frame, FB_process_time, marker="+",label='Forward-backend', linewidth=1)
plt.plot(Frame, of_process_time, marker="+",label='Lucas-Kanade', linewidth=1)

plt.xlim(0, len(FB_process_time))
plt.ylim(0, max(FB_process_time)+20)
plt.xlabel("Frame")
plt.ylabel("Time(ms)")



plt.legend(loc='best')

plt.rcParams['figure.dpi'] = 300 #Resolution
plt.tight_layout()
#plt.grid()  #grid
plt.savefig('Forward_Backend_LK_compare_MH01.png')
plt.show()
