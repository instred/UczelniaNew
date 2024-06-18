from typing import Tuple, List
from pandas import read_csv
import numpy as np


"""
Problem plecakowy

Mamy plecak z określoną dozwoloną jego wagą (np. w kg), mamy też listę przedmiotów - każdy ze swoją wagą oraz wartością.
Naszym zadaniem jest znaleźć możliwie jak najcenniejszy ładunek który zmieści się wagowo w naszym plecaku.

Zadanie te można rozwiązać klasycznym brute force'm - znajduje on rozwiązanie optymalne, jednak czasowo jest to O(2^n)
Mamy też możliwość zastosowania algorytmów aproksymacyjnych (tak jak w zadaniu z komiwojażerem)

Ja postanowiłem rozwiązać to zadanie za pomocą programowania dynamicznego.
Polega to na rozbiciu problemu na sub-problemy i rozwiązywaniu ich.
Algorytm inicjalizuje sobie macierz z zerami, macierz będzie rozmiaru w x n, gdzie w jest maksymalną wagą a n ilością przedmiotów (0 do n to ich indeksy)
Następnie rozwiązuje każdy sub-problem zaczynając od pierwszego przedmiotu i idą pokolei przez wagi 1 do w

Gdy nasza macierz zostanie zapełniona, możemy po prostu zwrócić wartość pod szukanym indeksem - to nasze rozwiązanie.
Dane wczytuje z pliku csv przy pomocy pandas, następnie zamieniam ją na liste par waga-wartosc, macierz inicjalizuje zerami za pomocą numpy

Złożoność algorytmu można opisać jako czasowo O(n*w), pamięciowo O(n*w) - obliczenia i miejsce zależy od wielkości naszej macierzy
"""



# Func for reading the csv with data
def read_file(file_name: str) -> List[Tuple[int, int]]:
    
    df = read_csv(file_name)
    tuple_list = list(df[['Waga', 'Wartosc']].itertuples(index=False, name=None))
    return tuple_list



def knapsack(items: List[Tuple[int, int]], weight: int) -> int:
    n = len(items)

    # initialize the matrix with zeros
    matrix = np.zeros((n + 1, weight + 1))

    # iterate through each subproblem to fill the cache
    for i in range(1, n + 1):
        for w in range(weight + 1):
            item_weight, item_value = items[i - 1]

            # if the item is heavier than our current weight, then insert same cache as for the i-1th item, 
            # else insert max from i-1th item with current weight and i-1th item with weight - current weight + its value
            if item_weight > w:
                matrix[i, w] = matrix[i - 1, w]
            else:
                matrix[i, w] = max(matrix[i - 1, w], matrix[i - 1, w - item_weight] + item_value)

    # showing the matrix table
    # print(matrix) 
    return int(matrix[n, weight])



if __name__ == '__main__':
    file_name = 'data.csv'
    data = read_file(file_name)
    # print(data)

    print(knapsack(data, 13))
