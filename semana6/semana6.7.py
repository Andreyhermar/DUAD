def is_prime(n):
    if n <=1: 
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

number_list = input("Insert numbers separated by a comma or space: ")
normalized_input = number_list.replace(',', ' ')
list_to_review = normalized_input.split()
list_to_review = [int(number.strip()) for number in list_to_review]
prime_numbers = list(filter(is_prime, list_to_review))

print("Prime numbers: ", prime_numbers)