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
dprepro $1 template.Energy.in Energy.dat
dprepro $1 template.Welding_End_Time.in Welding_End_Time.dat


# --------
# ANALYSIS
# --------

#/home/minamoto/Thermo-Calc/2015b/Console.sh  ShroudClad.tcm | tee ShroudClad.log
#$FEMCCV ct.modelm4.2d.4944.in | tee femccv_test01.log
#energy=`cat Energy.dat`
#echo "scale=8; $energy * 1000" | bc > Energy.dat
python3.6 ~/assets/modules/workflow_python_lib/workflow_execute.py  workflow_id:W000020000000219 token:13bedfd69583faa62be240fcbcd0c0c0b542bc92e1352070f150f8a309f441ed misystem:dev-u-tokyo.mintsys.jp weld_shape_pf_param_py_01:weld_shape_pf_param.py クランプ終了時間_01:Clamping_End_Time.dat クランプ開始時間_01:Clamping_Initial_Time.dat 入熱量_01:Energy.dat 冷却終了温度_01:Cooling_End_Time.dat 冷却開始時間_01:Cooling_Initial_Time.dat 初期温度_01:Initial_Temperature.dat 初期組織の相分率_01:init_microstructure.txt 効率_01:Efficiency.dat 溶接幅_01:Width.dat 溶接終了時間_01:Welding_End_Time.dat 溶接長さ_01:Length.dat 溶接開始時間_01:Welding_Initial_Time.dat 熱源移動速度_01:Velocity.dat 環境温度_01:Amient_Temp.dat 貫通_01:Penetration.dat number:-1 > output.txt

# ---------------
# POST-PROCESSING
# ---------------

# extract function value from the simulation output

#grep -A 1 'creep damage' output_ucd.00000010.inp   | grep '       1' | cut -d' ' -f10 | head -1 |expr `xargs`-0.000422  | calc -p | expr `xargs`^2 | bc > outres.txt
python3.6 objective_function.py 最高温度 > outres.txt
max_temp=`grep 最高温度 output.txt | awk '{split($0, file, ":");print(file[2])}' | xargs cat`
echo "`cat Welding_End_Time.dat`   `cat Energy.dat`  $max_temp" >> results.dat

echo "==========="
#cat output_ucd.00000010.inp
#cat outres.txt
echo "==========="
cp outres.txt $2
