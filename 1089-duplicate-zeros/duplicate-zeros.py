class Solution:
    def duplicateZeros(self, arr):

        tempArr = []

        # Traverse each element in the array
        for i in range(len(arr)):

            # If element is 0, add zero twice
            if arr[i] == 0:
                tempArr.append(0)
                tempArr.append(0)

            # Otherwise, add the element once
            else:
                tempArr.append(arr[i])

        # Copy only the original array length
        for i in range(len(arr)):
            arr[i] = tempArr[i]