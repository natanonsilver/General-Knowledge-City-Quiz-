# In version 3 of my quiz i will doing my 10 question quiz that is a multichoice quiz.


#asking user for name

try:
    name=str(input("enter your name:"))
    if name == "1234":
        raise Exception
except: 
    input("Please try again, enter your name \n")

#ask the user to enter there age.

try:
    age=int(input("Please enter your age?:"))
except:
    print("not valid")
else:
    print("Please continue")

#asking the user if they are ready to take the quiz
    ready=input("are you ready for the quiz?: press y to continue or x to exit:")


if ready=="y" or "yes" :
    print("lets continue")
    
elif ready== "x" or "no":
    print("Thank you come again")

#Preparing the dictionary

Captialcitesquiz=(
'1. What is the captial for Nigeria': 'Abuja',
'2. What is the captial for Spain': 'Madrid',
'3. What is the captial for Canada': 'Ottawa',
'4. What is the captial for New Zealand': 'Wellington',
'5. What is the captial for Italy': 'Rome',
'6. What is the captial for Peru': 'Lima',
'7. What is the captial for San Marino': 'San Marino',
'8. What is the captial for Mexico': 'Mexico City',
'9. What is the captial for United States Of America': 'Washington DC',
'10. What is the captial for Syria': 'Damascus',


}

#preparing the multi choice

optlist=['Abuja:11:12:13',
         '11:12:18:20',
         'Jumping:Swimming:Cycling:Running',
         'Speaking:Kicking:Dribbling:Jogging',
         'No running with the ball: No speaking with the ball:No passing of the ball:',
         'Ants:Coakroaches:Unicorns:Butterfly:',
         '3 seconds:50 seconds:10 seconds:100 seconds',
         '30 mins:1 hour:1 min:2 mins',
         '2 times: 1 time: 3 times: 4 times',
         'Running:Passing:Throwing:Breathing techniques',]
         








                                                                                                                                                    
    

                                        
    
