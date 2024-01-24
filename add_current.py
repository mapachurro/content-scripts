import os
import shutil

base_dir = '/home/mapachurro/repos/docs-mm-helpcenter/i18n'

for locale in os.listdir(base_dir):
    locale_dir = os.path.join(base_dir, locale, 'docusaurus-plugin-content-docs')
    
    if not os.path.isdir(locale_dir):
        continue

    print(f'Processing locale: {locale}')

    current_dir = os.path.join(locale_dir, 'current')
    os.makedirs(current_dir, exist_ok=True)

    for dir_name in os.listdir(locale_dir):
        if dir_name == 'current':
            continue

        dir_path = os.path.join(locale_dir, dir_name)
        dest_path = os.path.join(current_dir, dir_name)

        if os.path.isdir(dir_path):
            shutil.move(dir_path, dest_path)

print("Done!")
