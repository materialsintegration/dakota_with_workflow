#!python3.6
# -*- coding: utf-8 -*-

'''
Rosenblock関数を
bayes推定で絞る
dakotaで最適値を求める
'''

import sys, os
import shutil
import math
import datetime
from matplotlib import pyplot as plt
from bayes_opt import BayesianOptimization
import numpy as np
import subprocess

alti_results = np.array([
[4.10000000, 2.90000000,225.240000],
[4.09000000, 2.91000000,225.081000],
[4.08000000, 2.92000000,225.082000],
[4.07000000, 2.93000000,224.922000],
[4.06000000, 2.94000000,224.762000],
[4.05000000, 2.95000000,224.922000],
[4.04000000, 2.96000000,224.663000],
[4.03000000, 2.97000000,224.503000],
[4.02000000, 2.98000000,224.344000],
[4.01000000, 2.99000000,224.344000],
[4.00000000, 3.00000000,224.185000],
[3.99000000, 3.01000000,226.575000],
[3.98000000, 3.02000000,226.516000],
[3.97000000, 3.03000000,224.125000],
[3.96000000, 3.04000000,231.137000],
[3.95000000, 3.05000000,231.138000],
[3.94000000, 3.06000000,230.660000],
[3.93000000, 3.07000000,230.181000],
[3.92000000, 3.08000000,230.182000],
[3.91000000, 3.09000000,230.400000],
[3.90000000, 3.10000000,229.066000],
[3.89000000, 3.11000000,228.907000],
[3.88000000, 3.12000000,228.428000],
[3.87000000, 3.13000000,228.110000],
[3.86000000, 3.14000000,229.763000],
[3.85000000, 3.15000000,227.372000],
[3.84000000, 3.16000000,229.503000],
[3.83000000, 3.17000000,229.444000],
[3.82000000, 3.18000000,229.444000],
[3.81000000, 3.19000000,229.125000],
[3.80000000, 3.20000000,229.285000],
[3.79000000, 3.21000000,229.285000],
[3.78000000, 3.22000000,229.443000],
[3.77000000, 3.23000000,229.444000],
[3.76000000, 3.24000000,229.762000],
[3.75000000, 3.25000000,229.922000],
[3.74000000, 3.26000000,229.922000],
[3.73000000, 3.27000000,230.140000],
[3.72000000, 3.28000000,229.981000],
[3.71000000, 3.29000000,230.300000],
[3.70000000, 3.30000000,225.460000],
[3.69000000, 3.31000000,225.459000],
[3.68000000, 3.32000000,225.719000],
[3.67000000, 3.33000000,225.660000],
[3.66000000, 3.34000000,225.819000],
[3.65000000, 3.35000000,225.937000],
[3.64000000, 3.36000000,225.937000],
[3.63000000, 3.37000000,226.256000],
[3.62000000, 3.38000000,226.415000],
[3.61000000, 3.39000000,226.416000],
[3.60000000, 3.40000000,226.416000],
[3.59000000, 3.41000000,226.734000],
[3.58000000, 3.42000000,226.734000],
[3.57000000, 3.43000000,226.794000],
[3.56000000, 3.44000000,227.113000],
[3.55000000, 3.45000000,227.113000],
[3.54000000, 3.46000000,227.431000],
[3.53000000, 3.47000000,227.372000],
[3.52000000, 3.48000000,227.531000],
[3.51000000, 3.49000000,227.850000],
[3.50000000, 3.50000000,228.109000],
[3.49000000, 3.51000000,228.009000],
[3.48000000, 3.52000000,228.169000],
[3.47000000, 3.53000000,228.328000]])

def relu(x):
    '''
    '''
    return np.maximum(0, x)

def thermo_calc(ti):
    '''
    '''
    
    al = 7.0 - ti
    outfile = open("al.dat", "w")
    outfile.write("%f\n"%al)
    outfile.close()
    outfile = open("ti.dat", "w")
    outfile.write("%f\n"%ti)
    outfile.close()
    
    sys.stderr.write("\nAl = %3.8f / Ti = %3.8f\n"%(al, ti))

    # ワークフロー版Thermo-Calc実行
    cmd = "python3.6 ~/assets/modules/workflow_python_lib/workflow_execute.py workflow_id:W000020000000230 token:13bedfd69583faa62be240fcbcd0c0c0b542bc92e1352070f150f8a309f441ed misystem:dev-u-tokyo.mintsys.jp アルミニウム量_質量分率_01:al.dat チタン量_質量分率_01:ti.dat number:-1"
    sys.stderr.write("exec workflow via wf-api\n")
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    p.wait()
    stdout_data = p.stdout.read()
    lines = stdout_data.decode("utf8").split("\n")
    elines = p.stderr.read().decode("utf8").split("\n")
    for item in elines:
        if item == "":
            continue
        sys.stderr.write("%s\n"%item)

    objective_variables = {"gamma_prime相の体積率":"", "固液共存域温度":""}
    outfilename = ""
    for items in lines:
        if items == "":
            continue
        #print(str(items.split(":")))
        for object_var_name in objective_variables:
            if object_var_name == items.split(":")[0]:
                objective_variables[object_var_name] = items.split(":")[1]
    
    #print(objective_variables)
    gammap_size = None
    btr_value = None
    # gamma_size
    if ("gamma_prime相の体積率" in objective_variables) is True:
        infile = open(objective_variables["gamma_prime相の体積率"], "r")
        gammap_size = float(infile.read().split("\n")[0])
    # btr_value
    if ("固液共存域温度" in objective_variables) is True:
        infile = open(objective_variables["固液共存域温度"], "r")
        btr_value = float(infile.read().split("\n")[0])
    
    if gammap_size is None or btr_value is None:
        sys.stderr.write("cannot get gamma prime size or btr value\n")
        sys.exit(1)
    
    sys.stderr.write("diff = %f\n"%btr_value)
    sys.stderr.write("gamma prime Volume fruction = %f\n"%gammap_size)
    return -1.0 * (btr_value + (100 * relu(0.3 - gammap_size)))

