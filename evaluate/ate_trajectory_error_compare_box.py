import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


from evo.tools import file_interface
#load SVPI-SLAM trakectory error data:MH_01, MH_02, MH_03, MH_04, MH_05, V1_01, V1_02, V1_03, V2_01, V2_02, V2_03
SPVI_ate_MH_01_error = file_interface.load_res_file("/home/cc/output/SPVI_trajectory_190429/ate_MH_01.zip")
SPVI_ate_MH_01 = SPVI_ate_MH_01_error.np_arrays["error_array"]
SPVI_ate_MH_02_error = file_interface.load_res_file("/home/cc/output/SPVI_trajectory_190429/ate_MH_02.zip")
SPVI_ate_MH_02 = SPVI_ate_MH_02_error.np_arrays["error_array"]
SPVI_ate_MH_03_error = file_interface.load_res_file("/home/cc/output/SPVI_trajectory_190429/ate_MH_03.zip")
SPVI_ate_MH_03 = SPVI_ate_MH_03_error.np_arrays["error_array"]
SPVI_ate_MH_04_error = file_interface.load_res_file("/home/cc/output/SPVI_trajectory_190429/ate_MH_04.zip")
SPVI_ate_MH_04 = SPVI_ate_MH_04_error.np_arrays["error_array"]
SPVI_ate_MH_05_error = file_interface.load_res_file("/home/cc/output/SPVI_trajectory_190429/ate_MH_05.zip")
SPVI_ate_MH_05 = SPVI_ate_MH_05_error.np_arrays["error_array"]
SPVI_ate_V1_01_error = file_interface.load_res_file("/home/cc/output/SPVI_trajectory_190429/ate_V1_01.zip")
SPVI_ate_V1_01 = SPVI_ate_V1_01_error.np_arrays["error_array"]
SPVI_ate_V1_02_error = file_interface.load_res_file("/home/cc/output/SPVI_trajectory_190429/ate_V1_02.zip")
SPVI_ate_V1_02 = SPVI_ate_V1_02_error.np_arrays["error_array"]
SPVI_ate_V1_03_error = file_interface.load_res_file("/home/cc/output/SPVI_trajectory_190429/ate_V1_03.zip")
SPVI_ate_V1_03 = SPVI_ate_V1_03_error.np_arrays["error_array"]
SPVI_ate_V2_01_error = file_interface.load_res_file("/home/cc/output/SPVI_trajectory_190429/ate_V2_01.zip")
SPVI_ate_V2_01 = SPVI_ate_V2_01_error.np_arrays["error_array"]
SPVI_ate_V2_02_error = file_interface.load_res_file("/home/cc/output/SPVI_trajectory_190429/ate_V2_02.zip")
SPVI_ate_V2_02 = SPVI_ate_V2_02_error.np_arrays["error_array"]
SPVI_ate_V2_03_error = file_interface.load_res_file("/home/cc/output/SPVI_trajectory_190429/ate_V2_03.zip")
SPVI_ate_V2_03 = SPVI_ate_V2_03_error.np_arrays["error_array"]

