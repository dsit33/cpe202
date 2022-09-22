import queue

def charAt(lst, index):
    if len(lst) - 1 < index:
        return " "
    return lst[index]

def radixsort(lst, length):
    longest = ""
    result = []
    queueLst = [queue.Queue() for i in range(256)]
    mainQueue = queue.Queue()
    for string in lst:
        if len(string) > len(longest):
            longest = string
        mainQueue.enqueue(string)
    maxIndex = len(longest) - 1
    while maxIndex >= 0:
        for word in mainQueue.items:
            lastChar = charAt(word, maxIndex).lower()
            queueLst[ord(lastChar)].enqueue(word)
        mainQueue.clear()
        for cue in queueLst:
            while not cue.isEmpty():
                mainQueue.enqueue(cue.front())
                cue.dequeue()
        maxIndex -= 1
    for word in mainQueue.items:
        result.append(word)
        
    return result
        
            