#********************* Q1 **********************
"""The for loop is used when we already know the number of iterations,
which means when we know how many times a statement has to be executed.
That is why we have to specify the ending point in the for loop initialization. 
When we need to end the loop on a condition other than the number of times,
we use a while loop.1 
examples : for loop
for i in range(5):
   print(i)
   in this example we know how manhy tinme loop should be executed so 
   in that type of situatiin we use for loop
   
example : while loop
count=1
while count<6:
  print(count)
  count+=1 
  #in this example we are used while loop because we dont know how many times
  loop should be executed so thats why we use while loop we have to run program untill
  the desires condition can be fulfilled

"""


# ********************** Q2 ********************
sum=0
product=1
for i in range(1,11):
    sum=sum+i
    product=product*i
    
print("the sum of first 10 natural number : ",sum)
print("the product of first 10 natural number : ",product)
    
# ********************* Q3 ****************************
unit = int(input("enter the unit consumed by user : "))

if unit<=100:
    pa=unit*4.5
elif 101<=unit<=200:
    pa=(100*4.5)+((unit-100)*6)
elif 201<=unit<=300:
    pa=(100*4.5)+(100*6)+((unit-200) *10)
else:
    pa=(100*4.5)+(100*6)+(100 *10)+((unit-300)*20)
    
print("total amount have to pay : ",pa)
    
# ********************** Q4 *****************************
l=[]
l1=[]
for i in  range(1,101):
    l.append(i)
print(l)
    
for i in l: 
  print(i**3)
  if i**3%4==0 or i**3%5==0:
      l1.append(i**3)
print(l1)
 

# ****************** Q5 ********************************
string = "i want to become a data scientist"
print(len(string))
count=0
vowel=""

for i in string: 
     if i=="i" or i=="a" or i=="e" or i=="o" or i=="u":
         count+=1
         

print("total vowels are : ",count)
         
    
        