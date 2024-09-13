import random
import string

def generate_password(length, use_uppercase=True, use_digits=True, use_special_chars=True):
    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if use_uppercase else ''
    digits = string.digits if use_digits else ''
    special_chars = string.punctuation if use_special_chars else ''
    
    # Combine all characters to be used
    all_characters = lowercase + uppercase + digits + special_chars
    
    if not all_characters:
        raise ValueError("At least one character set must be selected.")
    
    # Generate the password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password

def main():
    print("Welcome to the Password Generator!")
    
    # Get user input
    try:
        length = int(input("Enter the length of the password: "))
        if length <= 0:
            raise ValueError("Length must be a positive integer.")
        
        use_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower() == 'yes'
        use_digits = input("Include digits? (yes/no): ").strip().lower() == 'yes'
        use_special_chars = input("Include special characters? (yes/no): ").strip().lower() == 'yes'
        
        # Generate and display the password
        password = generate_password(length, use_uppercase, use_digits, use_special_chars)
        print(f"Generated Password: {password}")
    
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
