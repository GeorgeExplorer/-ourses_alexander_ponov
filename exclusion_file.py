def devision_exlusion():

    devidend = int(input("Enter the first number: "))
    devisor = int(input("EntEnter the second number: "))

    try:
        qutient = devidend / devisor
    except ZeroDivisionError:
        result = int(qutient)
        result = "Calculating is not available"
        print("You can not divide by 0")


        print("Result is: " + str(result))

devision_exlusion()
