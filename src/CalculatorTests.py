import unittest
import csv
from Calculator import Calculator

test_data_file_object = None
test_data_row_list = list()


def load_test_data(test_data_file_path):
    global test_data_file_object, test_data_row_list
    test_data_file_object = open(test_data_file_path, 'r')
    csv_reader = csv.reader(test_data_file_object, delimiter=',')
    for row in csv_reader:
        test_data_row_list.append(row)


def close_test_data_file():
    global test_data_file_object
    if test_data_file_object is not None:
        test_data_file_object.close()
        test_data_file_object = None


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def tearDown(self) -> None:
        if self.calculator is not None:
            self.calculator = None
        close_test_data_file()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_add_method_calculator(self):
        load_test_data('../tests/Unit Test Addition.csv')
        for row in test_data_row_list:
            x = row[0]
            y = row[1]
            expect_result = row[2]
            result = self.calculator.add(x, y)
            self.assertEqual(float(result), float(expect_result))


if __name__ == '__main__':
    unittest.main()
