from collections import Counter


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        counts = Counter(tiles)

        def backtrack() -> int:
            total = 0
            for ch in counts:
                if counts[ch] > 0:
                    total += 1
                    counts[ch] -= 1
                    total += backtrack()
                    counts[ch] += 1
            return total

        return backtrack()