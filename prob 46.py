elements = input("Enter list elements separated by spaces: ").split()
element_to_remove = input("Enter the element to remove: ")
if element_to_remove in elements:
    elements.remove(element_to_remove)
    print("Updated list:", elements)
else:
    print("Element not found in the list.")
