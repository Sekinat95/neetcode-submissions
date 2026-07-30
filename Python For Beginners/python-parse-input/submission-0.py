from typing import List

def read_integers() -> List[int]:
    result = input()
    strings = result.split(",")
    int_lst= []
    for s in strings:
        int_lst.append(int(s))
    return int_lst

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
