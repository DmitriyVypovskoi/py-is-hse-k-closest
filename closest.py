def closest(array: list, target: int, count: int) -> list:
    """Находит в упорядоченном массиве `array` `count` чисел, ближайших по значению к `target`.
    :param array: массив, в котором идёт поиск
    :param target: число, от которого отсчитываются ближайшие
    :param count: количество чисел, которые необходимо выдать
    """
    left = -1
    right = len(array)
    while right > left + 1:
        middle = (right + left) // 2
        if array[middle] > target:
            right = middle
        else:
            left = middle
    a = []
    if target in array:
        if count == 1:
            a.append(array[left])
        elif (left - count) >= -1:
            if target == array[0]:
                a = (array[:count + 1])
            if target == array[-1]:
                a = array[-count:]
            elif (abs(array[left - 2] - target)) < abs((array[left + 1] - target)):
                a = (array[left - (count) // 2 - 1: left + 1])
            else:
                a = (array[left - (count // 2):left + (count // 2) + 1])
                if len(a) < count:
                    i = 0
                    while len(a) != count:
                        a = (array[left - (count // 2) - i:left + (count // 2) + 1] + i)
                        i += 1
        if left == 0:
            a = (array[left:count])
        elif (left - count) <= -1:
            if target == array[0]:
                a = (array[:count + 1])
            if target == array[-1]:
                a = array[-count:]
            else:
                a = array[left-(count//2):left+(count//2)+1]
    if target not in array:
        if left < 0:
            a = array[:count // 2 + 1]
        elif array[left] < target:
            a = array[left - (count // 2) + 1:left + (count // 2) + 1]
            if left - count < -1:
                a = array[:count]
        elif array[left] > target:
            a = (array[left - (count // 2):left + (count // 2) + 1])
    if type(a) != list:
        i = []
        for k in a:
            i.append(k)
        a = i
    if count == len(array):
        a = array
    if target < array[0]:
        a = array[:count]
    if target > array[-1]:
        a = array[-count:]

    return a