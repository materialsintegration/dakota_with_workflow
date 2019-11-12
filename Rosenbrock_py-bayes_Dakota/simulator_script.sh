#!/bin/sh
# Sample simulator to Dakota system call script
# See Advanced Simulation Code Interfaces chapter in Users Manual

# $1 is params.in FROM Dakota
# $2 is results.out returned to Dakota

# --------------
# PRE-PROCESSING
# --------------
# Incorporate the parameters from DAKOTA into the template, writing ros.in
# Use the following line if SNL's APREPRO utility is used instead of DPrePro.
# ../aprepro -c '*' -q --nowarning ros.template ros.in

#dprepro $1 G3+Mo_Temp02_ini.TDB G3+Mo_Temp02.TDB
dprepro $1 template.rosenbrock.in rosenbrock_in


# --------
# ANALYSIS
# --------

#/home/minamoto/Thermo-Calc/2015b/Console.sh  ShroudClad.tcm | tee ShroudClad.log
#$FEMCCV ct.modelm4.2d.4944.in | tee femccv_test01.log
python3.6 rosenbrock.py `cat rosenbrock_in` > outres.txt

# ---------------
# POST-PROCESSING
# ---------------

# extract function value from the simulation output

#grep -A 1 'creep damage' output_ucd.00000010.inp   | grep '       1' | cut -d' ' -f10 | head -1 |expr `xargs`-0.000422  | calc -p | expr `xargs`^2 | bc > outres.txt


echo "==========="
#cat output_ucd.00000010.inp
cat outres.txt
echo "==========="
cp outres.txt $2
