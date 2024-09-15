import random
import string

#Use def to define our entire function
def random_EC2_namegen ():
    # Ask the user for the department name
    dept = input('What is your department name? ')

    # Check if the department is FinOps, Marketing, or Accounting
    if dept == 'FinOps':
        pass  # If valid, continue
    elif dept == 'Marketing':
        pass  # If valid, continue
    elif dept == 'Accounting':
        pass  # If valid, continue
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

#Call the final function to execute everything above
random_EC2_namegen()