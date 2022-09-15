




def inputs():
    
    area = width * length  
    

def calculate():
    width = 1073741824
    length = 1073741824
    name = input("enter time: ")
    print(name)
    x1 = 0
    y1 = 0
    seconds = 1968526677
    sec = 0

    while( int(name) >= int(sec)):
        sec+=1
        x1+=0.2
        y1+=0.4
        x = (width - x1)
        print(x1)
        y = (length - y1)
        print(y1)      
        z1= (width - x1) + (length - y1)
        a= (x1) * (y1)

        print("X = ")
        print(x)
        print("Y = ")
        print(y)
        print("AREA OF LOCATION FROM STARTING POINT")
        print(a)
        print(z1 + x +y)
    return print("done")  



if __name__ == "__main__":
    calculate()