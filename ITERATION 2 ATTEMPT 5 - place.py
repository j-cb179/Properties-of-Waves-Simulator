#tkinter main window creation code
from tkinter import *
from tkinter.tix import *
root = Tk()
root.title("Iteration 2")
root.configure(background="grey")
root.state('zoomed') #fits monitor size

#declaring global variables
wlVAR = 0.0 #wavelength
velVAR = 0.0 #velocity
freqVAR = 0.0 #frequency
ampVAR = 0.0 #amplitude
period = 0.0 #period

#tooltips
indTip = Balloon(root)

#tkinter canvas'
mCanvas = Canvas(root, height=root.winfo_screenheight() * (78/100) , width=root.winfo_screenwidth() * (20/100), bg="light grey")
mCanvas.place(x= (root.winfo_screenwidth() * (5/100)), y= (root.winfo_screenheight() * (10/100)) )

presetCan = Canvas(root, height=root.winfo_screenheight() * (32/100), width=root.winfo_screenwidth() * (20/100), bg="light grey")
presetCan.place(x= root.winfo_screenwidth() * (70/100), y=root.winfo_screenheight() * (56/100) )

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
        if wlUnit.get() == "m":
            wlEntry.config(state=NORMAL)
            wlEntry.delete(0, END)
            wlEntry.insert(0, wlVAR)
            wlEntry.config(state=DISABLED)
        elif wlUnit.get() == "nm":
            wlEntry.config(state=NORMAL)
            wlEntry.delete(0, END)
            wlEntry.insert(0, (wlVAR *(10**9)) )
            wlEntry.config(state=DISABLED)
        else:
            wlEntry.config(state=NORMAL)
            wlEntry.delete(0, END)
            wlEntry.insert(0, (wlVAR *(10**6)) )
            wlEntry.config(state=DISABLED)
    elif varNonSelect.get() == "Vel":
        velEntry.config(state=NORMAL)
        velEntry.delete(0, END)
        velEntry.insert(0, velVAR)
        velEntry.config(state=DISABLED)
    elif varNonSelect.get() == "Freq":
        freqEntry.config(state=NORMAL)
        freqEntry.delete(0, END)
        freqEntry.insert(0, freqVAR)
        freqEntry.config(state=DISABLED)

def SelectGrayedInput():
    global varNonSelect
    if varNonSelect.get() == "Freq":
        freqEntry.config(state=DISABLED)
        wlEntry.config(state=NORMAL)
        velEntry.config(state=NORMAL)
        Output()
    elif varNonSelect.get() == "Vel":
        velEntry.config(state=DISABLED)
        wlEntry.config(state=NORMAL)
        freqEntry.config(state=NORMAL)
        Output()
    elif varNonSelect.get() == "Wl":
        wlEntry.config(state=DISABLED)
        freqEntry.config(state=NORMAL)
        velEntry.config(state=NORMAL)
        Output()

def SelectWaveInput():
    global radioButtonSelect
    if radioButtonSelect.get() == "Red":
        freqEntry.config(state=NORMAL)
        wlEntry.config(state=NORMAL)
        velEntry.config(state=NORMAL)
        wlNano.select()
        velSelectRB.select()
        wlEntry.delete(0, END)
        freqEntry.delete(0, END)
        velEntry.delete(0, END)
        wlEntry.insert(0, 700)
        freqEntry.insert(0, 428274940000000)
        velEntry.insert(0, 299792458)
        freqEntry.config(state=NORMAL)
        wlEntry.config(state=NORMAL)
        velEntry.config(state=DISABLED)
        
    elif radioButtonSelect.get() == "Blue":
        freqEntry.config(state=NORMAL)
        wlEntry.config(state=NORMAL)
        velEntry.config(state=NORMAL)
        wlNano.select()
        velSelectRB.select()
        wlEntry.delete(0, END)
        freqEntry.delete(0, END)
        velEntry.delete(0, END)
        wlEntry.insert(0, 460)
        freqEntry.insert(0, 651722734782609)
        velEntry.insert(0, 299792458)
        freqEntry.config(state=NORMAL)
        wlEntry.config(state=NORMAL)
        velEntry.config(state=DISABLED)
        
    elif radioButtonSelect.get() == "Micro":
        print("micro")
        
    elif radioButtonSelect.get() == "Gamma":
        print("gamma")
        
    elif radioButtonSelect.get() == "Custom":
        freqEntry.config(state=NORMAL)
        wlEntry.config(state=NORMAL)
        velEntry.config(state=NORMAL)
        wlMeter.select()
        freqSelectRB.select()
        wlEntry.delete(0, END)
        freqEntry.delete(0, END)
        velEntry.delete(0, END)
        wlEntry.insert(0, 0.0)
        freqEntry.insert(0, 0.0)
        velEntry.insert(0, 0.0)
        freqEntry.config(state=DISABLED)
        wlEntry.config(state=NORMAL)
        velEntry.config(state=NORMAL)


