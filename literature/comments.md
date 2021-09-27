# 文献阅读笔记

## 目录
- [文献阅读笔记](#文献阅读笔记)
  - [目录](#目录)
  - [SEQUENCE-BASED DEEP LEARNING ANTIBODY DESIGN FOR INSILICO ANTIBODY AFFINITY MATURATION](#sequence-based-deep-learning-antibody-design-for-insilico-antibody-affinity-maturation)


## SEQUENCE-BASED DEEP LEARNING ANTIBODY DESIGN FOR INSILICO ANTIBODY AFFINITY MATURATION
[原文](pdf/2103.03724.pdf)

|||
|:---:|---|
|预测内容|ΔΔG|
|数据集|AB-bind|
|方法|基于序列，但是用到了结构|

![](figure/2021-09-27%20154746.png)
说是基于序列，实际上是把序列看作两条链状的图，再根据复合物的结构加入额外的边，节点特征只使用氨基酸的 one-hot 编码，最后使用 `Hag-Net` 的图模型。