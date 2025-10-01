import unittest
from .merge_lists import merge_two_lists_with_dummy, ListNode


def list_to_linked_list(array):
    dummy = ListNode()
    current = dummy
    for value in array:
        current.next = ListNode(value)
        current = current.next
    return dummy.next


def linked_list_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


class TestMergeLists(unittest.TestCase):
    def test_merge_with_dummy(self):
        list1 = list_to_linked_list([1, 2, 4])
        list2 = list_to_linked_list([0, 4, 7])
        merged_1 = merge_two_lists_with_dummy(list1, list2)
        self.assertEqual(linked_list_to_list(merged_1), [0, 1, 2, 4, 4, 7])
        merged_2 = merge_two_lists_with_dummy(list_to_linked_list([]), list_to_linked_list([]))
        self.assertEqual(linked_list_to_list(merged_2), [])
        merged_3 = merge_two_lists_with_dummy(list_to_linked_list([]), list_to_linked_list([1]))
        self.assertEqual(linked_list_to_list(merged_3), [1])
        merged_4 = merge_two_lists_with_dummy(list_to_linked_list([1]), list_to_linked_list([]))
        self.assertEqual(linked_list_to_list(merged_4), [1])

if __name__ == '__main__':
    unittest.main()
