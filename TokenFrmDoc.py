import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
if __name__ == "__main__":
    file_path = input("Enter file path: ")
    with open(file_path, 'r', encoding='utf-8') as file:
        file_content = file.read()
    sentence_tokens = sent_tokenize(file_content)
    word_tokens = word_tokenize(file_content)
    print("Sentence Tokens:", sentence_tokens)
    print("Word Tokens:", word_tokens)
# Output  
# Enter file path: Textfile.txt
# Sentence Tokens: ['Lorem Ipsum is simply dummy text of the printing and typesetting industry.', "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book."]
# Word Tokens: ['Lorem', 'Ipsum', 'is', 'simply', 'dummy', 'text', 'of', 'the', 'printing', 'and', 'typesetting', 'industry', '.', 'Lorem', 'Ipsum', 'has', 'been', 'the', 'industry', "'s", 'standard', 'dummy', 'text', 'ever', 'since', 'the', '1500s', ',', 'when', 'an', 'unknown', 'printer', 'took', 'a', 'galley', 'of', 'type', 'and', 'scrambled', 'it', 'to', 'make', 'a', 'type', 'specimen', 'book', '.']