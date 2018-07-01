import csv

dates = []
scores = []

with open('FIS_Data.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        dates.append(row[2])
        scores.append(row[3])

print(dates)
print(scores)
