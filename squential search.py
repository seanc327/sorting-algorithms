# doesn't need to be sorted
def sequential_search(input_list, target):
    target_index = -1 #O(1)
    # for loop repeats all value for length of input_list
    for i in range(len(input_list)):
        # if statement where if the target is found, return i
        if input_list[i] == target:
            return i
    # target_index (-1) is returned when there is no target

    return target_index

if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    print(sequential_search(my_list, 3))  # expected: 2
    print(sequential_search(my_list, 0))  # expected: -1

    # complexity: best: O(1), worst: O(n), average: O(n/2)


