import os
import shutil

def move_files_one_directory_up(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            new_path = os.path.join(os.path.dirname(root), file)
            
            # Move the file one directory up
            shutil.move(file_path, new_path)
    
    # Delete the original parent directories (if they are empty)
    for root, dirs, files in os.walk(directory, topdown=False):
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            try:
                os.rmdir(dir_path)
            except OSError:
                # Directory is not empty, ignore and continue
                pass

if __name__ == "__main__":
    directory_to_process = ""  # Replace with your target directory
    move_files_one_directory_up(directory_to_process)