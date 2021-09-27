from addinity_prediction.data.data_interface import PackedAttribute
import unittest

from addinity_prediction.data import Chain

class Test(unittest.TestCase):
    def test_chain_data_structure(self):
        chain = Chain(
            'ABDP',
            chain_id = PackedAttribute('Chain_id'),
            charge = [0, 0, -1, 1],
            linkage = [[1, 2], [0], [0], []]
        )
        print(chain.chain_id)
        print(chain.sequence)
        print(chain[1])
        print(chain['linkage'])
        print(len(chain))


if __name__ == '__main__':
    unittest.main(verbosity=1)
