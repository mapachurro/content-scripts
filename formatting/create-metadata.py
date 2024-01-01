import os

def create_index_mdx(directory):
    for root, dirs, files in os.walk(directory):
        for dirname in dirs:
            subdir_path = os.path.join(root, dirname)
            index_mdx_path = os.path.join(subdir_path, 'index.mdx')

            # Check if index.mdx file already exists in the subdirectory
            if not os.path.exists(index_mdx_path):
                # Create the index.mdx file with the generated content
                with open(index_mdx_path, 'w') as f:
                    content = f'---\ntitle: "{dirname.replace("-", " ")}"\nsidebar_position: 1\n---\n'
                    f.write(content)

# Provide the root directory path to start the iteration
root_directory = '/home/mapachurro/mm-hc/docs-mm-helpcenter/docs'
# Call the function to create index.mdx files recursively
create_index_mdx(root_directory)
