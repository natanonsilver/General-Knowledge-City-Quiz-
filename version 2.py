# in version 2 i will try handle and fix some errors

# ask the user details

try:
    name=str(input("Enter Your Name : "))
    if name == "123456789":
        raise Exception

except:
    input("enter your name again please \n")

try:
    age=int(input("How old are you"))
except:
    print("Please enter your correct age")

    
    






                    #ask user details

#user details
name = input("Enter Your Name : ")

#user details
age = int(input("Enter Your Age : "))

#greeting 
print("Hello", name,"")

#ask if user wants to play the quiz
status = input("Would You Like To Play The Quiz? : {}?: \na. Yes \nb. No \n=>".format(name))

#what if the user is not ready
if status == 'No' or status == 'no' or status == 'B' or status == 'b' :
    print("See You Next Time.")

#what if the user is ready?
if status == 'Yes' or status == 'Yes' or status == 'A' or status == 'a' :
    print("Welcome To The Quiz")    






