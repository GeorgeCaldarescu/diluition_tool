# call more function

class the_process():
    def repeatAgro(times):
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
            

    def repeateBrad(times):
        def brad():
            od = float(input("write OD: ")) *10
            conc = float(input("What concentration in ng you want: "))
            a = ((od * 0.8847+0.128)*1000)
        
            # is the protein amount
            b = (conc/a) * 1000
            print("Take ", b, "of your proteins")
            # SDS amount
            print("Add", b/5, "of SDS")
        
        for i in range(times):
            brad()
    the_route = int(input("For Agro quantification please type 1 \nFor Bradford quantification type 2  \n"))

    if the_route == 1:
        repeatAgro(10)
    else:
        repeateBrad(10)



# now is working, when I will finish with all of them I can delete the upper part of the code (the commented one)

