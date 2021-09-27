# 文献阅读笔记

## 目录
- [文献阅读笔记](#文献阅读笔记)
  - [目录](#目录)
  - [SEQUENCE-BASED DEEP LEARNING ANTIBODY DESIGN FOR INSILICO ANTIBODY AFFINITY MATURATION](#sequence-based-deep-learning-antibody-design-for-insilico-antibody-affinity-maturation)
  - [Deep learning enables therapeutic antibody optimization in mammalian cells by deciphering high-dimensional protein sequence space](#deep-learning-enables-therapeutic-antibody-optimization-in-mammalian-cells-by-deciphering-high-dimensional-protein-sequence-space)
  - [Learning the protein language: Evolution, structure, and function](#learning-the-protein-language-evolution-structure-and-function)
  - [Mixture of Experts for Predicting Antibody-Antigen Binding Affinity from Antigen Sequence](#mixture-of-experts-for-predicting-antibody-antigen-binding-affinity-from-antigen-sequence)
  - [DeepAffinity: Interpretable Deep Learning of Compound-Protein Affinity through Unified Recurrent and Convolutional Neural Networks](#deepaffinity-interpretable-deep-learning-of-compound-protein-affinity-through-unified-recurrent-and-convolutional-neural-networks)
  - [ChemBoost: A Chemical Language Based Approach for Protein – Ligand Binding Affinity Prediction](#chemboost-a-chemical-language-based-approach-for-protein--ligand-binding-affinity-prediction)


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
|数据集|HIV抗体|
|方法|多专家系统、抗原序列|

对本课题意义不大，本文主要用于预测特定抗体对稍有变化的抗原的亲和力，每个抗体均训练一个专家模型，每个专家模型使L1正则化线性回归，完全只基于多种抗原对单个抗体的结合能信息和抗原本身的序列。

---
## DeepAffinity: Interpretable Deep Learning of Compound-Protein Affinity through Unified Recurrent and Convolutional Neural Networks
[原文](pdf/btz111.pdf)

[代码](https://github.com/Shen-Lab/DeepAffinity)

|||
|:---:|---|
|预测内容|抗体-小分子亲和力|
|数据集|BindingDB|
|方法|基于子序列属性、小分子的SMILES做RNN-CNN|

![](figure/2021-09-27%20183023.png)

可以考虑使用其中的 structural property sequence 一起表示序列。首先用 seq2seq 这个 RNN 模型来无监督预训练所有序列（蛋白和小分子），其次是在其中encoder和decoder中间添加注意力机制。

## ChemBoost: A Chemical Language Based Approach for Protein – Ligand Binding Affinity Prediction
[原文](pdf/minf.202000212.pdf)

|||
|:---:|---|
|预测内容|蛋白-小分子亲和力（甚至可以预测没见过的序列）|
|数据集|KIBA bioactivity、binding DB|
|方法|小分子用语义模型，以此向量为中心表示蛋白|

文章中提到了两种蛋白的表示方法：Smith-Waterman、ProtVec，后续再看看。

用蛋白的所有ligend+其亲和力或者仅强的ligend的向量表示来向量化蛋白质本身。然后当回归问题做。

又提到一个网络DeepDTA。