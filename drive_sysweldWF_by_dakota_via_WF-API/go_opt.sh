#!/bin/bash
# dakotaによる最適化の統括実行スクリプト
# パラメータにdakotaのパラメータファイルと、ログ類のファイル名追加文字列を指定する。
# bash go_opt.sh <パラメータファイル名> <ログ用追加文字列>
# ログ用追加文字列は、以下のルールに適用される。
# tabulargraphics.dat -> tabulargraphics.<ログ用追加文字列>.dat
# dakota.log -> dakota.<ログ追加文字列>.log  ※　標準出力
# results.dat -> results.<ログ追加文字列>.dat

ADDITIONAL_STRING=`date +%Y%m%d-%H%M%S`
DAKOTA_PARAM_NAME="opt_dakota.in"

if [ $# != 2 ]; then
    echo "bash go_opt.sh <パラメータファイル名> <ログ用追加文字列>"
    exit 1
fi
DAKOTA_PARAM_NAME=$1
ADDITIONAL_STRING=$2

#echo $ADDITIONAL_STRING
#echo $DAKOTA_PARAM_NAME

dakota -i ${DAKOTA_PARAM_NAME}.in | tee dakota.${ADDITIONAL_STRING}.log
mkdir result${ADDITIONAL_STRING}
mv tabulargraphics.dat result${ADDITIONAL_STRING}/tabulargraphics.${ADDITIONAL_STRING}.dat
mv results.dat result${ADDITIONAL_STRING}/results.${ADDITIONAL_STRING}.dat
cp ${DAKOTA_PARAM_NAME}.in result${ADDITIONAL_STRING}/${DAKOTA_PARAM_NAME}.${ADDITIONAL_STRING}.in
mv dakota.${ADDITIONAL_STRING}.log result${ADDITIONAL_STRING}
