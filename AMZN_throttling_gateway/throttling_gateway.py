# Failed this one because of trying to use sliding window
# Really simple answer

def droppedRequests(requestTime):
    dropped = 0
    for i in range(len(requestTime)):
        if i > 2 and requestTime[i] == requestTime[i - 3]:
            dropped += 1
        elif i > 19 and requestTime[i] < requestTime[i - 20] + 10:
            dropped += 1
        elif i > 59 and requestTime[i] < requestTime[i - 60] + 60:
            dropped += 1
    return dropped
