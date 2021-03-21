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
            x = row[0]
            y = row[1]
            expect_result = row[2]
            result = self.calculator.add(x, y)
            self.assertEqual(float(result), float(expect_result))

    def test_subtraction_method_calculator(self):
        test_data = load_test_data_into_list('../tests/Unit Test Subtraction.csv')
        for row in test_data:
            x = row[0]
            y = row[1]
            expect_result = row[2]
            result = self.calculator.subtract(x, y)
            self.assertEqual(float(result), float(expect_result))

    def test_multiplication_method_calculator(self):
        test_data = load_test_data_into_list('../tests/Unit Test Multiplication.csv')
        for row in test_data:
            x = row[0]
            y = row[1]
            expect_result = row[2]
            result = self.calculator.multiply(x, y)
            self.assertEqual(float(result), float(expect_result))

    def test_division_method_calculator(self):
        test_data = load_test_data_into_list('../tests/Unit Test Division.csv')
        for row in test_data:
            x = row[0]
            y = row[1]
            expect_result = row[2]
            result = self.calculator.divide(x, y)
            self.assertEqual(float(result), float(expect_result))


if __name__ == '__main__':
    unittest.main()
