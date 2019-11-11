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
dprepro $1 template.macro_only_al.in ti.dat
python3.6 prepro.py


# --------
# ANALYSIS
# --------

#/home/minamoto/Thermo-Calc/2015b/Console.sh  ShroudClad.tcm | tee ShroudClad.log
#$FEMCCV ct.modelm4.2d.4944.in | tee femccv_test01.log
#energy=`cat Energy.dat`
#echo "scale=8; $energy * 1000" | bc > Energy.dat
python3.6 ~/assets/modules/workflow_python_lib/workflow_execute.py workflow_id:W000020000000229 token:13bedfd69583faa62be240fcbcd0c0c0b542bc92e1352070f150f8a309f441ed misystem:dev-u-tokyo.mintsys.jp アルミニウム量_質量分率_01:al.dat チタン量_質量分率_01:ti.dat number:-1 > output.txt

# ---------------
# POST-PROCESSING
# ---------------

# extract function value from the simulation output

#grep -A 1 'creep damage' output_ucd.00000010.inp   | grep '       1' | cut -d' ' -f10 | head -1 |expr `xargs`-0.000422  | calc -p | expr `xargs`^2 | bc > outres.txt
echo "==========="
python3.6 objective_function.py gamma_prime相の体積率 固液共存域温度 > outres.txt

#cat output_ucd.00000010.inp
cat outres.txt
echo "==========="
cp outres.txt $2


