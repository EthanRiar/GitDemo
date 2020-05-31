import csv as c
import math as m

inDataFile = '2019_09_calgary_hourly.csv'
outFileName = 'results.txt'

FIELD_YEAR = 5
FIELD_MONTH = 6
FIELD_DAY = 7
FIELD_HOUR = 8
FIELD_TEMP = 9

userData = input('Enter a YEAR, Month and day e.g. 2019-09-01: ').split('-')

userYear = int(userData[0])
userMonth = int(userData[1])
userDay = int(userData[2])

currentColdestTemp = 9999999999.99
currentColdestHour = ['Not set yet!']
fileTempList = []
fileHourStr = []

with open(inDataFile, 'r') as datafile:
    csvFile = c.reader(datafile, dialect='excel')
    next(csvFile)  # skip the header
    for record in csvFile:
        fileYear = int(record[FIELD_YEAR])
        fileMonth = int(record[FIELD_MONTH])
        fileDay = int(record[FIELD_DAY])
        fileHour = str(record[FIELD_HOUR])
        fileTemp = float(record[FIELD_TEMP])

        if (userYear == fileYear) & (userMonth == fileMonth) & (userDay == fileDay):
            fileTempList.append(fileTemp)
            fileTempMin = min(fileTempList)

            if fileTempMin < currentColdestTemp:
                currentColdestHour.pop()
                currentColdestHour.append(fileHour)
                currentColdestHour.append(fileTempMin)
                fileTemp = currentColdestTemp
                currentColdestHour1 = str(currentColdestHour)
with open(outFileName,'w') as resultsFile:
    resultsFile.write(currentColdestHour1)






