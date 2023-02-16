try:
    print(myname)
except NameError:
    print("myname is not defined")
except:
    print("another issue")
