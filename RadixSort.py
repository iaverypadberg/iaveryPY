# Isaac Padberg
# 11.14.2019

"""Radix Sort"""


class Radix:

    def __init__(self, array):

        # Take the users input and copy it into our own array
        self.unsortedArray = array.copy()
        # Call radix sort and store its return value
        sortedArray = self.radixSort()
        self.sortedArray = []

        print("Here is your sorted array:", sortedArray, "\n")

    def radixSort(self):

        # Get the number with the most decimal places in the array.
        maxDeci = max(self.unsortedArray)

        # Decimal place counter that will be incremented by a multiple of 10.
        deciPlace = 1

        # Make 10 buckets(0-9) for the different values.
        self.sortedArray = [0] * len(self.unsortedArray)

        while deciPlace < maxDeci:

            # Call sortOnDeci and sort on the given decimal place.
            self.sortOnDeci(deciPlace)

            # Copy over the sorted array to the unsorted array
            self.unsortedArray = self.sortedArray.copy()

            # Increment decimal place by a factor of 10
            deciPlace *= 10
        return self.unsortedArray

    def sortOnDeci(self, deciPlace):

        length = len(self.unsortedArray)

        index = 0

        # Create a count array to store the number of occurrences of each number.
        countOccur = [0] * 10

        # Loop through the unsorted array and add the occurrence of each number to countOccur.
        for i in range(0, length):

            # Get the number from 0-9 at the specified decimal place
            index = (self.unsortedArray[i]/deciPlace) % 10

            # Change index to an integer named intIndex.
            intIndex= int(index)

            # Increase the occurrence of number by 1 in the count array
            countOccur[intIndex]+=1

        # Add up all the indices from the left to the right.
        # So (countOccur[1] = countedOccur[0]+countOccur[1]...)
        for a in range(0, len(countOccur)):
            countOccur[a] += countOccur[a-1]

        # Shift the values of each index in countOccur to the right.
        # Need to traverse array from right to left.
        # Index is now paired with the corresponding starting index of
        # that particular number in the sortedArray
        for x in reversed(range(0, len(countOccur))):
            countOccur[x] = countOccur[x-1]
            if x == 0:
                countOccur[x] = 0

        # Finally place the contents of the unsortedArray to the sortedArray using
        # the countOccur as a template for which index to place each number at.
        # Index of countOccur is the number to be placed, and the value at that
        # index is the starting index to place it at.
        for j in self.unsortedArray:
            intIndex = int(j/deciPlace) % 10
            self.sortedArray[countOccur[intIndex]] = j
            countOccur[intIndex] += 1


# Code to call the Radix Class and sort the given array.
arr1 = [55, 31, 44, 4, 5, 63, 4]
done = Radix(arr1)


# Important scratch work for understanding how the code above works.
# Still learning python so this is very helpful to have

print("## Code I found Helpful ##")
index1 = arr1.index(4)
print("Index of the the value 4:", index1)
arr2 = [1,23,4,1,2,]

temp = int((4/1)%10)

arr2 = arr1.copy()
arr1 = []
arr1 = arr2.copy()

count1 = [0]*10
count1[2] += 1
count1[2] += 1

print("Incrementing values at specific indices:",count1[2])



