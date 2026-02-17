import os
import string
from collections import Counter


def read_file(filepath):
    # Accesses file and reads content
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            lines = file.readlines()
            text = "".join(lines)
        return text, lines
    except FileNotFoundError:
        print("Error: File not found.")
        return None, None
    except PermissionError:
        print("Error: Permission denied.")
        return None, None


def normalize_text(text):
    # Normalizing text
    text = text.lower()
    translator = str.maketrans("", "", string.punctuation)
    return text.translate(translator)


def analyze_text(text, lines):
    # core analysis
    line_count = len(lines)
    char_count = len(text)  # includes spaces and newline characters

    cleaned_text = normalize_text(text)
    words = cleaned_text.split()
    word_count = len(words)

    frequency = Counter(words)

    return line_count, word_count, char_count, frequency


def display_results(line_count, word_count, char_count, frequency, top_n=10):
    # Structure analysis
    print("\n===== Text Analysis Report =====\n")
    print(f"Total Lines      : {line_count}")
    print(f"Total Words      : {word_count}")
    print(f"Total Characters : {char_count}")

    print(f"\nTop {top_n} Most Frequent Words:")
    print("-" * 35)

    for index, (word, count) in enumerate(frequency.most_common(top_n), start=1):
        print(f"{index}. {word:<15} -> {count}")

    print("\nAnalysis Completed.\n")


def get_text_files():
    return [f for f in os.listdir() if f.endswith(".txt")]


def main():
    print("Word Count & Frequency Analysis Tool")
    print("-------------------------------------")

    files = get_text_files()

    if not files:
        print("No files found in current directory.")
        return

    print("\nAvailable Text Files:")
    for i, file in enumerate(files, start=1):
        print(f"{i}. {file}")

    try:
        choice = int(input("\nSelect file number: "))
        filepath = files[choice - 1]
    except (ValueError, IndexError):
        print("Invalid selection.")
        return

    text, lines = read_file(filepath)

    if text is None:
        return

    results = analyze_text(text, lines)
    display_results(*results)
    


if __name__ == "__main__":
    main()
