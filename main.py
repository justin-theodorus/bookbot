

# ./github.com/justin-theodorus/bookbot/books/frankenstein.txt

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        #print(file_contents)

        def count_word(contents):
            count = contents.split()
            return len(count)
        def count_letter(contents):
            count = {}
            #words = contents.split()
            
            for c in contents:
                if c.lower() not in count:
                    count[c.lower()] = 1
                else:
                    count[c.lower()] += 1
            #print(count[' '])
            return count


        #print(count_letter(str(file_contents)))
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{count_word(str(file_contents))} words found in the document")
        print()
        count = count_letter(file_contents)
        for c in count:
            if c.isalpha():
                print(f"The '{c}' character was found {count[c]} times")


main()

