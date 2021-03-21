import unittest
import csv
from Calculator import Calculator

test_data_file_object = None


def load_test_data_into_list(test_data_file_path):
    global test_data_file_object
    my_list = list()
    test_data_file_object = open(test_data_file_path, 'r')
    csv_reader = csv.reader(test_data_file_object, delimiter=',')
    for row in csv_reader:
        my_list.append(row)
    test_data_file_object.close()
    test_data_file_object = None
    return my_list


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def tearDown(self) -> None:
        if self.calculator is not None:
            self.calculator = None

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_add_method_calculator(self):
        test_data = load_test_data_into_list('../tests/Unit Test Addition.csv')
        for row in test_data:
            result = self.calculator.add(row[0], row[1])
            self.assertEqual(float(result), float(row[2]))

    def test_subtraction_method_calculator(self):
        test_data = load_test_data_into_list('../tests/Unit Test Subtraction.csv')
        for row in test_data:
            result = self.calculator.subtract(row[0], row[1])
            self.assertEqual(float(result), float(row[2]))

    def test_multiplication_method_calculator(self):
        test_data = load_test_data_into_list('../tests/Unit Test Multiplication.csv')
        for row in test_data:
            result = self.calculator.multiply(row[0], row[1])
            self.assertEqual(float(result), float(row[2]))

    def test_division_method_calculator(self):
        test_data = load_test_data_into_list('../tests/Unit Test Division.csv')
        for row in test_data:
            result = self.calculator.divide(row[0], row[1])
            self.assertEqual(float(result), float(row[2]))

    def test_square_method_calculator(self):
        test_data = load_test_data_into_list('../tests/Unit Test Square.csv')
        for row in test_data:
            result = self.calculator.square(row[0])
            self.assertEqual(float(result), float(row[1]))

    def test_square_root_method_calculator(self):
        test_data = load_test_data_into_list('../tests/Unit Test Square Root.csv')
        for row in test_data:
            result = self.calculator.square_root(row[0])
            self.assertEqual(float(result), float(row[1]))


if __name__ == '__main__':
    unittest.main()