#Radiobutton Select Variable
varNonSelect = StringVar()
wlSelectRB = Radiobutton(root, variable=varNonSelect, value="Wl", bg="light grey", activebackground="light grey", command=SelectGrayedInput)#button for selecting wavelength
velSelectRB = Radiobutton(root, variable=varNonSelect, value="Vel", bg="light grey", activebackground="light grey", command=SelectGrayedInput)#button for selecting velocity
freqSelectRB = Radiobutton(root, variable=varNonSelect, value="Freq", bg="light grey", activebackground="light grey", command=SelectGrayedInput)#button for selecting frequency

wlSelectRB.place(x= root.winfo_screenwidth() *(8/100), y= root.winfo_screenheight() * (16.25/100) )
velSelectRB.place(x= root.winfo_screenwidth() *(8/100), y= root.winfo_screenheight() * (28.75/100) )
freqSelectRB.place(x= root.winfo_screenwidth() *(8/100), y= root.winfo_screenheight() * (41.25/100) )
freqSelectRB.select()

indTip.bind_widget(wlSelectRB, balloonmsg="Set wavelength as the dependant variable")
indTip.bind_widget(velSelectRB, balloonmsg="Set velocity as the dependant variable")
indTip.bind_widget(freqSelectRB, balloonmsg="Set frequency as the dependant variable")

#wavelength
wlEntryVAR = StringVar()
wlLabel = Label(root, text='Wavelength', bg="light grey")
wlLabel.place(x= root.winfo_screenwidth() * (13/100), y= root.winfo_screenheight() * (12.5/100) )
wlEntry = Entry(root, bd="1", relief="solid", textvariable= wlEntryVAR)#entry box
wlEntry.place(x= root.winfo_screenwidth() * (11.5/100), y= root.winfo_screenheight() * (16.5/100) )
wlEntryVAR.trace_add("write", callback=getWl)#constantly updating edits to wlVAR (wlEntry input)
#wavelength radiobuttons
wlUnit = StringVar() #designating wlUnit as variable for radio buttons
wlMeter = Radiobutton(root, text="m", variable=wlUnit, value="m", bg="light grey", activebackground="light grey")#button for 'm'
wlMicro = Radiobutton(root, text="μm", variable=wlUnit, value="μm", bg="light grey", activebackground="light grey")#button for 'μm'
wlNano = Radiobutton(root, text="nm", variable=wlUnit, value="nm", bg="light grey", activebackground="light grey") #button for 'nm'
wlMeter.place(x= root.winfo_screenwidth() *(10/100), y= root.winfo_screenheight() * (20/100) )
wlMicro.place(x= root.winfo_screenwidth() *(13.5/100), y= root.winfo_screenheight() * (20/100) )
wlNano.place(x= root.winfo_screenwidth() *(17/100), y= root.winfo_screenheight() * (20/100) )
wlMeter.select()#default select when open program
wlUnit.trace_add("write", callback=getWl)#constantly updating edits to wlUnit (changes to radiobuttons)


#velocity input
velEntryVAR = StringVar()
velLabel = Label(root, text="Velocity (m/s)", bg="light grey")
velLabel.place(x= (root.winfo_screenwidth() * (12.75/100)), y= (root.winfo_screenheight() * (25/100)) )
velEntry = Entry(root, bd="1", relief="solid", textvariable= velEntryVAR)#entry box
velEntry.place(x= root.winfo_screenwidth() * (11.5/100), y= root.winfo_screenheight() * (29/100) )
velEntryVAR.trace_add("write", callback=getVel)#constantly updating edits to velVAR (velEntry input)


