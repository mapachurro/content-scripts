import os
import re

def update_image_links(directory_a, directory_b):
    image_files = get_image_files(directory_b)

    for root, _, files in os.walk(directory_a):
        for file in files:
            if file.endswith(('.md', '.mdx')):
                file_path = os.path.join(root, file)
                update_file_image_links(file_path, image_files, directory_b)

def get_image_files(directory):
    image_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.svg')):
                image_files.append(os.path.join(root, file))
    return image_files

def update_file_image_links(file_path, image_files, directory_b):
    with open(file_path, 'r') as f:
        content = f.read()

    for image_file in image_files:
        image_file_name = os.path.basename(image_file)
        image_file_relative_path = os.path.relpath(image_file, directory_b).replace("\\", "/")
        image_file_relative_path = re.escape(image_file_relative_path)  # Escape special characters in the path

        # Update image links in the content using capture group and backreference
        content = re.sub(r'(!\[.*\]\()(' + re.escape(image_file_name) + r')', r'\1' + image_file_relative_path, content)

    with open(file_path, 'w') as f:
        f.write(content)

# Provide the paths of Directory A and Directory B
directory_a = '/home/mapachurro/mm-hc/docs-mm-helpcenter/docs'
directory_b = '/home/mapachurro/mm-hc/docs-mm-helpcenter/static/img/help-center-images'

# Call the function to update image links in the markdown files
update_image_links(directory_a, directory_b)
