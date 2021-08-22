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
            od = float(input("Insert OD: \n")) *10
        
            # for 150ng of proteins
            a = ((od * 0.8847+0.128)*1000)
            b = (150/a) * 1000
            print("Take ",b,"ul of your proteins to obtain 150ng of proteins \n")
        
            # this is for SDS
            print("Add", b/5, "ul of SDS to the proteins \n")

            # for 100ng of proteins
            c = (100/a) * 1000
            print("Take ",c,"ul of your proteins to obtain 100ng of proteins \n")
        
            # this is for SDS
            print("Add", c/5, "ul of SDS to the proteins \n")

            # for 50ng of proteins
            d = (50/a) * 1000
            print("Take ",d,"ul of your proteins to obtain 50ng of proteins \n")
        
            # this is for SDS
            print("Add", d/5, "ul of SDS to the proteins \n")
        
        for i in range(times):
            brad()
    the_route = int(input("For Agro quantification please type 1 \nFor Bradford quantification type 2  \n"))

    if the_route == 1:
        repeatAgro(10)
    else:
        repeateBrad(10)



# now is working, when I will finish with all of them I can delete the upper part of the code (the commented one)

