# Step 1: Import the necessary modules
import os

# Step 2: Define the file name
filename = "output.txt"

# Step 3: Get user input
user_input = input("Enter the text to be saved in the file: ")

# Step 4: Create and write to the file
try:
    # Open the file in write mode using the "with" statement
    with open(filename, "a") as file:
        # Use the "write" method to write the user input to the file
        file.write(user_input)
        # File writing successful, print a message
        print(f"File '{filename}' created and written successfully.")
except Exception as e:
    # An error occurred, print the error message
    print(f"Error occurred: {str(e)}")
    
    
