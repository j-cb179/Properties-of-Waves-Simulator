wlVAR = float(0.0)#wavelength
velVAR = float(0.0)#velocity
freqVAR = float(0.0)#frequency
ampVAR = float(0.0)#amplitude
period = float(0.0)#period

def inputVARFloat(message): #function to validate data type as float
    while True:
        try:
            varInput = float(input(message)) #attempts to cast user input as float
        except ValueError: #if an error message is returned
            print("Please enter integer/floating point value") #output to user
            continue #re-ask query
        else:
            if varInput > 0.0: 
                return varInput #returns result of input to program if it can be casted as float
                break
            else:
                print("Please enter value above 0")
                continue #re-ask query


def Calculation(): #procedure for mathematical calculations
    global wlVAR, velVAR, freqVAR, period #delcaring the global variables used in the procedure
    if wlVAR != 0.0: #if the user has provided an input for wavelength
        if freqVAR != 0.0: #if the user has provided an input for frequency
            velVAR = float(wlVAR * freqVAR)
            period = float(1 / freqVAR)
            printOutput() #will execute the procedure to print the results of the maths
        else: # if the user has provided an input for velocity
            freqVAR = float(velVAR / wlVAR)
            period = float(1 / freqVAR)
            printOutput() #will execute the procedure to print the results of the maths
    else: #if the user has provided inputs for frequency and velocity
            wlVAR = float(velVAR / freqVAR)
            period = float(1 / freqVAR)
            printOutput() #will execute the procedure to print the results of the maths
        

def printOutput(): #procedure for printing the result of calculations
    global wlVAR, velVAR, freqVAR, ampVAR, period #delcaring the global variables used in the procedure
    print("Your wavelength is:", wlVAR, "metres") #wavelength
    print("Your velocity is:", velVAR, "metres per second") #velocity
    print("Your frequency is:", freqVAR, "hertz") #frequency
    print("Your amplitude is:", ampVAR, "metres") #amplitude
    print("The period of your wave is:", period, "seconds") #period
    wlVAR = 0
    velVAR = 0
    freqVAR = 0
    ampVAR = 0
    period = 0


prevOp = " " #previous option
noEnt = 0 #number of entered data
while noEnt < 2: #indefinite iteration
    
    if noEnt == 0: 
        option = input("Select a variable to input (Wavelength (or w), Frequency (or f), Velocity (or v)): ") #initial input
        option = option.lower() #standardise the input to lowercase
        if option == "wavelength" or option == "w": #if user inputted wavelength (or variance)
            prevOp = "wl" #making wavelength the last picked option
            print("you picked wavelength")
            wlVAR = inputVARFloat("Please input wavelength in metres: ") #prompting user input using input function
            print("wavelength =", wlVAR)
            print("PrevOp =", prevOp)
            noEnt = 1 #changing the if perameter
            continue
        elif option == "frequency" or option == "f": #if user inputted frequency (or variance)
            prevOp = "freq" #making frequency the last picked option
            print("you picked frequency")
            freqVAR = inputVARFloat("Please input frequency in hertz: ") #prompting user input using input function
            print("frequency =", freqVAR)
            print("PrevOp =", prevOp)
            noEnt = 1 #changing the if perameter
            continue
        elif option == "velocity" or option == "v": #if user inputted velocity (or variance)
            prevOp = "vel" #making velocity the last picked option
            print("you picked velocity")
            velVAR = inputVARFloat("Please input velocity in metres/second: ") #prompting user input using input function
            print("velocity =", velVAR)
            print("PrevOp =", prevOp)
            noEnt = 1 #changing the if perameter
            continue
        else:
            print("Please enter valid input") #defensive design
            
    elif noEnt == 1:
        if prevOp == "wl": #if the user has already provided a value for the wavelength
            option = input("Select a variable to input (Frequency (or f), Velocity (or v)): ")
            option = option.lower() #standardise the input to lowercase
            if option == "frequency" or option == "f": #if user inputted frequency (or variance)
                print("you picked frequency")
                freqVAR = inputVARFloat("Please input frequency in hertz: ") #input
                print("frequency =", freqVAR)
                ampVAR = inputVARFloat("Please input an amplitude in metres: ") #amplitude input
                print("Calculating...")
                Calculation() #runs Calculation()
                noEnt=0 #keeps program within loop parameters
            elif option == "velocity" or option == "v": #if user inputted velocity (or variance)
                print("you picked velocity")
                velVAR = inputVARFloat("Please input velocity in metres/second: ") #input
                print("velocity =", velVAR)
                ampVAR = inputVARFloat("Please input an amplitude in metres: ") #amplitude input
                print("Calculating...")
                Calculation() #runs Calculation()
                noEnt=0 #keeps program within loop parameters
            else:
                print("Please enter valid input") #defensive design
        elif prevOp == "freq": #if the user has already provided a value for the frequency
            option = input("Select a variable to input (Wavelength (or w), Velocity (or v)): ")
            option = option.lower() #standardise the input to lowercase
            if option == "wavelength" or option == "w": #if user inputted wavelength (or variance)
                print("you picked wavelength")
                wlVAR = inputVARFloat("Please input wavelength in metres: ") #input
                print("wavelength =", wlVAR)
                ampVAR = inputVARFloat("Please input an amplitude in metres: ") #amplitude input
                print("Calculating...")
                Calculation() #runs Calculation()
                noEnt=0 #keeps program within loop parameters
            elif option == "velocity" or option == "v": #if user inputted velocity (or variance)
                print("you picked velocity")
                velVAR = inputVARFloat("Please input velocity in meters/second: ") #input
                print("velocity =", velVAR)
                ampVAR = inputVARFloat("Please input an amplitude in meters: ") #amplitude input
                print("Calculating...")
                Calculation() #runs Calculation()
                noEnt=0 #keeps program within loop parameters
            else:
                print("Please enter valid input") #defensive design
        elif prevOp == "vel": #if the user has already provided a value for the velocity
            option = input("Select a variable to input (Wavelength (or w), Frequency (or f): ")
            option = option.lower() #standardise the input to lowercase
            if option == "frequency" or option == "f": #if user inputted frequency (or variance)
                print("you picked frequency")
                freqVAR = inputVARFloat("Please input wavelength in hertz: ") #input
                print("frequency =", freqVAR)
                ampVAR = inputVARFloat("Please input an amplitude in meters: ") #amplitude input
                print("Calculating...")
                Calculation() #runs Calculation()
                noEnt=0 #keeps program within loop parameters
            elif option == "wavelength" or option == "w": #if user inputted wavelength (or variance)
                print("you picked wavelength")
                wlVAR = inputVARFloat("Please input wavelength in metres: ") #input
                print("wavelength =", wlVAR)
                ampVAR = inputVARFloat("Please input an amplitude in metres: ") #amplitude input
                print("Calculating...")
                Calculation() #runs Calculation()
                noEnt=0 #keeps program within loop parameters
            else:
                print("Please enter valid input") #defensive design

        else:
            print("Program error") #defensive design
            noEnt = 0
