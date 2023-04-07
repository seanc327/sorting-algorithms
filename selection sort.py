def selection_sort(input_list, reverse):
    sorted_list = []
    for i in range(len(input_list)):
        # minimum position = i
        minimum = i
        # j is the integer after i
        for j in range(i + 1, len(input_list)):
            # if reverse is true, sorted list will be in reverse
            if reverse == True:
                # if the minimum (i) is less than the next integer (j = i+1), i will be replaced by j
                if input_list[minimum] < input_list[j]:
                    minimum = j
            # if reverse is false, sorted list will be in order
            else:
                if reverse == False:
                    if input_list[minimum] > input_list[j]:
                        minimum = j
        # swaps positions
        input_list[i], input_list[minimum] = input_list[minimum], input_list[i]
        sorted_list = input_list
    return sorted_list

# complexity: O(n^2) 

if __name__ == "__main__":
    my_list = [5,1,2,4,3,2,1]
    print(selection_sort(my_list, True))  # expected: [5, 4, 3, 2, 1]

