list = [
    "Word1",
    "Word11",
    "Word111",
    "Word1111",
    "Word11111",
    "Word111111",
    "Word1111111",
]

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2
    left_half = arr[:middle]
    right_half = arr[middle:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Злиття
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if len(left[i]) <= len(right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

# Приклад використання




def sort_in_list(list):
    result = merge_sort(list)

    return result

def search_in_line(line, words):
    symbol = True
    var = 0
    for i in words:
        if var < len(line):
            if i == line[var]:
                var += 1
            elif symbol:
                symbol = False
            else:
                return False

    if len(words)-1 == len(line):
        return True
    return False



def in_line(list, word):
    list = sort_in_list(list)

    words = [word]

    word_val = len(word) + 1
    list_val = []

    while words:
        word = words.pop()
        if len(word) == 1:
            return word

        if word_val > len(word):
            list_val.clear()
            while list:
                i = list.pop()
                if len(i)+1 == len(word):
                    list_val.append(i)
                else:
                    if len(i) < len(word):
                        list.append(i)
                        break

        for i in list_val:
            if search_in_line(i, word):
                if i not in words:
                    words.append(i)
    return word


def result_calculation(first):
    with open('input.txt', 'r') as file:
        list = file.readlines()

    list = [line.strip() for line in list]

    last = in_line(list, first)

    with open("output.txt", 'w')as file:
        result = len(first) - len(last)
        file.write(f"{result}")



result = result_calculation("Word1111111")

print(result)


