import random 
word_list = ["aardvark", "baboon", "camel"]
choice_word = random.choice(word_list).lower()
guess = input("put a letter ")
display = []
for _ in choice_word:
    display += "_"
print (display)
for possition in range(len(choice_word)):
    letter = choice_word[possition]
    if letter == guess:
        display[possition] = letter
    else:
        print("Wrong") 


