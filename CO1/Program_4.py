word = input("enter the word:")
vowels=("AEIOUaeiou")
final=[]
for letter in word:
    if letter in vowels:
        final.append(letter)
print("",final)
