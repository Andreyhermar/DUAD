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
        

list_to_sort=[8, 5, 4, 1, 6, 9, 10, 2]
bubble_sort(list_to_sort)
    
print(list_to_sort)

