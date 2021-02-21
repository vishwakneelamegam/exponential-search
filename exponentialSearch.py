import time

def binarySearch(dataList,lowerBound,upperBound,searchElement):
    if lowerBound <= upperBound:
       mid = (lowerBound + upperBound) // 2
       if dataList[mid] == searchElement:
          return True
       if dataList[mid] > searchElement:
          return binarySearch(dataList,lowerBound,mid - 1,searchElement)
       return binarySearch(dataList,mid + 1,upperBound,searchElement)
    return False

def exponentialSearch(dataList,searchElement):
    try:
       listLength = len(dataList)
       if dataList[0] == searchElement:
          return True
       counter = 1
       while counter < listLength and dataList[counter] <= searchElement:
             counter = counter * 2
       return binarySearch(dataList,counter/2,min(counter,listLength - 1),searchElement)
    except Exception as e:
       return e


listData = list(range(1,9000000))
startTime = time.time()
print(exponentialSearch(listData,500))
endTime  = time.time() - startTime
print(endTime)
