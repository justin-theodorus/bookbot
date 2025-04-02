import sys
from stats import count_word

def count_letter(contents):
    count = {}
    for c in contents:
        c = c.lower()
        if c.isalpha():  
            count[c] = count.get(c, 0) + 1
    return count


def main():
    #  1. Check for correct number of CLI arguments
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)  # exit with error

    # 2. Get the file path from sys.argv
    file_path = sys.argv[1]

    # 3. Read the book file
    try:
        with open(file_path) as f:
            file_contents = f.read()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)

    # 4. Do the analysis and print the report
    print(f"--- Begin report of {file_path} ---")
    print(f"{count_word(file_contents)} words found in the document")
    print()
    
    count = count_letter(file_contents)
    
    for c in sorted(count):
        if c.isalpha():
            print(f"{c}: {count[c]}")

if __name__ == "__main__":
    main()
