"""
Assessment for BHC Software Developer Position
"""

"""
Class representing the Bale object as per appendix
"""
class Bale:
    def __init__(self, barcode, mass, price, grade, growerNumber):
        self.growerNumber = growerNumber
        self.mass = mass
        self.price = price
        self.grade = grade
        self.barcode = barcode


"""
Class representing the Debt object as per appendix
"""
class Debt:
    def __init__(self, amount, priority, interestRate):
        self.amount = amount
        self.priority = priority
        self.interestRate = interestRate


"""
Input lists for testing the functions
"""
Bales = [Bale('110000011', 70, 2.50, 'TMOS', '123456'), Bale('110000012', 20, 4.50, 'TLOS', '123456'),
         Bale('110000013', 10, 5.50, 'TLOS', '123456'), Bale('110000015', 80, 3.50, 'TMOS', '123456'),
         Bale('110000014', 20, 2.00, 'TMOS', '123456'), Bale('110000016', 100, 4.50, 'TLOS', '123456')]

Debts = [Debt(120, 1, 0.01), Debt(100, 2, 0.02), Debt(150, 3, 0.03)]

Rebates = ['REBATE_1', 'REBATE_2']

OldStock = [
    Bale('123456789', 120, 2.50, 'TMOS', '123456'),
    Bale('132456987', 107, 1.50, 'TMOS', '123456'),
    Bale('143256789', 100, 3.50, 'TMOS', '123456'),
    Bale('100256789', 101, 6.50, 'TMOS', '123456'),
    Bale('100256739', 129, 2.50, 'TMOS', '123456'),
    Bale('100256732', 1, 4.50, 'TLOS', '123456'),
    Bale('100456739', 121, 4.00, 'TLOS', '123456'),
    Bale('102256739', 125, 5.00, 'TLOS', '123456'),
    Bale('102456239', 129.5, 4.50, 'TLOS', '123456'),

]
NewStock = [
    Bale('123456789', 117, 2.50, 'TMOS', '123456'),
    Bale('132456987', 120, 1.50, 'TMOS', '123456'),
    Bale('143256789', 101, 3.50, 'TMOS', '123456'),
    Bale('100256789', 101, 6.50, 'TMOS', '123456'),
    Bale('100256739', 129, 2.50, 'TMOS', '123456'),
    Bale('100256732', 1, 4.50, 'TLOS', '123456'),
    Bale('100456739', 121, 4.00, 'TLOS', '123456'),
    Bale('102256739', 125, 5.00, 'TLOS', '123456'),
    Bale('102456239', 129.5, 4.50, 'TLOS', '123456'),

]
"""
 Part A :Question 1
"""

"""Item 1"""


def CalculateGross(Bales):
    grossIncome = 0
    #iterate through the list and sum up all the products of mass and price for each bale
    for bale in Bales:
        grossIncome += bale.price * bale.mass
    return grossIncome


"""Item 2"""


def CalculateTaxes(gross):
    #formulae for all the 3 taxes
    tax1 = 0.003 * gross
    tax2 = 0.015 * gross + 0.02 * sum(bale.mass for bale in Bales)
    tax3 = 5 * len(Bales)
    #subtract all taxes from the gross
    return gross - (tax1 + tax2 + tax3)


"""Item 3"""

"""Assuming the gross to be passed through params and since the debt object includes the interestRate, I did not pass the interestRate as a parameter"""


def DebtHandler(gross, debt):
    #calculate the interest and the commision
    interest = debt.amount * debt.interestRate
    commission = 0.005 * (debt.amount + interest)
    #subtract the debt, interest and commission from the gross
    netValue = gross - (debt.amount + interest + commission)
    return netValue, commission


"""Item 4"""


def ProcessDebts(gross, debts):
    commission = 0
    remainingGross = 0
    #sort the debts in order of priority
    for debt in sorted(debts, key=lambda x: x.priority):
        #call the DebtHandler method to deduct the debt, interest, and commission from the gross and return
        #the remaining gross and commission for each debt
        debtRemainingGross, debtCommission = DebtHandler(gross, debt)
        #sum for all the debts
        commission += debtCommission
        remainingGross += debtRemainingGross
    return commission, remainingGross


"""
Item 5 
Assuming rebate is passed as a string
"""


def Rebate(gross, rebate):
    if rebate == 'REBATE_1':
        rebateValue = 0.0005 * sum(bale.mass for bale in Bales)
    elif rebate == 'REBATE_2':
        rebateValue = 10 + 0.0002 * gross
    else:
        rebateValue = 0
    return gross + rebateValue


