# ワークフローを利用した最適化のいろいろ
ワークフローAPIを利用して、dakotaやbayes推定によるさまざまな金属工学的な問題の最適化ワークベンチ。

## 概要
金属工学的な問題をDakotaやbayes推定を用いて最適化を行う。最適化の対象はワークフローに実装したさまざまなソルバー（溶接シミュレーションや凝固計算など）をワークフローで用意し、基本的に全てワークフローAPIを経由して実行する。そのためのスクリプトなどを格納する。


## 履歴
* 2019年11月11日：Ni合金探索を最初の項目として挙げる。
* 2019年11月12日：SYSWELDをDakotaで最適化を挙げる
* 2019年11月12日：Rosenbrock関数をbayesとDakotaで最適化を挙げる

### 内容

* drive_sysweldWF_by_dakota_via_WF-API
  + SYSWELDをDakotaで最適化するためのスクリプト群
  + [概要や結果（Wiki）](https://github.com/materialsintegration/optimization_by_sipmi/wiki/Dakota%E3%81%A8SYSWELD%E3%82%92%E5%88%A9%E7%94%A8%E3%81%97%E3%81%9F%E6%9C%80%E9%81%A9%E5%8C%96%E3%81%AE%E3%81%BE%E3%81%A8%E3%82%81)
* seach_of_alloy_for_Ni_using_optimization:
  + 最適なNi合金探索のためのスクリプト群
  + [概要とまとめ（PDF）](https://github.com/materialsintegration/optimization_by_sipmi/blob/master/seach_of_alloy_for_Ni_using_optimization/3D%E7%A9%8D%E5%B1%A4%E9%80%A0%E5%BD%A2%E3%83%97%E3%83%AD%E3%82%BB%E3%82%B9%E3%81%AB%E3%81%8A%E3%81%84%E3%81%A6%E4%BA%80%E8%A3%82%E7%99%BA%E7%94%9F%E3%82%92%E6%8A%91%E5%88%B6%E5%8F%AF%E8%83%BD%E3%81%AANi%E5%90%88%E9%87%91%E7%B5%84%E6%88%90%E3%81%AE%E6%8E%A2%E7%B4%A2.pdf)
* Rosenbrock_py_bayes
  + Rosenbrock関数の最適化をbayes推定とDakotaの組み合わせで行ったスクリプト群
  + [概要とまとめ（Wiki）](https://github.com/materialsintegration/optimization_by_sipmi/wiki/Rosenbrock%E3%82%92bayes%E6%8E%A8%E5%AE%9A%E3%81%A8Dakota%E3%81%A7%E6%9C%80%E9%81%A9%E5%8C%96%E3%81%97%E3%81%9F%E3%81%BE%E3%81%A8%E3%82%81)
