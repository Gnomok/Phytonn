program = {
    "Bill_Gates" : "28/10/1955",
    "Mark_Zuckerberg" : "14/05/1984",
    "Ken_Tompson" : "04/02/1943"}
b = input("Введите програмиста и мы скажеи когда он родился")
a = program.get(b, "У нас нет такого програмитса :(")
print(a)
