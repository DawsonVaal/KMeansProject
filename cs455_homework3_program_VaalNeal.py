import csv
import math
from random import randint

myDict = {}

def makeInitialCentroids(n, dataPoints):
    for x in n:
        myDict.__setattr__(dataPoints[randint(0,99)], [])

def askUserInput():
    print("Please enter the number of clusters you want to form, 2 or 3. ")
    Index = int(input("Enter number : "))
    while True:
        if Index == 2 or Index == 3:
            return Index
        else:
            Index = int(input("That was an invalid number, please re-enter either 2 or 3: "))


def makePoints(data):
    pointList = []
    for x in range(len(data[0])):
        pointList.append([data[0][x], data[1][x]])
    return pointList

def normalize_data(data, min, max):
    normal_column = []
    for i in range(len(data)):
        new_value = round((data[i] - min) / (max - min) * 100)
        normal_column.append(new_value)
    return normal_column

with open('auto-mpg.csv', mode='r') as read_obj:
    reader = csv.reader(read_obj)
    dataAsRows = list(reader)

if __name__ == '__main__':
    dataPoints = []
    open('auto-mpg.csv')

    normalized_data = []
    for j in range(0,2):
        columnList = []
        for i in range(1, len(dataAsRows)):
                columnList.append(int(dataAsRows[i][j]))
        normalized_data.append(normalize_data(columnList, min(columnList), max(columnList)))
    dataPoints = makePoints(normalized_data)

    

