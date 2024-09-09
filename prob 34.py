def sort_words(sentence):
    words = sentence.split()
    words.sort()
    return ' '.join(words)
sentence = input("Enter a sentence: ")
sorted_sentence = sort_words(sentence)
print("Sorted words:", sorted_sentence)
