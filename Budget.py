def calcBills():
    myBills = {'Electric': 1200.00, 'Rent': 1200.00, 'Water_Sewer': 60.00, 'Car Insurance': 75.00, 'Phone': 65.00}

    total = 0
    for i in myBills:
        total += myBills[i]
    owed = 'The total owed for bills this month is: ${}'.format(total)
    return owed

def print_app():
    name = (__name__)
    return name

