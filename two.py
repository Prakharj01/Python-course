import one

print("Top level in two.py")

one.myfunc()
if __name__=="__main__":
    print("Two.py is being run directly")
else:
    print("It has been imported")