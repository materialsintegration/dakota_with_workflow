#!python3.6
# -*- coding: utf-8 -*-

'''
Rosenblock関数を
bayes推定で絞る
dakotaで最適値を求める
'''

import sys, os
import math
import shutil
import datetime
from bayes_opt import BayesianOptimization
import numpy as np
import subprocess

from rosenbrock import *

start = datetime.datetime.now()
init_p = int(sys.argv[1])
n_iter = int(sys.argv[2])
num = (sys.argv[3])
sys.stderr.write("init_points = %d / n_iter = %d\n"%(init_p, n_iter))

# bayes推定開始（大局解）
bo = BayesianOptimization(f=rosenbrock_for_bayes, pbounds={'x': (-5.0, 5.0), 'y': (-5.0, 5.0),})
bo.maximize(init_points=init_p, n_iter=n_iter)
sys.stderr.write("result x = %f / y = %f\n"%(bo.max["params"]["x"], bo.max["params"]["y"]))
#sys.stderr.write("%f %f"%(bo.max["params"]["x"], bo.max["params"]["y"]))

# 大局解から局所解のための初期値、最小値、最大値を求める
init_x = float(bo.max["params"]["x"])
init_y = float(bo.max["params"]["y"])
lower_x = lower_y = -5.0
upper_x = upper_y = 5.0
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
outfile.write("     convergence_tolerance=1e-7\n")
outfile.write("     scaling\n\n\n")
outfile.write("variables,\n")
outfile.write("\tcontinuous_design = 2\n")
outfile.write("\t  cdv_initial_point =  %2.3f  %2.3f\n"%(init_x, init_y)) 
outfile.write("\t  cdv_lower_bounds  =  %2.3f  %2.3f\n"%(lower_x, lower_y)) 
outfile.write("\t  cdv_upper_bounds  =  %2.3f  %2.3f\n"%(upper_x, upper_y))
outfile.write("\t  cdv_descriptor    =  'V001' 'V002' \n")
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

cmd = "dakota -i opt_rosenbrock_local.in 2>&1 | tee dakota_with_bayes-%s.log"%num
p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
while True:
    aline = p.stdout.readline()
    sys.stderr.write("%s"%aline.decode("utf8"))
    
    if not aline and p.poll() is not None:
        break
#p.wait()
#stdout_data = p.stdout.read()
#print(stdout_data.decode("utf8"))
if os.path.exists("tabulargraphics.dat") is True:
    shutil.copy("tabulargraphics.dat", "tabulargraphics-%s.dat"%num)

sys.stderr.write("start dakota with x = %f / y = %f\n"%(bo.max["params"]["x"], bo.max["params"]["y"]))
print("total time = %s"%(datetime.datetime.now() - start))
