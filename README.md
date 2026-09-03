# Python Document Search Engine

A Data Structures and Algorithms based document search engine built using Python.

This project performs efficient keyword-based search across multiple text documents using an **inverted index**, **Boolean AND/OR search**, **TF-IDF ranking**, **Top-K retrieval using a heap**, and **Trie-based autocomplete**.

---

## Features

- Text preprocessing and tokenization
- Inverted index for fast document retrieval
- Single and multi-keyword search
- Boolean AND / OR search
- TF-IDF based document ranking
- Top-K retrieval using a heap / priority queue
- Trie-based prefix autocomplete
- Search engine statistics
- Interactive command-line interface

---

## Data Structures and Algorithms Used

### Hash Map / Dictionary

A dictionary is used to build the inverted index.

Each word is mapped to the set of documents in which it appears.

Example:

```text
machine -> {doc1.txt, doc3.txt}
algorithms -> {doc2.txt, doc5.txt}
```

This allows fast lookup of documents containing a particular word.

### Set

Python sets are used for Boolean search operations.

- AND Search uses set intersection.
- OR Search uses set union.

### Trie

A Trie data structure is used for prefix-based autocomplete.

Example:

```text
Prefix: ma
```

Possible suggestions:

```text
machine
management
```

### Heap / Priority Queue

Python's `heapq` module is used to retrieve the highest-ranked documents efficiently.

The heap stores documents based on their TF-IDF relevance scores and returns the Top-K results.

### TF-IDF Ranking

TF-IDF is used to measure how relevant a document is to a search query.

TF represents how frequently a word occurs in a document.

IDF reduces the importance of words that appear in many documents.

The final TF-IDF score is used to rank matching documents.

---

## Project Structure

```text
Python_Search_Engine/
│
├── search_engine.py
├── README.md
│
└── documents/
    ├── doc1.txt
    ├── doc2.txt
    ├── doc3.txt
    ├── doc4.txt
    ├── doc5.txt
    ├── doc6.txt
    ├── doc7.txt
    └── doc8.txt
```

---

## How the Search Engine Works

The program follows these steps:

1. Reads all `.txt` files from the `documents` folder.
2. Converts document text to lowercase.
3. Tokenizes the text into individual words.
4. Builds an inverted index.
5. Stores document frequency information for every word.
6. Builds a Trie for autocomplete.
7. Accepts a search query from the user.
8. Performs AND or OR retrieval using set operations.
9. Calculates TF-IDF scores for matching documents.
10. Uses a heap to return the Top-K ranked results.

---

## How to Run

Make sure Python 3 is installed.

Clone the repository:

```bash
git clone https://github.com/karthikeyavarmaP/Python_Search_Engine.git
```

Move into the project directory:

```bash
cd Python_Search_Engine
```

Run the program:

```bash
python search_engine.py
```

No external Python libraries are required.

---

## Search Engine Menu

When the program starts:

```text
DOCUMENT SEARCH ENGINE
----------------------------------------
1. Search documents
2. Autocomplete
3. Exit
```

---

## Example: AND Search

```text
Enter your choice: 1
Enter search query: machine learning
Choose mode (AND/OR): AND
```

The program retrieves documents containing both `machine` and `learning`.

Matching documents are ranked using TF-IDF scores.

---

## Example: OR Search

```text
Enter your choice: 1
Enter search query: data algorithms
Choose mode (AND/OR): OR
```

The search engine returns documents containing either `data` or `algorithms`.

---

## Example: Autocomplete

```text
Enter your choice: 2
Enter prefix: ma
```

Possible output:

```text
Suggestions:
- machine
- management
```

Autocomplete is implemented using a Trie.

---

## Search Engine Statistics

The program displays:

```text
SEARCH ENGINE STATISTICS
----------------------------------------
Documents Indexed: 8
Total Words: ...
Vocabulary Size: ...
```

These values represent the number of indexed documents, total tokens, and unique searchable terms.

---

## Core Concepts Demonstrated

- Data Structures and Algorithms
- Hash Maps
- Sets
- Trie
- Heap / Priority Queue
- String Processing
- Inverted Indexing
- Boolean Retrieval
- TF-IDF Ranking
- Top-K Retrieval
- Information Retrieval
- Object-Oriented Programming
- File Handling in Python

---

## Time Complexity

Let:

- `N` = total number of words across all documents
- `P` = prefix length
- `D` = number of matching documents

### Building the Index

```text
O(N)
```

### Keyword Lookup

Average dictionary lookup:

```text
O(1)
```

### Trie Prefix Search

```text
O(P)
```

to reach the prefix node, followed by traversal of matching words.

### Top-K Retrieval

For the current implementation:

```text
O(D log D)
```

---

## Technologies Used

- Python 3
- os
- re
- math
- heapq
- collections.defaultdict
- collections.Counter

Only Python standard-library modules are used.

---

## Future Improvements

- Stop-word removal
- Stemming and lemmatization
- Phrase search
- Fuzzy search
- Search-result snippets
- Larger document datasets
- Persistent indexing
- Graphical user interface
- Web-based search interface

---

## Resume Description

**Document Search Engine & Retrieval System | Personal Project**

Built a Python document search engine using inverted indexing, hash maps and set operations to support multi-keyword AND/OR retrieval.

Implemented TF-IDF ranking, heap-based Top-K retrieval and Trie-based autocomplete for efficient search and prefix suggestions.

---

## Author

**Karthikeyavarma**
