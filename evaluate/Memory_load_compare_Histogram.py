import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

plt.figure(figsize=(10, 5))

SPVI_memory_load=[21.922,21.755,22.762,22.105,21.580,22.745,21.972,22.285,22.839,22.827,21.434]
ORB_memory_load=[23.476,23.117,22.49,20.695,20.432,20.828,20.225,21.034,21.206,21.199,20.561]
OKVIS_memory_load=[11.032,11.226,11.034,11.103,11.225,11.286,11.634,11.677,11.678,11.814,12.113]
names = (u'SPVI-SLAM', u'ORB-SLAM2',u'OKVIS')
bar_width = 0.80
index = np.arange(len(SPVI_memory_load))
#rects1 = plt.bar(index*3-bar_width, SPVI_memory_load, bar_width, color='red', label=names[0])
#rects2 = plt.bar(index*3, ORB_memory_load, bar_width, color='green', label=names[1])
#rects3 = plt.bar(np.arange(len(OKVIS_memory_load))*3+bar_width, OKVIS_memory_load, bar_width, color='blue', label=names[2])

rects1 = plt.bar(index*3-bar_width, SPVI_memory_load, bar_width, label=names[0])
rects2 = plt.bar(index*3, ORB_memory_load, bar_width, label=names[1])
rects3 = plt.bar(np.arange(len(OKVIS_memory_load))*3+bar_width, OKVIS_memory_load, bar_width, label=names[2])


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
# set range for lengend
plt.ylim(0, 30)
plt.tight_layout()
plt.ylabel("Memory load(%)")

add_labels(rects1)
add_labels(rects2)
add_labels(rects3)
plt.legend(loc=1)

plt.rcParams['figure.dpi'] = 300 #Resolution
plt.tight_layout()
#plt.grid()  #grid
plt.savefig('memory_load_histogram.png')
plt.show()
