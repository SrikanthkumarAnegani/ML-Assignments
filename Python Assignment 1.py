# 1. Write a program which will find all such numbers which are divisible by 7 but are not a
# multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed
# in a comma-separated sequence on a single line.

n1=[]
for x in range(2000,3200):
    if(x%7==0) and (x%5==0):
        n1.append(str(x))
        print(','.join(n1))
        
        
    # 2. Write a Python program to accept the user's first and last name and then getting them
    # printed in the the reverse order with a space between first name and last name.
        
fname = input("Input your First Name : ")
lname = input("Input your Last Name : ")
print ("Hello  " + lname + " " + fname)

# 3. Write a Python program to find the volume of a sphere with diameter 12 cm.
# Formula: V=4/3 * ð * r


pi = 3.1415926535897931
r= 12.0
V= 4.0/3.0*pi* r**3
print('The volume of the sphere is: ',V)


# show the input in list or tuple
values=input("enter the inputs")
l=values.split(",")
list=[l]
t=tuple(l)
print( l)

#5.Display the  below star format
n=5;
for i in range(n):
    for j in range(i):
        print ('* ', end="")
    print('')

for i in range(n,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')
    
    
    #6. Reverse the input value
    list1=[]
    val=input("enter the value :")
    list1=val
    list1[::-1]
    
    #7. print the below value 
    
 print('WE, THE PEOPLE OF INDIA,\n having solemnly resolved to constitute India into a SOVEREIGN,!\n SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC \n and to secure to all  its citizens')


    