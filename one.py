def myfunc():
    print("This is myfunc in one.py")

print("Top level in one.py")
if __name__=="__main__":
    print("This is a direct call to one.py")
else:
    print("One.py has been imported")




