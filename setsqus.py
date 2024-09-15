print("\n")
# Given a string convert Into a set
my_string = "anu"
my_set = set(my_string)
print(my_set)

print("\n")

# What is s + t ?
s = {10, 20, 30}
t = {100, 200}
x = s.union(t)
print(x)

print("\n")

# Explain *x
x = {1, 2, 3, 4}
print(*x)

print("\n")

# operators
a = {10, 20, 30, 40, 50, 60, 70}
b = {33, 44, 51, 10, 20, 50, 30, 33}
union_result = a.union(b)
print("A or B:", union_result)

intersection_result = a.intersection(b)
print("A and B:", intersection_result)

difference_result = a - b
print("A - B:", difference_result)

difference_result_b = b - a
print("B - A:", difference_result_b)

symmetric_difference_result = a.symmetric_difference(b)
print("A ^ B:", symmetric_difference_result)

is_subset = a.issuperset(b)
print("A >= B:", is_subset)

is_subset_b = a.issubset(b)
print("A <= B:", is_subset_b)

print("\n")


# min , max , sum , len...

S = {10, 2, -3, 4, 5, 88}

num_items = len(S)
print("Number of items in S:", num_items)

max_element = max(S)
print("Maximum element in S:", max_element)

min_element = min(S)
print("Minimum element in S:", min_element)

sum_elements = sum(S)
print("Sum of all elements in S:", sum_elements)

sorted_set = sorted(S)
print("Sorted set of S:", sorted_set)

is_member_100 = 100 in S
print("Is 100 a member of S:", is_member_100)

print("\n")


""" A set contains name which begins A or B . WAP to separate out 
the name such that one set contain with a and another set contain the set b."""

original_set = {"Anu", "Boby", "prachi", "Boy", "Anshu", "Charlie", "David"}

a = set()
b = set()

for name in original_set:
    if name.startswith("A"):
        a.add(name)
    elif name.startswith("B"):
        b.add(name)

print("Names starting with 'A':", a)
print("Names starting with 'B':", b)

print("\n")
