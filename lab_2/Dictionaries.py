car = {
    "brend": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(car.get("model"))
#Mustang

car = {
    "brend": "Ford",
    "model": "Mustang",
    "year": 1964
}
car["year"] = 2020
#Ford, Mustang, 2020

car = {
    "brend": "Ford",
    "model": "Mustang",
    "year": 1964
}
car["color"] = "red"
#Ford,..., red

car = {
    "brend": "Ford",
    "model": "Mustang",
    "year": 1964
}
car.pop("model")
#Ford, 1964

car = {
    "brend": "Ford",
    "model": "Mustang",
    "year": 1964
}
car.clear()
#