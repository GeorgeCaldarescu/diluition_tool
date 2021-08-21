def agroCalc():
    conc = float(input("Please choose between 0.03 and 0.05 (for P19): " ))
    print("\n") 
    od = float(input("Please write the OD600 you obtained: "))
    print("\n")
    if conc == 0.03:
        a = ((od * 50)/conc)
        b = (500/a)*4
        print("Your volume to add to 2ml is :" , b)
        print("\n")
    elif conc == 0.05:
        a = ((od * 50)/conc)
        b = (500/a)*4
        print("Your volume to add to 2ml is :" , b)
        print("\n")
    else:
        print("The concentration you chooce is not available.")

    
# define the function that repeat the agroCalc function
def repeat(times, f):
    for i in range(times):
        agroCalc()



repeat(200, agroCalc())


