# 文献阅读笔记

## 目录
- [文献阅读笔记](#文献阅读笔记)
  - [目录](#目录)
  - [SEQUENCE-BASED DEEP LEARNING ANTIBODY DESIGN FOR INSILICO ANTIBODY AFFINITY MATURATION](#sequence-based-deep-learning-antibody-design-for-insilico-antibody-affinity-maturation)
  - [Deep learning enables therapeutic antibody optimization in mammalian cells by deciphering high-dimensional protein sequence space](#deep-learning-enables-therapeutic-antibody-optimization-in-mammalian-cells-by-deciphering-high-dimensional-protein-sequence-space)


## SEQUENCE-BASED DEEP LEARNING ANTIBODY DESIGN FOR INSILICO ANTIBODY AFFINITY MATURATION
[原文](pdf/2103.03724.pdf)

|||
|:---:|---|
|预测内容|ΔΔG|
|数据集|AB-bind|
|方法|基于序列，但是用到了结构|

![](figure/2021-09-27%20154746.png)
说是基于序列，实际上是把序列看作两条链状的图，再根据复合物的结构加入额外的边，节点特征只使用氨基酸的 one-hot 编码，最后使用 `Hag-Net` 的图模型。

---
## Deep learning enables therapeutic antibody optimization in mammalian cells by deciphering high-dimensional protein sequence space
[原文](pdf/617860v2.full.pdf)

|||
|:---:|---|
|预测内容|对一个HER2抗体的优化|
|数据集|基于实验生成|
|方法|完全基于序列|

![](figure/2021-09-27%20163346.png)
利用 CRISPR-Cas9 homology-durected mutagenesis，结合 deep mutational scanning 获取到的 CDR 区域关键氨基酸，来产生一个点突变库。使用的网络相当初级，且是定长的，我认为此文献没有太大价值。