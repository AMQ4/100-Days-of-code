import pandas

# Read the CSV file 'nato_phonetic_alphabet.csv' into a pandas DataFrame and store it in the 'file' variable.
file = pandas.read_csv("./nato_phonetic_alphabet.csv")

# Create a dictionary 'd' to store the NATO phonetic alphabet code for each letter.
# The dictionary is created using a dictionary comprehension, iterating over each row of the 'file' DataFrame.
# The keys are the 'letter' column values, and the values are the 'code' column values from the DataFrame.
d = {value.letter: value.code for (key, value) in file.iterrows()}

# Ask the user to enter a word and convert it to uppercase to ensure consistency.
word = input("Enter a word: ").upper()

# Create a list 'word_in_nato' to store the NATO phonetic alphabet codes for each letter in the input word. The list
# is generated using a list comprehension, where each letter of the input word is looked up in the 'd' dictionary.
word_in_nato = [d[letter] for letter in word]

# Print the list of NATO phonetic alphabet codes corresponding to the letters in the input word.
print(word_in_nato)

# However, we can do better using a few of line of code :

# Create a list 'word_in_nato' to store the NATO phonetic alphabet codes for each letter in the input word. The list
# is generated using a list comprehension with nested iteration. For each letter in the input word, the code iterates
# over each row of the 'file' DataFrame. If the 'letter' column value of the row matches the current letter,
# it extracts the 'code' column value and adds it to the list.

# word_in_nato = [row.code for letter in word for (index, row) in file.iterrows() if row.letter == letter]

# Print the list of NATO phonetic alphabet codes corresponding to the letters in the input word.
# print(word_in_nato)
