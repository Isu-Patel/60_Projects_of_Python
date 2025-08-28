print("Welcome to Mad Libs Generator!")
print("Fill in the blanks to create a funny story!\n")

adjective1 = input("Enter an adjective: ")
noun1 = input("Enter a noun: ")
verb = input("Enter a verb: ")
adjective2 = input("Enter another adjective: ")
noun2 = input("Enter another noun: ")
animal = input("Enter an animal: ")
color = input("Enter a color: ")

story = f"""
Once upon a time, there was a {adjective1} {noun1} who loved to {verb}.
Every day, the {adjective2} {noun2} would dance with a {color} {animal}.
They lived happily ever after in their magical world!
"""

print("\nHere's your Mad Libs story:")
print(story)