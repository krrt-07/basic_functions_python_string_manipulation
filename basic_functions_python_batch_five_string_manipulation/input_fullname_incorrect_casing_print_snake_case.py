# ask the user to input their fullname in incorrect casing.
user_fullname = input("Enter your full name (incorrect casing): ") 

# make a condition that will make the fullname in lower casing and remove the spacing and change it to "_".
snake_case = user_fullname.lower().replace(" ", "_")  

# print the fullname in snake case.
print(snake_case) 