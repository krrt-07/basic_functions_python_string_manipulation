# ask the user to put a statement.
user_statement = input("Enter a complete statement: ") 

# make a condition that will count the word in the statement.
word_count = len(user_statement.split())

# print how many word in the statement.
print(f"Number of words: {word_count}") 