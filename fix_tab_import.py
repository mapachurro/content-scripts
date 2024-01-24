import os
# this script deletes duplicate import statements. 
# specify the directory you want to start from
rootDir = '/home/mapachurro/repos/docs-mm-helpcenter/i18n'

for dirName, subdirList, fileList in os.walk(rootDir):
    for fname in fileList:
        if fname.endswith('.mdx'):
            file_path = os.path.join(dirName, fname)
            with open(file_path, 'r') as file:
                lines = file.readlines()

            new_lines = []
            imports_found = False
            for line in lines:
                if "import Tabs from '@theme/Tabs'; import TabItem from '@theme/TabItem';" in line:
                    if not imports_found:
                        new_lines.append(line)
                        imports_found = True
                else:
                    new_lines.append(line)

            with open(file_path, 'w') as file:
                file.writelines(new_lines)
