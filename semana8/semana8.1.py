def order_alphabetically(path):
    with open(path) as file:
        return sorted(file.readlines())
    
def write_new_file(input_path, output_path):
    sorted_file = order_alphabetically(input_path)
    with open(output_path, 'w') as file:
        for line in sorted_file:
            file.write(line.strip() + '\n')

write_new_file('semana8.txt', 'semana8.2.txt')
