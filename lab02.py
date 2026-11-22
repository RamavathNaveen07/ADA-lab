# 2. Design a Sort class containing merge_sort(arr: List[int]) -> List[int] and quick_sort(arr:
# List[int]) -> List[int] methods that accept an unsorted integer array and return the sorted
# array.



class Sort:

    def merge_sort(self, arr: list[int]) -> list[int]:
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2

        left = self.merge_sort(arr[:mid])
        right = self.merge_sort(arr[mid:])

        return self.merge(left, right)

    def merge(self, left: list[int], right: list[int]) -> list[int]:
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])

        return result

from typing import List



def quick_sort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]

    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)

    


s = Sort()

arr = [9, 7, 2, 8, 4, 6]

print("Original:", arr)
print("Merge Sort:", s.merge_sort(arr))
print("Quick_sort :", quick_sort(arr))