def countWordsSentence(sentence):
    words = 0
    for i in sentence:
        if i == " " or i == "\t" or i == "\n":
            words += 1

    if len(sentence) > 0:
        return words + 1
    else:
        return 0

print("Sample output 1:")
input_sentence = input("Enter a sentence: ")
print(f"Number of words: {countWordsSentence(input_sentence)}")

print("\nSample output 2:")
input_sentence = input("Enter a sentence: ")
print(f"Number of words: {countWordsSentence(input_sentence)}")

print("\nSample output 3:")
input_sentence = input("Enter a sentence: ")
print(f"Number of words: {countWordsSentence(input_sentence)}")
