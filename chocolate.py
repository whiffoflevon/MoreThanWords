# allow user to add a new fragrance to the list
def add_fragrance(fragrance_list, name, house, price, size):
    fragrance_list.append({"name": name, "house": house, "price": price, "size": size})
    return fragrance_list

fragrance_list =[
    {"name": "Naxos", "house": "Xerjoff", "price": "$315.00", "size": "3.4 oz"}, 
    {"name":"Oud Noir", "house":"Aaron Terence Hughes", "price": "$200.00", "size":  "1.7 oz"},
    {"name":"Carlisle", "house": "Parfums de Marly", "price": "$275.00", "size":  "4.2 oz"}
]

while True:
    name = input("Name: ")
    if name == "exit":
        break
    
    house = input("House: ")
    price = input("Price: ")
    size = input("Size: ")

    add_fragrance(fragrance_list, name, house, price, size)


for frag in fragrance_list: 
        print(frag["name"] + " by " + frag["house"] + " is " + frag["price"] + " for " + frag["size"] + ".")




    
