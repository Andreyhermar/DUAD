import csv

def videogames_to_csv():
    num_games = int(input("Enter the number of videogames: \n"))

    with open('videogames.csv', 'w', newline='') as csvfile:
        fields = ['Name', 'Genre', 'Developer', 'Clasification ESRB']
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        for i in range(num_games):
            print(f"Enter the details for videogame {i + 1}:")
            name = input("Enter the name of the videogame: \n")
            genre = input("Enter the genre of the videogame: \n")
            developer = input("Enter the developer of the videogame: \n")
            clasification = input("Enter the clasification of the videogame: \n")
            
            writer.writerow({
                'Name': name, 
                'Genre': genre, 
                'Developer': developer, 
                'Clasification ESRB': clasification
            })
    print("CSV file created successfully.")

videogames_to_csv()