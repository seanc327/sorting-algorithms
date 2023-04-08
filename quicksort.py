import time

def original_quicksort(input_list):
    #O(nlogn)
    sorted_list = []
    pivot_less = []
    pivot_more = []
    if len(input_list) <= 1:
        return input_list
    else:
        # take pivot value out on another list
        pivot = input_list.pop()
    for element in input_list:
        # compares pivot with next element, if smaller, placed to the pivot more list
        if element > pivot:
            pivot_more.append(element)
        # same as previous but larger
        else:
            pivot_less.append(element)
        # combining all three lists to equal one sorted list
        sorted_list = original_quicksort(pivot_less) + [pivot] + original_quicksort(pivot_more)
    # returns sorted_list
    return sorted_list

def modified_quicksort(input_list):
    #O(n^2)
    sorted_list = []
    for i in range(1, len(input_list)):
        j = i
        # swap conditions
        while j > 0 and input_list[j - 1] > input_list[j]:
            input_list[j - 1], input_list[j] = input_list[j], input_list[j - 1]
            # go further to left
            j -= 1
        sorted_list = input_list
    # returns sorted_list
    return sorted_list

if __name__ == "__main__":
    my_list = [3, 4, 1, 5, 2]
    print(original_quicksort(my_list))  # Correct Output: [1, 2, 3, 4, 5]
    print(modified_quicksort(my_list))  # Correct Output: [1, 2, 3, 4, 5]
    # TODO (optional): Your testing code here

# modified quicksort should be more optimal compared to original quicksort
# complexity- original: O(nlogn), modified: O(n^2)

