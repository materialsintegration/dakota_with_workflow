#!/usr/bin/python3.6
import sys
import math
import numpy as np

'''
Dakotaへ評価値を返すための計算を行う
1. 最初のパラメータ：γ’体積率のポート名
2. 次のパラメータ：固液共存域温度のポート名
3. 出力：固液共存域温度の値から、γ’体積率を30%でReLUした値
'''

def relu(x):
    '''
    '''
    return np.maximum(0, x)

objective_variables = {}
for item in range(1, len(sys.argv)):
    objective_variables[sys.argv[item]] = ""

# 出力ファイルの列はoutput.txtで存在する。
infile = open("output.txt", "r")
lines = infile.read().split("\n")
infile.close()

outfilename = ""
for items in lines:
    #print(str(items.split(":")))
    for object_var_name in objective_variables:
        if object_var_name == items.split(":")[0]:
            objective_variables[object_var_name] = items.split(":")[1]

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
sys.stderr.write("gamma prime size = %f\n"%gammap_size)
print("%f\n"%(btr_value + (100 * relu(0.3 - gammap_size))))

