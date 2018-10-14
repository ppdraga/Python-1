# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    def elem_fibonacci(num):
        if (num == 1) | (num == 2):
            return 1
        else:
            return elem_fibonacci(num - 1) + elem_fibonacci(num - 2)
    series = []
    if m < n :
        pass
    elif m == n :
        series.append(elem_fibonacci(n))
    else:
        series.append(elem_fibonacci(n))
        series.append(elem_fibonacci(n+1))
        counter = m - n - 1
        idx = 2
        while counter > 0:
            series.append(series[idx-1] + series[idx-2])
            counter -= 1
            idx += 1
    return series
print(fibonacci(3,7))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()
li = [5,2,7,4,0,9,8,6] 


def sort_to_max(origin_list):
    n = 1 
    length_array = len(origin_list)
    while n < length_array:
        for i in range(length_array-n):
            if origin_list[i] > origin_list[i+1]:
                origin_list[i], origin_list[i+1] = origin_list[i+1], origin_list[i]
        n += 1

list0 = [2, 10, -12, 2.5, 20, -11, 4, 4, 0]
sort_to_max(list0)
print(list0)

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.
def my_filter(lambda_f, array):
    result = []
    for elem in array:
        if lambda_f(elem):
            result.append(elem)
    return result

numbers = [10, -4, 2, -1, 6]
list0 = list(my_filter(lambda x: x < 0, numbers))
print(list0)

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.
A1 = [1,0]
A2 = [2,2]
A3 = [4,3]
A4 = [3,1]

def is_parallelogram(A1,A2,A3,A4):
    A1A2 = [A2[0]-A1[0],A2[1]-A1[1]]
    A3A4 = [A4[0]-A3[0],A4[1]-A3[1]]
    A1A4 = [A4[0]-A1[0],A4[1]-A1[1]]
    A2A3 = [A3[0]-A2[0],A3[1]-A2[1]]
    if ((A1A2[0]*A3A4[1]-A1A2[1]*A3A4[0]) == 0 ) & ((A1A4[0]*A2A3[1]-A1A4[1]*A2A3[0]) == 0 ):
        return True
    else:
        return False

print(is_parallelogram(A1,A2,A3,A4))