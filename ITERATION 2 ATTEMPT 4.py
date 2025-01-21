from tkinter import *

#tkinter base code
root = Tk()
root.title("Wave Sim (iteration 1)")
root.configure(background="#99ccff")
root.state('zoomed')#fullscreens my program
canvas = Canvas(root, height=root.winfo_screenheight(), width= root.winfo_screenwidth(), bg="#99ccff")



#declaring global variables
wlVAR = 0.0 #wavelength
velVAR = 0.0 #velocity
freqVAR = 0.0 #frequency
ampVAR = 0.0 #amplitude
period = 0.0 #period


#canvas
canvas.create_rectangle(50, 100, 400, 700, outline="black", fill="white", width=5)#inputs box
canvas.pack()


waveCanvas = Canvas(root, height=700, width=800, bg="white", border=0)
print(waveCanvas.winfo_screenheight())
print(root.winfo_screenheight())
waveCanvas.place(x=600, y=150)
# Arcs for the wave visualisation
coord1 = 10, 10, 100, 600#1. left, 2. top, 3. right, 4.height
coord2 = 100, 0, 190, 600#1. left, 2. top, 3. right, 4.height
coord3 = 280, 10, 190, 600#1. left, 2. top, 3. right, 4.height
coord4 = 370, 0, 280, 600#1. left, 2. top, 3. right, 4.height
coord5 = 460, 10, 370, 600#1. left, 2. top, 3. right, 4.height
coord6 = 550, 0, 370, 600#1. left, 2. top, 3. right, 4.height
# Create the arc with extent=150
arc1 = waveCanvas.create_arc(coord1, start=0, extent=180, style=ARC)
arc2 = waveCanvas.create_arc(coord2, start=180, extent=180, style=ARC)
arc3 = waveCanvas.create_arc(coord3, start=0, extent=180, style=ARC)
arc4 = waveCanvas.create_arc(coord4, start=180, extent=180, style=ARC)
arc5 = waveCanvas.create_arc(coord5, start=0, extent=180, style=ARC)
arc6 = waveCanvas.create_arc(coord6, start=180, extent=180, style=ARC)


def getWl(var, index, mode):#whenever edit to wavelength input occurs ("write" trace)
    global wlVAR
    global wlUnit
    wlVAR = float(wlEntryVAR.get())
    if wlUnit.get() == "m":#check radiobutton value
        print(wlVAR)
        print(wlUnit.get())
        root.after(0, wlCalculation())
    elif wlUnit.get() == "nm":#check radiobutton value
        print(wlVAR)
        print(wlUnit.get())
        wlVAR = float(wlVAR / 1000000000)#convert wl to correct unit for calculation (m)
        print(str(wlVAR)+"m")
        root.after(0, wlCalculation())
    else:#check radiobutton value
        print(wlVAR)
        print(wlUnit.get())
        wlVAR = float(wlVAR / 1000000)#convert wl to correct unit for calculation (m)
        print(str(wlVAR)+"m")
        root.after(0, wlCalculation())

def getVel(var, index, mode):#whenever edit to velocity input occurs ("write" trace)
    global velVAR
    global velUnit
    velVAR = float(velEntryVAR.get())
    print(velVAR)
    root.after(0, velCalculation())

def getFreq(var, index, mode):#whenever edit to frequency input occurs ("write" trace)
    global freqVAR
    global freqUnit
    freqVAR = float(freqEntryVAR.get())
    print(freqVAR)
    root.after(0, freqCalculation())

def getAmp(var, index, mode):#whenever edit to amplitude input occurs ("write" trace)
    global ampVAR
    global ampUnit
    ampVAR = float(ampEntryVAR.get())
    if ampUnit.get() == "m":#check radiobutton value
        print(ampVAR)
        print(ampUnit.get())
    elif ampUnit.get() == "mm":#check radiobutton value
        print(ampVAR)
        print(ampUnit.get())
        ampVAR = float(ampVAR / 1000)#convert amplitude to correct unit for calculation (m)
        print(str(ampVAR)+"m")
    else:#check radiobutton value
        print(ampVAR)
        print(ampUnit.get())
        ampVAR = float(ampVAR / 1000000)#convert amplitude to correct unit for calculation (m)
        print(str(ampVAR)+"m")
 

def wlCalculation():
    global wlVAR
    global velVAR
    global freqVAR
    if varNonSelect.get() == "Freq":
        freqVAR = velVAR / wlVAR
        period = float(1 / freqVAR)
        root.after(0, Output())
    elif varNonSelect.get() == "Vel":
        velVAR = wlVAR * freqVAR
        period = float(1 / freqVAR)
        root.after(0, Output())
        
    
def velCalculation():
    global wlVAR
    global velVAR
    global freqVAR
    if varNonSelect.get() == "Wl":
        wlVAR = velVAR / freqVAR
        period = float(1 / freqVAR)
        root.after(0, Output())
    elif varNonSelect.get() == "Freq":
        freqVAR  = velVAR/wlVAR
        period = float(1 / freqVAR)
        root.after(0, Output())
    

def freqCalculation():
    global wlVAR
    global velVAR
    global freqVAR
    if varNonSelect.get() == "Wl":
        wlVAR = velVAR / freqVAR
        period = float(1 / freqVAR)
        root.after(0, Output())
    elif varNonSelect.get() == "Freq":
        velVAR = wlVAR * freqVAR
        period = float(1 / freqVAR)
        root.after(0, Output())


