import random
import string

# Ask the user for the department name
dept = input('What is your department name? ')

# Check if the department is FinOps
if dept == 'FinOps':
    pass  # If valid, continue
# Check if the department is Marketing
elif dept == 'Marketing':
    pass  # If valid, continue
# Check if the department is Accounting
elif dept == 'Accounting':
    pass  # If valid, continue
# If the department is none of the above, print an error message and stop
else:
    print('This is not a usable department name')
    exit()  # Exit the program since the input is invalid

# Ask how many EC2 instance names are needed
amount = int(input('How many EC2 instance names do you need? '))

# Define the characters to use in the random name generation
str_characters = string.ascii_letters + string.digits + "!@#$%^&*"

# Function to generate random names for the EC2 instances
def name_gen():
    for i in range(amount):  # Loop through the required number of names
        name_length = random.randint(9, 15)  # Generate a random name length between 9 and 15 characters
        generated_name = ''.join(random.choice(str_characters) for _ in range(name_length))  # Create the random string
        print(dept + generated_name)  # Print the department name + generated name

# Print a header for the generated names
print('Here are your generated EC2 names: ')
# Call the function to generate and display the names
name_gen()
