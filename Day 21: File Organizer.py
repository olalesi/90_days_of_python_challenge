import os
import shutil

def organize_files(folder_path):
    # Check if the provided path exists
    if not os.path.exists(folder_path):
        print("The folder does not exist. Please provide a valid folder path.")
        return

    # Loop through all files in the folder
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        
        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Extract file extension (e.g., .txt, .jpg)
        file_extension = os.path.splitext(file)[1].lower()  # Convert to lowercase for consistency

        if file_extension:  # Skip files without extensions
            # Create a folder name based on the file extension
            folder_name = file_extension[1:].capitalize() + "Files"  # Remove the dot and capitalize
            destination_folder = os.path.join(folder_path, folder_name)

            # Create the destination folder if it doesn't exist
            if not os.path.exists(destination_folder):
                os.mkdir(destination_folder)

            # Move the file to the appropriate folder
            shutil.move(file_path, os.path.join(destination_folder, file))
            print(f"Moved: {file} -> {destination_folder}")

    print("Files organized successfully!")

# Ask the user for the folder path
folder_to_organize = input("Enter the path of the folder you want to organize: ")
organize_files(folder_to_organize)