def Output():
    global wlVAR
    global velVAR
    global freqVAR
    global period
    print(wlVAR)
    print(velVAR)
    print(freqVAR)
    print(period)
    if varNonSelect.get() == "Wl":
        wlEntry.config(state=NORMAL)
        wlEntry.delete(0, len(wlEntry.get()))
        wlEntry.insert(0, wlVAR)
        wlEntry.config(state=DISABLED)
    elif varNonSelect.get() == "Vel":
        velEntry.config(state=NORMAL)
        velEntry.delete(0, len(velEntry.get()))
        velEntry.insert(0, velVAR)
        velEntry.config(state=DISABLED)
    elif varNonSelect.get() == "Freq":
        freqEntry.config(state=NORMAL)
        freqEntry.delete(0, len(freqEntry.get()))
        freqEntry.insert(0, freqVAR)
        freqEntry.config(state=DISABLED)

def SelectGrayedInput():
    global varNonSelect
    if varNonSelect.get() == "Freq":
        freqEntry.config(state=DISABLED)
        wlEntry.config(state=NORMAL)
        velEntry.config(state=NORMAL)
        Output()
    if varNonSelect.get() == "Vel":
        velEntry.config(state=DISABLED)
        wlEntry.config(state=NORMAL)
        freqEntry.config(state=NORMAL)
        Output()
    if varNonSelect.get() == "Wl":
        wlEntry.config(state=DISABLED)
        freqEntry.config(state=NORMAL)
        velEntry.config(state=NORMAL)
        Output()

#Radiobutton Select Variable
varNonSelect = StringVar()
wlSelectRB = Radiobutton(root, variable=varNonSelect, value="Wl", bg="white", activebackground="white", command=SelectGrayedInput)#button for selecting wavelength
velSelectRB = Radiobutton(root, variable=varNonSelect, value="Vel", bg="white", activebackground="white", command=SelectGrayedInput)#button for selecting velocity
freqSelectRB = Radiobutton(root, variable=varNonSelect, value="Freq", bg="white", activebackground="white", command=SelectGrayedInput)#button for selecting frequency
wlSelectRB.place(x=120, y=190)
velSelectRB.place(x=120, y=290)
freqSelectRB.place(x=120, y=390)
freqSelectRB.select()#default select when open program

#wavelength input
wlEntryVAR = StringVar()
wlLabel = Label(root, text="Wavelength", bg="white").place(x=150, y=175)#label
wlEntry = Entry(root, bd="2", relief="solid", textvariable= wlEntryVAR)#entry box
wlEntry.place(x=150, y=200)
wlEntryVAR.trace_add("write", callback=getWl)#constantly updating edits to wlVAR (wlEntry input)

#wavelength radiobuttons
wlUnit = StringVar() #designating wlUnit as variable for radio buttons
wlMeter = Radiobutton(root, text="m", variable=wlUnit, value="m", bg="white", activebackground="white")#button for 'm'
wlMicro = Radiobutton(root, text="μm", variable=wlUnit, value="μm", bg="white", activebackground="white")#button for 'μm'
wlNano = Radiobutton(root, text="nm", variable=wlUnit, value="nm", bg="white", activebackground="white") #button for 'nm'
wlMeter.place(x=140, y=225)
wlMicro.place(x=190, y=225)
wlNano.place(x=240, y=225)
wlMeter.select()#default select when open program
wlUnit.trace_add("write", callback=getWl)#constantly updating edits to wlUnit (changes to radiobuttons)


#velocity input
velEntryVAR = StringVar()
velLabel = Label(root, text="Velocity (m/s)", bg="white").place(x=150, y=275)#label
velEntry = Entry(root, bd="2", relief="solid", textvariable= velEntryVAR)#entry box
velEntry.place(x=150, y=300)
velEntryVAR.trace_add("write", callback=getVel)#constantly updating edits to velVAR (velEntry input)


#frequency input
freqEntryVAR = StringVar()
freqLabel = Label(root, text="Frequency (Hz)", bg="white").place(x=150, y=375)#label
freqEntry = Entry(root, bd="2", relief="solid", textvariable= freqEntryVAR)#entry box
freqEntry.place(x=150, y=400)
freqEntryVAR.trace_add("write", callback=getFreq)#constantly updating edits to freqVAR (freqEntry input)


#amplitude input
ampEntryVAR = StringVar()
ampLabel = Label(root, text="Amplitude", bg="white").place(x=150, y=475)#label
ampEntry = Entry(root, bd="2", relief="solid", textvariable= ampEntryVAR)#entry box
ampEntry.place(x=150, y=500)
ampEntryVAR.trace_add("write", callback=getAmp)#constantly updating edits to ampVAR (ampEntry input)

#amplitude radiobuttons
ampUnit = StringVar() #designating ampUnit as variable for radio buttons
ampMeter = Radiobutton(root, text="m", variable=ampUnit, value="m", bg="white", activebackground="white")#button for 'm'
ampMilli = Radiobutton(root, text="mm", variable=ampUnit, value="mm", bg="white", activebackground="white")#button for 'mm'
ampMicro = Radiobutton(root, text="μm", variable=ampUnit, value="μm", bg="white", activebackground="white") #button for 'μm'
ampMeter.place(x=140, y=525)
ampMilli.place(x=190, y=525)
ampMicro.place(x=240, y=525)
ampMeter.select()#default select when open program
ampUnit.trace_add("write", callback=getAmp)#constantly updating edits to ampUnit (changes to radiobuttons)

wlEntry.insert(0, 0.0)
velEntry.insert(0, 0.0)
freqEntry.insert(0, 0.0)
SelectGrayedInput()
root.mainloop()

