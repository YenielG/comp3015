
def age():
    global currentYear
    global birthYear
    birthYear=2020
    currentAge = currentYear - birthYear       
    print(f'Your age is {currentAge}')

    currentYear = int(input('current year:'))
    birthYear= int(input("birth year:")) 

    age()
    print(birthYear)