# SinglyNode class creates a singly linked list
class SinglyNode:
    def __init__(self, val: int, next=None) -> None:
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)

# rearranges nodes around pivot, sorts the linked list
def partition(head, end):
    pivot = end
    prev, curr = None, head # to traverse the list
    tail = pivot
    new_head, new_end = None, None

    while curr != pivot:
        if curr.val < pivot.val:
            if new_head is None: # smaller than pivot are placed before that
                new_head = curr # First smaller node becomes new head
            prev = curr
        else:
            if prev: # greater than pivot, move it to the end
                prev.next = curr.next # detach it from its original position
            temp = curr.next
            curr.next = None
            tail.next = curr
            tail = curr
            curr = temp
            continue
        curr = curr.next

    if new_head is None:
        new_head = pivot # pivot is the smallest element
    new_end = tail

    return new_head, pivot, new_end

# recursively sorts the linked list with pivot node as the last node.
def quick_sort_rec(head, end):
    if not head or head == end:
        return head # base case, cannot sort the linked list anymore since it is empty or has only one node.

    new_head, pivot, new_end = partition(head, end)

    # recursively partition on the right
    if new_head != pivot:
        temp = new_head
        while temp.next != pivot:
            temp = temp.next # last node
        temp.next = None
        new_head = quick_sort_rec(new_head, temp)
        temp = new_head
        while temp.next:
            temp = temp.next
        temp.next = pivot

    # recursively partition on the right
    pivot.next = quick_sort_rec(pivot.next, new_end)

    return new_head

# makes function call to quick_sort_rec()
def quick_sort(head):
    if not head or not head.next:
        return head # base case, linked list is empty or has only one node

    end = head
    while end.next:
        end = end.next # last node, pivot node
    return quick_sort_rec(head, end)

if __name__ == "__main__":

    # create an unsorted linked list
    Head = SinglyNode(4)
    A = SinglyNode(2)
    B = SinglyNode(8)
    C = SinglyNode(5)
    D = SinglyNode(1)
    E = SinglyNode(7)
    F = SinglyNode(3)
    G = SinglyNode(6)

    Head.next = A
    A.next = B
    B.next = C
    C.next = D
    D.next = E
    E.next = F
    F.next = G

    print("Linked list before sorting")

    curr = Head
    while curr:
        print(curr.val, end=" ")
        curr = curr.next
    print("\n")

    sorted_head = quick_sort(Head)

    print("Linked list after sorting")

    curr = sorted_head
    while curr:
        print(curr.val, end=" ")
        curr = curr.next
