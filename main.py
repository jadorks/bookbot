file_name = "books/frankenstein.txt"

def main():
    with open(file_name) as f:
        file_contents = f.read()
        num_words = count_words(file_contents)
        result = count_letters(file_contents)
        print_result(result, num_words)
        
def count_words(text):
    return (len(text.split()))

def count_letters(text):
    result = {}
    for letter in text:
        if letter.isalpha():
            lower_case_letter = letter.lower()
            result[lower_case_letter] = result.get(lower_case_letter, 0) + 1   
    return result

def print_result(result, num_words):
    print(f"--- Begin report of {file_name} ---")
    print(f"{num_words} words found in the document\n\n")
    
    sorted_result = sorted(result.items(), key=lambda item: item[1], reverse=True)
    for letter, count in sorted_result:
        print(f"The '{letter}' character was found {count} times")

main()