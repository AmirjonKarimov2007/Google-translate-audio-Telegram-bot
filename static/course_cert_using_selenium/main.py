from test import get_certificate

def main():
    try:
        # Replace these values with the actual name, email, and password
        name = "asdlkjfhadsklfhadskjhfa"
        email = "slkjadlfkasdsa4jdhflksaj44@gmail.com"
        password = "laskjdfkadsjhfkasdjhflkadsjhflkasdhf"

        get_certificate(name, email, password)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
