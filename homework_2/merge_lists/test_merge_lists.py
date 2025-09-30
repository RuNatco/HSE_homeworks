import unittest
from .merge_lists import merge_two_lists_with_dummy, merge_two_lists_without_dummy, ListNode


def list_to_linked_list(lst):
    dummy = ListNode()
    current = dummy
    for value in lst:
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
        list2 = list_to_linked_list([1, 3, 4])
        merged = merge_two_lists_with_dummy(list1, list2)
        self.assertEqual(linked_list_to_list(merged), [1, 1, 2, 3, 4, 4])

    def test_merge_without_dummy(self):
        list1 = list_to_linked_list([1, 2, 4])
        list2 = list_to_linked_list([1, 3, 4])
        merged = merge_two_lists_without_dummy(list1, list2)
        self.assertEqual(linked_list_to_list(merged), [1, 1, 2, 3, 4, 4])

if __name__ == '__main__':
    unittest.main()
