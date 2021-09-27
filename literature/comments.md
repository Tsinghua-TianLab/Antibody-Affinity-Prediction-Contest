# 文献阅读笔记

## 目录
- [文献阅读笔记](#文献阅读笔记)
  - [目录](#目录)
  - [SEQUENCE-BASED DEEP LEARNING ANTIBODY DESIGN FOR INSILICO ANTIBODY AFFINITY MATURATION](#sequence-based-deep-learning-antibody-design-for-insilico-antibody-affinity-maturation)
  - [Deep learning enables therapeutic antibody optimization in mammalian cells by deciphering high-dimensional protein sequence space](#deep-learning-enables-therapeutic-antibody-optimization-in-mammalian-cells-by-deciphering-high-dimensional-protein-sequence-space)
  - [Learning the protein language: Evolution, structure, and function](#learning-the-protein-language-evolution-structure-and-function)
  - [Mixture of Experts for Predicting Antibody-Antigen Binding Affinity from Antigen Sequence](#mixture-of-experts-for-predicting-antibody-antigen-binding-affinity-from-antigen-sequence)


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

---
## Learning the protein language: Evolution, structure, and function
[原文](pdf/learning_protein_sequence_embe.pdf)

[代码](https://github.com/tbepler/prose)

[前置文章：LEARNING PROTEIN SEQUENCE EMBEDDINGS USING INFORMATION FROM STRUCTURE](pdf/learning_protein_sequence_embe.pdf)

|||
|:---:|---|
|预测内容|序列的embedding|
|数据集|[SCOP](https://scop.mrc-lmb.cam.ac.uk/)|
|方法|基于语义模型，用结构信息监督学习|

![](figure/2021-09-27%20174608.png)

分为三层，首层为 `biLSTM` 作为 encoder，通过 mask-predict 任务来预训练。一些其他的文献中也使用 `doc2vec` 模型来直接做 encoder。后续使用此嵌入来进行包括预测结构和预测两条不同链之间相似性的工作。可能可以替换下游任务。

---
## Mixture of Experts for Predicting Antibody-Antigen Binding Affinity from Antigen Sequence
[原文](pdf/511360v1.full.pdf)

|||
|:---:|---|
|预测内容|多种抗体对新抗原的识别|
|数据集|[SCOP](https://scop.mrc-lmb.cam.ac.uk/)|
|方法|多专家系统、抗原序列|

对本课题意义不大，本文主要用于预测特定抗体对稍有变化的抗原的亲和力，每个抗体均训练一个专家模型，每个专家模型使L1正则化线性回归，完全只基于多种抗原对单个抗体的结合能信息和抗原本身的序列。