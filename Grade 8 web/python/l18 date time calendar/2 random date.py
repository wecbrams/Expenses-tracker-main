import random
import time

def getRandomDate(startDate, endDate):
    print(f"Printing random date between {startDate} and {endDate}")
    randomGenerator = random.random()
    dateFormat = '%m/%d/%Y'
    
    startDate = time.mktime(time.strptime(startDate, dateFormat))
    endDate = time.mktime(time.strptime(endDate, dateFormat))
    
    randomTime = startDate + randomGenerator * (endDate - startDate)
    randomDate = time.strftime(dateFormat, time.localtime(randomTime))
    
    return randomDate

print("Random Date = ", getRandomDate("1/1/2016", "12/12/2026"))