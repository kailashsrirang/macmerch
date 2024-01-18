import sys


def parseArguments():
    arguments = {
        "price": sys.argv[1],
        "quantity": 1,
        "province": "ON"
    }
    return arguments


def taxRate(province):
    tax = {
        "ON": 1.13
    }
    return tax[province]


def mcmerchCalculator():
    arguments = parseArguments()
    taxrate = taxRate(arguments["province"])
    print(float(arguments['price']) *
          float(arguments['quantity']) * (1+taxrate))


mcmerchCalculator()
