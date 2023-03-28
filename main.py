print("SECURE LOGIN")
username = input("Username: ")
password = input("Password: ")

if username == "jenna" and password == "jenna1":
  print("Nice to see you again Jenna!")
elif username == "joey" and password == "joey1":
  print("Thanks for logging in Joey!")
elif username == "stan" and password == "stan1":
  print("Welcome back, Stan!")
else:
  print("User not recognized. Please try logging in again with the correct credentials.")
