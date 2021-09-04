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

                
Brad()
