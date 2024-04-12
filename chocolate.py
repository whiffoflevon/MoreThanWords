fragrance_list =[
    {"name": "Naxos", "house": "Xerjoff", "price": "$315.00", "size": "3.4 oz"}, 
    {"name":"Oud Noir", "house":"Aaron Terence Hughes", "price": "$200.00", "size":  "1.7 oz"},
    {"name":"Carlisle", "house": "Parfums de Marly", "price": "$275.00", "size":  "4.2 oz"},
    {"name": "More Than Words", "house": "Xerjoff", "price": "$550.00", "size": "3.4 oz"}, 
    {"name": "Oud Satin Mood", "house": "Maison Francis Kurkdjian", "price": "$300.00", "size": "2.4 oz"},
    {"name": "Herod", "house": "Parfums de Marly", "price": "$295.00", "size": "4.2 oz"},
    {"name": "Portrait of a Lady", "house": "Frederic Malle", "price": "$380.00", "size": "3.4 oz"},
    {"name": "Santal 33", "house": "Le Labo", "price": "$275.00", "size": "3.4 oz"},
    {"name": "Aventus", "house": "Creed", "price": "$435.00", "size": "3.4 oz"},
    {"name": "Black Phantom", "house": "By Kilian", "price": "$295.00", "size": "1.7 oz"},
    {"name": "Baccarat Rouge 540", "house": "Maison Francis Kurkdjian", "price": "$300.00", "size": "2.4 oz"},
    {"name": "Gris Charnel Extrait", "house": "BDK", "price": "$275.00", "size": "3.4 oz"},
    {"name": "Oud Wood", "house": "Tom Ford", "price": "$250.00", "size": "3.4 oz"},
    {"name": "Oud Minerale", "house": "Tom Ford", "price": "$240.00", "size": "1.7 oz"},
    {"name": "By the Fireplace", "house": "Maison Margiela", "price": "$130.00", "size": "3.4 oz"},
    {"name": "Tobacco Vanille", "house": "Tom Ford", "price": "$250.00", "size": "3.4 oz"},
    {"name": "Santal Carmin", "house": "Atelier Cologne", "price": "$250.00", "size": "3.4 oz"},
    {"name": "Tuxedo", "house": "YSL", "price": "$250.00", "size": "3.4 oz"},
    {"name": "Molecule 01", "house": "Escentric Molecules", "price": "$135.00", "size": "3.4 oz"},
    {"name": "Aqua Celestia Forte", "house": "Maison Francis Kurkdjian", "price": "$225.00", "size": "2.4 oz"},
    {"name": "Enigma", "house": "Roja Parfums", "price": "$485.00", "size": "3.4 oz"},
    {"name": "Oudh Infini", "house": "Dusita", "price": "$285.00", "size": "1.7 oz"},
    {"name": "Cuir 28", "house": "Le Labo", "price": "$320.00", "size": "3.4 oz"}, 
]

# allow user to add a new fragrance to the list
def add_fragrance(fragrance_list, name, house, price, size):
    fragrance_list.append({"name": name, "house": house, "price": price, "size": size})
    


def search_fragrance(): 
    try:
        search = input("Enter a fragrance name: ")
    except ValueError:
        print("Please enter a valid string.")
        return search_fragrance()
    for frag in fragrance_list:
        if frag["name"] == search:
            print(frag["name"] + " by " + frag["house"] + " is " + frag["price"] + " for " + frag["size"] + ".")
            break
        else:
            print("Fragrance not found.")
            return search_fragrance()


def delete_fragrance():
    try:
        delete=input("Which fragrance would you like to delete?: ")
    except ValueError:
        print("Please enter a valid string.")
        return delete_fragrance()
    for frag in fragrance_list:
        if frag["name"]==delete:
            fragrance_list.remove(frag)
            print(frag["name"] + " has been removed.")
            break
        else:
            print("Fragrance not found.")
            return delete_fragrance() 
    

 #Display the list of fragrances
def display_list():
    for frag in fragrance_list: 
        print(frag["name"] + " by " + frag["house"] + " is " + frag["price"] + " for " + frag["size"] + ".")

#Update the list of fragrances
def update_list():
    try:
        update=input("Which fragrance would you like to update?: ")
    except ValueError:
        print("Please enter a valid string.")
        return update_list()
    for frag in fragrance_list:
        if frag["name"] == update:
            frag["name"] = input("Enter the new name: ")
            frag["house"] = input("Enter the new house: ")
            frag["price"] = input("Enter the new price: ")
            frag["size"] = input("Enter the new size: ")
            print("Fragrance has been updated.")
            break
        else:
            print("Fragrance not found.")
            return update_list()

while True:
    print("Welcome to the fragrance store!")
    print()
    print("""
    Press (1) To Add a fragrance | Press (2) To Search for a fragrance 
    | Press (3) To Delete a fragrance | (4) Update a fragrance | (5) Display List | (6) Exit""")
    print()
    try:
        ops=int(input("Select: "))
    except ValueError:
        print("Please enter a valid integer.")
    if ops == 6:
        break    
    elif ops == 1:
        name = input("Name: ")
        house = input("House: ")
        price = input("Price: ")
        size = input("Size: ") 
        add_fragrance(fragrance_list, name, house, price, size)
    elif ops == 2:
         search_fragrance()
    elif ops == 3:
        delete_fragrance()
    elif ops == 5:
        display_list()
    elif ops == 4:
        update_list()
    else:
        print("Invalid selection.")
        continue
         
         


    
 
