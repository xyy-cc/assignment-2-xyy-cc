"""
Part E: Write two tests of your own.

The provided tests are good, but they can't think of everything. Add one test
for your array list and one for your linked list. Each should check something
the provided tests do not check directly. Ideas:
  * a case you were unsure about while writing your code
  * a longer or stranger sequence of operations
  * a check on 'moves' or 'size' that you worked out on paper in Part A
Give each test a name that says what it checks, replace the `self.fail(...)`
line, and make sure it PASSES with your code.

A test is a method whose name starts with `test_`, inside a class that extends
unittest.TestCase. A good one has three steps: set up, execute, check.

    def test_removing_the_only_value_leaves_the_list_empty(self):
        lst = create_array_list()                       # 1. set up
        array_list_insert_at(lst, 0, 'only')
        removed = array_list_remove_at(lst, 0)          # 2. execute
        self.assertEqual('only', removed)               # 3. check
        self.assertEqual(0, array_list_length(lst))
        assert_array_list_valid(lst)

(That one is an example -- write a different test.)

Useful checks:  self.assertEqual(expected, actual)    self.assertTrue(x)
                self.assertIsNone(x)    self.assertIs(a, b)
                with self.assertRaises(IndexError):  <code that should raise>

Run with:  python3 student_tests.py
"""
import unittest

from array_list import *
from linked_list import *
from list_checks import assert_array_list_valid, assert_linked_list_valid


class MyArrayListTests(unittest.TestCase):

    def test_array_list_multiple_grows_and_moves_count(self):
        """
        Tests that multiple consecutive grows in an Array List update capacity,
        length, moves count, and internal structure correctly.
        """
        # 1. Set up
        lst = create_array_list(capacity=2)

        # 2. Execute: Insert 5 elements sequentially at the end
        # (Triggers two grows: capacity 2 -> 4 -> 8)
        values = ['a', 'b', 'c', 'd', 'e']
        for i in range(len(values)):
            array_list_insert_at(lst, i, values[i])

        # 3. Check:
        # - Length 5
        self.assertEqual(5, array_list_length(lst))
        # - Capacity 8
        self.assertEqual(8, len(lst[ARRAY_DATA_KEY]))
        # - 6 moves
        self.assertEqual(6, lst[ARRAY_MOVES_KEY])
        # - Verify:
        self.assertEqual(['a', 'b', 'c', 'd', 'e'], array_list_to_python_list(lst))
        # - Validate structure integrity
        assert_array_list_valid(lst)


class MyLinkedListTests(unittest.TestCase):

    def test_linked_list_reverse_then_insert_at_head_and_tail(self):
        """
        Tests that inserting at the head and tail of a Linked List
        after an in-place reverse correctly maintains head pointer and size.
        """
        # 1. Set up
        lst = create_linked_list()
        linked_list_insert_at(lst, 0, 1)
        linked_list_insert_at(lst, 1, 2)
        linked_list_insert_at(lst, 2, 3)

        # 2. Execute: Reverse the list
        linked_list_reverse(lst)
        # Insert 99 at the new head
        linked_list_insert_at(lst, 0, 99)
        # Insert 88 at the new tail
        linked_list_insert_at(lst, 4, 88)

        # 3. Check:
        self.assertEqual(5, linked_list_length(lst))
        self.assertEqual([99, 3, 2, 1, 88], linked_list_to_python_list(lst))
        self.assertEqual(99, linked_list_get(lst, 0))
        self.assertEqual(88, linked_list_get(lst, 4))
        assert_linked_list_valid(lst)

if __name__ == '__main__':
    unittest.main()
