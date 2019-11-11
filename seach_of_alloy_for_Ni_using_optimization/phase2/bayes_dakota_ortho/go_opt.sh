#!/bin/bash

atomics=(C Co Cr Mo Nb Ta W Zr)

for item in ${atomics[@]}; do
    echo "treate about atomic $item"
    python3.6 -u ~/assets/modules/P67_manaka/thermo-calc-bayes-dakota.py 3 10 $item W000020000000229 13bedfd69583faa62be240fcbcd0c0c0b542bc92e1352070f150f8a309f441ed dev-u-tokyo.mintsys.jp $item 2>&1 | tee results-$item.log
done
