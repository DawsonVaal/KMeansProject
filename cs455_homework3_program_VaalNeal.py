import csv
import math

myDict = {}

with open('auto-mpg.csv', mode='r') as read_obj:
    reader = csv.reader(read_obj)
    dataAsRows = list(reader)

def makeInitialCentroid(n, data):
    r = []
    for x in n:
        r.append(x[0])
    return r

def askUserInput():
    print("Please enter the number of clusters you want to form, 2 or 3. ")
    Index = int(input("Enter number : "))
    while True:
        if Index == 2 or Index == 3:
            return Index
        else:
            Index = int(input("That was an invalid number, please re-enter either 2 or 3: "))


def normalize_data(data, min, max):
    normal_column = []
    for i in range(len(data)):
        new_value = round((data[i] - min) / (max - min), 2) * 100
        normal_column.append(new_value)
    return normal_column

def compute_distance_numerical(new_data):
    distance_matrix = []
    for i in range(len(new_data)):
        temp = []
        for j in range(len(new_data)):
            distance = round(math.fabs(new_data[i] - new_data[j]),2)
            temp.append(distance)
        distance_matrix.append(temp)
    return distance_matrix

if __name__ == '__main__':
    open('auto-mpg.csv')

    normalized_data = []
    for j in range(0,1):
        columnList = []
        for i in range(1, len(dataAsRows)):
                columnList.append(int(dataAsRows[i][j]))
        normalized_data.append(normalize_data(columnList, min(columnList), max(columnList)))

    first_numerical_distance = compute_distance_numerical(normalized_data[0])
    second_numerical_distance = compute_distance_numerical(normalized_data[1])
    

