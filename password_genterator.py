import random
import string

# Function to generate a random password
def generate_password(length):
    # Define the possible characters in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Randomly choose characters from the 'characters' string and join them into a password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

# Main program
def main():
    # Prompt the user to specify the desired password length
    try:
        length = int(input("Enter the desired length of the password: "))
        
        if length < 6:
            print("Password length should be at least 6 characters for security reasons.")
            return

        # Generate the password
        password = generate_password(length)

        # Display the generated password
        print(f"Generated Password: {password}")
    except ValueError:
        print("Please enter a valid number for the password length.")

# Run the program
if __name__ == "__main__":
    main()
