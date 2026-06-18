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