#load ORB-SLAM trakectory error data:MH_01, MH_02, MH_03, MH_04, MH_05, V1_01, V1_02, V1_03, V2_01, V2_02, V2_03
ORB_ate_MH_01_error = file_interface.load_res_file("/home/cc/output/ORB-SLAM2_trajectory/ate_MH_01.zip")
ORB_ate_MH_01 = ORB_ate_MH_01_error.np_arrays["error_array"]
ORB_ate_MH_02_error = file_interface.load_res_file("/home/cc/output/ORB-SLAM2_trajectory/ate_MH_02.zip")
ORB_ate_MH_02 = ORB_ate_MH_02_error.np_arrays["error_array"]
ORB_ate_MH_03_error = file_interface.load_res_file("/home/cc/output/ORB-SLAM2_trajectory/ate_MH_03.zip")
ORB_ate_MH_03 = ORB_ate_MH_03_error.np_arrays["error_array"]
ORB_ate_MH_04_error = file_interface.load_res_file("/home/cc/output/ORB-SLAM2_trajectory/ate_MH_04.zip")
ORB_ate_MH_04 = ORB_ate_MH_04_error.np_arrays["error_array"]
ORB_ate_MH_05_error = file_interface.load_res_file("/home/cc/output/ORB-SLAM2_trajectory/ate_MH_05.zip")
ORB_ate_MH_05 = ORB_ate_MH_05_error.np_arrays["error_array"]
ORB_ate_V1_01_error = file_interface.load_res_file("/home/cc/output/ORB-SLAM2_trajectory/ate_V1_01.zip")
ORB_ate_V1_01 = ORB_ate_V1_01_error.np_arrays["error_array"]
ORB_ate_V1_02_error = file_interface.load_res_file("/home/cc/output/ORB-SLAM2_trajectory/ate_V1_02.zip")
ORB_ate_V1_02 = ORB_ate_V1_02_error.np_arrays["error_array"]
ORB_ate_V1_03_error = file_interface.load_res_file("/home/cc/output/ORB-SLAM2_trajectory/ate_V1_03.zip")
ORB_ate_V1_03 = ORB_ate_V1_03_error.np_arrays["error_array"]
ORB_ate_V2_01_error = file_interface.load_res_file("/home/cc/output/ORB-SLAM2_trajectory/ate_V2_01.zip")
ORB_ate_V2_01 = ORB_ate_V2_01_error.np_arrays["error_array"]
ORB_ate_V2_02_error = file_interface.load_res_file("/home/cc/output/ORB-SLAM2_trajectory/ate_V2_02.zip")
ORB_ate_V2_02 = ORB_ate_V2_02_error.np_arrays["error_array"]
ORB_ate_V2_03_error = file_interface.load_res_file("/home/cc/output/ORB-SLAM2_trajectory/ate_V2_03.zip")
ORB_ate_V2_03 = ORB_ate_V2_03_error.np_arrays["error_array"]

#load OKVIS trakectory error data:MH_01, MH_02, MH_03, MH_04, MH_05, V1_01, V1_02, V1_03, V2_01, V2_02. V2_03 (can not get full trajectory)
OKVIS_ate_MH_01_error = file_interface.load_res_file("/home/cc/output/OKVIS_trajecotry/ate_MH_01.zip")
OKVIS_ate_MH_01 = OKVIS_ate_MH_01_error.np_arrays["error_array"]
OKVIS_ate_MH_02_error = file_interface.load_res_file("/home/cc/output/OKVIS_trajecotry/ate_MH_02.zip")
OKVIS_ate_MH_02 = OKVIS_ate_MH_02_error.np_arrays["error_array"]
OKVIS_ate_MH_03_error = file_interface.load_res_file("/home/cc/output/OKVIS_trajecotry/ate_MH_03.zip")
OKVIS_ate_MH_03 = OKVIS_ate_MH_03_error.np_arrays["error_array"]
OKVIS_ate_MH_04_error = file_interface.load_res_file("/home/cc/output/OKVIS_trajecotry/ate_MH_04.zip")
OKVIS_ate_MH_04 = OKVIS_ate_MH_04_error.np_arrays["error_array"]
OKVIS_ate_MH_05_error = file_interface.load_res_file("/home/cc/output/OKVIS_trajecotry/ate_MH_05.zip")
OKVIS_ate_MH_05 = OKVIS_ate_MH_05_error.np_arrays["error_array"]
OKVIS_ate_V1_01_error = file_interface.load_res_file("/home/cc/output/OKVIS_trajecotry/ate_V1_01.zip")
OKVIS_ate_V1_01 = OKVIS_ate_V1_01_error.np_arrays["error_array"]
OKVIS_ate_V1_02_error = file_interface.load_res_file("/home/cc/output/OKVIS_trajecotry/ate_V1_02.zip")
OKVIS_ate_V1_02 = OKVIS_ate_V1_02_error.np_arrays["error_array"]
OKVIS_ate_V1_03_error = file_interface.load_res_file("/home/cc/output/OKVIS_trajecotry/ate_V1_03.zip")
OKVIS_ate_V1_03 = OKVIS_ate_V1_03_error.np_arrays["error_array"]
OKVIS_ate_V2_01_error = file_interface.load_res_file("/home/cc/output/OKVIS_trajecotry/ate_V2_01.zip")
OKVIS_ate_V2_01 = OKVIS_ate_V2_01_error.np_arrays["error_array"]
OKVIS_ate_V2_02_error = file_interface.load_res_file("/home/cc/output/OKVIS_trajecotry/ate_V2_02.zip")
OKVIS_ate_V2_02 = OKVIS_ate_V2_02_error.np_arrays["error_array"]
#OKVIS_ate_V2_03_error = file_interface.load_res_file("/home/cc/output/OKVIS_trajecotry/ate_V2_03.zip")
#OKVIS_ate_V2_03 = OKVIS_ate_V2_03_error.np_arrays["error_array"]

