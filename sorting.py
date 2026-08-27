import os

def organize_files(folder_path="."):
    files = os.listdir(folder_path)
    moved_count = 0

    for file in files:
        if file.endswith(".py"):
            try:
                if os.path.isfile(file):
                    extension = file.split(".")[-1]
                    folder_name = extension + "_files"

                    if not os.path.exists(folder_name):
                        os.makedirs(folder_name)

                    os.rename(file, os.path.join(folder_name, file))
                    moved_count += 1
                    print(f"Moved {file} to {folder_name}")

            except Exception as e:
                print(f"Couldn't move {file}: {e}")

    print(f"Done! Organized {moved_count} files.")

organize_files()