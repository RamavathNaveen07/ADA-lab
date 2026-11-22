from typing import List
import random


def strStr(haystack: str, needle: str) -> int:
    if needle == "":
        return 0

    # Build LPS array
    lps = [0] * len(needle)
    length = 0
    i = 1

    while i < len(needle):
        if needle[i] == needle[length]:
            length += 1
            lps[i] = length
            i += 1
        elif length > 0:
            length = lps[length - 1]
        else:
            lps[i] = 0
            i += 1

    # KMP search
    i = 0
    j = 0

    while i < len(haystack):
        if haystack[i] == needle[j]:
            i += 1
            j += 1

            if j == len(needle):
                return i - j

        elif j > 0:
            j = lps[j - 1]
        else:
            i += 1

    return -1


class Randomizer:

    def __init__(self, stream: List[int]):
        self.stream = stream

    def getRandom(self) -> int:
        result = None

        for i, value in enumerate(self.stream):
            if random.randint(1, i + 1) == 1:
                result = value

        return result


# Example 1: KMP
print(strStr("hello", "ll"))
print(strStr("aaaaa", "bba"))

# Example 2: Reservoir Sampling
randomizer = Randomizer([10, 20, 30, 40, 50])
print("Random element:", randomizer.getRandom())