# LINK TO PROBLEM -----> https://leetcode.com/problems/circular-sentence/


def isCircularSentence(sentence: str) -> bool:
    arr = sentence.split(" ")
    if arr[0][0] != arr[-1][-1]:
        return False
    for i, item in enumerate(arr):
        if item == arr[-1]:
            break
        elif not item.endswith(arr[i + 1][0]):
            return False
    return True


def better_memory_usage_solution(sentence: str) -> bool:
    words = sentence.split()
    words += [words[0]]
    return all(a[-1] == b[0] for a, b in zip(words, words[1:]))
    # Check Later


def better_mem_usage_solution_2(sentence: str) -> bool:
    words = sentence.split()
    return all(w[-1] == words[(i + 1) % len(words)][0] for i, w in enumerate(words))
    # Check later
