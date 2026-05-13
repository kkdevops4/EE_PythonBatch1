sizes = {
    "small": 150,
    "regular": 270,
    "large": 400
}

crusts = {
    "regular": 0,
    "thin": 40,
    "cheese burst": 100
}

toppings = {
    "extra cheese": 50,
    "mushroom": 30,
    "onion": 20,
    "paneer": 50,
    "corn": 25
}
    

print("pizza menu")

# print(sizes)
print("\nPlease select your pizza size")
size_l = list(sizes.keys())
for i, key in enumerate(size_l, 1):
     print(f"({i}). {key} - {sizes[key]}")

size_choice = int(input("enter your choice: "))
if size_choice <1 or size_choice>len(sizes):
    print("invalid selection!")
    exit()

selected_size= size_l[size_choice - 1]

# print(crusts)
print("\nPlease select your crust type")
crust_l =list(crusts.keys())
for i, key in enumerate(crust_l, 1):
     print(f"({i}). {key} - {crusts[key]}")

crust_choice = int(input("enter your choice: "))
if crust_choice <1 or crust_choice>len(crusts):
    print("invalid selection!")
    exit()

selected_crust=crust_l[crust_choice-1]


# print(toppings)
print("\nPlease select your topping option1")
topping1 =list(toppings.keys())
for i, key in enumerate(topping1, 1):
     print(f"({i}). {key} - {toppings[key]}")

topping1_choice = int(input("enter your choice: "))
if topping1_choice <1 or topping1_choice>len(toppings):
    print("invalid selection!")
    exit()
selected_t1=topping1[topping1_choice-1]

# print(toppings)

print("\nPlease select your topping option2")
topping2 =list(toppings.keys())
for i, key in enumerate(topping2, 1):
     print(f"({i}). {key} - {toppings[key]}")

topping2_choice = int(input("enter your choice: "))
if topping2_choice <1 or topping2_choice>len(toppings):
    print("invalid selection!")
    exit()
selected_t2=topping2[topping2_choice-1]

print("\npizza size : ", selected_size, "\ncrust type : ", selected_crust, "\npizza topping 1 : ", selected_t1, "\npizza topping 2 : ",selected_t2)

total = sizes.get(selected_size, 0) + crusts.get(selected_crust, 0) + toppings.get(selected_t1, 0) + toppings.get(selected_t2, 0)
print("\norder price: ", total)
print("\ntax on order is 18% : ", total* 0.18)
print("\ntotal price: ", total+(total*0.18),"rs")


print("\n        ---BILL---        \n")
print(f"Size ({selected_size})         :  {sizes.get(selected_size)}rs")
print(f"Crust ({selected_crust})       :  {crusts.get(selected_crust)}rs")
print(f"Topping 1 ({selected_t1})      :  {toppings.get(selected_t1)}rs")
print(f"Topping 2 ({selected_t2})      :  {toppings.get(selected_t2)}rs")

print("\norder price         : ", total)
print("\ntax on order is 18% : ", total* 0.18  )

print("------------------------------")
print(f"Total Amount         :  {total+(total*0.18)}rs")
print("------------------------------")