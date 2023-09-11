import itertools

# Function to print text in red color using ANSI escape codes
def print_red(text):
    print("\033[91m" + text + "\033[0m")

# Print the red ASCII art
red_ascii_art = """
\033[91m
                   :*#####*:                   
                 :###########:                 
                :###-.    :###:                
                +##=       -##+                
                +##=                           
             .+#################+.             
             -###################-             
             -########*-*########-             
             -#######*.  +#######-             
             -########+#=########-             
             -###################-              \033[0m
"""

print_red(red_ascii_art)



def generate_passwords(name):
    name = name.lower()  # Convert to lowercase for consistent processing
    variations = set()   # Use a set to automatically remove duplicates

    # Replace 'a's with '@' and 'i's with '1'
    variations.add(name.replace('a', '@').replace('i', '1'))

    # Generate progressive numbers 1, 12, 123, ..., 12345
    progressive_num = ''
    for num in range(1, len(name) + 1):
        progressive_num += str(num)
        if len(progressive_num) >= 5:
            break  # Stop when the length reaches 5
        variations.add(name + progressive_num)

    # Combine two-word names into one
    if ' ' in name:
        names = name.split()
        combined_name = ''.join(names)
        variations.add(combined_name)

        # Also add the original two-word name
        variations.add(name)

        # Add the reversed order of the two-word name
        reversed_name = ' '.join(reversed(names))
        variations.add(reversed_name)

    # Capitalize the first letter and add variations with the first letter in lowercase
    name_capitalized = name.capitalize()
    variations.add(name_capitalized)
    variations.add(name_capitalized.lower())

    # Add the original name and variations with the first letter in lowercase
    variations.add(name)
    variations.add(name.lower())

    return list(variations)  # Convert the set back to a list

def print_passwords(passwords):
    # Print all the generated passwords
    for password in passwords:
        print(password)

def generate_and_save_passwords_from_file(filename, output_filename):
    try:
        with open(filename, 'r') as file:
            names = [line.strip() for line in file]
            generated_passwords = []
            for name in names:
                passwords = generate_passwords(name)
                generated_passwords.extend(passwords)
            
            # Save all passwords to the same output file
            with open(output_filename, 'w') as output_file:
                for password in generated_passwords:
                    output_file.write(password + '\n')

            print(f"Passwords have been saved to '{output_filename}'")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")

# Main menu loop
while True:
    print("\nMenu:")
    print("1. Generate Passwords from File")
    print("2. Generate Passwords for a Name and Exit")
    print("3. Exit")

    choice = input("Select an option: ")

    if choice == '1':
        input_filename = input("Enter the name of the file containing names: ")
        output_filename = input("What should the file be called: ")
        generate_and_save_passwords_from_file(input_filename, output_filename)
        break
    elif choice == '2':
        name = input("Enter the name you want to create passwords for: ")
        passwords = generate_passwords(name)
        print_passwords(passwords)
        break
    elif choice == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3 to select an option.")
