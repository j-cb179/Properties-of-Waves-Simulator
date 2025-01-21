from tkinter import *

#tkinter base code
root = Tk()
root.title("Wave Sim (iteration 1)")
root.configure(background="#99ccff")
root.state('zoomed')


#declaring global variables
wlVAR = 0.0 #wavelength
velVAR = 0.0 #velocity
freqVAR = 0.0 #frequency
ampVAR = 0.0 #amplitude
period = float(0.0) #period

toggleState = True #used to toggle between input types sliders and textboxes


#Selecting the amplitude and unit via slider and radiobuttons
def selectAmp(self):
    global ampVAR
    global ampUnit
    ampVAR = ampScale.get() #retrieving the number set on the slider
    ampVAR = float(ampVAR) #converting to float
    print(str(ampVAR) + ampUnit.get()) #temporary output
    root.after(0, Calculate(self))
    

#Selecting the wavelength and unit via slider and radiobuttons
def selectWaveL(self):
    global wlVAR #declaring wlVAR and wlUnit as global to use in the function
    global wlUnit
    wlVAR = wlScale.get() #retrieving the number set on the slider
    wlVAR = float(wlVAR) #converting to float
    print(str(wlVAR) + wlUnit.get()) #temporary output
    root.after(0, Calculate(self))
    

#Selecting the amplitude and unit via slider and radiobuttons
def selectFreq(self):
    global freqVAR
    freqVAR = freqScale.get()
    freqVAR = float(freqVAR) #converting to float
    print(str(freqVAR) + "Hz") #temporary output
    root.after(0, Calculate(self))


#Selecting the amplitude and unit via slider and radiobuttons
def selectVel(self):
    global velVAR
    velVAR = velScale.get()
    velVAR = float(velVAR) #converting to float
    print(str(velVAR) + " m/s") #temporary output
    root.after(0, Calculate(self))


def Calculate(self):
    global wlVAR
    global freqVAR
    global velVAR
    if wlVAR != 0.0:
        if velVAR != 0.0:
            freqVAR = velVAR / wlVAR
            period = float(1 / freqVAR)
            print("The wavelength is", wlVAR, wlUnit)
            print("The velocity is", velVAR, "m/s")
            print("The frequency is: ", freqVAR, "Hz")
            print("The period is: ", period, "s")
            root.after(0, editScales(self))
        else:
            velVAR = wlVAR * freqVAR
            period = float(1 / freqVAR)
            print("The wavelength is", wlVAR, wlUnit)
            print("The velocity is", velVAR, "m/s")
            print("The frequency is: ", freqVAR, "Hz")
            print("The period is: ", period, "s")
            root.after(0, editScales(self))
    else:
        if velVAR == 0 and freqVAR == 0:
            return 0
        elif velVAR == 0 or freqVAR == 0:
            return 0
        else:
            wlVAR = velVAR / freqVAR
            period = float(1 / freqVAR)
            print("The wavelength is", wlVAR, wlUnit)
            print("The velocity is", velVAR, "m/s")
            print("The frequency is: ", freqVAR, "Hz")
            print("The period is: ", period, "s")
            root.after(0, editScales(self))


def editScales(self):
    global wlVAR
    global freqVAR
    global velVAR
    global period
    global ampVAR
    ampScale.set(ampVAR)
    wlScale.set(wlVAR)
    freqScale.set(freqVAR)
    velScale.set(velVAR)


def selectToggle():
    global toggleState
    if selectButton.config('text')[-1]=='Boxes':
        selectButton.config(text='Sliders')
        selectLabel.config(text='Sliders')
        toggleState = False
    else:
        selectButton.config(text='Boxes')
        selectLabel.config(text='Text Boxes')
        toggleState = True
    

#select between an input of sliders or inputboxes
selectLabel = Label(root,text="Text Boxes", bg="#99ccff", font=("Ariel", 20)).place(x=85,y=120)
selectButton = Button(root, text="Boxes", width=5, command=selectToggle)
selectButton.pack()
selectButton.place(x=30, y=127)

#amplitude label and inputs
ampLabel = Label(root,text="Amplitude", bg="#99ccff").place(x=100, y=175)
ampScale = Scale(root, bd=0, from_=0, to=100, orient="horizontal", length=150, command=selectAmp) #slider
ampScale.pack()
ampScale.place(x=55, y=200)

#amplitude radiobuttons
ampUnit = StringVar() #designating ampUnit as variable for radio buttons
ampMeter = Radiobutton(root, text="m", variable=ampUnit, value="m", bg="#99ccff", activebackground="#99ccff")
ampMilli = Radiobutton(root, text="mm", variable=ampUnit, value="mm", bg="#99ccff", activebackground="#99ccff")
ampMicro = Radiobutton(root, text="μm", variable=ampUnit, value="μm", bg="#99ccff", activebackground="#99ccff")
ampMeter.place(x=55, y=250)
ampMilli.place(x=105, y=250)
ampMicro.place(x=165, y=250)
ampMeter.select()


#wavelength label and inputs
wlLabel = Label(root,text="Wavelength", bg="#99ccff").place(x=100, y=300)
wlScale = Scale(root, bd=0, from_=0, to=750, orient="horizontal", length=150, command=selectWaveL) #slider
wlScale.pack()
wlScale.place(x=55, y=325)

#wavelength radiobuttons
wlUnit = StringVar() #designating wlUnit as variable for radio buttons
wlMeter = Radiobutton(root, text="m", variable=wlUnit, value="m", bg="#99ccff", activebackground="#99ccff")
wlMicro = Radiobutton(root, text="μm", variable=wlUnit, value="μm", bg="#99ccff", activebackground="#99ccff")
wlNano = Radiobutton(root, text="nm", variable=wlUnit, value="nm", bg="#99ccff", activebackground="#99ccff")
wlMeter.place(x=55, y=375)
wlMicro.place(x=105, y=375)
wlNano.place(x=165, y=375)
wlMeter.select()


#frequency label and inputs
freqLabel = Label(root,text="Frequency(Hz)", bg="#99ccff").place(x=90, y=425)
freqScale = Scale(root, bd=0, from_=0, to=750, orient="horizontal", length=150, command=selectFreq) #slider
freqScale.pack()
freqScale.place(x=55, y=450)


#velocity label and inputs
velLabel = Label(root,text="Velocity(m/s)", bg="#99ccff").place(x=90, y=550)
velScale = Scale(root, bd=0, from_=0, to=750, orient="horizontal", length=150, command=selectVel) #slider
velScale.pack()
velScale.place(x=55, y=575)


root.mainloop()

