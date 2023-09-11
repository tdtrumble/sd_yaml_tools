import yaml
import os

last_key = "0"

def create_files_recursive(data, path=""):
    global last_key
    if isinstance(data, list):
        with open(os.path.join("./output/" + path, f"{last_key}.txt"), "w") as file:
            for item in data:
                file.write(item + "\n")
    elif isinstance(data, dict):
        for key, value in data.items():
            last_key = key
            new_path = os.path.join(path, key)
            os.makedirs("./output/" + new_path, exist_ok=True)  # Create the directory if it doesn't exist
            create_files_recursive(value, new_path)

def main(input_yaml):
    with open(input_yaml, "r") as yaml_file:
        data = yaml.safe_load(yaml_file)
        create_files_recursive(data)

if __name__ == "__main__":
    input_yaml = "/path/file.yaml"  # Replace with your YAML file path
    main(input_yaml)




