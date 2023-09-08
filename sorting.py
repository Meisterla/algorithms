import sys


def swap(list_: list, e1: int, e2: int):
    tmp = list_[e1]
    list_[e1] = list_[e2]
    list_[e2] = tmp
    return list_


def sawp2(list_: list, e1: int, e2: int):
    list_[e1] = list_[e1] ^ list_[e2]
    list_[e2] = list_[e1] ^ list_[e2]
    list_[e1] = list_[e1] ^ list_[e2]
    return list_


# 选择排序
def selection_sort(num_list):
    length = len(num_list)
    if length <= 1:
        return num_list

    for j in range(length):
        # 假设第一个元素为最小元素
        min_num_index = j

        # 遍历未排序区域元素，以此和未排序区域的第一个元素做对比
        for i in range(j + 1, length):
            if num_list[i] < num_list[min_num_index]:
                min_num_index = i

        num_list[min_num_index], num_list[j] = num_list[j], num_list[min_num_index]
#        num_list = swap(num_list, min_num_index, j)

    return num_list


# 冒泡排序
def bubble_sort(num_list):
    for i in range(len(num_list) - 1):
        flag = True  # 用order来记录这一趟是否发生了数字交换
        for j in range(len(num_list) - i - 1):
            if num_list[j] > num_list[j + 1]:
                num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]
                flag = False  # 若发生交换，改变flag变量的值
        if flag:
            # 若flag值没有发生变化，则证明本趟没有数字交换，此时数列已经有序，break退出排序
            break
    return num_list


# 插入排序
def insertion_sort(num_list):
    if len(num_list) <= 1:
        return num_list
    for i in range(1, len(num_list)):
        for j in reversed(range(0, i)):
            if num_list[j] > num_list[j+1]:
                swap(num_list, j, j+1)
    return num_list


def merge(left, right):
    ll, rr = 0, 0
    result = []
    while ll < len(left) and rr < len(right):
        if left[ll] < right[rr]:
            result.append(left[ll])
            ll += 1
        else:
            result.append(right[rr])
            rr += 1
    result += left[ll:]
    result += right[rr:]
    return result


# 归并排序
def merge_sort(num_list):
    if len(num_list) <= 1:
        return num_list
    num = len(num_list) // 2  # 从中间划分两个子序列
    left = merge_sort(num_list[:num])  # 对左侧子序列进行递归排序
    right = merge_sort(num_list[num:])  # 对右侧子序列进行递归排序
    return merge(left, right)  # 归并


# 快速排序
def quick_sort(num_list, start, end):
    if start >= end:
        return
    mid_data, left, right = num_list[start], start, end
    while left < right:
        while num_list[right] >= mid_data and left < right:
            right -= 1
        num_list[left] = num_list[right]
        while num_list[left] < mid_data and left < right:
            left += 1
        num_list[right] = num_list[left]
    num_list[left] = mid_data
    quick_sort(num_list, start, left-1)
    quick_sort(num_list, left+1, end)
    return num_list


def heap_insert(num_list, index):
    while num_list[index] > num_list[int((index-1)/2)]:
        swap(num_list, index, int((index-1)/2))
        index = int((index-1)/2)


# 堆排序
def heapify(num_list, index, heap_size):
    left = index * 2 + 1
    right = left + 1
    while left < heap_size:
        largest = right if right < heap_size and num_list[left] < num_list[right] else left
        largest = largest if num_list[largest] > num_list[index] else index
        if largest == index:
            break
        swap(num_list, largest, index)
        index = largest
        left = index * 2 + 1
        right = left + 1


def heap_sort(num_list):
    heap_size = len(num_list) - 1
    if len(num_list) <= 1:
        return num_list
    for i in range(0, len(num_list)):
        heap_insert(num_list, i)
    swap(num_list, 0, heap_size)
    heap_size -= 1
    while heap_size > 0:
        heapify(num_list, 0, heap_size)
        swap(num_list, 0, heap_size)
        heap_size -= 1
    return num_list


if __name__ == '__main__':
    a = [1, 3, 2, 6, 4, 12, 33, 5, 25, 3, 23, 43, 34]
    print(a)
    print(selection_sort(a.copy()))
    print(bubble_sort(a.copy()))
    print(insertion_sort(a.copy()))
    print(merge_sort(a.copy()))
    print(quick_sort(a.copy(), 0, len(a)-1))
    print(heap_sort(a.copy()))
