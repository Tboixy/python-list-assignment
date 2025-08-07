# File Handling and Exception Handling Assignment

def modify_content(content):
    """
    Simple function to modify the file content.
    Here, we will convert text to uppercase.
    """
    return content.upper()

# Ask user for input file name
filename = input("Enter the filename to read: ")

try:
    # Read from file
    with open(filename, "r") as file:
        data = file.read()

    # Modify the data
    modified_data = modify_content(data)

    # Write modified data to a new file
    new_filename = "modified_" + filename
    with open(new_filename, "w") as file:
        file.write(modified_data)

    print(f"File successfully modified! New file saved as: {new_filename}")

except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")
except PermissionError:
    print(f"Error: Permission denied when accessing '{filename}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
