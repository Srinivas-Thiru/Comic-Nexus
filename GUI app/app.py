from tkinter import *
import json




# First Class
class FirstWindow:

    
    @classmethod
    def loadfile(self):
        with open("LoginCredentials.json", 'r') as file:
            total_dict = json.load(file)
        return total_dict

    @classmethod
    def logout(self):
        self.save()
        new.destroy()
        main()
        
    @classmethod    
    def save(self):
        final_list = your_collection.get(0,END)
        final = []
        for i in final_list:
            final.append(i.lower())    
        member_dict["comicbook"] = final
        with open("LoginCredentials.json", 'w') as f:
            json.dump(total_dict, f, indent=4)
        label_add_remove_saved.config(text="Saved Successfully")    
            


# Second Class
class Inventory :
    
    @classmethod
    def delete(self):
        label_add_remove_saved.config(text="")        
        end_index = your_collection.index("end")
        if end_index == 0:
            label_add_remove_saved.config(text="Your Inventory is already empty")
        else :     
            your_collection.delete(0,END)    
            label_add_remove_saved.config(text="Inventory Deleted Successfully.")
        
    @classmethod
    def remove(self):
        
        label_add_remove_saved.config(text="")
        current_selection = your_collection.curselection()
        if current_selection:
            your_collection.delete(ANCHOR) 
            label_add_remove_saved.config(text="Item removed Successfully.")
        else:
            label_add_remove_saved.config(text="Select an item to remove")
    
    @classmethod    
    def select(self):

        label_add_remove_saved.config(text="")
        current = your_collection.get(0, END)
        
        for i in comic_collection.curselection():
            selected = comic_collection.get(i)
        
        try :
            
            if selected in current:
                label_add_remove_saved.config(text="Item already in your collection")
            else:    
                your_collection.insert(END, selected)
                label_add_remove_saved.config(text="Item Added Successfully.")
                
        except UnboundLocalError:
            label_add_remove_saved.config(text="Please Select an item to add.")            
    
    



