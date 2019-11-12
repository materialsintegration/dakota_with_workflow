# ワークフローを利用した最適化のいろいろ
ワークフローAPIを利用して、dakotaやbayes推定によるさまざまな金属工学的な問題の最適化ワークベンチ。

## 概要
金属工学的な問題をDakotaやbayes推定を用いて最適化を行う。最適化の対象はワークフローに実装したさまざまなソルバー（溶接シミュレーションや凝固計算など）をワークフローで用意し、基本的に全てワークフローAPIを経由して実行する。そのためのスクリプトなどを格納する。


## 履歴
* 2019年11月11日：Ni合金探索を最初の項目として挙げる。
* 2019年11月12日：SYSWELDをDakotaで最適化を挙げる

### 内容

* drive_sysweldWF_by_dakota_via_WF-API
  + SYSWELDをDakotaで最適化するためのスクリプト群
  + [概要や結果](https://github.com/materialsintegration/optimization_by_sipmi/wiki/Dakota%E3%81%A8SYSWELD%E3%82%92%E5%88%A9%E7%94%A8%E3%81%97%E3%81%9F%E6%9C%80%E9%81%A9%E5%8C%96%E3%81%AE%E3%81%BE%E3%81%A8%E3%82%81)
* seach_of_alloy_for_Ni_using_optimization:
  + 最適なNi合金探索のためのスクリプト群

