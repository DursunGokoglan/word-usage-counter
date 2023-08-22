from pypdf import PdfReader
from en import most_used_words

pdf_to_use = input("Enter PDF: ")


def text_extractor(pdf):
    reader = PdfReader(pdf)
    number_of_pages = len(reader.pages)

    result = ''

    for page_number in range(number_of_pages):
        page = reader.pages[page_number]
        result += page.extract_text()

    result = result.lower()

    return result


def make_list(raw_text):
    word_list = raw_text.split()
    return word_list


def clean_list(cleaning_list):
    symbol_list = [".", ",", "?", "!", "'", '"', "(", ")"]

    for index in range(len(cleaning_list)):
        for symbol in symbol_list:
            cleaning_list[index] = cleaning_list[index].replace(symbol, "")

    return cleaning_list


def make_dict(word_list):
    word_dict = {}

    for item in word_list:
        if item not in word_dict:
            word_dict[item] = 1
        else:
            word_dict[item] += 1

    return word_dict


def sort_dict(word_dict):
    sorted_dict = sorted(word_dict.items(), key=lambda x: x[1])
    sorted_dict = sorted_dict[::-1]

    return sorted_dict


text = text_extractor(pdf_to_use)
uncleaned_bank = make_list(text)
word_bank = clean_list(uncleaned_bank)
usage_dict = make_dict(word_bank)
sorted_usage_list = sort_dict(usage_dict)

for word_dict in most_used_words["words"]:
    for couple in sorted_usage_list:
        if couple[0] == word_dict["englishWord"]:
            sorted_usage_list.remove(couple)

for pair in sorted_usage_list:
    print(f"{pair[0]} is used {pair[1]} times.")
