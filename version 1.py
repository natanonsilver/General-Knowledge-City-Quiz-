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


