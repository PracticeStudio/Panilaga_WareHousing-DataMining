def countWordsSentence():
    sentence = input("Enter a sentence: ")
    words = sentence.split()
    return len(words)

print("Sample output 1:")
print(f"Number of words: {countWordsSentence()}")

print("\nSample output 2:")
print(f"Number of words: {countWordsSentence()}")

print("\nSample output 3:")
print(f"Number of words: {countWordsSentence()}")
