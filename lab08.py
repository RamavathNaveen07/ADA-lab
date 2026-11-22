from dataclasses import dataclass
from typing import Dict
import heapq


@dataclass
class Node:
    char: str
    frequency: int
    left: object = None
    right: object = None


class HuffmanCoder:

    def __init__(self):
        self.root = None

    def build_tree(self, frequencies: Dict[str, int]) -> Node:
        heap = []
        counter = 0

        # Create leaf nodes
        for char, frequency in frequencies.items():
            node = Node(char, frequency)
            heapq.heappush(heap, (frequency, counter, node))
            counter += 1

        # Build Huffman Tree
        while len(heap) > 1:
            f1, _, left = heapq.heappop(heap)
            f2, _, right = heapq.heappop(heap)

            new_node = Node(
                "",
                f1 + f2,
                left,
                right
            )

            heapq.heappush(
                heap,
                (new_node.frequency, counter, new_node)
            )

            counter += 1

        self.root = heap[0][2]

        return self.root

    def generate_codes(self) -> Dict[str, str]:
        codes = {}

        def generate(node, code):
            if node is None:
                return

            # Leaf node
            if node.char != "":
                codes[node.char] = code
                return

            generate(node.left, code + "0")
            generate(node.right, code + "1")

        generate(self.root, "")

        return codes


# Example
frequencies = {
    'a': 5,
    'b': 9,
    'c': 12,
    'd': 13,
    'e': 16,
    'f': 45
}

huffman = HuffmanCoder()

huffman.build_tree(frequencies)

codes = huffman.generate_codes()

print("Huffman Codes:")

for char, code in codes.items():
    print(char, ":", code)