import time

def timeit(func):
    def timeit_wrapper(*args, **kwargs):
        start = time.time()
        run = func(*args, **kwargs)
        end = time.time()

        print('function: %r took: %2.4f sec' % (func.__name__, end-start))
        return run
    
    return timeit_wrapper

def read_file(file_name):
    with open(file_name, 'r') as f:
        text = f.read()
    return text.split("\n")

@timeit
def min_max(numbers):
    maximum = float("-inf")
    minimum = float("inf")
    i = 0
    while i < len(numbers):
        if not numbers[i]:
            break
        elif numbers[i] < minimum:
            minimum = numbers[i]
        elif numbers[i] > maximum:
            maximum = numbers[i]
        i += 1
    return minimum, maximum


def min_max_ascii(numbers):
    maximum = float("-inf")
    minimum = float("inf")
    i = 0
    while i < len(numbers):
        j = 0
        ascii_count = 0
        if not numbers[i]:
            break
        while j < len(numbers[i]):
            ascii_count += ord(numbers[i][j])
            j += 1
        if ascii_count < minimum:
            minimum = ascii_count
        elif ascii_count > maximum:
            maximum = ascii_count
        i += 1
    return minimum, maximum

@timeit
def bubble(numbers):
    i = 0
    swapped = False
    while i < len(numbers):
        j = 0
        while j < len(numbers)-i-1:
            if numbers[j] > numbers[j+1]:
                numbers[j+1], numbers[j] = numbers[j], numbers[j+1]
                swapped = True
            j += 1
        i += 1
        if not swapped:
            break
    return numbers

@timeit
def select(numbers):
    i = 0
    while i < len(numbers):
        minn_idx = i
        j = i+1
        while j < len(numbers):
            if numbers[j] < numbers[minn_idx]:
                minn_idx = j
            j += 1
        tmp = numbers[i]
        numbers[i] = numbers[minn_idx]
        numbers[minn_idx] = tmp

        i += 1
    return numbers

@timeit
def insert(numbers):
    i = 1
    while i < len(numbers):
        j = i-1
        while j >= 0 and numbers[j+1] < numbers[j]:
            numbers[j+1], numbers[j] = numbers[j], numbers[j+1]
            j -= 1
        i += 1
    return numbers

@timeit
def merge_sort(numbers):
    def merge_s(numbers):
        if len(numbers) > 1:
            mid = len(numbers) // 2
            l = numbers[:mid]
            r = numbers[mid:]
            merge_s(l)
            merge_s(r)

            merge(numbers, l, r)
    merge_s(numbers)

def merge(numbers, l, r):
    i = j = k = 0

    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            numbers[k] = l[i]
            i += 1
        else:
            numbers[k] = r[j]
            j += 1
        k += 1

    while i < len(l):
        numbers[k] = l[i]
        i += 1
        k += 1

    while j < len(r):
        numbers[k] = r[j]
        j += 1
        k += 1

@timeit
def count_sort(numbers):
    maximum = max(numbers)
    minimum = min(numbers)
    tmp = [0] * (maximum - minimum + 1)
    i = 0
    while i < len(numbers):
        tmp[numbers[i] - minimum] += 1
        i += 1
    i = 1
    while i < len(tmp):
        tmp[i] = tmp[i] + tmp[i-1] 
        i+= 1
    out = [0] * len(numbers)
    i = len(numbers) - 1
    while i >= 0:
        out[ tmp[numbers[i] - minimum] - 1] = numbers[i]
        tmp[numbers[i] - minimum] -= 1
        i -= 1    
    return out

@timeit
def bin_search(numbers, x):
    l, r = 0, len(numbers)
    while l <=r:
        mid = l+(r-l) // 2
        if numbers[mid] == x:
            return mid
        
        if x > numbers[mid]:
            l = mid +1
        else:
            r = mid -1 
    return -1



numbers = []
numbers.append(read_file("dane0.txt"))
# numbers.append(read_file("dane1.txt"))
# numbers.append(read_file("dane2.txt"))

for number_set in numbers:
    number_set.pop()
    number_set = list(map(int, number_set))
    print(min_max(number_set))
    # (bubble(number_set))
    (select(number_set))
    # (insert(number_set))
    # (merge_sort(number_set))
    # (count_sort(number_set))





