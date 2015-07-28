import unittest
from parse_csv import ParseCSV


class testParseCSVTest(unittest.TestCase):

    def setUp(self):
        self.data = './CSV_data/products.csv'
        self.test = ParseCSV(self.data)
        self.parsed_data = self.test.read_data()

    def test_csv_read_data_headers(self):
        self.assertEqual(
            self.parsed_data[0],
            ['Monday', 'Milk', '3',]
            )

    def test_csv_read_random_data_points(self):
        self.assertEqual(self.test.read_data()[1][0], 'Monday')
        self.assertEqual(self.test.read_data()[1][2], '7')

    # def get_min_difference(self, parsed_data, column1, column2):
    #     column1_list = [x[column1] for x in parsed_data[1:]]
    #     column2_list = [x[column2]for x in parsed_data[1:]]
    #     values = [float(x) - float(y) for x, y in zip(column1_list, column2_list)]
    #     return values.index(min(values))

if __name__ == '__main__':
    unittest.main()
