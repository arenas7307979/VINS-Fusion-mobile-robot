import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#import seaborn as sns

from evo.tools import file_interface
#load SVPI-SLAM trakectory error data:MH_01, MH_02, MH_03, MH_04, MH_05, V1_01, V1_02, V1_03, V2_01, V2_02, V2_03
SPVI_rpe_MH_01_error = file_interface.load_res_file("/home/cc/output/SPVI_trajectory_190429/rpe_MH_01.zip")
SPVI_rpe_MH_01 = SPVI_rpe_MH_01_error.np_arrays["error_array"]
SPVI_rpe_MH_02_error = file_interface.load_res_file("/home/cc/output/SPVI_trajectory_190429/rpe_MH_02.zip")
SPVI_rpe_MH_02 = SPVI_rpe_MH_02_error.np_arrays["error_array"]
SPVI_rpe_MH_03_error = file_interface.load_res_file("/home/cc/output/SPVI_trajectory_190429/rpe_MH_03.zip")
SPVI_rpe_MH_03 = SPVI_rpe_MH_03_error.np_arrays["error_array"]
SPVI_rpe_MH_04_error = file_interface.load_res_file("/home/cc/output/SPVI_trajectory_190429/rpe_MH_04.zip")
SPVI_rpe_MH_04 = SPVI_rpe_MH_04_error.np_arrays["error_array"]
SPVI_rpe_MH_05_error = file_interface.load_res_file("/home/cc/output/SPVI_trajectory_190429/rpe_MH_05.zip")
SPVI_rpe_MH_05 = SPVI_rpe_MH_05_error.np_arrays["error_array"]
SPVI_rpe_V1_01_error = file_interface.load_res_file("/home/cc/output/SPVI_trajectory_190429/rpe_V1_01.zip")
SPVI_rpe_V1_01 = SPVI_rpe_V1_01_error.np_arrays["error_array"]
SPVI_rpe_V1_02_error = file_interface.load_res_file("/home/cc/output/SPVI_trajectory_190429/rpe_V1_02.zip")
SPVI_rpe_V1_02 = SPVI_rpe_V1_02_error.np_arrays["error_array"]
SPVI_rpe_V1_03_error = file_interface.load_res_file("/home/cc/output/SPVI_trajectory_190429/rpe_V1_03.zip")
SPVI_rpe_V1_03 = SPVI_rpe_V1_03_error.np_arrays["error_array"]
SPVI_rpe_V2_01_error = file_interface.load_res_file("/home/cc/output/SPVI_trajectory_190429/rpe_V2_01.zip")
SPVI_rpe_V2_01 = SPVI_rpe_V2_01_error.np_arrays["error_array"]
SPVI_rpe_V2_02_error = file_interface.load_res_file("/home/cc/output/SPVI_trajectory_190429/rpe_V2_02.zip")
SPVI_rpe_V2_02 = SPVI_rpe_V2_02_error.np_arrays["error_array"]
SPVI_rpe_V2_03_error = file_interface.load_res_file("/home/cc/output/SPVI_trajectory_190429/rpe_V2_03.zip")
SPVI_rpe_V2_03 = SPVI_rpe_V2_03_error.np_arrays["error_array"]

