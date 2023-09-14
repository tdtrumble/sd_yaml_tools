import os

def remove_commented_lines_and_sort(file_path):
    # Read the file, remove commented lines, and store non-commented lines in a list
    with open(file_path, 'r') as file:
        lines = [line for line in file if not line.strip().startswith("#")]

    # Sort the non-commented lines
    lines.sort()

    # Write the sorted lines back to the file
    with open(file_path, 'w') as file:
        file.writelines(lines)

def process_directory(directory_path):
    for root, _, files in os.walk(directory_path):
        for file_name in files:
            if file_name.endswith(".txt"):  # Adjust the file extension as needed
                file_path = os.path.join(root, file_name)
                remove_commented_lines_and_sort(file_path)
                print(f"Removed comments and sorted lines in {file_path}")

if __name__ == "__main__":
    directory_to_process = "/home/tdtru/yaml_writer/WILDCARDS"

    if os.path.isdir(directory_to_process):
        process_directory(directory_to_process)
        print("Commented lines removed and lines sorted in all eligible files.")
    else:
        print("The specified path is not a directory.")
