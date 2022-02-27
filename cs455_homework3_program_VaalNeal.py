import csv
import math
import matplotlib.pyplot as plot
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
        clusters.append([points[randint(1,99)], []])
    return clusters

def makePoints(data):
    pointList = []
    for x in range(len(data[0])):
        pointList.append([data[0][x], data[1][x]])
    return pointList

def clusterizeData(clusters, points):
    for cluster in clusters:
        cluster[1].clear()
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

def SSE (center, cluster):
    sum = 0
    for point in cluster:
        distance = computeDistance(center, point)
        sum = sum + distance^2
    return sum

def visiualize_clusters(clusterCentroids):
    X = []
    Y = []
    for point in clusterCentroids[0][1]:
        X.append(point[0])
        Y.append(point[1])
    plot.xlim([0,105])
    plot.ylim([0,105])
    plot.scatter(X,Y, color = "red")
    plot.scatter(clusterCentroids[0][0][0], clusterCentroids[0][0][1], color = "black", marker = "^")
    X.clear()
    Y.clear()

    for point in clusterCentroids[1][1]:
        X.append(point[0])
        Y.append(point[1])
    plot.xlim([0, 105])
    plot.ylim([0, 105])
    plot.scatter(X, Y, color = "green")
    plot.scatter(clusterCentroids[1][0][0], clusterCentroids[1][0][1], color="black", marker="^")
    X.clear()
    Y.clear()

    if len(clusterCentroids) == 3:
        for point in clusterCentroids[2][1]:
            X.append(point[0])
            Y.append(point[1])
        plot.xlim([0, 105])
        plot.ylim([0, 105])
        plot.scatter(X, Y, color = "blue")
        plot.scatter(clusterCentroids[2][0][0], clusterCentroids[2][0][1], color="black", marker="^")
        X.clear()
        Y.clear()

    plot.show()

def recalibrateCentroids(clusters):
    for cluster in clusters:
        xSum = 0
        ySum = 0
        for point in cluster[1]:
            xSum += point[0]
            ySum += point[1]
        xAverage = xSum/len(cluster[1])
        yAverage = ySum/len(cluster[1])
        cluster[0] = [xAverage, yAverage]
    return clusters

with open('auto-mpg.csv', mode='r') as read_obj:
    reader = csv.reader(read_obj)
    dataAsRows = list(reader)

if __name__ == '__main__':
    open('auto-mpg.csv')

    normalized_data = []
    for j in range(0,2):
        columnList = []
        for i in range(1, len(dataAsRows)):
                columnList.append(int(round(float(dataAsRows[i][j]))))
        normalized_data.append(normalize_data(columnList, min(columnList), max(columnList)))
    
    dataPoints = makePoints(normalized_data)
    clusterCentroids = makeInitialCentroids(askUserInput(), dataPoints)
    clusterCentroids = clusterizeData(clusterCentroids, dataPoints)
    visiualize_clusters(clusterCentroids)
    for i in range(0, len(clusterCentroids)):
        print("SSE for cluster "+str(i+1)+": "+str(SSE(clusterCentroids[i][0], clusterCentroids[i][1])))


    loop = 0
    while True:
        tempClusters = str(clusterCentroids.copy())
        recalibratedCentroids = recalibrateCentroids(clusterCentroids)
        clusterCentroids = clusterizeData(recalibratedCentroids, dataPoints)
        loop += 1
        if tempClusters == str(clusterCentroids):
            break
    print("Completed with " + str(loop) + " loop(s)!")
    for i in range(0, len(clusterCentroids)):
        print("SSE for cluster "+str(i+1)+": "+str(SSE(clusterCentroids[i][0], clusterCentroids[i][1])))
    visiualize_clusters(clusterCentroids)