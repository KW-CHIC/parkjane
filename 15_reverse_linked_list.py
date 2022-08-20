#219p

# 아래와 같이 뜨는 NameError 해결해야 함.
# name 'ListNode' is not defined

def reverse_list(self, head : ListNode) -> ListNode:
    node, prev = head, None

    while node:
        next, node.next = node.next, prev
        prev, node = node, next
    return prev
