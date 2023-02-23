import time
from colors import *

def selectionSort(data, drawInfo, timeTick):
    size = len(data)

    for i in range(size):
        min_idx = i
        for j in range(i+1, size):
            if data[j] < data[min_idx]:
                min_idx = j
    
        data[i], data[min_idx] = data[min_idx], data[i]
        drawInfo(data, [BLACK if x == min_idx or x == i else RED for x in range(len(data))] )
        time.sleep(timeTick)

    drawInfo(data, [DARK_BLUE for x in range(len(data))])


