from Controller import Controller
from Description import FuzzyDescriptions
from Ruler import FuzzyRule


def trapRegion(a, b, c, d):
    return lambda x: max(0, min((x - a) / (b - a), 1, (d - x) / (d - c)))


def triRegion(a, b, c):
    return trapRegion(a, b, b, c)


def inverseLine(a, b):
    return lambda val: val * (b - a) + a


def inverseTri(a, b, c):
    return lambda val: (inverseLine(a, b)(val) + inverseLine(c, b)(val)) / 2


if __name__ == '__main__':
    temperature = FuzzyDescriptions()
    humidity = FuzzyDescriptions()
    time = FuzzyDescriptions()
    rules = []

    #hummmidity 0/100
    #temperature -30/35

    temperature.addRegion('very cold', trapRegion(-1000, -30, -20, 5))
    temperature.addRegion('cold', triRegion(-5, 0, 10))
    temperature.addRegion('normal', trapRegion(5, 10, 15, 20))
    temperature.addRegion('warm', triRegion(15, 20, 25))
    temperature.addRegion('hot', trapRegion(25, 30, 35, 1000))

    humidity.addRegion('dry', triRegion(-1000, 0, 50))
    humidity.addRegion('normal', triRegion(0, 50, 100))
    humidity.addRegion('wet', triRegion(50, 100, 1000))

    time.addRegion('short', triRegion(-1000, 0, 50), inverseLine(50, 0))
    time.addRegion('medium', triRegion(0, 50, 100), inverseTri(0, 50, 100))
    time.addRegion('long', triRegion(50, 100, 1000), inverseLine(50, 100))

    rules.append(FuzzyRule({'temperature': 'very cold', 'humidity': 'wet'},
                           {'time': 'short'}))
    rules.append(FuzzyRule({'temperature': 'cold', 'humidity': 'wet'},
                           {'time': 'short'}))
    rules.append(FuzzyRule({'temperature': 'normal', 'humidity': 'wet'},
                           {'time': 'short'}))
    rules.append(FuzzyRule({'temperature': 'warm', 'humidity': 'wet'},
                           {'time': 'short'}))
    rules.append(FuzzyRule({'temperature': 'hot', 'humidity': 'wet'},
                           {'time': 'medium'}))

    rules.append(FuzzyRule({'temperature': 'very cold', 'humidity': 'normal'},
                           {'time': 'short'}))
    rules.append(FuzzyRule({'temperature': 'cold', 'humidity': 'normal'},
                           {'time': 'medium'}))
    rules.append(FuzzyRule({'temperature': 'normal', 'humidity': 'normal'},
                           {'time': 'medium'}))
    rules.append(FuzzyRule({'temperature': 'warm', 'humidity': 'normal'},
                           {'time': 'medium'}))
    rules.append(FuzzyRule({'temperature': 'hot', 'humidity': 'normal'},
                           {'time': 'long'}))

    rules.append(FuzzyRule({'temperature': 'very cold', 'humidity': 'dry'},
                           {'time': 'medium'}))
    rules.append(FuzzyRule({'temperature': 'cold', 'humidity': 'dry'},
                           {'time': 'long'}))
    rules.append(FuzzyRule({'temperature': 'normal', 'humidity': 'dry'},
                           {'time': 'long'}))
    rules.append(FuzzyRule({'temperature': 'warm', 'humidity': 'dry'},
                           {'time': 'long'}))
    rules.append(FuzzyRule({'temperature': 'hot', 'humidity': 'dry'},
                           {'time': 'long'}))

    ctrl = Controller(temperature, humidity, time, rules)

    '''
    hummmidity 0/100
    temperature -30/35
    '''

    print(ctrl.compute({'humidity': 12, 'temperature': 40}))
    print(ctrl.compute({'humidity': 30, 'temperature': -10}))
    print(ctrl.compute({'humidity': 60, 'temperature': -20}))
    print(ctrl.compute({'humidity': 75, 'temperature': 20}))
