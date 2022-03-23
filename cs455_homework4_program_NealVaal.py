import csv

with open('auto-mpg.csv', mode='r') as read_obj:
    reader = csv.reader(read_obj)
    dataAsRows = list(reader)

if __name__ == '__main__':
    open('auto-mpg.csv')