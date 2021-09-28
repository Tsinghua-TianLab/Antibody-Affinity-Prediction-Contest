# Copyright (c) 2021, TianLab@THU
# File       : data_interface.py
# Created at : 2021-09-27 21:51:50
# Author     : QiuKe <qk21@mails.tsinghua.edu.cn>
# Description: An interface for structural and sequencial information of proteins.

from typing import Any, Dict, List, Optional, Union


class PackedAttribute:
    def __init__(self, value: Any):
        self._value = value

    def unpack(self) -> Any:
        return self._value


class AbstractData:
    def __init__(self, **attributes):
        self._element_attr_length: Optional[int] = 0
        self._element_attr: Dict[str, List[Any]] = {}
        self._global_attr: Dict[str, Any] = {}

        for k, v in attributes.items():
            if v is None:
                continue
            if hasattr(v, '__len__'):
                if self._element_attr_length == 0:
                    self._element_attr_length = len(v)
                assert self._element_attr_length == len(v)
                self._element_attr[k] = v
            else:
                self._global_attr[k] = v if not isinstance(v, PackedAttribute) else v.unpack()

    
    def global_keys(self) -> List[str]:
        return self._global_attr.keys()
    
    def element_keys(self) -> List[str]:
        return self._element_attr.keys()

    def keys(self) -> List[str]:
        return [*self.global_keys(), *self.element_keys()]

    def __getitem__(self, index_or_attr_key: Union[int, str]) -> Dict[str, Any]:
        if isinstance(index_or_attr_key, str):
            return getattr(self, index_or_attr_key)
        if isinstance(index_or_attr_key, int):
            return {
                k: v[index_or_attr_key] for k, v in self._element_attr.items()
            }
        raise KeyError(f'Cannot use {type(index_or_attr_key)} as a key.')
        
    def __getattribute__(self, name: str) -> Any:
        try:
            return super().__getattribute__(name)
        except:
            try:
                return self._element_attr[name]
            except KeyError:
                try:
                    return self._global_attr[name]
                except KeyError:
                    raise AttributeError
    
    def get_elements_size(self) -> int:
        return self._element_attr_length
    
    def get_data_structure(self) -> Dict:
        structure = {
            'global': {},
            'element': {}
        }
        for key, value in self._global_attr.items():
            structure['global'][key] = value.get_data_structure() if isinstance(value, AbstractData) else type(value)
        for key, values in self._element_attr.items():
            value = values[0]
            structure['element'][key] = value.get_data_structure() if isinstance(value, AbstractData) else type(value)
        return structure
