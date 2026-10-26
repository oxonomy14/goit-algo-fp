from module.linked_list import Node


def get_middle(head):
    """Знаходить середину зв'язного списку."""
    slow = head
    fast = head.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


def merge_sorted_lists(left, right):
    """Об'єднує два відсортовані зв'язні списки."""
    dummy = Node()
    tail = dummy

    while left and right:
        if left.data <= right.data:
            tail.next = left
            left = left.next
        else:
            tail.next = right
            right = right.next

        tail = tail.next

    # Приєднуємо вузли, що залишилися
    if left:
        tail.next = left
    else:
        tail.next = right

    return dummy.next


def merge_sort_linked_list(head):
    """Сортує зв'язний список злиттям."""
    if head is None or head.next is None:
        return head

    # 1. Знаходимо середину
    middle = get_middle(head)

    # 2. Розділяємо список на дві частини
    right = middle.next
    middle.next = None
    left = head

    # 3. Рекурсивно сортуємо обидві частини
    left = merge_sort_linked_list(left)
    right = merge_sort_linked_list(right)

    # 4. Об'єднуємо відсортовані частини
    return merge_sorted_lists(left, right)