#frequency input
freqEntryVAR = StringVar()
freqLabel = Label(root, text="Frequency (Hz)", bg="light grey")
freqLabel.place(x= (root.winfo_screenwidth() * (12.75/100)), y= (root.winfo_screenheight() * (37.5/100)) )#label
freqEntry = Entry(root, bd="1", relief="solid", textvariable= freqEntryVAR)#entry box
freqEntry.place(x= root.winfo_screenwidth() * (11.5/100), y= root.winfo_screenheight() * (41.5/100) )
freqEntryVAR.trace_add("write", callback=getFreq)#constantly updating edits to freqVAR (freqEntry input)


#amplitude input
ampEntryVAR = StringVar()
ampLabel = Label(root, text="Amplitude", bg="light grey")
ampLabel.place(x= (root.winfo_screenwidth() * (13/100)), y= (root.winfo_screenheight() * (50/100)) )#label
ampEntry = Entry(root, bd="1", relief="solid", textvariable= ampEntryVAR)#entry box
ampEntry.place(x= root.winfo_screenwidth() * (11.5/100), y= root.winfo_screenheight() * (54/100) )
ampEntryVAR.trace_add("write", callback=getAmp)#constantly updating edits to ampVAR (ampEntry input)
#amplitude radiobuttons
ampUnit = StringVar() #designating ampUnit as variable for radio buttons
ampMeter = Radiobutton(root, text="m", variable=ampUnit, value="m", bg="light grey", activebackground="light grey")#button for 'm'
ampMilli = Radiobutton(root, text="mm", variable=ampUnit, value="mm", bg="light grey", activebackground="light grey")#button for 'mm'
ampMicro = Radiobutton(root, text="μm", variable=ampUnit, value="μm", bg="light grey", activebackground="light grey") #button for 'μm'
ampMeter.place(x= root.winfo_screenwidth() *(10/100), y= root.winfo_screenheight() * (57.5/100) )
ampMilli.place(x= root.winfo_screenwidth() *(13.5/100), y= root.winfo_screenheight() * (57.5/100) )
ampMicro.place(x= root.winfo_screenwidth() *(17/100), y= root.winfo_screenheight() * (57.5/100) )
ampMeter.select()#default select when open program
ampUnit.trace_add("write", callback=getAmp)#constantly updating edits to ampUnit (changes to radiobuttons)


#PRESETS BOX
preLabel = Label(root, text="WAVE PRESETS", bg="light grey", font= ('TkDefaultFont', 20))
preLabel.place(x= root.winfo_screenwidth() * (73.5/100), y= root.winfo_screenheight() * (58.5/100))

radioButtonSelect = StringVar()
redLightRadioB = Radiobutton(root, variable=radioButtonSelect, text="Red Light", value="Red", bg="light grey", activebackground="light grey", command=SelectWaveInput)
blueLightRadioB = Radiobutton(root, variable=radioButtonSelect, text="Blue Light",value="Blue", bg="light grey", activebackground="light grey", command=SelectWaveInput)
microWaveRadioB = Radiobutton(root, variable=radioButtonSelect, text="Microwave",value="Micro", bg="light grey", activebackground="light grey", command=SelectWaveInput)
gammaWaveRadioB = Radiobutton(root, variable=radioButtonSelect, text="Gamma ray",value="Gamma", bg="light grey", activebackground="light grey", command=SelectWaveInput)
customWaveRadioB = Radiobutton(root, variable=radioButtonSelect, text="Custom",value="Custom", bg="light grey", activebackground="light grey", command=SelectWaveInput)
customWaveRadioB.select()
redLightRadioB.place(x= root.winfo_screenwidth() * (75/100), y= root.winfo_screenheight() * (62.4/100) )
blueLightRadioB.place(x= root.winfo_screenwidth() * (75/100), y= root.winfo_screenheight() * (68.8/100) )
microWaveRadioB.place(x= root.winfo_screenwidth() * (75/100), y= root.winfo_screenheight() * (75.2/100) ) 
gammaWaveRadioB.place(x= root.winfo_screenwidth() * (75/100), y= root.winfo_screenheight() * (81.6/100) )
customWaveRadioB.place(x= root.winfo_screenwidth() * (82.5/100), y= root.winfo_screenheight() * (72/100) )


wlEntry.insert(0, 0.0)
velEntry.insert(0, 0.0)
freqEntry.insert(0, 0.0)
ampEntry.insert(0, 0.0)
SelectGrayedInput()

root.mainloop()
