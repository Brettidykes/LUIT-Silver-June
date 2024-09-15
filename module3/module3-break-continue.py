# Infinite loop, keeps running until 'EXIT' is entered
while True:  
    # Prompts the user to input their name or type 'EXIT' to stop the program
    name = input('Enter your name or EXIT to close the program: ')  
    
    # If the user enters 'EXIT', the loop breaks and the program ends
    if name == 'EXIT':  
        break  # Exit the loop
    
    # If 'EXIT' is not entered, greet the user by their name
    print('Hello', name)  

# Loop through the numbers from 1 to 20
for i in range(1, 21):  
    # If the number is divisible by 5, skip the rest of the loop and go to the next iteration
    if i % 5 == 0:  
        continue  # Skip the current iteration
    
    # Print the current number if it's not divisible by 5
    print(i)
