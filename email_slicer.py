email = input("Enter your mail: ")

count = email.index('@')

username = email[:count]
domain = email[count + 1 : ]

print(f"Username: {username}\n Domain: {domain}")