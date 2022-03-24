import csv
import math

with open('auto-mpg.csv', mode='r') as read_obj:
    reader = csv.reader(read_obj)
    dataAsRows = list(reader)


def ask_user_input():
    print("Please enter an ODD number of clusters you want to form from 1-11. ")
    index = int(input("Enter number : "))
    while True:
        if 11 > index > 1 == index % 2:
            break
        else:
            index = int(input("That was an invalid number, please re-enter an ODD number from 1-11: "))
    return index


def normalize_data(data, min, max):
    normal_column = []
    for i in range(len(data)):
        new_value = round((data[i] - min) / (max - min) * 100)
        normal_column.append(new_value)
    return normal_column


def make_points(data):
    point_list = []
    for x in range(len(data[0])):
        point_list.append([data[0][x], data[1][x]])
    return point_list


def compute_distance(point1, point2):
    return int(math.fabs(point1[0] - point2[0]) + math.fabs(point1[1] - point2[1]))


def compute_all_distances(new_point, data):
    distances = []
    shortest = []
    shortest_points = []
    for point in data:
        distances.append(compute_distance(new_point, point))

    for i in range(0, k):
        shortest.append(sorted(distances)[i])

    for i in range(0, len(distances)):
        for distance in shortest:
            if distances[i] == distance:
                shortest_points.append(data[i])
                shortest.remove(distance.__index__())
    return shortest_points


def predict_label(shortest_points):
    truck_vote = 0
    sedan_vote = 0

    for point in shortest_points:
        if point[2] == 'truck':
            truck_vote += 1
        else:
            sedan_vote += 1
    if truck_vote > sedan_vote:
        return 'truck'
    else:
        return 'sedan'


def calculate_accuracy(test_data, train_data):
    sedan_total = 0
    truck_total = 0
    sedan_correct = 0
    truck_correct = 0

    for testPoint in test_data:
        if testPoint[2] == 'truck':
            truck_total += 1
            if testPoint[2] == predict_label(compute_all_distances(testPoint, train_data)):
                truck_correct += 1
        else:
            sedan_total += 1
            if testPoint[2] == predict_label(compute_all_distances(testPoint, train_data)):
                sedan_correct += 1

    truck_accuracy = round(((truck_correct / truck_total) * 100), 2)
    sedan_accuracy = round(((sedan_correct / sedan_total) * 100), 2)

    print("Truck Correct: " + str(truck_accuracy) + "%")
    print("Sedan Correct: " + str(sedan_accuracy) + "%")
    print("Overall Accuracy: " + str(round((truck_accuracy + sedan_accuracy) / 2, 2)) + "%")


if __name__ == '__main__':
    open('auto-mpg.csv')

    k = ask_user_input()

    normalized_data = []
    for j in range(0, 2):
        columnList = []
        for i in range(1, len(dataAsRows)):
            columnList.append(int(round(float(dataAsRows[i][j]))))
        normalized_data.append(normalize_data(columnList, min(columnList), max(columnList)))

    dataPoints = make_points(normalized_data)
    for i in range(1, len(dataAsRows)):
        dataPoints[i - 1].append(dataAsRows[i][2])

    training_data = dataPoints[:49]
    testing_data = dataPoints[50:]

    calculate_accuracy(testing_data, training_data)
