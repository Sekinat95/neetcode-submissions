import heapq
from typing import List


def heapify_strings(strings: List[str]) -> List[str]:
    hp_str = list(strings)
    heapq.heapify(hp_str)
    return hp_str


def heapify_integers(integers: List[int]) -> List[int]:
    hp_int = list(integers)
    heapq.heapify(hp_int)
    return hp_int
    


def heap_sort(nums: List[int]) -> List[int]:
    hp = list(nums)
    heapq.heapify(hp)
    res = []
    while hp:
        res.append(heapq.heappop(hp))
    return res


# do not modify below this line
print(heapify_strings(["b", "a", "e", "c", "d"]))
print(heapify_integers([3, 4, 5, 1, 2, 6]))
print(heap_sort([3, 4, 5, 1, 2, 6]))