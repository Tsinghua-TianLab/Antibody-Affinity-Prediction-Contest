# Copyright (c) 2021, TianLab@THU
# File       : data_interface.py
# Created at : 2021-09-28 19:50:27
# Author     : QiuKe <qk21@mails.tsinghua.edu.cn>
# Description: Package file for datset implementation submodule.

from .example_dataset import ExampleDataset

datasets_define = {
    ExampleDataset.get_dataset_name(): ExampleDataset
}
