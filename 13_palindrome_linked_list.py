#201p

#linked list는 가장 크게 Node들로 구성이 되고 Node는 노드가 가지는 값과 다음 노드가 어떻 녀석인지에 대한 부분(Next)으로 나누어지고 
#리스트의 가장 마지막 녀석의 Next는 Null값이다.
def is_palindrome(head: ListNode) -> bool:
  q = []
  if not head:
    return True
  
  node = head
  #연결 리스트를 파이썬의 리스트로 변환
  while node is not None:
    q.append(node.val)
    node = node.next
    
  #팰린드롬 판별
  while len(q) > 1: 
    if q.pop(0) != q.pop():
      return False
    
  return True
  
  
