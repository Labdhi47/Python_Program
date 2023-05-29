for row in range(7):
    for col in range(7):
        if (col==0 and (row==1 or row==2)) or (col==1 and (row==0 or row==3)) or (col==2 and (row==0 or row==4)) or (col==3 and (row==1 or row==5)) or (col==4 and (row==0 or row==4)) or (col==5 and (row==0 or row==3)) or (col==6 and (row==1 or row==2)):
            print("*",end="")
        else:
            print(end=" ")
    print() 
    
