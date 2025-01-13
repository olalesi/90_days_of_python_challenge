# User inputs file name
file_name = input("Enter the name of the text file (e.g., 'example.txt'): ")

try:
    # Open the file in read mode
    with open(file_name, 'r') as file:
        # Read all lines from the file
        lines = file.readlines()
        
        # Count the number of lines
        num_lines = len(lines)
        
        # Count the number of words
        num_words = 0
        for line in lines:
            num_words += len(line.split())  # Split the line into words and count them

    # Display results
    print(f"The file '{file_name}' has:")
    print(f"- {num_lines} lines")
    print(f"- {num_words} words")

except FileNotFoundError:
    print(f"Error: The file '{file_name}' does not exist. Please check the name and try again.")
