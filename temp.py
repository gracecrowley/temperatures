# Exercise -Temperature Database
def displayMenu():
    choice = input('''Please choose from the following menu or press enter to end \n 
  Choose 1 to enter a new temperature measurement\n
  Choose 2 to retrieve a temperature for a given date \n
  Choose 3 to print all the temperature measurements \n
  Choose 4 to print the average temperature\n ''')
    return choice


def enterNewMeasurement(measDict):
    date = input('Please enter todays date: ')
    temp = float(input('Please enter the temperature for today: '))

    measDict[date] = temp
    return measDict


def retrieveMeasurement(measDict):
    date = input('Please enter a date: ')
    if date in measDict:
        temp = measDict[date]
        return (f'The temperature on {date} was {temp}')
    else:
        return 'This date is not in the database'


def printAllMeasurements(measDict):
    print('The temperatures to date are:')
    for value in measDict.values():
        print(value)


def getAverage(measDict):
    sum = 0
    for temp in measDict.values():
        sum += temp
    length = len(measDict)
    average = sum / length
    return (f'The average temperature is {average}')


measDict = {}

loop = True
while loop == True:
    choice = displayMenu()
    if choice == '1':
        measDict = enterNewMeasurement(measDict)
    if choice == '2':
        print(retrieveMeasurement(measDict))
    if choice == '3':
        print(printAllMeasurements(measDict))
    if choice == '4':
        print(getAverage(measDict))
    if choice == '*':
        loop = False
print('Bye')