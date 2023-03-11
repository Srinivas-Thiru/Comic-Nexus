from ProjectFunc import Login

    

def main():
    
    print("\n\nWELCOME TO CARLOS COMIC BOOK STORE\n\n")
    numb = Login.get_initial_input()
    
    while numb == '1' or numb == '2' :
        if numb == '1':
            Login.SignUpDict()
            
        if numb == '2':
            Login.SignInDict()
        numb = Login.get_initial_input()
    
    if numb == '3':
        print("\nBYE\nHave a Great Day!!!!\n")


main()
