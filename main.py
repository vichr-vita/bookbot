from dataclasses import dataclass
import sys
import pathlib


@dataclass
class WordCount:
    word: str
    count: int

    def increment(self) -> None:
        self.count += 1


def sort_on_count(wc: WordCount):
    return wc.count


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python script.py <path_to_file>")
        sys.exit(1)

    file_path_str = sys.argv[1]
    file_path = pathlib.Path(file_path_str)
    with open(file_path) as f:
        file_contents = f.read().lower()
        words = file_contents.split()

        total_word_count = len(words)

        words_count: dict[str, WordCount] = {}
        for word in words:
            if word in words_count:
                words_count[word].increment()
            else:
                words_count[word] = WordCount(word, 1)
        words_count_leaderboard = list(words_count.values())
        words_count_leaderboard = sorted(
            words_count_leaderboard, key=sort_on_count, reverse=True
        )

        character_count: dict[str, int] = {}
        for ch in file_contents:
            if ch in character_count:
                character_count[ch] += 1
            else:
                character_count[ch] = 1
        character_count_leaderboard = [(k, v) for k, v in character_count.items()]
        character_count_leaderboard = sorted(
            character_count_leaderboard, key=lambda x: x[1], reverse=True
        )

        wordcount_header = f"Word count leaderboard for {file_path.name}:"
        print(wordcount_header)
        print("=" * len(wordcount_header))
        for i, word_count in enumerate(words_count_leaderboard[0:10]):
            print(f'{i+1}. "{word_count.word}" x{word_count.count}')

        character_count_header = f"Character count leaderboard for {file_path.name}:"
        print(character_count_header)
        print("=" * len(character_count_header))
        for i, character_count_item in enumerate(character_count_leaderboard[0:10]):
            print(f'{i+1}. "{character_count_item[0]}" x{character_count_item[1]}')


if __name__ == "__main__":
    main()