#load ORB-SLAM trakectory error data:MH_01, MH_02, MH_03, MH_04, MH_05, V1_01, V1_02, V1_03, V2_01, V2_02, V2_03
ORB_rpe_MH_01_error = file_interface.load_res_file("/home/cc/output/ORB-SLAM2_trajectory/rpe_MH_01.zip")
ORB_rpe_MH_01 = ORB_rpe_MH_01_error.np_arrays["error_array"]
ORB_rpe_MH_02_error = file_interface.load_res_file("/home/cc/output/ORB-SLAM2_trajectory/rpe_MH_02.zip")
ORB_rpe_MH_02 = ORB_rpe_MH_02_error.np_arrays["error_array"]
ORB_rpe_MH_03_error = file_interface.load_res_file("/home/cc/output/ORB-SLAM2_trajectory/rpe_MH_03.zip")
ORB_rpe_MH_03 = ORB_rpe_MH_03_error.np_arrays["error_array"]
ORB_rpe_MH_04_error = file_interface.load_res_file("/home/cc/output/ORB-SLAM2_trajectory/rpe_MH_04.zip")
ORB_rpe_MH_04 = ORB_rpe_MH_04_error.np_arrays["error_array"]
ORB_rpe_MH_05_error = file_interface.load_res_file("/home/cc/output/ORB-SLAM2_trajectory/rpe_MH_05.zip")
ORB_rpe_MH_05 = ORB_rpe_MH_05_error.np_arrays["error_array"]
ORB_rpe_V1_01_error = file_interface.load_res_file("/home/cc/output/ORB-SLAM2_trajectory/rpe_V1_01.zip")
ORB_rpe_V1_01 = ORB_rpe_V1_01_error.np_arrays["error_array"]
ORB_rpe_V1_02_error = file_interface.load_res_file("/home/cc/output/ORB-SLAM2_trajectory/rpe_V1_02.zip")
ORB_rpe_V1_02 = ORB_rpe_V1_02_error.np_arrays["error_array"]
ORB_rpe_V1_03_error = file_interface.load_res_file("/home/cc/output/ORB-SLAM2_trajectory/rpe_V1_03.zip")
ORB_rpe_V1_03 = ORB_rpe_V1_03_error.np_arrays["error_array"]
ORB_rpe_V2_01_error = file_interface.load_res_file("/home/cc/output/ORB-SLAM2_trajectory/rpe_V2_01.zip")
ORB_rpe_V2_01 = ORB_rpe_V2_01_error.np_arrays["error_array"]
ORB_rpe_V2_02_error = file_interface.load_res_file("/home/cc/output/ORB-SLAM2_trajectory/rpe_V2_02.zip")
ORB_rpe_V2_02 = ORB_rpe_V2_02_error.np_arrays["error_array"]
ORB_rpe_V2_03_error = file_interface.load_res_file("/home/cc/output/ORB-SLAM2_trajectory/rpe_V2_03.zip")
ORB_rpe_V2_03 = ORB_rpe_V2_03_error.np_arrays["error_array"]

#load OKVIS trakectory error data:MH_01, MH_02, MH_03, MH_04, MH_05, V1_01, V1_02, V1_03, V2_01, V2_02. V2_03 (can not get full trajectory)
OKVIS_rpe_MH_01_error = file_interface.load_res_file("/home/cc/output/OKVIS_trajecotry/rpe_MH_01.zip")
OKVIS_rpe_MH_01 = OKVIS_rpe_MH_01_error.np_arrays["error_array"]
OKVIS_rpe_MH_02_error = file_interface.load_res_file("/home/cc/output/OKVIS_trajecotry/rpe_MH_02.zip")
OKVIS_rpe_MH_02 = OKVIS_rpe_MH_02_error.np_arrays["error_array"]
OKVIS_rpe_MH_03_error = file_interface.load_res_file("/home/cc/output/OKVIS_trajecotry/rpe_MH_03.zip")
OKVIS_rpe_MH_03 = OKVIS_rpe_MH_03_error.np_arrays["error_array"]
OKVIS_rpe_MH_04_error = file_interface.load_res_file("/home/cc/output/OKVIS_trajecotry/rpe_MH_04.zip")
OKVIS_rpe_MH_04 = OKVIS_rpe_MH_04_error.np_arrays["error_array"]
OKVIS_rpe_MH_05_error = file_interface.load_res_file("/home/cc/output/OKVIS_trajecotry/rpe_MH_05.zip")
OKVIS_rpe_MH_05 = OKVIS_rpe_MH_05_error.np_arrays["error_array"]
OKVIS_rpe_V1_01_error = file_interface.load_res_file("/home/cc/output/OKVIS_trajecotry/rpe_V1_01.zip")
OKVIS_rpe_V1_01 = OKVIS_rpe_V1_01_error.np_arrays["error_array"]
OKVIS_rpe_V1_02_error = file_interface.load_res_file("/home/cc/output/OKVIS_trajecotry/rpe_V1_02.zip")
OKVIS_rpe_V1_02 = OKVIS_rpe_V1_02_error.np_arrays["error_array"]
OKVIS_rpe_V1_03_error = file_interface.load_res_file("/home/cc/output/OKVIS_trajecotry/rpe_V1_03.zip")
OKVIS_rpe_V1_03 = OKVIS_rpe_V1_03_error.np_arrays["error_array"]
OKVIS_rpe_V2_01_error = file_interface.load_res_file("/home/cc/output/OKVIS_trajecotry/rpe_V2_01.zip")
OKVIS_rpe_V2_01 = OKVIS_rpe_V2_01_error.np_arrays["error_array"]
OKVIS_rpe_V2_02_error = file_interface.load_res_file("/home/cc/output/OKVIS_trajecotry/rpe_V2_02.zip")
OKVIS_rpe_V2_02 = OKVIS_rpe_V2_02_error.np_arrays["error_array"]
#OKVIS_rpe_V2_03_error = file_interface.load_res_file("/home/cc/output/OKVIS_trajecotry/rpe_V2_03.zip")
#OKVIS_rpe_V2_03 = OKVIS_rpe_V2_03_error.np_arrays["error_array"]

