#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def listToArray(self, head: Optional[ListNode]) -> List[Optional[ListNode]]:
        if head is None:
            return []
        array = []
        temp = head
        while temp is not None:
            array.append(temp.val)
            temp = temp.next
        
        return array
    def returnListPartsFromArray(self, arrayList) -> Optional[ListNode]:
        if(len(arrayList) < 0):
            return
        head = ListNode(arrayList[0])
        temp = head
        for i in arrayList[1 : ]:
            temp.next = ListNode(arrayList[i])
            temp = temp.next
        return head
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        count = 0
        temp = head
        array = []
        returnArr = []
        array = self.listToArray(head)
        length = len(array)
        r = length % k
        partSize = length // k
        j = 0
        for i in range(k):
            if(j > length):
                returnArr.append([])
                continue
            if(r > 0):
                returnArr.append(self.returnListPartsFromArray(array[j : j + partSize + 1]))
                j = j + partSize + 1
                r -= 1
            else:
                returnArr.append(self.returnListPartsFromArray(array[j : j + partSize]))
                j = j + partSize
        return returnArr

class Solution2:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        res = []
        count = 0
        cur = head
        while cur:
            count += 1
            cur = cur.next
        group_size = count//k
        rest = count % k
        cur=head
        while cur:
            res.append(cur)
            for i in range(group_size-1):
                cur = cur.next
            if group_size > 0 and rest > 0:
                cur = cur.next
                rest -= 1
            next_cur = cur.next
            cur.next = None
            cur = next_cur
        for i in range(len(res), k):
            res.append(None)
        return res