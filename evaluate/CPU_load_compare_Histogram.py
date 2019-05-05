import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

plt.figure(figsize=(10, 5))

SPVI_CPU_load=[43.225,44.140,42.873,41.476,41.934,40.070,37.925,35.003,40.291,40.360,38.791]
ORB_CPU_load=[25.142,23.77,22.224,21.324,20.923,23.028,22.873,25.892,13.432,17.273,14.725]
OKVIS_CPU_load=[47.323,45.144,49.013,48.446,45.744,40.668,44.583,63.324,49.672,52.926,56.748]
names = (u'SPVI-SLAM', u'ORB-SLAM2',u'OKVIS')
bar_width = 0.80
index = np.arange(len(SPVI_CPU_load))
#rects1 = plt.bar(index*3-bar_width, SPVI_CPU_load, bar_width, color='red', label=names[0])
#rects2 = plt.bar(index*3, ORB_CPU_load, bar_width, color='green', label=names[1])
#rects3 = plt.bar(np.arange(len(OKVIS_CPU_load))*3+bar_width, OKVIS_CPU_load, bar_width, color='blue', label=names[2])

rects1 = plt.bar(index*3-bar_width, SPVI_CPU_load, bar_width, label=names[0])
rects2 = plt.bar(index*3, ORB_CPU_load, bar_width, label=names[1])
rects3 = plt.bar(np.arange(len(OKVIS_CPU_load))*3+bar_width, OKVIS_CPU_load, bar_width, label=names[2])


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
plt.ylim(0, 70)
plt.tight_layout()
plt.ylabel("CPU load(%)")




add_labels(rects1)
add_labels(rects2)
add_labels(rects3)
plt.legend(loc=1)

plt.rcParams['figure.dpi'] = 300 #Resolution
plt.tight_layout()
#plt.grid()  #grid
plt.savefig('CPU_load_histogram.png')
plt.show()
