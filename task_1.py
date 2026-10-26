from module.linked_list import LinkedList
from module.merge_sort_linked_list import merge_sorted_lists

llist = LinkedList()

# Вставляємо вузли в початок
llist.insert_at_beginning(5)
llist.insert_at_beginning(15)
llist.insert_at_beginning(10)
llist.insert_at_beginning(17)
llist.insert_at_beginning(19)

# Вставляємо вузли в кінець
llist.insert_at_end(20)
llist.insert_at_end(27)
llist.insert_at_end(25)
llist.insert_at_end(23)
llist.insert_at_end(71)

# Друк зв'язного списку
print("Початковий зв'язний список:")
llist.print_list()

print("Реверсний зв'язний список:")
llist.reverse()
llist.print_list()

llist.sort()

print("Відсортований зв'язний список:")
llist.print_list()

# Створюємо два відсортовані зв'язні списки
list1 = LinkedList()
for value in [1, 4, 7, 10]:
    list1.insert_at_end(value)

list2 = LinkedList()
for value in [2, 3, 8, 12]:
    list2.insert_at_end(value)

print("Перший відсортований список:")
list1.print_list()

print("Другий відсортований список:")
list2.print_list()

# Об'єднуємо списки
merged_head = merge_sorted_lists(list1.head, list2.head)

# Створюємо LinkedList для виведення результату
merged_list = LinkedList()
merged_list.head = merged_head

print("Об'єднаний відсортований список:")
merged_list.print_list()
