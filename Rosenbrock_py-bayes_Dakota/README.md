# Rosenbrock関数の最適化をbayes推定の後、Dakotaで行う。

## 概要
Rosenbrockの最適化を題材に、bayse推定とDakotaによる最適化を実施する。bayes推定は変数が１つ（1次元）だとよい結果を出すが、２変数以上（多次元）だととたんに収束が悪くなる傾向にある。とはいえ、大局解は出せる。他方Dakotaは与える変数に対して、初期値が必要となる。この初期値により収束にかかる計算時間やシミュレーション回数が増えることが予想される。このことからbayes推定で得られる解を大局解としてDakotaの初期として指定し、Daokotaの局所解導出を行ってみる。
まとめると
* bayes推定は少ない変数ではそこそこよい結果を出す。複数の変数でも大局解としてみることでDakotaなどの初期値に使える。
* Dakotaは局所解を求めることが可能であるが、初期値いかんで計算量、時間共に多くかかる。

以上から本プロジェクトではbayes推定による大局解をもとめ、それを初期としてDakotaを実行して局所解を求める。この時の時間やシミュレーション回数をDakota単体での実行と比べてみた。その時使用したスクリプトを格納してある。


## 内容
* README.md
  + このファイル
* go_opt.py
  * この最適化を行うためのシェルスクリプト
* simulator_script.sh
  * Dakotaのパラメータ内、interface->analysis_driverに指定する目的関数
* template.rosenbrock.in
  + Dakotaのパラメータ内、vaiablesに指定する変数ファイル作成テンプレートファイル。
* rosenbrock.py
  + Rosenbrock評価関数。

## 準備
Rosenbrockの最適化探索範囲として、最小値と最大値を決める。go_opt.pyスクリプト中に、以下のように設定する。
```
bo = BayesianOptimization(f=rosenbrock_for_bayes, pbounds={'x': (-5.0, 5.0), 'y': (-5.0, 5.0),})
```
※ これはX、Yともに-5.0から5.0を探索範囲として指定したことをあらわす。

## 使用方法
```
$ python3.6 go_opt.py <init_points> <n_iter> <添字> | tee bayes_dakota-001.log
```

init_pointsとn_iterはPython bayes推定の関数パラメータ。添字は、ログファイルなどの使われる。
添字を001などとした場合、以下の様になる。
* Dakotaによる最適化の標準出力を「dakota_with_bayes-001.log」と言うファイル名で記録する。
* Dakotaが作成するtabulargraphics.datを「tabulargraphic-001.dat」というファイル名に変更する。
* teeコマンドの後ろのbayes_dakota-001.logはこの一連の（bayes推定後のDakotaによる）最適化の標準出力を記録する。