data_SPVI=[SPVI_ate_MH_01,SPVI_ate_MH_02,SPVI_ate_MH_03,SPVI_ate_MH_04,SPVI_ate_MH_05,SPVI_ate_V1_01,SPVI_ate_V1_02,SPVI_ate_V1_03,SPVI_ate_V2_01,SPVI_ate_V2_02,SPVI_ate_V2_03]
data_ORB=[ORB_ate_MH_01,ORB_ate_MH_02,ORB_ate_MH_03,ORB_ate_MH_04,ORB_ate_MH_05,ORB_ate_V1_01,ORB_ate_V1_02,ORB_ate_V1_03,ORB_ate_V2_01,ORB_ate_V2_02,ORB_ate_V2_03]
data_OKVIS=[OKVIS_ate_MH_01,OKVIS_ate_MH_02,OKVIS_ate_MH_03,OKVIS_ate_MH_04,OKVIS_ate_MH_05,OKVIS_ate_V1_01,OKVIS_ate_V1_02,OKVIS_ate_V1_03,OKVIS_ate_V2_01,OKVIS_ate_V2_02]

ticks = ['MH_01', 'MH_02', 'MH_03','MH_04', 'MH_05','V1_01','V1_02', 'V1_03','V2_01','V2_02', 'V2_03']

def set_box_color(bp, color):
    plt.setp(bp['boxes'], color=color)
    plt.setp(bp['whiskers'], color=color)
    plt.setp(bp['caps'], color=color)
    plt.setp(bp['medians'], color=color)

plt.figure(figsize=(10, 5))

bpl = plt.boxplot(data_SPVI, positions=np.array(xrange(len(data_SPVI)))*3.0-0.6, sym='', widths=0.5)
bpm = plt.boxplot(data_ORB, positions=np.array(xrange(len(data_ORB)))*3.0, sym='', widths=0.5)
bpr = plt.boxplot(data_OKVIS, positions=np.array(xrange(len(data_OKVIS)))*3.0+0.6, sym='', widths=0.5)

set_box_color(bpl, '#D7191C') # colors are from http://colorbrewer2.org/
set_box_color(bpm, '#008000')
set_box_color(bpr, '#2C7BB6')

# draw temporary red, green and blue lines and use them to create a legend
plt.plot([], c='#D7191C', label='SPVI-SLAM')
plt.plot([], c='#008000', label='ORB-SLAM2')
plt.plot([], c='#2C7BB6', label='OKVIS')
plt.legend()


plt.xticks(xrange(0, len(ticks) * 3, 3), ticks)
plt.xlim(-3, len(ticks)*3)
plt.tight_layout()
plt.ylabel("ATE(m)")
plt.xlabel("EuRoC datasets")
plt.rcParams['figure.dpi'] = 300 #Resolution
plt.tight_layout()
#plt.grid()  #grid
plt.savefig('ate_compare_box.png')
plt.show()
