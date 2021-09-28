# Copyright (c) 2021, TianLab@THU
# File       : datasets.py
# Created at : 2021-09-27 21:51:50
# Author     : QiuKe <qk21@mails.tsinghua.edu.cn>
# Description: An interface for all datasets.

import abc
from typing import Dict, Union

from . import datasets_impl
from .data_interface import AbstractData


class Dataset(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __init__(self, data_dir: str, *args, **kvargs):
        pass
    
    @abc.abstractmethod
    def _get_dataset_size(self) -> int:
        pass
    
    @abc.abstractmethod
    def _get_data_by_index(self, index: int) -> AbstractData:
        pass
    
    @abc.abstractclassmethod
    def get_dataset_name() -> str:
        pass
    
    def get_dataset_data_structure(self) -> Dict[str, Union[type, Dict]]:
        return self._get_data_by_index(0).get_data_structure()

    def __iter__(self):
        for i in range(self._get_dataset_size()):
            yield self._get_data_by_index(i)
