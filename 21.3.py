def swap(first_elem, second_elem):
    tempFirst = first_elem[:]
    tempSecond = second_elem[:]
    change(first_elem, tempSecond)
    change(second_elem, tempFirst)


def change(array, tempArr):
    for i in range(len(tempArr)):
        array[i] = tempArr[i]
    while len(array) != len(tempArr):
        array.pop(-1)


first = [1, 2, 3]
second = [4, 5, 6]
first_content = first[:]
second_content = second[:]
swap(first, second)
print(first, second_content, first == second_content)
print(second, first_content, second == first_content)
