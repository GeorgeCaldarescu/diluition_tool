def agroCalc():
    conc = float(input("Please choose between 0.03 and 0.05 (for P19): " ))
    od = float(input("Please write the OD600 you obtained: "))

    if conc == 0.03:
        a = ((od * 50)/conc)
        b = (500/a)*4
        print("Your volume to add to 2ml is : ", b)
    elif conc == 0.05:
        a = ((od * 50)/conc)
        b = (500/a)*4
        print("Your volume to add to 2ml is : ", b)
    else:
        print("The concentration you chooce is not available.")

    return

agroCalc()
