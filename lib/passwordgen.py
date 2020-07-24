def password_generator(request):
    while True:
        try: 
            pw_length = int(char_no)
            print("Here you go:")
            #Secrets.choice for high entropy character selection.
            char_list = string.ascii_letters + string.digits
            password = ''.join(secrets.choice(char_list) for i in range(pw_length)) 
            print(password) 
        #Re-ask for an integer if invalid input
        except ValueError:
            print("Please enter a valid number into funtion: ")
            continue
    
        else:
            break

make_password(12)
    password = "password"
    return render(request, "swissarmywife/password_generator.html", {
                "password": password
    })
    