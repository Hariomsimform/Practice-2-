def add(a, b):
    try:
       return (int (a)+ int (b))
    except Exception as error:
        return (error)
print(add(int(input("Enter 1st no.:")), int(input("Enter 2nd no. :"))))
print(add(input("Enter 1st no.:"), input("Enter 2nd no. (enter string & see the output):")))