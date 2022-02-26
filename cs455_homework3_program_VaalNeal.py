from cmath import pi
import csv
import math
from random import randint

def computeDistance(point1, point2):
    return int(math.fabs(point1[0] - point2[0]) + math.fabs(point1[1] - point2[1]))


def askUserInput():
    print("Please enter the number of clusters you want to form, 2 or 3. ")
    Index = int(input("Enter number : "))
    while True:
        if Index == 2 or Index == 3:
            break
        else:
            Index = int(input("That was an invalid number, please re-enter either 2 or 3: "))
    return Index

def makeInitialCentroids(n, points):
    clusters = []
    for x in range(0,n):
        clusters.append([points[randint(1,100)], []])
    return clusters

def makePoints(data):
    pointList = []
    for x in range(len(data[0])):
        pointList.append([data[0][x], data[1][x]])
    return pointList

def clusterizeData(clusters, points):
    for x in points:
        if len(clusters) == 2:
            if (computeDistance(x, clusters[0][0]) < computeDistance(x, clusters[1][0])):
                clusters[0][1].append(x)
            else:
                clusters[1][1].append(x)
        else:
            if (computeDistance(x, clusters[0][0]) < computeDistance(x, clusters[1][0]) and computeDistance(x, clusters[0][0]) < computeDistance(x, clusters[2][0])):
                clusters[0][1].append(x)
            elif (computeDistance(x, clusters[1][0]) < computeDistance(x, clusters[0][0]) and computeDistance(x, clusters[1][0]) < computeDistance(x, clusters[2][0])):
                clusters[1][1].append(x)
            else:
                clusters[2][1].append(x)
    return clusters


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
    open('auto-mpg.csv')

    normalized_data = []
    for j in range(0,2):
        columnList = []
        for i in range(1, len(dataAsRows)):
                columnList.append(int(dataAsRows[i][j]))
        normalized_data.append(normalize_data(columnList, min(columnList), max(columnList)))
    
    dataPoints = makePoints(normalized_data)
    clusterCentroids = makeInitialCentroids(askUserInput(), dataPoints)
    
    clusterCentroids = clusterizeData(clusterCentroids, dataPoints)
    print(clusterCentroids)

    

