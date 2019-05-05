import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

plt.figure(figsize=(10, 5))

SPVI_scale_error=[0.518,1.211,0.27,0.845,1.223,0.542,0.216,1.565,0.125,0.244,1.442]
ORB_scale_error=[0.316,0.562,0.358,0.622,0.538,0.483,1.088,0.065,0.077,0.458,2.733]
OKVIS_scale_error=[1.372,1.774,0.415,1.076,1.6,0.545,0.438,1.105,0.617,0.734]
names = (u'SPVI-SLAM', u'ORB-SLAM2',u'OKVIS')
bar_width = 0.80
index = np.arange(len(SPVI_scale_error))
#rects1 = plt.bar(index*3-bar_width, SPVI_scale_error, bar_width, color='red', label=names[0])
#rects2 = plt.bar(index*3, ORB_scale_error, bar_width, color='green', label=names[1])
#rects3 = plt.bar(np.arange(len(OKVIS_scale_error))*3+bar_width, OKVIS_scale_error, bar_width, color='blue', label=names[2])

rects1 = plt.bar(index*3-bar_width, SPVI_scale_error, bar_width, label=names[0])
rects2 = plt.bar(index*3, ORB_scale_error, bar_width, label=names[1])
rects3 = plt.bar(np.arange(len(OKVIS_scale_error))*3+bar_width, OKVIS_scale_error, bar_width, label=names[2])


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
plt.ylim(0, 3.5)
plt.tight_layout()
plt.ylabel("Scale error(%)")

add_labels(rects1)
add_labels(rects2)
add_labels(rects3)
plt.legend(loc=1)

plt.rcParams['figure.dpi'] = 300 #Resolution
plt.tight_layout()
#plt.grid()  #grid
plt.savefig('scale_error_histogram.png')
plt.show()
