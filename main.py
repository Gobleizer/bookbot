def main():
    with open('./books/frankenstein.txt') as f:
        file_contents = f.read()
        print_book_report(file_contents)
        
def calculate_word_count(input):
    return len(input.split())

def printBook(book_text):
    print(book_text)

def calculate_character_counts(input):
    character_counts = {}
    lower_case_input = input.lower()
    for char in lower_case_input:
        if character_counts.get(char):
            character_counts[char] += 1
        else:
            character_counts[char] = 1
    return character_counts

def print_book_report(book):
    print("--- Begin report of books/frankenstein.txt ---")
    word_count = calculate_word_count(book)
    print(f"{word_count} words found in the document")
    character_counts = calculate_character_counts(book)
    character_counts_list = []
    for char, count in character_counts.items():
        if char.isalpha():
            character_counts_list.append({"char": char, "count": count})
    
    character_counts_list.sort(key=lambda x: x["count"], reverse=True)    
    for item in character_counts_list:
        char = item["char"]
        count = item["count"]
        print(f"The '{char}' character was found {count} times")

    print("--- End report ---")

main()