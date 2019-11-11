#!/usr/bin/python3.6
import sys
import math

objective_variables = []
for item in range(1, len(sys.argv)):
    objective_variables.append(sys.argv[item])

# ファイルはti.datで存在する。
infile = open("ti.dat", "r")
lines = infile.read().split("\n")
infile.close()

outfilename = ""
read_start = False
temp_hist = []
for aline in lines:
    if aline == "":
        continue
    items = aline.split()
#    c = float(items[0])
#    co = float(items[1])
#    cr = float(items[2])
#    mo = float(items[3])
#    nb = float(items[4])
#    ta = float(items[5])
#    ti = float(items[6])
#    w = float(items[7])
#    zr = float(items[8])
    ti = float(items[0])

al = 7.0 - ti
outfile = open("al.dat", "w")
outfile.write("%f\n"%al)
outfile.close()

sys.stderr.write("Al = %3.8f / Ti = %3.8f\n"%(al, ti))
