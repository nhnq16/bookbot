def main():
    file_path = "books/frankenstein.txt"
    with open(file_path) as f:
        file_contents = f.read()
    num_words = len(file_contents.split()) 
    char_count = get_char_count(file_contents)

    print(f"--- Begin report of {file_path} ---")
    print(f"{num_words} words found in the document")
    print()
    for char, count in char_count.items():
        if (char.isalpha()):
            print(f"The '{char}' character was found {count} times")
    print("--- End report ---")

def get_char_count(text):
    char_count = {}
    for char in text.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

main()