"""Item 6"""


def CalculateRebates(rebates, gross):
    totalGross = 0
    for rebate in rebates:
        netAfterRebate = Rebate(gross, rebate)
    totalGross += netAfterRebate
    return totalGross



def ProcessSale(bales, debts, rebates):
    gross = CalculateGross(bales)
    print('Gross value :', gross)
    grossAfterTaxes = CalculateTaxes(gross)
    print('Gross value after taxes :', grossAfterTaxes)
    commission, net = ProcessDebts(grossAfterTaxes, debts)
    print(f"After debts the net is {net:.2f} and the total commission is {commission:.2f}")
    netAfterRebate = CalculateRebates(rebates,net)
    print(f"After adding rebates, the net is {netAfterRebate:.2f}")
    return netAfterRebate, commission


"""
Part A : Question 2
"""


def Reworks(bales):
    # Find possible combinations of two bales with the same grade
    selectedCombinations = []
    #Assuming a bale can only be in one combination, the usedBales set will keep track of the bales already paired
    usedBales = set()
    for bale in bales:
        #if bale is paired skip
        if bale in usedBales:
            continue
        else:
            #include the bale so that it can be considered on the nexxt step
            usedBales.add(bale)
            for i in range(bales.index(bale), len(bales)):
                if bales[i] in usedBales:
                    continue
                else:
                    #check if the pairs meet the criteria for total mass <= 120
                    if bale.mass + bales[i].mass > 120:
                        continue
                    else:
                        selectedCombinations.append((bale, bales[i]))
                        usedBales.update([bales[i]])
                        break

    # Calculate the new barcode, mass, grade, and price for each selected combination
    newBales = []
    for bale1, bale2 in selectedCombinations:
        newBarcode = f"{bale1.barcode}_{bale2.barcode}"
        newMass = bale1.mass + bale2.mass
        newGrade = bale1.grade
        newGross = bale1.mass * bale1.price + bale2.mass * bale2.price
        newPrice = newGross / newMass
        newBale = Bale(newBarcode, newMass, newPrice, newGrade, bale.growerNumber)
        newBales.append(newBale)

    # Calculate new price for the merged bales
    mergedGross = sum(bale.mass * bale.price for bale in newBales)
    mergedMass = sum(bale.mass for bale in newBales)
    newPrice = mergedGross / mergedMass

    # Print rejected bales and the new average price

    for bale in bales:
        if bale not in usedBales:
            print(f"{bale.barcode} is rejected")
    if selectedCombinations:
        print("Selected combinations:")
        for bale1, bale2 in selectedCombinations:
            print(f"- {bale1.barcode} + {bale2.barcode} => {newBale.barcode}")
        print(f"New Price: {newPrice:.2f}")
    else:
        print("No valid combinations found.")

    # Return the selected combinations
    return selectedCombinations

"""
Part B: Question 3
"""

def WeighBale(Bales):
    for bale in Bales:
        #variable accepted to track whether a bale meets all the weighing conditions
        accepted = True
        #check for each criteria
        if bale.mass < 5:
            accepted = False
        elif bale.mass > 130:
            accepted = False
        else:
            if bale.mass >= 121 and bale.mass <= 125:
                bale.mass = 120
            else:
                bale.mass =abs(125-bale.mass) + 120
        print(f'Bale {bale.barcode} is accepted. Bale Mass is {bale.mass}' if accepted else f'Bale {bale.barcode} is rejected. Bale Mass is {bale.mass}' )

def ReWeigh(OldStock, NewStock):
    #dictionary to keep the old stock for easy access using key instead of looping
    hash = {}
    for item in OldStock:
        hash[item.barcode] = item.mass
    for bale in NewStock:
        #check the difference between the massess
        variance = bale.mass - hash[bale.barcode]
        if variance > 0 and variance > 2:
            print(f'Bale {bale.barcode} is overweight')
        elif variance < 0 and abs(variance) > 2:
            print(f'Bale {bale.barcode} is underweight')
        else:
            print(f'Accepted {bale.barcode}')





#run the script.
if __name__ == '__main__':
    #print(ProcessDebts(CalculateGross(Bales), Debts))
    #Reworks(Bales)
    #ReWeigh(OldStock, NewStock)
    ProcessSale(Bales, Debts, Rebates)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
