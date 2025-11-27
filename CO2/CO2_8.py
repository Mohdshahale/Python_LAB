def longest_word_length(words):
    longest = max(words, key=len)
    return len(longest)

words = input("Enter words separated by spaces: ").split()

print("Length of the longest word:", longest_word_length(words))
