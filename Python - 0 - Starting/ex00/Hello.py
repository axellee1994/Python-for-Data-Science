ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

print(type(ft_list))    # Ordered, changeable and allow duplicates
print(type(ft_tuple))   # Ordered, unchangeable and allow duplicates
print(type(ft_set))     # Unordered, unchangeable, and no duplicates
print(type(ft_dict))    # Ordered, changeable and no duplicates

# Modifying list value
ft_list[1] = "World"

# Converting tuple(immutable) to list(mutable) and modifying it
ft_tuple_convert = list(ft_tuple)
ft_tuple_convert[1] = "Singapore"
ft_tuple = tuple(ft_tuple_convert)

# Modifying set value
ft_set.remove("tutu!")
ft_set.add("Singapore")

# Modifying dictionary value
ft_dict.update({"Hello": "42Singapore"})

# your code here
print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
