# k ближайших чисел
Задача: найти `k` чисел, ближайших к заданному значению, в *упорядоченном* массиве. Само значение может не встретиться в массиве.

Пример:
```python3
assert closest([1,4,8,10], target=2, count=3) == [1, 4, 8]
```

Решение должно иметь сложность O(log(n) + k).

Будьте внимательны с тестом `range`: в нём очень большой массив, который может и в память не влезть при попытке копирования.

Использовать модуль `bisect` в этом задании запрещено. Вспоминайте первую лекцию и реализуйте поиск самостоятельно.