data_SPVI=[SPVI_rpe_MH_01,SPVI_rpe_MH_02,SPVI_rpe_MH_03,SPVI_rpe_MH_04,SPVI_rpe_MH_05,SPVI_rpe_V1_01,SPVI_rpe_V1_02,SPVI_rpe_V1_03,SPVI_rpe_V2_01,SPVI_rpe_V2_02,SPVI_rpe_V2_03]
data_ORB=[ORB_rpe_MH_01,ORB_rpe_MH_02,ORB_rpe_MH_03,ORB_rpe_MH_04,ORB_rpe_MH_05,ORB_rpe_V1_01,ORB_rpe_V1_02,ORB_rpe_V1_03,ORB_rpe_V2_01,ORB_rpe_V2_02,ORB_rpe_V2_03]
data_OKVIS=[OKVIS_rpe_MH_01,OKVIS_rpe_MH_02,OKVIS_rpe_MH_03,OKVIS_rpe_MH_04,OKVIS_rpe_MH_05,OKVIS_rpe_V1_01,OKVIS_rpe_V1_02,OKVIS_rpe_V1_03,OKVIS_rpe_V2_01,OKVIS_rpe_V2_02]

ticks = ['MH_01', 'MH_02', 'MH_03','MH_04', 'MH_05','V1_01','V1_02', 'V1_03','V2_01','V2_02', 'V2_03']

#def set_box_color(bp, color):
#    plt.setp(bp['boxes'], color=color)
#    plt.setp(bp['whiskers'], color=color)
#    plt.setp(bp['caps'], color=color)
#    plt.setp(bp['medians'], color=color)

plt.figure(figsize=(10, 5))

bpl = plt.violinplot(data_SPVI, positions=np.array(xrange(len(data_SPVI)))*3.0-0.6, widths=0.5)
bpm = plt.violinplot(data_ORB, positions=np.array(xrange(len(data_ORB)))*3.0, widths=0.5)
bpr = plt.violinplot(data_OKVIS, positions=np.array(xrange(len(data_OKVIS)))*3.0+0.6, widths=0.5)

#set_voilin_color(bpl, '#D7191C') # colors are from http://colorbrewer2.org/
#set_voilin_color(bpm, '#008000')
#set_voilin_color(bpr, '#2C7BB6')

#plt.voilin(bpl, label='SPVI-SLAM')
#plt.voilin(bpm, label='ORB-SLAM2')
#plt.voilin(bpr, label='OKVIS')
#plt.legend([bpl,bpm,bpr],['SPVI-SLAM','ORB-SLAM2','OKVIS'],'best')


plt.xticks(xrange(0, len(ticks) * 3, 3), ticks)
plt.xlim(-3, len(ticks)*3)
plt.tight_layout()
plt.ylabel("RPE(m)")
plt.xlabel("EuRoC datasets")
plt.rcParams['figure.dpi'] = 300 #Resolution
plt.tight_layout()
#plt.grid()  #grid
plt.savefig('rpe_compare_volin.png')
plt.show()
