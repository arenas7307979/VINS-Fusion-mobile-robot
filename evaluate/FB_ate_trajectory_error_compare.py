import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


from evo.tools import file_interface
#load FB trakectory error data
FB_ate_MH_01_error = file_interface.load_res_file("/home/cc/output/FB_MH01_ape.zip")
FB_ate_MH_01 = FB_ate_MH_01_error.np_arrays["error_array"]


#load of trakectory error data
of_ate_MH_01_error = file_interface.load_res_file("/home/cc/output/of_MH01_ape.zip")
of_ate_MH_01 = of_ate_MH_01_error.np_arrays["error_array"]

FB_Frame=np.linspace(1,  len(FB_ate_MH_01), num=len(FB_ate_MH_01))
of_Frame=np.linspace(1,  len(of_ate_MH_01), num=len(of_ate_MH_01))

#print(np.mean(FB_process_time))
#print(np.mean(of_process_time))
#plt.plot(FB_Frame, FB_ate_MH_01, marker=".",label='Forward-Backend', linewidth=1)
#plt.plot(of_Frame, of_ate_MH_01, marker=".",label='L-K', linewidth=1)
plt.plot(FB_Frame, FB_ate_MH_01,label='Forward-backend', linewidth=1)
plt.plot(of_Frame, of_ate_MH_01,label='Lucas-Kanade', linewidth=1)

plt.xlim(0, max(len(FB_Frame),len(of_Frame)))
#plt.ylim(0, max(of_ate_MH_01))
plt.xlabel("Keyframe")
plt.ylabel("ATE(m)")



plt.legend(loc='best')

plt.rcParams['figure.dpi'] = 300 #Resolution
plt.tight_layout()
#plt.grid()  #grid
plt.savefig('Forward_Backend_LK_trajectory_compare_MH01.png')
plt.show()



