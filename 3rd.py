# Take input from the user for a word
word = input("Enter a word:")

# Loop through the word, accessing every second character (step of 2)
for index in range(0, len(word), 2):
    # Print the character at the current index
    print(f"{word[index]}")
