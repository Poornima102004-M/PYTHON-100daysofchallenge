# Define a function to read a file and calculate the average of numbers in it
def calculate_average(filename):
    total = 0
    count = 0
    try:
        with open(filename, 'r') as file:
            for line in file:
                try:
                    number = float(line.strip())
                    total += number
                    count += 1
                except ValueError:
                    print(f"Warning: Skipping non-numeric value '{line.strip()}'")
        if count == 0:
            raise ValueError("No valid numbers found in the file")
        return total / count
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
    except IOError:
        print(f"Error: Could not read from file '{filename}'")

# Example usage
filename = "numbers.txt"
try:
    average = calculate_average(filename)
    print(f"Average of numbers in '{filename}': {average}")
except ValueError as ve:
    print(f"ValueError: {ve}")
except Exception as e:
    print(f"Exception occurred: {e}")
