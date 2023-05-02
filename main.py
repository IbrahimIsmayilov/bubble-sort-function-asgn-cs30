nums = [10, 70, 30, 100, 40, 45, 90, 80, 85]
words = ["dog","at", "good", "eye", "cat", "ball", "fish"]

def bubbleSort(anArray):
    num = len(anArray) - 1
    # Complete the amount of comparisons or passes needed
    for i in range(num):
        # Looping through the array and sorting values
        for n in range(num-i-1):
            # Swap the values if they are out of order
            if anArray[n] > anArray[n+1]:
                anArray[n], anArray[n+1] = anArray[n+1], anArray[n]    

