from collections import Counter
from typing import Counter as CounterType


def count_chars(s1: str, s2: str) -> CounterType:
    s1_ = list(s1)
    s2_ = list(s2)
    
    counter= Counter(s1_)
    counter.update(s2_)
    return counter
  

# do not modify below this line
print(count_chars("hello", "world"))
print(count_chars("hello", "worldhello"))
print(count_chars("areallylongstring", "heyhowisitgoing"))
