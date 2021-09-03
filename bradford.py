# def brad():
#         od = float(input("Insert OD: \n")) *10
        
#         # for 150ng of proteins
#         a = ((od * 0.8847+0.128)*1000)
#         b = (150/a) * 1000
#         print("Take ",b,"ul of your proteins to obtain 150ng of proteins \n")
        
#         # this is for SDS
#         print("Add", b/5, "ul of SDS to the proteins \n")

#         # for 100ng of proteins
#         c = (100/a) * 1000
#         print("Take ",c,"ul of your proteins to obtain 100ng of proteins \n")
        
#         # this is for SDS
#         print("Add", c/5, "ul of SDS to the proteins \n")

#         # for 50ng of proteins
#         d = (50/a) * 1000
#         print("Take ",d,"ul of your proteins to obtain 50ng of proteins \n")
        
#         # this is for SDS
#         print("Add", d/5, "ul of SDS to the proteins \n")

# brad()

# try to make it without preset mass

def newBrad():
        od = float(input("write OD: ")) *10
        conc = float(input("What concentration in ng you want: "))
        a = a = ((od * 0.8847+0.128)*1000)
        
        # is the protein amount
        b = (conc/a) * 1000
        print("Take ", b, "of your proteins")
        # SDS amount
        print("Add", b/5, "of SDS")

newBrad()
