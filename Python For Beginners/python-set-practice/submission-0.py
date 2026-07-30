from typing import List

def contains_duplicate(words: List[str]) -> bool:
    unique = set(words)
    for i in unique:
        if words.count(i) > 1:
            return True
        else:
            return False

# do not modify code below this line
print(contains_duplicate(["hello", "world", "hello"]))
print(contains_duplicate(["hello", "world", "i", "am", "great"]))
print(contains_duplicate(["hello", "hello", "hello"]))
print(contains_duplicate(["Hello", "hellooo", "hello"]))
