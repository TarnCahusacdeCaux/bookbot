def main():
    with open("books/frankenstein.txt") as f:
        return f.read()


def count_words(book):
    words = book.split()
    return f"{len(words)} words found in the document\n"


def count_characters(book):
    lower_case_string = book.lower()
    character_frequency = {}
    for character in lower_case_string:
        if character.isalpha():
            if character not in character_frequency:
                character_frequency[character] = 1
            else:
                character_frequency[character] += 1
        final_string = ""
        for character in character_frequency:
            final_string += f"The '{character}' character was found {character_frequency[character]} times\n"
    return final_string


print("--- Begin report of books/frankenstein.txt ---\n", count_words(main()))
print(count_characters(main()), "\n--- End report ---")
