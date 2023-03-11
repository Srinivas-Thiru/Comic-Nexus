import json

'''
def cleansing(name) :
    name = str(name.lower().strip())
    return name
'''


class Login:
    
    @classmethod
    def get_initial_input(self):
        numb_input = input("If you wanna signup, Press '1'\nIf you wanna signin, Press '2'\nIf you wanna quit, Press '3'\n\nYour Answer : ").strip()
        numb_ans = ['1','2', '3']
        while numb_input not in numb_ans:
            print("\nPlease enter a valid input!!!\n")
            numb_input = Login.get_initial_input()
        return numb_input

    @classmethod
    def get_answer_for_inventory(self) :
        print("\nINVENTORY MENU : ")
        print("\nWhat do you wanna do to your inventory?\nTo ADD new items - Press 1\nTo REMOVE any items - Press 2\nTo SEE items in your inventory - Press 3\nTo DELETE the inventory - Press 4\nTo Logout - Press 5\n")
        numb = input("Your answer : ").strip()
        inventory = ['1','2','3','4','5']
        while numb not in inventory:
            print("\nInvalid input\nPlease enter a valid input\n")
            numb = self.get_answer_for_inventory()
            
        return numb
      
    @classmethod  
    def changeInventory(self,user_name, pass_word):
        #user_name = input("Username : ").lower().strip()
        #pass_word = str(input("Password : "))
        with open("LoginCredentials.json", 'r') as f:
            file = json.load(f)
            comic_collection = file["comiccollection"]
            
            for key in file :
                if key == user_name :
                    member_dict = file[key]
                    if member_dict["password"] == pass_word :
                        memb_comic = member_dict["comicbook"]

            numb = self.get_answer_for_inventory()
            
            while numb != '5' :
                if numb == '3' :
                    if not memb_comic:
                        print("\nYou have no collection...\n")
                    else:
                        print("\nYOUR COMIC COLLECTION\n")
                        for comic in memb_comic:
                            print(comic.capitalize())
                    #numb = get_answer_for_inventory()
            
                if numb == '1' :
                    print("\nCOMIC COLLECTION\n")
                    for comic in comic_collection:
                        print(comic.capitalize())
                    add = input("\n\nEnter your choice : ").lower().strip()
                    if add in comic_collection:
                        if add not in memb_comic:
                            memb_comic.append(add)
                            print("\nAdded Successfully.\n")
                        elif add in memb_comic :
                            print("\nComic Book already in your inventory...\nPlease select a different one.\n")
                    else :
                         print("\nSorry, We don't have that right now...\nMaybe in future...\n")   
                    #numb = get_answer_for_inventory()
            
                if numb == '4' :
                    if not memb_comic:
                        print("\nYou have no comic in your collection to delete.\n")
                    else:
                        member_dict["comicbook"] =  []
                        print("\nDeleted Successfully.\n")
                    #numb = get_answer_for_inventory()
            
                if numb == '2' :
                    print("\nYOUR COMIC COLLECTION\n")
                    for comic in memb_comic:
                        print(comic.capitalize())
                    if not memb_comic :
                        print("\nYour inventory is empty\nPlease add somehting to remove it.\n")
                    else :
                        want_to_remove = input("\nEnter the name of the comic you wanna remove : ").lower().strip()
                        if want_to_remove in memb_comic :
                            memb_comic.remove(want_to_remove)
                            print("\nRemoved Successfully.\n")
                        else :
                            print("\nSorry, Comic Book not found in your collection.\nTry again\n")
                numb = self.get_answer_for_inventory()
                
            
            if numb == '5' :
                with open("LoginCredentials.json", "w") as f :
                    file[user_name] = member_dict
                    json.dump(file, f, indent= 4)
                print("\nLogged Out Successfully\nHave a great day!!!\n")
            

    @classmethod
    def SignInDict(self) : 
        user_name = input("\nUsername : ").lower().strip()
        pass_word = str(input("Password : ")).strip()
        with open("LoginCredentials.json", "r") as f :
            total_dict = json.load(f)
            user_name_list = []
            for key in total_dict :
                user_name_list.append(key)
            if user_name in user_name_list :
                username_dict = total_dict[user_name]
                if username_dict["password"] == pass_word :
                    print("\nLogin Successful!!!\n")
                    self.changeInventory(user_name, pass_word)  
                else:
                    print("\nInvalid Passsword...\n") 
            else : 
                print("\nInvalid Username...\nSignup to Login\n")
            
    @classmethod                   
    def SignUpDict(self) : 
        user_name = input("\nUsername : ").lower().strip()
        pass_word = str(input("Password : ")).strip()
        with open("LoginCredentials.json", "r") as f :
            total_dict = json.load(f)
            user_name_list = []
            for key in total_dict :
                user_name_list.append(key)
            if user_name in user_name_list :
                print("\nUsername already taken.\nTry again using a different Username\n")
            elif not user_name:
                print("\nUsername cannot be empty\n")
            elif not pass_word:
                print("\nPassword cannot be empty\n")
            else:  
                new_ID = {}
                new_ID["username"] = user_name
                new_ID["password"] = pass_word
                new_ID["comicbook"] = []
                total_dict[user_name] = new_ID
                with open("LoginCredentials.json", "w") as f :
                    json.dump(total_dict, f, indent= 4)
                print("\nCreated ID Successfully.\n")                





class LoginCheck:
    
    @classmethod
    def get_input_main_menu(self):
        num = input("\nIf you wanna signup, Press '1'\nIf you wanna signin, Press '2'\nIf you wanna quit, Press '3'\n\nYour Answer : ").strip()
        while num not in ['1','2','3'] :
            num = input("\nInvalid Input.\nPlease enter a valid input.\n\nIf you wanna signup, Press '1'\nIf you wanna signin, Press '2'\nIf you wanna quit, Press '3'\n\nYour Answer : ").strip()
        return num
    
  
  
