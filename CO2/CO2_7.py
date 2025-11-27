text=input("enter the string:")
if text.endswith("ing"):
    text = text[:-3]+"ly"
    
elif text.endswith("ly"):
        text = text[:-2]+"ing"
else:
    text += "ing"
print(text)
