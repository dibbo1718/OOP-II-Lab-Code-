list_input = input("Enter list of tuples : ").split()
list_of_tuples = [tuple(item.split('=')) for item in list_input]
dictionary = dict(list_of_tuples)
print("Dictionary:", dictionary)
