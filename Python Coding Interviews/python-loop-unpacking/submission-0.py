from typing import List, Tuple


def best_student(scores: List[Tuple[str, int]]) -> str:
    sc = []
    for score in scores:
        x,y = score
        sc.append(y)
    max_score = max(sc)
    result = 0
    for k,v in scores:
        if v == max_score:
            result = k
    return result
        




# do not modify below this line
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))