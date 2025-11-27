
def count_characters(text):
    frequency = {}
    
    for char in text:
        if char != " ":
            frequency[char] = frequency.get(char, 0) + 1
    
    return frequency

if __name__ == "__main__":
    text = input("Enter a string: ")
    result = count_characters(text)

    print("\nCharacter frequencies:")
    for char, count in result.items():
        print(f"'{char}': {count}")
