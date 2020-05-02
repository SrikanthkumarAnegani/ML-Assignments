
#1.Write a function to compute 5/0 and use try/except to catch the exceptions.

def my_function():
  print("Try  except implementaion")
  
try:
    x = 5 / 0
except:
    print("Error dividing by zero")
finally:
        print("Sucess if try sucess")
    
    
    #outpout
        
       # Error dividing by zero"
        
#2. 2. Implement a Python program to generate all sentences where subject is in ["Americans", "Indians"] and verb is in ["Play", "watch"] and the object is in ["Baseball","cricket"].
        subject=["Americans","Indians"]
        Verbs=["Play","watch"]
        Object=["Baseball","Cricket"]
        
        All_sentence=[(sub+" " + Ver + " " + obj) for sub in subject for Ver in Verbs for obj in Object]
            for i in All_sentence:
                    print(i)
    
  
    ##output

Americans Play Baseball
Americans Play Cricket
Americans watch Baseball
Americans watch Cricket
Indians Play Baseball
Indians Play Cricket
Indians watch Baseball
Indians watch Cricket