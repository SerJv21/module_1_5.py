immutable_var = (1, 2, 'a', True)
print(immutable_var)
# immutable_var[3] = False
# print(immutable_var)
mutable_list = ["car", "call", " long"]
print(mutable_list)
mutable_list.append(100)
mutable_list[2] = "Map"
mutable_list[1] = "look"
mutable_list.remove("look")
print(mutable_list)
