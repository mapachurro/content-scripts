import os
import string

def clean_name(name):
    # Replace spaces with dashes
    name = name.replace(' ', '-')

    # Convert uppercase letters to lowercase
    name = name.lower()

    # Remove characters: colons, question marks, exclamation marks, parentheses, brackets, semicolons
    characters_to_remove = ':?!()[];'
    name = name.translate(str.maketrans('', '', characters_to_remove))

    return name

def rename_recursive(directory):
    for root, dirs, files in os.walk(directory):
        # Rename files
        for filename in files:
            old_path = os.path.join(root, filename)
            new_filename = clean_name(filename)
            new_path = os.path.join(root, new_filename)

            # Rename the file
            os.rename(old_path, new_path)

        # Rename directories
        for dirname in dirs:
            old_path = os.path.join(root, dirname)
            new_dirname = clean_name(dirname)
            new_path = os.path.join(root, new_dirname)

            # Rename the directory
            os.rename(old_path, new_path)

# Provide the directory path where the files and directories are located
directory_path = './image-import/'

# Call the function to rename recursively in the specified directory
rename_recursive(directory_path)
