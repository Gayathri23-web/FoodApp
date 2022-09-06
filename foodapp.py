import random

class Admin:
    def __init__(self):
        self.admin_login= False
        self.admin_details={}
        #self.food=[]
        self.foods={}
        self.user_details={}
        self.order_history=[]
        self.user_login=False
    
    def register_admin(self):
        self.admin_name= input("\n Enter your name ")
        a=int(input("\n Enter your mobile number : "))
        if len(str(a))==10:
            self.admin_number=a
        else:
            print("\n Please enter valid number")
        
        self.admin_mail= input("\n Enter your mail id ")
        self.admin_pass= input("\n Enter your password ")
        d={}
        d["admin_name"]= self.admin_name
        d["admin_mail"]= self.admin_mail
        d["admin_number"]= self.admin_number
        d["admin_pass"]= self.admin_pass
        self.admin_details[self.admin_number]=d
        print("\n Your registration sucessfully completed ")

    def login_admin(self):
        num= int(input("Enter ur number "))
        if num in self.admin_details:
            z= input("\n Enter ur password ")
            if self.admin_details[num]["admin_pass"]== z:
                self.admin_login= True
                print("\n Loggin sucessful")
                
        else:
            print("\n Register first or enter valid num")

    def add_new_food(self):
        self.food=[]
        self.food_id= random.randrange(1,1000,1)
        n= input("\n Enter food name ")
        self.food.append(n)
        q= int(input("\n Enter the quantity in pieces "))
        self.food.append(q)
        p= int(input("\n Enter the price "))
        self.food.append(p)
        self.foods[self.food_id]= self.food
        print("\n Food item added sucessfully")
        print(self.foods)

    def edit_food(self):
        t= int(input("\n Enter your food ID "))
        if t in self.foods:
            j=int(input("\n 1 to change food ID \n 2 to change food name  \n 3 to change food quantity \n 4 to change food price"))
            if j==1:
                b=self.foods[t]
                self.foods.pop(t)
                c=input(" \n Enter new id for that food : ")
                self.foods[c]=b
                print(" \n  Your food's has been changed sucessfully ")
            if j==2:
                self.foods[t][0]=input("Please enter new name to the food ")
                print(" \n  Your food's name has been changed sucessfully ")
            if j==3:
                self.foods[t][1]=int(input("Please enter new quantity for the food "))
                print("\n  Your food's quantity has been changed")
            if j==4:
                self.foods[t][2]=int(input("please enter new price "))
                print("\n Your food's price has been changed ")
                
        else:
            print("\n Invalid food ID ")
            
    def list_of_food_items(self):
        print("These are the available food list \n ",self.foods.values())
        
    
    
    def remove_food(self):
        d=int(input(" \n Enter your food id "))
        if d in self.foods:
            p=input(" \n  Do you want to delete this food if Yes type Y or y")
            if p=="Y" or "y":
                self.foods.pop(d)
                print(" \n Your list was updated after removing that food ")
            if p=="N" or "n":
                    pass
        else:
            
            print(" \n Your food id was not found ")

    def user_register(self):
        self.user_name= input("\n Enter your full name ")
        a=int(input("\n Enter your mobile number : "))
        if len(str(a))==10:
            self.user_number=a
        else:
            print("\n Please enter valid number")
        
        self.user_mail= input("\n Enter your mail id ")
        self.user_pass= input("\n Enter your password ")
        self.user_address= input("\n Enter your address ")
        s={}
        s["user_name"]= self.user_name
        s["user_mail"]= self.user_mail
        s["user_number"]= self.user_number
        s["user_pass"]= self.user_pass
        s["user_address"]= self.user_address
        self.user_details[self.user_number]=s
        print("\n Your registration sucessfully completed ")


    def login_user(self):
        #self.order_history=[]
        num= int(input("Enter ur number "))
        if num in self.user_details:
            z= input("\n Enter ur password ")
            if self.user_details[num]["user_pass"]== z:
                self.user_login= True
                print("\n Loggin sucessful")
                z= int(input("\n 1 Place new order  \n 2 Order history  \n 3 Update profile "))
                if z==1:
                    print("\n Here is list of all food items with name, quantity & price \n " ,list(self.foods.values()))
                    print("\n But you have to enter food id of that food following is the food id with food details \n ", self.foods)
                    t= int(input("\n Enter your food id "))
                    if t in self.foods:
                        r= input("\n Plz enter y or Y to confirm")
                        if r=="y" or "Y":
                            g=self.foods.pop(t)
                            
                            self.order_history.append(g)
                            print("\n Order place succesfully ")
                        else:
                            print("\n You don't like our product? Sorry for the incovinience sir")
                    else:
                        print("\n Food id not found ")
                        
                if z==2:
                    print("\n Your order details saved in this list ", self.order_history)
                    
                if z==3:
                    x= int(input("\n Enter your number "))
                    if x in self.user_details:
                        e= list(self.user_details.values())[0]
                        n= int(input(" \n 1 to change name \n 2 to change mail \n 3 to change number \n 4 to change password \n 5 to change address "))
                        if n==1:
                            e["user_name"]= input("\n Enter new user name ")
                            print("\n Profile updated sucessfully ", self.user_details)
                    
                        elif n==2:
                            e["user_name"]= input("\n Enter new mail ")
                            print("\n Profile updated sucessfully ", self.user_details)
                    
                        elif n==3:
                            e["user_number"]=int(input("\n Enter new number "))
                            print("\n Profile updated sucessfully ", self.user_details)
                     
                        elif n==4:
                            e["user_pass"]= input("\n Enter new password ")
                            print("\n Profile updated sucessfully ", self.user_details)
                     
                        elif n==5:
                            e["user_address"]= input("\n Enter new address ")
                            print("\n Profile updated sucessfully ", self.user_details)
                            
                    else:
                        print("Entered wrong number")
                     


    
                            
                      
                    
                            
        
                
                
        else:
            print("\n Register first or enter valid num")
                      
    
    
    def menu(self):
        w= True
        while w:
            u= int(input("\n 1 To register admin \n 2 To login admin \n 3 To add new food item \n 4 To see current stock \n 5 To edit food \n 6 To see list of food items \n 7 To remove food \n 8 To user register \n 9 To user login "))
            if u==1:
                self.register_admin()
            if u==2:
                self.login_admin()
            if u==3:
                self.add_new_food()
            if u==5:
                self.edit_food()
            if u==4:
                self.list_of_food_items()
            if u==7:
                self.remove_food()
            if u==9:
                self.user_register()
            if u==10:
                self.login_user()
                
        else:
            print("Entered wrong input ")


a = Admin()
a.menu()