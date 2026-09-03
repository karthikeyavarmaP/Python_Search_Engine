import os
import re
from collections import defaultdict

folder = "documents"

documents = {}
inverted_index = defaultdict(set)

# Read all documents
for file_name in os.listdir(folder):

    if file_name.endswith(".txt"):

        path = os.path.join(folder, file_name)

        with open(path, "r", encoding="utf-8") as file:
            text = file.read()

        documents[file_name] = text


# Tokenization function
def tokenize(text):

    text = text.lower()

    words = re.findall(r"[a-z0-9]+", text)

    return words


# Build inverted index
for file_name, text in documents.items():

    words = tokenize(text)

    for word in words:

        inverted_index[word].add(file_name)


# Display inverted index
print("INVERTED INDEX")
print("-" * 40)

for word in sorted(inverted_index):

    print(word, "->", sorted(inverted_index[word]))

# Search function
def search_word(query):

    query = query.lower()

    if query in inverted_index:

        return sorted(inverted_index[query])

    else:

        return []


# User search
print("\nSEARCH ENGINE")
print("-" * 40)

query = input("Enter a word to search: ")

results = search_word(query)

if results:

    print("\nWord found in:")

    for file_name in results:
        print(file_name)

else:

    print("\nNo matching document found.")
