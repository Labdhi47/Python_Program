for row in range(7):
    for col in range(6):
        if (row==0 and (col>=0 and col<5)) or (col==0 and (row>0 and row<7)) or (row==6 and (col>0 and col<5)) or (row==3 and (col>2 and col<6)) or (col==4 and (row==4 or row==5)):
            print("*",end="")
        else:
            print(end=" ")
    print() 
