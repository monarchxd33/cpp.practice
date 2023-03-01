li=[["maggie",12,40],
     ["pasta",20,40],
     ["vinegar",35,40],
     ["wiper" ,150,40], 
     ["broom",120,40], 
     ["pen",10,40], 
    ["sooji",40,40], 
    ["juice",40,40], 
    ["can",20,40],
    ["namkeen",60,40], 
    ["soap",80,40], 
    ["brush",20,40], 
    ["shampoo",60,40], 
    ["conditionar",50,40], 
    ["facewash",60,40], 
    ["perfume",140,40], 
    ["cream",50,40],
    ["honey",70,40],
    ["oil",100,40],
    ["fevistick",5,40],
    ["eno",8,40],
    ["tape",25,40],
    ["biscuit",40,40]
 ]

print("HELLO WELCOME TO E-MANGAER")
m="y"
count=100000
while m=="y":
    bill=""
    b=0
    print("PRESS 1 FOR Billing System")
    print("PRESS 2 FOR Stock Management, Updation and Availability")
    s=input()
    if s=="1":
        count=count+1
        print("Dear Customer Your Coupon Number is : ",count)
        c=int(input("PLEASE ENTER TOTAL NUMBER OF UNIQUE COMMODITIES: "))
        for i in range (c):
            flag=False
            while flag==False:
                print("➽ NAME OF ITEM NO.",i+1," :")
                item=input()
                x=item.lower()
                for j in range (len(li)):
                    if li[j][0]==x:
                        flag=True
                        print("QUANTITY OF ",x, " :")
                        quantity=int(input())
                        if quantity>li[j][2]:
                            print("Stock not available")
                            break
                        else:
                            c1=li[j][1]                        
                            t1=c1*quantity                        
                            li[j][2]=(int(li[j][2])-quantity)                                        
                            print("COST OF ONE ",x, " : Rs",c1)
                            print("TOTAL COST OF",x, " : Rs",t1)
                            # print("stock of",item,"left =",li[j][2])
                        print()
                        b=b+t1
                        if bill=="":
                            bill=bill + str(t1)
                        else:
                            bill=bill + "+" + str(t1)
                if flag ==False:
                    print("Sorry,Item not found,Please retry") 

        if c==1:
            print("TOTAL AMOUNT TO BE PAID BY Coupon Number ",count ," = Rs",b)
        else:
            print("TOTAL AMOUNT TO BE PAID BY Coupon Number ",count ,"=", bill," = Rs",b)
    if s=="2":
        print("ONLY FOR STAFF USE")
        y=input("Enter Password : ")
        #password="manager"
        if y=="manager":
            print("For Knowing Stock Left Press 'A'")
            print("For Stock Management And Updation Press 'B' ")
            p=input()
            if p=="A":
                print("STOCK LEFT:")
                for i in range(len(li)):
                    print(li[i][0],"=",li[i][2])
                print()
                print()
                for k in range(len(li)):
                    e=li[k][2]
                    if e<6:
                        print("WARNING: Item ",li[k][0],"left with only",e ,"quantity")  
            if p=="B":
                print("Stock Updation") 
                x=int(input("Total Number of Unique Commodities Whose Stock Is To Updated : "))
                for l in range(x):
                    fla=False
                    while fla==False:
                        print("input ",l+1,") ITEM NAME whose stock is to be updated")
                        f=input()
                        o=f.lower()
                        for k in range(len(li)):
                            if li[k][0]==o:
                                fla=True
                                print("previous stock available =",li[k][2])
                                print("amount of",f,"to be added in the stock")
                                g=int(input())
                                li[k][2]=li[k][2]+g
                                print("after updation - stock available of ",f,"=",li[k][2])
                        if fla==False:
                            print("Sorry,Item not found,Please retry") 
        else:
            print("Sorry,Wrong password")
          
  
  
    m=input("type 'y' to continue, any other key to exit :  ")
else:
    print("Thanks For Using E-Manager")
    a=input()

    
