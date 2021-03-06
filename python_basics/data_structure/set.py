# Set: is an unordered collection data type that is iterable, mutable and compared to list has no duplicate elements.
# it has a highly optimized method for checking whether a specific element is contained in the set.
# which is actually based on hash-table .
# Since sets are unordered, we cannot access items using indexes like we do in lists.
# Types: Normal and Frozen set

# Create empty set
# var_set = set()
# print(var_set)
# print(type(var_set))
# Create set with values (include duplicates)
# var_set = set()
# var_set = {"hello", "hello", 123, 456}
# print(var_set)
# print(type(var_set))
# Get (not allowed)
# item = var_set[0]

# Add
# var_set.add("Python")
# print(var_set)

# Remove
# var_set.remove(123)
# print(var_set)

# Pop (removes a random item and returns the item)
# item = var_set.pop()
# print(var_set)
# print("Popped item is:", item)
# Frozen is set (immutable set i.e. we can not change it after creation)

# the frozenset immutable i.e. we can not change it after creation
# Builds an immutable unordered collection of unique elements.
frozen_set = frozenset({"hello", 234, 5.44, 89, 5.44, 89, "hello", "Hello"})
# frozen_set.add(345) # uncommenting this will throw an error
print(frozen_set)
print(type(frozen_set))
