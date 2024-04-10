fragrance_list =[
    {"name": "Naxos", "house": "Xerjoff", "price": "$315.00", "size": "3.4 oz"}, 
    {"name":"Oud Noir", "house":"Aaron Terence Hughes", "price": "$200.00", "size":  "1.7 oz"},
    {"name":"Carlisle", "house": "Parfums de Marly", "price": "$275.00", "size":  "4.2 oz"}
]
# allow user to add a new fragrance to the list
def add_fragrance(fragrance_list, name, house, price, size):
    fragrance_list.append({"name": name, "house": house, "price": price, "size": size})
    return fragrance_list


def search_fragrance(): 
    try:
        search = input("Enter a fragrance name: ")
        for frag in fragrance_list:
            if frag["name"] == search:
                print(frag["name"] + " by " + frag["house"] + " is " + frag["price"] + " for " + frag["size"] + ".")
                break
        else:
            print("Fragrance not found.")
            return search_fragrance()
    except ValueError:
        print("Please enter a valid string.")
        return search_fragrance()


def delete_fragrance():
    try:
        delete=input("Which fragrance would you like to delete?: ")
        for frag in fragrance_list:
            if frag["name"]==delete:
                frag.pop("name")
                print("Fragrance has been removed.")
            elif delete == "exit":
                break
            else:
                print("Fragrance not found.")
                return delete_fragrance()
    except ValueError:
        print("Please enter a valid string.")
        return delete_fragrance()
        

i=0
while i < 1:
    print("""
    Welcome to the fragrance store! Press (1) To Add a fragrance | Press (2) To Search for a fragrance 
    | Press (3) To Delete a fragrance | (4) Exit""")
    print()
    try:
     ops=int(input("Select: "))
     if ops == 4:
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
         
    except ValueError:
        print("Please enter a valid integer.")
        continue

for frag in fragrance_list: 
        print(frag["name"] + " by " + frag["house"] + " is " + frag["price"] + " for " + frag["size"] + ".")


    
 