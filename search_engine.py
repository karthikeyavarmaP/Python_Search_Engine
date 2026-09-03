import os
import re
import math
import heapq
from collections import defaultdict, Counter


# -------------------- TRIE --------------------

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()

            node = node.children[char]

        node.is_end = True

    def autocomplete(self, prefix, limit=10):
        node = self.root

        for char in prefix:
            if char not in node.children:
                return []

            node = node.children[char]

        suggestions = []

        def dfs(current_node, current_word):

            if len(suggestions) >= limit:
                return

            if current_node.is_end:
                suggestions.append(current_word)

            for char in sorted(current_node.children):
                dfs(
                    current_node.children[char],
                    current_word + char
                )

        dfs(node, prefix)

        return suggestions


# -------------------- SEARCH ENGINE --------------------

class SearchEngine:

    def __init__(self, folder="documents"):

        self.folder = folder

        self.documents = {}

        self.tokens_by_document = {}

        self.inverted_index = defaultdict(set)

        self.document_frequency = Counter()

        self.trie = Trie()


    # Convert text into words
    def tokenize(self, text):

        text = text.lower()

        words = re.findall(r"[a-z0-9]+", text)

        return words


    # Read documents
    def load_documents(self):

        for file_name in os.listdir(self.folder):

            if file_name.endswith(".txt"):

                path = os.path.join(
                    self.folder,
                    file_name
                )

                with open(
                    path,
                    "r",
                    encoding="utf-8"
                ) as file:

                    text = file.read()

                self.documents[file_name] = text

                self.tokens_by_document[file_name] = (
                    self.tokenize(text)
                )


    # Build inverted index
    def build_index(self):

        for file_name, words in (
            self.tokens_by_document.items()
        ):

            unique_words = set(words)

            for word in unique_words:

                self.inverted_index[word].add(
                    file_name
                )

                self.document_frequency[word] += 1

                self.trie.insert(word)


    # Calculate TF-IDF score
    def tf_idf(self, word, file_name):

        words = self.tokens_by_document[file_name]

        word_count = words.count(word)

        if word_count == 0:
            return 0

        # Term Frequency
        tf = word_count / len(words)

        total_documents = len(self.documents)

        document_frequency = (
            self.document_frequency[word]
        )

        # Inverse Document Frequency
        idf = math.log(
            (total_documents + 1)
            /
            (document_frequency + 1)
        ) + 1

        return tf * idf


    # Search documents
    def search(self, query, mode="AND", top_k=5):

        query_words = self.tokenize(query)

        if not query_words:
            return []

        document_sets = []

        for word in query_words:

            document_sets.append(
                self.inverted_index.get(
                    word,
                    set()
                )
            )


        # AND Search
        if mode == "AND":

            candidate_documents = (
                set.intersection(
                    *document_sets
                )
            )


        # OR Search
        elif mode == "OR":

            candidate_documents = (
                set.union(
                    *document_sets
                )
            )

        else:

            return []


        # Priority Queue / Heap
        heap = []

        for file_name in candidate_documents:

            score = 0

            for word in query_words:

                score += self.tf_idf(
                    word,
                    file_name
                )

            heapq.heappush(
                heap,
                (-score, file_name)
            )


        # Top-K results
        results = []

        while heap and len(results) < top_k:

            negative_score, file_name = (
                heapq.heappop(heap)
            )

            results.append(
                (
                    file_name,
                    -negative_score
                )
            )

        return results


    # Search statistics
    def statistics(self):

        total_words = sum(
            len(words)
            for words
            in self.tokens_by_document.values()
        )

        print("\nSEARCH ENGINE STATISTICS")
        print("-" * 40)

        print(
            "Documents Indexed:",
            len(self.documents)
        )

        print(
            "Total Words:",
            total_words
        )

        print(
            "Vocabulary Size:",
            len(self.inverted_index)
        )


# -------------------- MAIN PROGRAM --------------------

def main():

    engine = SearchEngine()

    engine.load_documents()

    engine.build_index()

    engine.statistics()


    print("\nDOCUMENT SEARCH ENGINE")

    print("-" * 40)

    print("1. Search documents")

    print("2. Autocomplete")

    print("3. Exit")


    while True:

        choice = input(
            "\nEnter your choice: "
        )


        # Document Search
        if choice == "1":

            query = input(
                "Enter search query: "
            )

            mode = input(
                "Choose mode (AND/OR): "
            ).upper()

            results = engine.search(
                query,
                mode
            )


            if results:

                print("\nTOP SEARCH RESULTS")

                print("-" * 40)

                for rank, result in enumerate(
                    results,
                    start=1
                ):

                    file_name = result[0]

                    score = result[1]

                    print(
                        f"{rank}. {file_name}"
                    )

                    print(
                        f"   TF-IDF Score: "
                        f"{score:.4f}"
                    )

            else:

                print(
                    "\nNo matching documents found."
                )


        # Autocomplete
        elif choice == "2":

            prefix = input(
                "Enter prefix: "
            ).lower()

            suggestions = (
                engine.trie.autocomplete(
                    prefix
                )
            )


            if suggestions:

                print(
                    "\nSuggestions:"
                )

                for word in suggestions:

                    print(
                        "-",
                        word
                    )

            else:

                print(
                    "\nNo suggestions found."
                )


        # Exit
        elif choice == "3":

            print(
                "\nSearch Engine Closed."
            )

            break


        else:

            print(
                "\nInvalid choice."
            )


if __name__ == "__main__":
    main()
