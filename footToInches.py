inches = 12

def feetToInc(feet):
    inc = feet * inches
    display(inc,feet)

def display(inc,feet):
    print(feet," Feet = ",inc," inches")

def enter():
    feet = int(input("Enter input in feets : "))
    feetToInc(feet)


enter()




