# English to Pig Latin
print("Enter the English message to tranlate into Pig Latin:")
message = input()
VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')
pigLatin = []
for word in message.split():
    # Seperate the non-letters t teh start of this word
    prefixNonLetters = ''
    while len(word) > 0 and not word[0].isalpha():
        word = word[1:]
    if len(word) == 0:
        pigLatin.append(prefixNonLetters)
        continue
    # Seperate the non-letters at the end of this word
    suffixNonLetters = ''
    while not word[-1].isalpha():
        suffixNonLetters += word[-1]
        word = word[:-1]
    # Remember if the word was in uppercase or title case
    wasUpper = word.isupper()
    wasTitle = word.istitle()

    word = word.lower()
    