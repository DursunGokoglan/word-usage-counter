from pypdf import PdfReader

pdf_to_use = input("Enter PDF: ")


def text_extractor(pdf):
    reader = PdfReader(pdf)
    number_of_pages = len(reader.pages)

    text = ''

    for page_number in range(number_of_pages):
        page = reader.pages[page_number]
        text += page.extract_text()

    text = text.lower()

    return text


word_bank = text_extractor(pdf_to_use).split()
symbol_list = [".", ",", "?", "!", "'", '"', "(", ")"]

for index in range(len(word_bank)):
    for symbol in symbol_list:
        word_bank[index] = word_bank[index].replace(symbol, "")

usage_dict = {}

for word in word_bank:
    if word not in usage_dict:
        usage_dict[word] = 1
    else:
        usage_dict[word] += 1

sorted_usage_dict = sorted(usage_dict.items(), key=lambda x: x[1])
sorted_usage_dict = sorted_usage_dict[::-1]

for pair in sorted_usage_dict:
    print(f"{pair[0]} is used {pair[1]} times.")
