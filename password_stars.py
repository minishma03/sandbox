def main():
    """Get a password and display stars."""
    password = input("Enter password: ")

    while len(password) < 4:
        print("Password must be at least 4 characters")
        password = input("Enter password: ")

    print("*" * len(password))


main()
