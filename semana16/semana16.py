# 1. Bubble Sort
#
# Time complexity:
# Best case: O(n)
# Average case: O(n²)
# Worst case: O(n²)
#
# The algorithm has two nested loops, so in the average
# and worst cases the number of operations grows quadratically.
# The has_changed variable allows the function to stop early
# if the list is already sorted.

def bubble_sort(list_to_sort):
    for outer_index in range(0, len(list_to_sort) - 1):
        has_changed = False

        for index in range(0, len(list_to_sort) - 1 - outer_index):
            current_element = list_to_sort[index]
            next_element = list_to_sort[index + 1]

            if current_element > next_element:
                list_to_sort[index + 1] = current_element
                list_to_sort[index] = next_element
                has_changed = True

        if not has_changed:
            return


# 2. print_numbers_times_2
#
# Time complexity: O(n)
#
# The function loops through every element in the list once.
# Therefore, the number of operations grows linearly with
# the size of the list.

def print_numbers_times_2(numbers_list):
    for number in numbers_list:
        print(number * 2)


# 3. check_if_lists_have_an_equal
#
# Time complexity: O(n * m)
#
# The function has two nested loops.
# If both lists have approximately the same size,
# the complexity can be expressed as O(n²).
#
# In the worst case, every element from list_a is compared
# with every element from list_b.

def check_if_lists_have_an_equal(list_a, list_b):
    for element_a in list_a:
        for element_b in list_b:
            if element_a == element_b:
                return True

    return False


# 4. print_10_or_less_elements
#
# Time complexity: O(1)
#
# The function prints a maximum of 10 elements regardless
# of how large the list is.
# Because the number of iterations is limited to a constant,
# the complexity is O(1).

def print_10_or_less_elements(list_to_print):
    list_len = len(list_to_print)

    for index in range(min(list_len, 10)):
        print(list_to_print[index])


# 5. generate_list_trios
#
# Time complexity: O(n³)
#
# The function contains three nested loops.
# If all three lists contain n elements, the loops execute
# approximately n * n * n operations.
# Therefore, the complexity is O(n³).

def generate_list_trios(list_a, list_b, list_c):
    result_list = []

    for element_a in list_a:
        for element_b in list_b:
            for element_c in list_c:
                result_list.append(
                    f"{element_a} {element_b} {element_c}"
                )

    return result_list