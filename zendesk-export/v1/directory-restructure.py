import os
import shutil

def match_directory_structure(directory_a, directory_b):
    for root, dirs, files in os.walk(directory_a):
        relative_path = os.path.relpath(root, directory_a)
        target_dir = os.path.join(directory_b, relative_path)

        # Create the corresponding directory in Directory B if it doesn't exist
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)

        # Copy files from Directory A to Directory B
        for file in files:
            source_file = os.path.join(root, file)
            target_file = os.path.join(target_dir, file)
            if not os.path.exists(target_file):
                shutil.copy2(source_file, target_file)

# Provide the paths of Directory A and Directory B
directory_a = 'home/mapachurro/mm-hc/help-center-images'
directory_b = 'home/mapachurro/mm-hc/docs-mm-helpcenter/static/img/help-center-images'

# Call the function to match the directory structure
match_directory_structure(directory_a, directory_b)
