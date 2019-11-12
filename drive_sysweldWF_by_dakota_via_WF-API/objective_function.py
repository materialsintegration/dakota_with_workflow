#!/usr/bin/python3.6
import sys
import math

objective_variables = []
for item in range(1, len(sys.argv)):
    objective_variables.append(sys.argv[item])

# 出力ファイルの列はoutput.txtで存在する。
infile = open("output.txt", "r")
lines = infile.read().split("\n")
infile.close()

outfilename = ""
for items in lines:
    #print(str(items.split(":")))
    for object_var_name in objective_variables:
        if object_var_name == items.split(":")[0]:
            outfilename = items.split(":")[1]

if outfilename == "":
    sys.exit(1)

infile = open(outfilename, "r")
value = float(infile.read().split("\n")[0])

sys.stderr.write("%f\n"%value)
o_value = math.sqrt((value - 1000.0) ** 2)
print(o_value)
