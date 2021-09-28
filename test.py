import unittest

from affinity_prediction.data import get_dataset

class Test(unittest.TestCase):
    def test_dataset(self):
        example_dataset = get_dataset('example', './example_dataset')
        print(example_dataset.get_dataset_data_structure())
        for index, data in enumerate(example_dataset):
            print(f'-----{index}-----')
            print(f'affinity: {data.affinity}')
            print('chain_a:')
            print(data.chain_a.sequence)
            for item in data.chain_a:
                print(item)
            print('chain_b:')
            print(data.chain_b.sequence)
            for item in data.chain_b:
                print(item)


if __name__ == '__main__':
    unittest.main(verbosity=1)
