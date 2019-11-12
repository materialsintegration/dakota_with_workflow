# SYSWELD実行WFをdakotaで最適化
## 概要
dakotaを使って、SYSWELDを実行するWFをWF-API経由で実行し、最適化を行う雛形スクリプト群。最適化の変数は入熱量と溶接終了時間とし、そのようにパラメータを組んだ。

## 内容
* README.md  
  このファイル
* go_opt.sh  
　この最適化の統合スクリプト
* objective_function.py  
  Dakotaのパラメータ内、responseで指定する評価関数
* opt_sysweld.in  
  Dakotaへ与えるパラメータファイル
* scatter_plot.py  
  tabulargraphics.datを読み込んで、離散図を作成するスクリプト(要、matplotlibパッケージ)
* simulator_script.sh  
  Dakotaのパラメータ内、interface->analysis_driverに指定する目的関数
* template.Energy.in  
  Dakotaのパラメータ内、vaiablesに指定する変数ファイル作成テンプレートファイル。
* template.Welding_End_Time.in  
  Dakotaのパラメータ内、vaiablesに指定する変数ファイル作成テンプレートファイル。
* その他のdatファイル。固定されたSYSWELD実行用パラメータ。 
  ```
  Amient_Temp.dat
  Clamping_End_Time.dat
  Clamping_Initial_Time.dat
  Cooling_End_Time.dat
  Cooling_Initial_Time.dat
  Efficiency.dat
  Initial_Temperature.dat
  Length.dat
  Penetration.dat
  Velocity.dat
  Welding_Initial_Time.dat
  Width.dat
  ```
  
## 準備と説明
これらのスクリプトを利用して、最適化を行うためには、以下のパラメータをあらかじめ決めておく必要がある。
* 入熱量の初期値、最小値、最大値
* 溶接終了時間の初期値、最小値、最大値
* SYSWELDを実行するワークフローのワークフローID
* 同、ワークフローのポート名の取得
* ワークフローAPI実行用のAPIトークンの取得
* ワークフローを実行するMIntシステムのURLの取得

### 入熱量と溶接終了時間
opt_sysweld.inファイルの、variablesセクションに以下の用に設定します。  
```
variables,
    continuous_design = 2
      initial_point =  4.17     0.500
      lower_bounds  =  3.753    0.450
      upper_bounds  =  4.587    0.550
      descriptor    =  'Weld_End_Time' 'Energy'
```

### ワークフローID
ワークフローIDは、通常Wで始まる15桁の数字である。たとえば用意した例では、"W000020000000219"となる。これは、simulation_scripti.sh内に以下の様に設定する。

```
python3.6 ~/assets/modules/workflow_python_lib/workflow_execute.py  workflow_id:W000020000000219 token:{あなたのAPIトークン} misystem:dev-u-tokyo.mintsys.jp weld_shape_pf_param_py_01:weld_shape_pf_param.py クランプ終了時間_01:Clamping_End_Time.dat クランプ開始時間_01:Clamping_Initial_Time.dat 入熱量_01:Energy.dat 冷却終了温度_01:Cooling_End_Time.dat 冷却開始時間_01:Cooling_Initial_Time.dat 初期温度_01:Initial_Temperature.dat 初期組織の相分率_01:init_microstructure.txt 効率_01:Efficiency.dat 溶接幅_01:Width.dat 溶接終了時間_01:Welding_End_Time.dat 溶接長さ_01:Length.dat 溶接開始時間_01:Welding_Initial_Time.dat 熱源移動速度_01:Velocity.dat 環境温度_01:Amient_Temp.dat 貫通_01:Penetration.dat number:-1 > output.txt
```
ここで、 workflow_id:W000020000000219 となっている部分がそれにあたる。

### ワークフローのポート名
ワークフローは入力パラメータとしてポート名を用意してある。ワークフローの実行はこのポート名に与えるパラメータを記述したファイルを指定することで行われる。
ワークフローIDのところで説明したものがWF-APIを利用してワークフローを実行するスクリプトであるが、ここに例えば、「クランプ開始時間_01:Clamping_Initial_Time.dat」とあるものが、ポート名に対するパラメータファイルの指定の方法である。
このポート名は以下のスクリプトを利用することで得ることができる。

```
$ python3.6 ~/assets/modules/workflow_python_lib/workflow_params.py workflow_id:W000020000000219 token:{あなたのAPIトークン} misystem:dev-u-tokyo.mintsys.jp
input parameters
port = weld_shape_pf_param_py_01(True)
port = クランプ終了時間_01(True)
port = クランプ開始時間_01(True)
port = 入熱量_01(True)
port = 冷却終了温度_01(True)
port = 冷却開始時間_01(True)
port = 初期温度_01(True)
port = 初期組織の相分率_01(True)
port = 効率_01(True)
port = 溶接幅_01(True)
port = 溶接終了時間_01(True)
port = 溶接長さ_01(True)
port = 溶接開始時間_01(True)
port = 熱源移動速度_01(True)
port = 環境温度_01(True)
port = 貫通_01(True)
output for results
port = 作成したメッシュ先端_01(file)
port = 作成したメッシュ全体_01(file)
port = 最大温度分布画像_01(file)
port = 最高温度_01(file)
port = 残留応力_01(file)
port = 残留応力画像_01(file)
port = 溶接画像_01(file)
port = 硬さ分布_01(file)
port = 硬さ分布画像_01(file)
port = 粒径情報_01(file)
port = 結果ファイル_01(file)
```
※ カッコの中は必須ポートであるかどうかを示す。必須ポートは省略できない。  
※詳細な使用方法は[ワークフロー実行ヘルパープログラム群](https://github.com/materialsintegration/workflow_python_lib)を参照のこと。

### ワークフローを実行するMIntシステムのURL
ワークフローIDのところで説明したパラメータにある、「misystem:dev-u-tokyo.mintsys.jp」がそれである。

## 使用方法
以下の用に、スクリプト名に続き、dakotaのパラメータファイル(.inを除いたもの)、ログへの追加文字列を指定する。
```
$ sh go_opt.sh opt_sysweld 001
```
追加文字列に「001」を指定したので、これで以下のようなファイルが作成される。
* result001というディレクトリが作成される。
* Dakotaの標準出力が、result001/dakota.001.logに記録される。
* Dakotaが作成するtabularagraphics.datがresult001/tabulargraphics.001.datと言うファイル名に変更される。
* Dakotaへ指定したパラメータファイルをresult001/opt_sysweld.001.inと言うファイル名に変更される。

