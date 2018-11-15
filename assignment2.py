
#from sense_hat import SenseHat   #This will import to code for the sensehat
import time      #This will import the code for time                          
#sense = SenseHat() #This is putting sensehat() into a globel veriable.
##################################################################################################
'''
Bradley Hubbard
Assignment 2 
'''
##################################################################################################
def Menu():                                 # This will get the user to input there option out of the three

    choice = ""

    print ("For Gyroscope input G:")                        # This will let the user choose which test
    print ("For Magnetometer (Compass) input M:")
    print ("For Temperature input T:")
    print ("For Quit in Q: ")
    print ("\n")                                # This will leave a blank line

    while choice == "":                         # This will loop until an input is enter
        choice = input ('Please input your choice: ')
        choice = choice.upper()                 # This is turn any input into captials so that what every is inputted will work.
        print ("\n" * 5)

   #this will get the user choose and run the requested test def statement.
    if choice == "G":
        Gyroscope()
    elif choice == "M":
        Magnetometer()
    elif choice == "T":
        Temperature()
    else: choice == "Q"

############################################
def Gyroscope():    # this is the gyroscope test.

    mychar = ''
    Testnumber = input ('Please enter a Number for the test: ')
    Testname = input ('Please enter a name for the test: ')
    if "£" in Testname :
        mychar = mychar  + "£" #Match? store it
    if "*" in Testname:
        mychar = mychar + "*" #Match? store it
    elif "@" in Testname:
        mychar = "@" #Match? store it
    elif "\n" in Testname:
        mychar = "\n" #Match? store it
    elif "|" in Testname:
        mychar = "|" #Match? store it
    #Where any legal charactors found in the test name.
    if mychar != '':
        print ("The following Charactors are not allowed", mychar)
    else:
        print("[Processing Gyroscope data...]")

    count = 0
    count = count + 1
    time.sleep(0.2)  #This will pause the test for 0.2 seconds to get 5 result per second.
    myarray=[]
    t_end = time.time() + 10

    while time.time() < t_end:
        pry = sense.get_gyroscope()
        o = sense.get_orientation()
        pitch = o["pitch"]
        roll = o["roll"]
        yaw = o["yaw"]

    if count > 37:
        print("pitch {0} roll {1} yaw {2}".format(pitch, roll, yaw))


    while cont == "Q":
        cont = input ("Q to quit ").upper

##############################################################################################
def Magnetometer():

    myarray=[]
    count = 0
    t_end = time.time() + 10

    mychar = ''
    Testnumber = input ('Please enter a Number for the test: ')
    Testname = input ('Please enter a name for the test: ')
    if "£" in Testname :
        mychar = mychar  + "£" #Match? store it
    if "*" in Testname:
        mychar = mychar  + "*" #Match? store it
    elif "@" in Testname:
        mychar = "@" #Match? store it
    elif "\n" in Testname:
        mychar = "\n" #Match? store it
    elif "|" in Testname:
        mychar = "|" #Match? store it
    #Where any legal charactors found in the test name.
    if mychar != '':
        print ("The following Charactors are not allowed", mychar)
    else:
        print("[Printing Temperature data...]")

    while time.time() < t_end:
      north = sense.get_compass()
      myarray.append(count + north) # this will print the test results.
      time.sleep(0.2)
      count = count + 1

    if count > 30:
        print("North: %s" % north)



    cont = "Q"

    while cont == "Q":
        cont = input ("Q to quit ").upper

##############################################################################
def Temperature():

    lenArray = []
    Count = 0
    Testname = ""
    t_end = time.time() + 10
    while time.time() < t_end:
        temp = sense.get_temperature() #This will run the temperture sense until the time runs out.
        lenArray.append(Count) + temp # this will print the test results.
        time.sleep(0.2)     #This will pause the test for 0.2 seconds to get 5 result per second.
        Count = Count + 1

    while Testname == "":
        Testnumber = input ('Please enter a Number for the test: ')
        mychar = ''
        Testname = input ('Please enter a name for the test: ')
        if "£" in Testname :
            mychar = mychar  + "£" #Match? store it
        if "*" in Testname:
            mychar = mychar  + "*" #Match? store it
        elif "@" in Testname:
            mychar = "@" #Match? store it
        elif "\n" in Testname:
            mychar = "\n" #Match? store it
        elif "|" in Testname:
            mychar = "|" #Match? store it
        #Where any legal charactors found in the test name.
        if mychar != '':
            print ("The following Charactors are not allowed", mychar)
        else:
            print("[Printing Temperature data...]")


    print ("\n" * 50)
    print (Testnumber)
    print (Testname)
    print ("\n" * 2)
    print(lenArray[40:]) #this will print the last 10 results


    cont = "Q"

    while cont == "Q":
        cont = input ("Q to quit ").upper

################################################################################################
Menu() #this will run the menu.

