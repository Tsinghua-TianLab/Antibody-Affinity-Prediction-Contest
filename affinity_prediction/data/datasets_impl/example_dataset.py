# 如何创建一个新的数据集呢？


from glob import glob
import os

from typing import overload, List

from ..data_interface import AbstractData, PackedAttribute
from ..datasets import Dataset

# 首先定义你要返回的数据结构
class Chain(AbstractData):
    def __init__(self, sequence: str, amino_acid_charges: List[int]):
        super().__init__(
            sequence = PackedAttribute(sequence), # 如果不希望一个列表被拆分为其中单个元素的
                                                  # 属性，使用`PackedAttribute`包裹它
            amino_acid = sequence,
            charge = amino_acid_charges
        )

class ChainAffinityData(AbstractData):
    def __init__(self, chain_a: Chain, chain_b: Chain, affinity: float):
        super().__init__(
            chain_a = chain_a,
            chain_b = chain_b,
            affinity = affinity
        )

# 继承 `Dataset` 类
class ExampleDataset(Dataset):
    def __init__(self, data_dir: str, *args, **kvargs):
        # 在此处下载一些需要的数据或者读取已有的数据
        self.data_dir = data_dir
        assert self.data_dir is not None
        self.__file_lists = glob(os.path.join(self.data_dir, '*.txt'))
        self.__amino_acid_charges = {
            'A': 0,
            'B': 0,
            'C': -1,
            'D': 1
        }
    
    def _get_dataset_size(self) -> int:
        # 你的数据集中有多少条数据
        return len(self.__file_lists)
    
    def _get_data_by_index(self, index: int) -> AbstractData:
        # 返回其中一条数据
        file_name = self.__file_lists[index]
        with open(file_name, 'r') as file:
            lines = [line.strip() for line in file.readlines()]
            return ChainAffinityData(
                Chain(lines[0], [self.__amino_acid_charges[aa] for aa in lines[0]]),
                Chain(lines[1], [self.__amino_acid_charges[aa] for aa in lines[1]]),
                float(lines[2])
            )
            
    def get_dataset_name() -> str:
        return 'example'

# 最后在本目录下的 __init__.py 中添加相关信息
