def bubble_sort(list_to_sort):
    for outer_index in range(0, len(list_to_sort) -1):
        has_changed=False
        for index in range(0, len(list_to_sort) -1 -outer_index):
            current_element=list_to_sort[index]
            next_element=list_to_sort[index+1]
        
            print(f'iteration #{outer_index}, index #{index}. Current Element: {current_element}, Next Element: {next_element}')

            if current_element > next_element:
                print(f'Current element is grater than the next element. Exchanging them... ')
                list_to_sort[index+1] = current_element
                list_to_sort[index] = next_element
                has_changed=True
        
        if not has_changed:
            return
        
def validated_bubble_sort(list_to_sort):

    if len(list_to_sort) == 0:
        raise ValueError("La lista está vacía")

    for element in list_to_sort:
        if not isinstance(element, (int, float)):
            raise TypeError("La lista contiene elementos no numéricos")

    bubble_sort(list_to_sort)
    return list_to_sort

try:
    result = validated_bubble_sort([5, "hola", 2])
    print(result)

except (ValueError, TypeError) as error:
    print(f"Error: {error}")

