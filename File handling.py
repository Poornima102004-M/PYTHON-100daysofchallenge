def count_word_occurrences(input_file, output_file):
    try:
        # Open the input file for reading
        with open(input_file, 'r') as file:
            # Read the contents of the file
            text = file.read()

            # Split the text into words
            words = text.split()

            # Count the occurrences of each word
            word_count = {}
            for word in words:
                # Convert word to lowercase to avoid case sensitivity
                word = word.lower()
                word_count[word] = word_count.get(word, 0) + 1

        # Open the output file for writing
        with open(output_file, 'w') as file:
            # Write the word count to the output file
            for word, count in word_count.items():
                file.write(f"{word}: {count}\n")

        print("Word count written to", output_file)

    except FileNotFoundError:
        print("Input file not found.")
    except Exception as e:
        print("An error occurred:", e)

def main():
    input_file = "input.txt"
    output_file = "output.txt"
    count_word_occurrences(input_file, output_file)

if __name__ == "__main__":
    main()