def main():

    global total_dict
    total_dict = FirstWindow.loadfile()
    
    # Creates a new form and load the member's comic collection.
    def new_window():
    
        global label_welcome, comic_collection, button_logout, memb_comic, your_collection, button_delete,new
        global label_collection,label_your_collection, button_add, button_remove, label_add_remove_saved, button_save
    
        new = Tk()
        window_name = username + "'s Inventory"
        new.title(window_name.capitalize())
        #new.geometry("500x750")
    
        button_logout = Button(new, text="Log out", command=FirstWindow.logout).pack(side=TOP, anchor='e', padx='2', pady='2')
        label_welcome = Label(new, text="Welcome " + username.capitalize() , font= ('helvetica', 20, 'bold')).pack()
        
        profile_frame = Frame(new, padx='25', pady='20')
        profile_frame.pack()
        
        label_collection = Label(profile_frame, text="Our Collection", pady='10', font=('helvetica', 14,'bold') ).grid(row=1,column=1)
        
        comic_frame = Frame(profile_frame)
    
        comic_collection_scroll = Scrollbar(comic_frame, orient=VERTICAL)
        
        
        comic_collection = Listbox(comic_frame,width=20, yscrollcommand=comic_collection_scroll.set)
        for i in total_dict["comiccollection"]:
            comic_collection.insert(END, i.capitalize())
        

        comic_collection_scroll.config(command= comic_collection.yview)
        comic_collection_scroll.pack(side=RIGHT,fill=Y)
        comic_collection.pack()

        
        comic_frame.grid(row=2,column=1)

        
        remove_delete_frame = Frame(profile_frame)
        remove_delete_frame.grid(row=3,column=3)

        button_add = Button(profile_frame, text="Add" , command= Inventory.select).grid(row=3,column=1)
        
        button_remove= Button(remove_delete_frame, text="Remove", command = Inventory.remove).grid(row=1,column=1)
        
        button_delete= Button(remove_delete_frame, text="Delete", command = Inventory.delete).grid(row=1,column=2)
        
        button_save= Button(new, text="Save", command = FirstWindow.save).pack(side=BOTTOM, anchor='e', padx='8', pady='8')
        
        label_gap = Label(profile_frame, text="       ")
        label_gap.grid(row=2,column=2)
        
        label_add_remove_saved = Label(new, text="", font=('arial', 15, 'underline'))
        label_add_remove_saved.pack()
        
        label_your_collection = Label(profile_frame, text= "Your Collection", pady='10', font=('helvetica', 14,'bold')).grid(row=1,column=3)
        
        your_collection_frame = Frame(profile_frame)
        
        your_collection_scroll = Scrollbar(your_collection_frame, orient=VERTICAL)
        
        your_collection = Listbox(your_collection_frame, width=20, yscrollcommand=your_collection_scroll.set)
        memb_comic = member_dict["comicbook"]
        for i in memb_comic:
            your_collection.insert(END, i.capitalize())
    

        your_collection_scroll.config(command=your_collection.yview)
        your_collection_scroll.pack(side=RIGHT, fill=Y)
        your_collection.pack()
        
        your_collection_frame.grid(row=2,column=3)
        
        
    # Login/Singup Window
    login_window = Tk()
    login_window.title("CARLOS COMIC BOOK STORE")
    login_window.geometry("500x500")

    
    def get_username_from_database(total) :
        username_list = []
        for key in total :
            username_list.append(key)
        return username_list

    def login():
        global username, password, member_dict
        username_list = get_username_from_database(total_dict)
        username = entry_username.get().strip().lower()
        password = entry_password.get()
        if username in username_list:
            member_dict = total_dict[username]
            if password == member_dict["password"]:
                label_status.config(text="Login successful!")
                login_window.destroy()
                new_window()
            else:
                label_status.config(text="Invalid Username/password.\n", font= ('arial', 15,'underline'))
        else:
            label_status.config(text="Invalid Username/password.\n",font= ('arial', 15,'underline'))


    def SignUp():
        username_list = get_username_from_database(total_dict)
        username = entry_username.get().strip().lower()
        password = entry_password.get()
        if username in username_list:
            label_status.config(text="Username already exist,\nTry a different one")
        elif not username:
            label_status.config(text="Username can't be empty,\nTry a different one")
        elif not password:
            label_status.config(text="Password can't be empty,\nTry a different one")

        else :
            memb_dict = {}
            memb_dict["username"] = username
            memb_dict["password"] = password
            memb_dict["comicbook"] = []
            total_dict[username] = memb_dict
            label_status.config(text="Successfully Signed Up.")
        with open("LoginCredentials.json", 'w') as f:
            json.dump(total_dict, f, indent =4)
            
        



    label = Label(login_window, text= "\n\nWELCOME TO CARLOS COMIC BOOK STORE\n", font= ('Helvetica', 20, 'bold'))
    label.pack()

    lbl = Label(login_window, text="Login, If you have an account\nSign up to create an account\n\n")
    lbl.pack()

    label_username = Label(login_window, text="Username:")
    label_username.pack()

    entry_username = Entry(login_window)
    entry_username.focus_set()
    entry_username.pack()

    label_password = Label(login_window, text="Password:")
    label_password.pack()
    entry_password = Entry(login_window, show="*")
    entry_password.pack()

    label_status = Label(login_window, text="\n")
    label_status.pack()
    
    login_button_frame = Frame(login_window)
    login_button_frame.pack()

    button_login = Button(login_button_frame, text="Login", command=login)
    button_login.grid(row=1,column=1)

    button_signup = Button(login_button_frame, text= "Sign Up", command = SignUp)
    button_signup.grid(row=1,column=2)

    button_exit = Button(login_window, text= "Exit", command = login_window.destroy)
    button_exit.pack(side=BOTTOM, anchor='e', padx='8', pady='8')

    login_window.mainloop()


if __name__ == '__main__' :
    main()

