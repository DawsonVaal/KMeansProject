import csv
import math

with open('auto-mpg.csv', mode='r') as read_obj:
    reader = csv.reader(read_obj)
    dataAsRows = list(reader)

def askUserInput():
    print("Please enter an ODD number of neighbors you want to form from 1-11. ")
    Index = int(input("Enter number : "))
    while True:
        if Index >= 1 and Index <= 11 and Index % 2 == 1:
            break
        else:
            Index = int(input("That was an invalid number, please re-enter an ODD number from 1-11: "))
    return Index

def normalize_data(data, min, max):
    normal_column = []
    for i in range(len(data)):
        new_value = round((data[i] - min) / (max - min) * 100)
        normal_column.append(new_value)
    return normal_column

def makePoints(data):
    pointList = []
    for x in range(len(data[0])):
        pointList.append([data[0][x], data[1][x]])
    return pointList

def computeDistance(point1, point2):
    return int(math.fabs(point1[0] - point2[0]) + math.fabs(point1[1] - point2[1]))

def computeAllDistances(newPoint, trainingData):
    distances = []
    shortest = []
    shortestPoints = []
    for point in trainingData:
        distances.append(computeDistance(newPoint, point))

    for i in range(0, k):
        shortest.append(sorted(distances)[i])

    for i in range(0, len(distances)):
        for distance in shortest:
            if distances[i] == distance:
                shortestPoints.append(trainingData[i])
                shortest.remove(distance.__index__())
    return shortestPoints

def predictLabel(shortestPoints):
    truckVote = 0
    sedanVote = 0

    for point in shortestPoints:
        if point[2] == 'truck':
            truckVote += 1
        else:
            sedanVote += 1
    if truckVote > sedanVote:
        return 'truck'
    else:
        return 'sedan'

def calculateAccuracy(testing_data, training_data):
    total = 0
    sedanCorrect = 0
    truckCorrect = 0

    for testPoint in testing_data:
        total += 1
        if testPoint[2] == predictLabel(computeAllDistances(testPoint, training_data)):
            if testPoint[2] == 'truck':
                truckCorrect += 1
            else:
                sedanCorrect += 1

    truckAccuracy = round(((truckCorrect/total)*100), 2)
    sedanAccuracy = round(((sedanCorrect/total)*100), 2)

    print("Truck Correct: " + str(truckAccuracy) + "%")
    print("Sedan Correct: " + str(sedanAccuracy) + "%")
    print("Overall Accuracy: " + str(round((truckAccuracy+sedanAccuracy)/2, 2)) + "%")
    return round((truckAccuracy+sedanAccuracy)/2, 2)

if __name__ == '__main__':
    open('auto-mpg.csv')

    k = askUserInput()

    normalized_data = []
    for j in range(0,2):
        columnList = []
        for i in range(1, len(dataAsRows)):
                columnList.append(int(round(float(dataAsRows[i][j]))))
        normalized_data.append(normalize_data(columnList, min(columnList), max(columnList)))

    dataPoints = makePoints(normalized_data)
    for i in range(1, len(dataAsRows)):
        dataPoints[i-1].append(dataAsRows[i][2])

    training_data = dataPoints[:49]
    testing_data = dataPoints[50:]

    print("Round 1 Results\n"
          "--------------")
    round1_accuracy = calculateAccuracy(testing_data, training_data)

    print("\nRound 2 Results\n"
          "--------------")
    round2_accuracy = calculateAccuracy(training_data, testing_data)

    print("\nTotal Accuracy Overall\n"
          "----------------------\n"
          "Overall Accuracy: " + str(round((round1_accuracy + round2_accuracy)/2, 2)) + "%")