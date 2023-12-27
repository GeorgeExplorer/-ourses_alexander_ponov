# # list: it's possible to create a duplicate values
# firstPeople = ["Paul", "John", "Alex", "Paul"]
# print(firstPeople)
#
# # set: it's impossible to create a duplicate values, but you can use the same words in any Case (upper/lower)
# secondPeople = {"Paul", "John", "Alex", "Paul", "alex"}
# print(secondPeople)

# dictionary: it contains a pair of key + value
thirdPeople = {
    "husband": "George",
    "wife": "Nastya",
    "pet1": "Pepsik",
    "pet2": "Leo"
}

for a, b in thirdPeople.items():
    print(a + " - " + b)