start = datetime.datetime.now()
init_p = int(sys.argv[1])
n_iter = int(sys.argv[2])
num = sys.argv[3]
sys.stderr.write("init_points = %d / n_iter = %d\n"%(init_p, n_iter))

# bayes推定開始（大局解）
bo = BayesianOptimization(f=thermo_calc, pbounds={'ti': (2.9, 3.54)})
bo.maximize(init_points=init_p, n_iter=n_iter)
sys.stderr.write("result ti = %f\n"%(bo.max["params"]["ti"]))
#sys.stderr.write("%f %f"%(bo.max["params"]["x"], bo.max["params"]["y"]))

# 描画１(True)
Ti = []
Rt = []
for item in alti_results:
    Ti.append(item[1])
    Rt.append(item[2] * -1.0)
plt.plot(Ti, Rt, label='true')

# 描画２(Prediction)
xs = [p['params']['ti'] for p in bo.res]
ys = [p['target'] for p in bo.res]

plt.scatter(xs, ys, c='green', s=20, zorder=10, label='sample')
plt.plot(bo.max["params"]["ti"], bo.max["target"], marker="o", c="red", label="opt")
mean, sigma = bo._gp.predict(np.array(Ti).reshape(-1, 1), return_std=True)

plt.plot(Ti, mean, label='pred')
plt.fill_between(Ti, mean + sigma, mean - sigma, alpha=0.1)

plt.legend()
plt.grid()
plt.show()

# 大局解からdakotaによる局所解導出のための初期値を設定する
init_ti = float(bo.max["params"]["ti"])
lower_ti = 2.9
upper_ti = 3.54
#if init_x < 0:
#    lower_x = init_x + (init_x * .1)
#    upper_x = init_x - (init_x * .1)
#else:
#    lower_x = init_x - (init_x * .1)
#    upper_x = init_x + (init_x * .1)
#if init_y < 0:
#    lower_y = init_y + (init_y * .1)
#    upper_y = init_y - (init_y * .1)
#else:
#    lower_y = init_y - (init_y * .1)
#    upper_y = init_y + (init_y * .1)

outfile = open("opt_rosenbrock_local.in", "w")
outfile.write("environment,\n")
outfile.write("\tgraphics\n")
outfile.write("    tabular_graphics_data\n")
outfile.write("       tabular_graphics_file = 'tabulargraphics.dat'\n\n")
outfile.write("# method, coliny_ea\n\n")
outfile.write("method, conmin_frcg\n")
outfile.write('     id_method ="frcg"\n') 
outfile.write("     max_iterations = 10000\n")
outfile.write("     convergence_tolerance=1e-7\n\n\n")
outfile.write("variables,\n")
outfile.write("\tcontinuous_design = 1\n")
outfile.write("\t  cdv_initial_point =  %f\n"%(init_ti))
outfile.write("\t  cdv_lower_bounds  =  2.9\n")
outfile.write("\t  cdv_upper_bounds  =  3.54\n")
outfile.write("\t  cdv_descriptor    =  'wt_ti'\n")
outfile.write("      cdv_scale_type  'value'\n")
outfile.write("      cdv_scales  0.01\n\n\n")
outfile.write("interface,\n")
outfile.write("\t system #asynch evaluation_concurrency = 5\n")
outfile.write("\t  analysis_driver = 'simulator_script.sh'\n")
outfile.write("\t  parameters_file = 'params.in'\n")
outfile.write("\t  results_file = 'results.out'\n")
outfile.write("\t	  dprepro\n\n\n")
outfile.write("responses,\n")
outfile.write("\tobjective_functions = 1")
outfile.write("\tnumerical_gradients\n")
outfile.write("\t  method_source dakota\n")
outfile.write("\t  interval_type central\n")
outfile.write("\t  fd_step_size = 0.01\n")
outfile.write("\tno_hessians\n")
outfile.close()

cmd = "dakota -i opt_rosenbrock_local.in"
p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
while True:
    aline = p.stdout.readline()
    sys.stderr.write("%s"%aline.decode("utf8"))

    if not aline and p.poll() is not None:
        break

if p.returncode != 0:
    sys.stderr.write("dakota exit with not normal.\n")
    sys.exit(1)

if os.path.exists("tabulargraphics.dat") is True:
    shutil.copy("tabulargraphics.dat", "tabulargraphics-%s.dat"%num)

print("total time = %s"%(datetime.datetime.now() - start))
