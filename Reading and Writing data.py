import json

def write_to_json(data, filename):
    try:
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"Data successfully written to '{filename}'.")
    except IOError:
        print(f"Error writing to file '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def read_from_json(filename):
    data = {}
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
        print(f"Data read successfully from '{filename}':")
        print(json.dumps(data, indent=4))
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except json.JSONDecodeError as json_err:
        print(f"Error decoding JSON from '{filename}': {json_err}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return data

def main():
    data_to_write = {
        "name": "John Doe",
        "age": 30,
        "city": "New York"
    }
    filename = 'data.json'
    
    # Write data to JSON file
    write_to_json(data_to_write, filename)
    
    # Read data from JSON file
    data_read = read_from_json(filename)

if __name__ == "__main__":
    main()
