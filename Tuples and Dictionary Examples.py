# Tuples Examples

# Example 1: Basic Tuple Creation
basic_tuple = (1, 2, 3)
print(basic_tuple)

# Example 2: Tuple with Mixed Data Types
mixed_tuple = (1, "two", 3.0, True)
print(mixed_tuple)

# Example 3: Tuple Unpacking
x, y, z= (10, 11, 12)
print(x, y, z)

# Example 4: Tuple as a Dictionary Key
my_dict = {(1, 2): "value"}
print(my_dict[(1, 2)])

# Example 5: Tuple Methods
my_tuple = (1, 2, 3)
print(my_tuple.count(3))  # Output: 1

# Dictionaries Examples

# Example 1: Basic Dictionary Creation
basic_dict = {"name": "John", "age": 30}
print(basic_dict)

# Example 2: Dictionary with Mixed Data Types
mixed_dict = {"integer": 1, "string": "two cars", "float": 3.0, "boolean": True}
print(mixed_dict)

# Example 3: Dictionary Methods
my_dict = {"name": "John", "age": 30}
print(my_dict.keys())  # Output: dict_keys(['name', 'age'])

# Example 4: Dictionary with Nested Tuples
nested_dict = {"student1": (1, "Alice", "Math"), "student2": (2, "Bob")}
print(nested_dict)

# Example 5: Dictionary Comprehension
squared_dict = {x: x**2 for x in range(1, 11)}
print(squared_dict)
