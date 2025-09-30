class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_two_lists_with_dummy(list1, list2):
    dummy = ListNode()
    current = dummy
    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    current.next = list1 if list1 else list2
    return dummy.next


def merge_two_lists_without_dummy(list1, list2):
    if not list1:
        return list2
    if not list2:
        return list1
    if list1.val < list2.val:
        list1.next = merge_two_lists_without_dummy(list1.next, list2)
        return list1
    else:
        list2.next = merge_two_lists_without_dummy(list1, list2.next)
        return list2
