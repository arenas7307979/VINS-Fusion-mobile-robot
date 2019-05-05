import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

plt.figure(figsize=(10, 5))

SPVI_running_frequency=[36.72,36.825,35.762,36.461,35.951,34.72,34.355,36.315,34.594,34.631,40.439]
ORB_running_frequency=[12.438,6.545,7.74,15.586,8.795,10.441,8.579,9.447,11.107,9.131,12.01]
OKVIS_running_frequency=[23.846,20.828,20,20,21.509,23.802,16.296,21.584,22.306,20.105,21.425]
names = (u'SPVI-SLAM', u'ORB-SLAM2',u'OKVIS')
bar_width = 0.80
index = np.arange(len(SPVI_running_frequency))
#rects1 = plt.bar(index*3-bar_width, SPVI_running_frequency, bar_width, color='red', label=names[0])
#rects2 = plt.bar(index*3, ORB_running_frequency, bar_width, color='green', label=names[1])
#rects3 = plt.bar(np.arange(len(OKVIS_running_frequency))*3+bar_width, OKVIS_running_frequency, bar_width, color='blue', label=names[2])

rects1 = plt.bar(index*3-bar_width, SPVI_running_frequency, bar_width, label=names[0])
rects2 = plt.bar(index*3, ORB_running_frequency, bar_width, label=names[1])
rects3 = plt.bar(np.arange(len(OKVIS_running_frequency))*3+bar_width, OKVIS_running_frequency, bar_width, label=names[2])


# add data lable
def add_labels(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()+ rect.get_width() / 2, height, height, ha='center', fontsize=5, va='bottom')
        # histogram use white color to full edge
        rect.set_edgecolor('white')



ticks = ['MH_01', 'MH_02', 'MH_03','MH_04', 'MH_05','V1_01','V1_02', 'V1_03','V2_01','V2_02', 'V2_03']

plt.xticks(xrange(0, len(ticks) * 3, 3), ticks)
plt.xlim(-3, len(ticks)*3)
plt.ylim(0, 50)
plt.tight_layout()
plt.ylabel("Running frequency(Hz)")

add_labels(rects1)
add_labels(rects2)
add_labels(rects3)
plt.legend(loc=1)

plt.rcParams['figure.dpi'] = 300 #Resolution
plt.tight_layout()
#plt.grid()  #grid
plt.savefig('running_frequency_histogram.png')
plt.show()
