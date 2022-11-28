from math import sqrt


def findMax(distance: int, bolts: list):
    length: float = 0
    if len(bolts) <= 50:
        isElementsInLimits: bool = True
        for bolt in bolts:
            if bolt < 1 or bolt > 100:
                isElementsInLimits = False
                break
        if isElementsInLimits:
            isLastWasChangedToOne: bool = False
            index: int = 0
            for bolt in bolts:
                index += 1
                if index != len(bolts):
                    if isLastWasChangedToOne:
                        if bolts[index] > 1:
                            length += sqrt((bolts[index] - 1)**2 + distance**2)
                        else:
                            length += distance
                        isLastWasChangedToOne = False
                    else:
                        withNoChanges = sqrt((bolts[index] - bolt)**2 + distance**2)
                        withChanges = sqrt((1 - bolt)**2 + distance**2)
                        if withChanges > withNoChanges:
                            isLastWasChangedToOne = True
                            length += withChanges
                        else:
                            length += withNoChanges
        else:
            print("Elements must be in limit between 1 to 100")
    else:
        print("List is longer than 50 elements")

    print(f'You need {round(length, 2)} m of cable')