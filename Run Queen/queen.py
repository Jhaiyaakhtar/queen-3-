import os
import sys
import time
import json
import datetime
from random import *
import urllib.request 
from PIL import Image # pip install pillow
from turtle import * # pkg install turtle 
import random

#          import module 
#_________________________________________


print(os.system("clear"))
def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./10)
banner = open("logo.txt","r")
run_banner = banner.read()
print(run_banner)
img = Image.open('queen.txt') # image display run time queen.py
img.show()        
project_banner = open ("project_banner.txt","r")
run_banner = project_banner.read()
print(run_banner)
print("\n")
Break = input(" Enter project password: ")
with open("password_username.txt", "w") as j:
  j.write(Break + "\n")    
if Break=="joyriya":#password project
  print('\n')
  Break_2= input('Enter project username: ')
  with open ("password_username.txt","w") as j:
    j.write(Break_2 +"\n")  
  if Break_2=='joya':#username project
    print(os.system("clear"))
    print('\n')
    project_banner = open("project_banner.txt","r")
    run = project_banner.read()
    print (run)  
    option = open("option.txt","r")
    slowprint(option.read())    
    choice=int(input("please choice the number : "))
    if choice==1:# one number line
      time = datetime.datetime.now()
      print("\n")    
      print('==================================\n'
           f'||    {time} ||\n'
            '==================================\n')
      print("Exit...")               
    elif choice==2:#two number line
      print(os.system("clear"))
      banner = open("project_banner.txt","r")
      print(banner.read())
      print ("\n")
      user_password = input("Enter your password : ")
      password = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"
                  "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"
                  "1","2","3","4","5","6","7","8","9","0"]
                 #"@","$","_","&","-","+","(",")","/","*",":",";","!","?",",","~","`","|","•","√","π","÷","×","¶","∆","£"
                 #"¢","€","¥","^","°","=","{","}","\","%","©","®","™","✓","[","]","<",">"]
      guess = ""
      while (guess != user_password):                    
        guess = ""
        for letter in range(len(user_password)):    
          guess_letter = password[randint(0,25)]
          guess = str(guess_letter) + str(guess)
          print (guess)
          print ("try password:", guess," -  failed try! - ","   please wait -")
        if guess==user_password:
          print("\n")
          print("--------------------------------------")        
          print ("your password is = ", guess,"    programmer:joyriya queen ")
          print("exit...")
    elif choice==3:# three number line
      print(os.system("clear"))
      project_banner = open("project_banner.txt","r")
      print(project_banner.read())
      okay=input("tumi ekhon usa te aco !\n"
                 "\n"
                 "bari asba kise [bimane/hete] : ")
      if okay=='bimane':              
        print(os.system("clear"))
        project_banner = open("project_banner.txt","r")
        print(project_banner.read())
        okay = input("jodi biman maj pothe nosto hoye jai\n"
                     "\n"
                     " ki korbe perasut ek ta ace \n"
                     "\n"
                     "bimane ek ta bacca o ace \n"
                     "\n"
                     "tumi ki tar reke nije baste caw\n"
                     "\n"
                     "[y/n]")
        if okay=='y':
          print(os.system("clear"))
          project_banner = open("project_banner.txt","r")
          print(project_banner.read())                              
          slowprint("tumi to manus valo na \n"
                    "\n"
                    "bacca tar na baciye \n"
                    "\n"
                    "nije asco...\n"
                    "\n"
                    "end game....\n")
        else:
          print(os.system("clear"))
          project_banner = open("project_banner.txt","r")
          print(project_banner.read())        
          slowprint("❤️❤️❤️congratulations ❤️❤️❤️\n"
                    "\n"
                    "tumi game tai jeteco!")             
      else:
        print(os.system("clear"))
        project_banner = open("project_banner.txt","r")
        print(project_banner.read())      
        slowprint("hete aste aste tumi mara jabe\n"
                  "\n"
                  "End game...")   
    elif choice==4:# four number line
      print(os.system("clear"))
      banner = open("project_banner.txt","r")
      print(banner.read())   
      slowprint("        Please  enter correct answer 😌","\n")
      un = input("       what is name :")
      un2 = input(".      what is mother name : ")
      un3 = input("       what is father name : ")
      un4 = input("       relationship or single : ")
      print("\n")     
      slowprint(f"     ===========================================\n"
               f"     || 1 : my cat name is : {un}                            \n"
               f"     || 2 : my cat mother name is : {un2}                    \n"
               f"     || 3 : my cat father name is : {un3}                    \n"
               f"     || 4 : my cat is : {un4}                                \n"
                "     ||==========================================")
      slowprint("DONE MINE_JUST FOR FUN")
      print("Exit...")
    elif choice==5:# five number choice
      print(os.system("clear"))
      project_banner = open("project_banner.txt","r")
      print(project_banner.read()) 
      def guess_the_number():
        ran = random.randint(0,100)
        chance = 10
        while True:
          user_input = int(input("Enter your guess number : "))
          if ran > user_input:
            print("Your guess number small")
            chance -=1
            print(f"Your chance ={chance}______")
            if chance == 0:
              break
            continue
          elif ran < user_input:
            print("Your guess number high")
            chance -=1
            print(f"Your chance = {chance}______")
            if chance == 0:
              break
            continue
          else:
            print("❤️❤️congratulations ❤️❤️")
            break
      guess_the_number()                       
    elif choice==6:#six number choice
      print(os.system("clear"))
      project_banner = open("project_banner.txt","r")
      print(project_banner.read())
      contacts = {}
      def add_contact(name, number):
        contacts[name] = number
        print("Contact added successfully!")
      def search_contact(name):
        if name in contacts:
          print(f"Name: {name}, Number: {contacts[name]}")
        else:
          print("Contact not found!")
      def delete_contact(name):
        if name in contacts:
          del contacts[name]
          print("Contact deleted successfully!")
        else:
          print("Contact not found!")
      def display_contacts():
        if contacts:
          print("Contacts List:")
          for name, number in contacts.items():          
            print(f"Name: {name}\n, Number: {number}\n")
        else:
          print("No contacts found!")
      def main():
        while True:
          print("\n1. Add Contact\n2. Search Contact\n3. Delete Contact\n4. Display Contacts\n5. Exit")
          choice = int(input("Enter your choice: "))
          if choice == 1:                      
            name = input("Enter name: ")
            number = input("Enter number: ")
            add_contact(name, number)
          elif choice == 2:                      
            name = input("Enter name to search: ")
            search_contact(name)
          elif choice == 3:
            name = input("Enter name to delete: ")
            delete_contact(name)
          elif choice == 4:                     
            display_contacts()
          elif choice == 5:                   
            print("Exiting program...")
            break
          else:          
            print("Invalid choice!")
      if __name__ == "__main__":         
        main()
    elif choice==7: # seven number choice
      print(os.system("clear"))
      project_banner = open("project_banner.txt","r")
      print(project_banner.read())   
      class Car:
        def __init__(self, brand, model, year):                 
          self.brand = brand
          self.model = model
          self.year = year
          self.speed = 0
          self.direction = "straight"    
        def accelerate(self, acceleration):
          self.speed += acceleration    
        def brake(self, deceleration):
          if self.speed - deceleration >= 0:        
            self.speed -= deceleration
          else:
            self.speed = 0    
        def turn(self, direction):
          self.direction = direction
      def main():            
        my_car = Car("Toyota", "Corolla", 2022)
        while True:        
          print("\nCurrent Speed:", my_car.speed)
          print("Current Direction:", my_car.direction)
          print("1. Accelerate\n2. Brake\n3. Turn\n4. Exit")
          choice = int(input("Enter your choice: "))
          if choice == 1:
            acceleration = float(input("Enter acceleration amount: "))
            my_car.accelerate(acceleration)
          elif choice == 2:                      
            deceleration = float(input("Enter deceleration amount: "))
            my_car.brake(deceleration)
          elif choice == 3:
            direction = input("Enter direction (left/right/straight): ")
            my_car.turn(direction)
          elif choice == 4:           
            print("Exiting program...")
            break
          else:   
            print("Invalid choice!")
      if __name__ == "__main__":       
        main() 
    elif choice==8: #eight number choice
      print(os.system("clear"))
      project_banner = open("project_banner.txt","r")
      print(project_banner.read())
      ip_banner = open("ip_banner.txt","r")
      print(ip_banner.read())     
      print("\n")
      ip1 = input("Enter the targeted ip address: ")
      url = "http://ip-api.com/json/" + ip1
      try:        
        response = urllib.request.urlopen(url)
        data = response.read()
        values = json.loads(data)
        print("\n")
        slowprint("#################################################################")
        slowprint("#      Query      : " + values['query'])
        slowprint("#      Status     : " + values['status'])
        slowprint("#      Country    : " + values['country'])
        slowprint("#      RegionName : " + values['regionName'])
        slowprint("#      City       : " + values['city'])
        slowprint("#      ZipCode    : " + values['zip'])
        slowprint("#      Isp        : " + values['isp'])
        slowprint("#      Org        : " + values['org'])
        slowprint("#      As         : " + values['as'])
        slowprint("#      Region     : " + values['region'])
        slowprint("#################################################################")
      except Exception as e:
        print("An error occurred:", e)
    elif choice==9:#nine number choice
      print(os.system("clear"))
      project_banner = open("project_banner.txt","r")
      print(project_banner.read())
      print("\n")
      input_text = input("Enter text: ")
      repeat = int(input("Enter range: "))
      for i in range(repeat):
        print(input_text)
      print("\n")
      print("exit.................Programmer joyriya akhtar")
    elif choice==10:#ten number choice
      print(os.system("clear"))
      banner = open("project_banner.txt","r")
      print(banner.read()) 
      print("\n")    
      print("------------------------------------ \n")            
      i = open("info.txt","r")
      r = i.read()
      print(r) 
    elif choice==11: # eleven number choice
      print(os.system("clear"))    
      code = open("code.txt","r")
      print(code.read()) 
    elif choice==12: # twelve number choice
      print(os.system("clear"))
      print("\n")
      while True: 
        calculator_1 = int(input("        Enter number :"))
        operation = input("        Enter [+ - × ÷ %] :")
        calculator_2 = int(input("        Enter number :"))
        if operation == "+":
          print("        Your Answer =", calculator_1 + calculator_2)
        elif operation == "-":
          print("        Your Answer =", calculator_1 - calculator_2)
        elif operation == "×":
          print("        Your Answer =", calculator_1 * calculator_2)        
        elif operation == "÷":
          print("        Your Answer =", calculator_1 / calculator_2)
        elif operation == "%":
          print("        Your Answer =", calculator_1 % calculator_2)
        else:
          print("Try Again............")
    elif choice == 13: #__
      print(os.system("clear"))    
      def run_project():    
        Data = [ ]
        while True:       
          print("                     1 : Add Number\n","                    2 : Display Number\n","                    3 : Delete Number\n")
          choice = int(input("  Please Enter yout choice : "))
          if choice == 1: 
            data = int(input("  Add Number : "))
            Data.append(data)
            print("  Number Add Successfully \n")
          elif choice == 2:          
            print(f"  Your All Number ={Data}\n")
          elif choice == 3:          
            delete = int(input(f"  Enter Delete number ={Data} : "))
            Data.remove(delete)
            print("  Number Delete Successfully \n")
          else:          
            print("Please Try Again")
      run_project()                
    elif choice == 14:
      print("\n")            
      a = datetime.datetime.now()
      class WeatherStation:      
        def __init__(self):
          self.weather_conditions = ["Sunny", "Cloudy", "Rainy", "Stormy", "Snowy"]
        def get_temperature(self):
          # Simulate temperature between -10 and 40 degrees Celsius
          return random.uniform(-10, 40)
        def get_humidity(self):
          # Simulate humidity between 20% and 100%
          return random.uniform(20, 100)
        def get_condition(self):
          # Randomly select a weather condition
          return random.choice(self.weather_conditions)
        def generate_report(self):
          temperature = self.get_temperature()
          humidity = self.get_humidity()
          condition = self.get_condition()
          return f" Today's Weather Report : {a}\n" \
                 f"     Condition: {condition}\n" \
                 f"     Temperature: {temperature:.2f} °C\n" \
                 f"     Humidity: {humidity:.2f} %"    
      # Example usage:
      weather_station = WeatherStation()
      # Generate and print a daily weather report
      print(weather_station.generate_report())
    
      
    
    elif choice == 15:
      print(os.system("clear"))    
      turtle_banner = open("turtle_banner.txt","r")
      print(turtle_banner.read())
      print("\n")    
      turtle = open("turtle_option.txt","r")
      print(turtle.read())
      print("\n")
      choice = int(input("Enter your turtle project : "))
      if choice == 1:
        print(os.ststem("clear"))
        print("\n")      
        bgcolor("black")
        fillcolor("black")
        color("green")
        rt(-180)
        fd(100)
        rt(60)
        fd(50)
        rt(-60)
        fd(50)
        rt(-50)
        fd(50)
        rt(50)
        fd(100)
        rt(80)
        fd(120)
        rt(98)
        fd(150)
        rt(-60)
        fd(70)
        rt(60)
        fd(150)
        rt(45)
        fd(120)
        rt(-45)
        fd(150)
        rt(90) 
        fd(100)
        rt(90)
        fd(150)
        rt(45)
        fd(50)
        rt(-45)
        fd(50)
        rt(-70)
        fd(50)
        rt(-150)
        fd(35)
        for i in range(16):                
          rt(20)
          fd(12)            
        rt(-180)
        fd(0)
        rt(80)
        fd(110)
        rt(70)
        fd(50)
        rt(-70)
        fd(50)
        rt(-60)
        fd(40)
        for i in range(16):                
          rt(-20)
          fd(12)
        rt(90)   
        fd(20)
        rt(110)
        fd(70)
        rt(-70)
        fd(60)
        rt(30)
        fd(30)
        rt(30)
        fd(20)
        rt(30)
        fd(30)
        rt(20)
        fd(50)
        rt(20)
        fd(30)
        rt(10)
        fd(20)
        rt(-120)
        fd(90)
        rt(-90)
        fd(100)
        rt(-90)
        fd(70)
        rt(52)
        fd(155)
        rt(-90)
        fd(100)
        done()
      elif choice == 2:
        print(os.system("clear"))
        a = open("turtle_banner.txt","r")
        print(a.read())
        print("\n")
        print("this option is empty ")      
      else:
        print(os.system("clear"))
        print("\n")
           # turtle if else statement 
        print("input wrong...... Exiting......")
      
      
         
    
      
      
      
      
      
      
      
                     	      
   
    else:#Exit choice number.
      print('Exiting...')    
  else:#username exit line 
    slowprint('project Username not correct ! end Program ....')          
else:#password exit line 
  slowprint("project password not correct ! end program......")                      