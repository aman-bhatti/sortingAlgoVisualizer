import time
from colors import *

def insertionSort(data, drawInfo, timeSet):
    for i in range(len(data)):
        value = data[i]
        j = i 
        while j > 0 and value < data[j-1]:
            data[j] = data[j - 1]
            j -= 1
        data[j] = value
        drawInfo(data, [YELLOW if x == j or x == i else BLUE for x in range(len(data))])
        time.sleep(timeSet)

    drawInfo(data, [BLUE for x in range(len(data))])