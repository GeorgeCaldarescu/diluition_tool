# call more function

class the_process():
    def Agro():
        while True:
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
            l = input("You wanto to continue y/n: ")
            if l.strip() == "n":
                print("Good luck with your experiment :)")
                break
            
    def Brad():
        while True:
                od = float(input("write OD: ")) *10
                conc = float(input("What concentration in ng you want: "))
                a = a = ((od * 0.8847+0.128)*1000)
        
                # is the protein amount
                b = (conc/a) * 1000
                print("Take ", b, "of your proteins")
                # SDS amount
                print("Add", b/5, "of SDS")

                # loop
                l = input("You want to continue y/n: ")
                if l.strip() == "n":
                        print("Good luck with the Western :)")
                        break
    
    the_route = int(input("For Agro quantification please type 1 \nFor Bradford quantification type 2  \n"))

    if the_route == 1:
        Agro()
    else:
        Brad()



