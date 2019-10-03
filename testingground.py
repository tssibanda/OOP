word = "Thamsanqa"
newWord = ""
ltr: str
for ltr in word:
    if ltr == word[0] or ltr == word[len(word)-1]:
        newWord = newWord + ltr
    else:
        newWord = newWord + ltr
print(newWord)