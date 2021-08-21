# def agroCalc():
#     conc = float(input("Please choose between 0.03 and 0.05 (for P19): " ))
#     print("\n") 
#     od = float(input("Please write the OD600 you obtained: "))
#     print("\n")
#     if conc == 0.03:
#         a = ((od * 50)/conc)
#         b = (500/a)*4
#         print("Your volume to add to 2ml is :" , b)
#         print("\n")
#     elif conc == 0.05:
#         a = ((od * 50)/conc)
#         b = (500/a)*4
#         print("Your volume to add to 2ml is :" , b)
#         print("\n")
#     else:
#         print("The concentration you chooce is not available.")

    
# # define the function that repeat the agroCalc function
# def repeat(times, f):
#     for i in range(times):
#         agroCalc()



# repeat(200, agroCalc())


# call many function

class the_process():
    # def agroCalc():
    #     conc = float(input("Please choose between 0.03 and 0.05 (for P19): " ))
    #     print("\n") 
    #     od = float(input("Please write the OD600 you obtained: "))
    #     print("\n")
    #     if conc == 0.03:
    #         a = ((od * 50)/conc)
    #         b = (500/a)*4
    #         print("Your volume to add to 2ml is :" , b)
    #         print("\n")
    #     elif conc == 0.05:
    #         a = ((od * 50)/conc)
    #         b = (500/a)*4
    #         print("Your volume to add to 2ml is :" , b)
    #         print("\n")
    #     else:
    #         print("The concentration you chooce is not available.")

    def repeat(times):
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
        for i in range(times):
            agroCalc()
            

    def ciao():
        print("ciao")
    
    the_route = int(input("type 1 or 2: "))

    if the_route == 1:
        repeat(3)
    else:
        ciao()



# now is working, when I will finish with all of them I can delete the upper part of the code (the commented one)

