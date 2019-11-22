# Ni合金の探索
最適化を用いたNi合金の探索を行うためのスクリプト

## 概要
詳細は[Wiki](https://github.com/materialsintegration/optimization_by_sipmi/wiki/3D積層造形プロセスにおいてき裂発生を抑制可能なNi合金組成の探索)を参照のこと。

## 内容

* phase1: 解析１の最適化を実現するためのスクリプト格納場所
  + bayes_dakota_ortho: 解析１のオルソ平衡を実現するためのスクリプト格納場所
  + bayes_dakota_para: 解析１のパラ平衡を実現するためのスクリプト格納場所
* phase2: 解析２の最適化を実現するためのスクリプト格納場所。
  * bayes_dakota_ortho: 解析２のオルソ平衡を実現するためのスクリプト格納場所
  * bayes_dakota_para: 解析２のパラ平衡を実現するためのスクリプト格納場所
* [3D積層造形プロセスにおいて亀裂発生を抑制可能なNi合金組成の探索.pdf](https://github.com/materialsintegration/optimization_by_sipmi/blob/master/seach_of_alloy_for_Ni_using_optimization/3D%E7%A9%8D%E5%B1%A4%E9%80%A0%E5%BD%A2%E3%83%97%E3%83%AD%E3%82%BB%E3%82%B9%E3%81%AB%E3%81%8A%E3%81%84%E3%81%A6%E4%BA%80%E8%A3%82%E7%99%BA%E7%94%9F%E3%82%92%E6%8A%91%E5%88%B6%E5%8F%AF%E8%83%BD%E3%81%AANi%E5%90%88%E9%87%91%E7%B5%84%E6%88%90%E3%81%AE%E6%8E%A2%E7%B4%A2.pdf): 報告書
## 使用方法
各最適化について、簡単な使い方を記述する。オルソ平衡、パラ平衡の使い方（スクリプトの実行方法など）に違いは無い。
### phase1: 解析１の最適化
### phase2: 解析２の最適化
* 作成して置くファイル
  + al.dat/ti.dat : 固定化したAlとTiの値を記述する。
* 実行
  ```
  $ sh go_opt.sh
  ``` 

## 結果ファイル
実行した後に作成されるファイルについて説明する。

### 共通なもの
* workflow_exec.dev-u-tokyo.mintsys.jp.log : ラン番号と実行時、パラメータ指定したポート名とその値を記録する。自動追加のみ行うので、手動で削除しない限り初期化されない。
