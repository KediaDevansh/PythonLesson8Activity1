pasta = ("White Sauce Pasta","Italian",100,"Medium")
pizza = ("Cheese Pizza","Italian",150,"Large")
print("First Recipe: ",pasta[0])
print("Cuisine: ",pasta[1])
print("Money: ",pasta[2])
print("Size: ",pasta[3])

allrecipe = (pasta,pizza)
print("First Recipe: ",allrecipe[0][0])
print("Second Recipe: ", allrecipe[1][0])
print("Size of Pizza: ",allrecipe[1][3])

print("\nPizza Recipe Details:")
for i in pasta:
    print("  -",i)

p = {"tomato","garlic","chilli","pasta","olive oil"}
pi = {"pizza base","tomato","cheese","pepper",}

print("\nIngredients In Pasta: ",p)
print("\nIngredients In Pizza: ",pi)
print("No Of Ingredients In Pasta: ",len(p))
print("No of Ingredients In Pizza: ",len(pi))

p.add("Parmesan")
p.discard("Chilli")
print("Updated Pasta Ingredients: ",p)

all = p.union(pi)
common = p.intersection(pi)
unique = p.symmetric_difference(pi)
onlypi = p.difference(pi)

print("\nTotal Ingredients: ",all)
print("Common Ingredients: ",common)
print("Unique Ingredients: ",unique)
print("Ingredients Only In Pizza: ",onlypi)