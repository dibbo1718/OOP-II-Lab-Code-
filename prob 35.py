import string
def remove_punctuation(s):
    return s.translate(str.maketrans('', '', string.punctuation))
text = input("Enter a string: ")
clean_text = remove_punctuation(text)
print("String without punctuation:", clean_text)
