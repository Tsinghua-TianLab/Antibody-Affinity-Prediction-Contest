# Copyright (c) 2021, TianLab@THU
# File       : __init__.py
# Created at : 2021-09-27 21:51:31
# Author     : QiuKe <qk21@mails.tsinghua.edu.cn>
# Description: Package file for data submodule.

from .datasets_impl import datasets_define
from .datasets import Dataset


def get_dataset(dataset_name: str, data_dir: str, *args, **kvargs) -> Dataset:
    return datasets_define[dataset_name](data_dir, *args, **kvargs)

__all__ = ['get_dataset']
