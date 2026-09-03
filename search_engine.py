import os

folder = "documents"

for file_name in os.listdir(folder):
    if file_name.endswith(".txt"):
        path = os.path.join(folder, file_name)

        with open(path, "r", encoding="utf-8") as file:
            text = file.read()

        print(file_name)
        print(text)
        print("-" * 40)
