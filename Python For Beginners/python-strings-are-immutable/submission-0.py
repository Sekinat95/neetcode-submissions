def remove_fourth_character(word: str) -> str:
    fourth = word[3]
    new_str = word[:3]  + word[4:]
    return new_str



# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
