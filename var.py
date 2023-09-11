s1 = "john"
s2 = "doe"

print("Name is : " + s1 + " " + s2 + "!")

print("")

names = ["Alice", "Bob", "Charlie", "Dave"]

names[1] = "Bard"
# names[4] = "Zach"

names.append("Frank")

i = 1
for name in names:
    print(str(i) + ". Name = " + name)
    i += 1