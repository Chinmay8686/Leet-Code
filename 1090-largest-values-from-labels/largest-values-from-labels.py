class Solution:
    def largestValsFromLabels(self, values, labels, numWanted, useLimit):

        items = []

        for i in range(len(values)):
            items.append((values[i], labels[i]))

        items.sort(reverse=True)

        count = {}
        total = 0
        selected = 0

        for value, label in items:

            if selected == numWanted:
                break

            if count.get(label, 0) < useLimit:

                total += value
                selected += 1

                count[label] = count.get(label, 0) + 1

        return total