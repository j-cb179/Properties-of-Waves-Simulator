#tkinter main window creation code
from tkinter import *
import numpy as np
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)
from tkinter.tix import *
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt


root = Tk()
root.title("Iteration 2")
root.configure(background="grey")
root.state('zoomed') #fits monitor size
waveFrame = Frame(root)
waveFrame.place(x= root.winfo_screenwidth() * (30/100), y= root.winfo_screenheight() * (10/100) )

#declaring global variables
wlVAR = float(1.0) #wavelength
velVAR = float(1.0) #velocity
freqVAR = float(0.0) #frequency
ampVAR = float(1.0) #amplitude
period = float(0.0) #period
planck = float((6.62607015)*(10**-34))


#tooltips
tooltips = Balloon(root)


#tkinter canvas'
mCanvas = Canvas(root, height=root.winfo_screenheight() * (78/100) , width=root.winfo_screenwidth() * (20/100), bg="light grey")
mCanvas.place(x= (root.winfo_screenwidth() * (5/100)), y= (root.winfo_screenheight() * (10/100)) )

presetCanvas = Canvas(root, height=root.winfo_screenheight() * (32/100), width=root.winfo_screenwidth() * (20/100), bg="light grey")
presetCanvas.place(x= root.winfo_screenwidth() * (70/100), y=root.winfo_screenheight() * (56/100) )

infoCanvas = Canvas(root, height=root.winfo_screenheight() * (32/100), width=root.winfo_screenwidth() * (30/100), bg="light grey")
infoCanvas.place(x= root.winfo_screenwidth() * (30/100), y=root.winfo_screenheight() * (56/100) )

waveCanvas = None




def PlotGraph():
    global waveCanvas
    global wlVAR
    global ampVAR
    WaveGraph, wGraph = plt.subplots()
    wGraph.set_ylabel("Amplitude (m)")
    wGraph.set_xlabel("Time (s)")
    if waveCanvas: waveCanvas.get_tk_widget().pack_forget()
    waveCanvas = FigureCanvasTkAgg(WaveGraph, master = waveFrame)
    waveCanvas.get_tk_widget().pack()
    wGraph.set_ylim(-(ampVAR+2), (ampVAR+2))
  
    def animation_fig(frame):
        global wlVAR, velVAR, ampVAR
        x = np.linspace(frame * velVAR, (frame +10) *velVAR, 1000) #num1 = start point, num2 = end point, num3 = no. of generated coords
        y = ( np.sin(2*np.pi / wlVAR * x) *ampVAR) # y co-ordinates, models wave as sine wave
        sineWave.set_data(x, y)
        wGraph.set_xlim(x.min(), x.max())
        return sineWave,
    
    #The init function is the initialisation of the graph for each frame of animation to be placed on top of.
    def anim_init():
        sineWave.set_data([], [])#this sets the x and y values of anything plotted on the graph to blank to clear the graph
        return sineWave, #returns these empty values to the FuncAnimation function
    
    sineWave, = wGraph.plot([], [])
    animate = FuncAnimation(WaveGraph, animation_fig, init_func=anim_init, blit=True, interval=50 )
    waveCanvas.draw()


def getWl(var, index, mode):#whenever edit to wavelength input occurs ("write" trace)
    global wlVAR
    global wlUnit
    wlVAR = float(wlEntryVAR.get())
    if wlUnit.get() == "m":#check radiobutton value
        print(wlVAR)
        print(wlUnit.get())
        wlCalculation()
    elif wlUnit.get() == "nm":#check radiobutton value
        print(wlVAR)
        print(wlUnit.get())
        wlVAR = float(wlVAR / 1000000000)#convert wl to correct unit for calculation (m)
        print(str(wlVAR)+"m")
        wlCalculation()
    else:#check radiobutton value
        print(wlVAR)
        print(wlUnit.get())
        wlVAR = float(wlVAR / 1000000)#convert wl to correct unit for calculation (m)
        print(str(wlVAR)+"m")
        wlCalculation()


def getVel(var, index, mode):#whenever edit to velocity input occurs ("write" trace)
    global velVAR
    velVAR = float(velEntryVAR.get())
    print(velVAR)
    velCalculation()


def getFreq(var, index, mode):#whenever edit to frequency input occurs ("write" trace)
    global freqVAR
    freqVAR = float(freqEntryVAR.get())
    print(freqVAR)
    freqCalculation()


def getAmp(var, index, mode):#whenever edit to amplitude input occurs ("write" trace)
    global ampVAR
    global ampUnit
    ampVAR = float(ampEntryVAR.get())
    test = 1/ampVAR #Defensive design
    if ampUnit.get() == "m":#check radiobutton value
        print(ampVAR)
        print(ampUnit.get())
        Output()
    elif ampUnit.get() == "mm":#check radiobutton value
        print(ampVAR)
        print(ampUnit.get())
        ampVAR = float(ampVAR / 1000)#convert amplitude to correct unit for calculation (m)
        print(str(ampVAR)+"m")
        Output()
    else:#check radiobutton value
        print(ampVAR)
        print(ampUnit.get())
        ampVAR = float(ampVAR / 1000000)#convert amplitude to correct unit for calculation (m)
        print(str(ampVAR)+"m")
        Output()
 

def wlCalculation():
    global wlVAR
    global velVAR
    global freqVAR
    global period
    if varNonSelect.get() == "Freq":
        freqVAR = velVAR / wlVAR #Use of the wl = vel / freq to find frequency
        period = float(1 / freqVAR) #Use of the period = 1 / frequency to find period
        Output()
    elif varNonSelect.get() == "Vel":
        velVAR = wlVAR * freqVAR #use of the wl = vel / freq to find velocity
        period = float(1 / freqVAR) #use of period = 1 / frequency to find period
        Output()
    else:
        print("Math Error has occured")
    
    
def velCalculation():
    global wlVAR
    global velVAR
    global freqVAR
    global period
    if varNonSelect.get() == "Wl":
        wlVAR = velVAR / freqVAR
        period = float(1 / freqVAR)
        Output()
    elif varNonSelect.get() == "Freq":
        freqVAR  = velVAR/wlVAR
        period = float(1 / freqVAR)
        Output()
    else:
        print("Math Error has occured")
    

def freqCalculation():
    global wlVAR
    global velVAR
    global freqVAR
    global period
    if varNonSelect.get() == "Wl":
        wlVAR = velVAR / freqVAR
        period = float(1 / freqVAR)
        Output()
    elif varNonSelect.get() == "Vel":
        velVAR = wlVAR * freqVAR
        period = float(1 / freqVAR)
        Output()
    else:
        print("Math Error has occured")


def Output():
    global wlVAR
    global velVAR
    global freqVAR
    global period
    global planck
    energy = (planck * freqVAR)
    energy = (energy * (6.242*(10**18))) #convert from joules to electronvolts
    print(wlVAR)
    print(velVAR)
    print(freqVAR)
    print(period)
    
    wlOutEntry.config(state=NORMAL)
    wlOutEntry.delete(0, END)
    wlOutEntry.insert(0, wlVAR)
    wlOutEntry.config(state=DISABLED)
    
    ampOutEntry.config(state=NORMAL)
    ampOutEntry.delete(0, END)
    ampOutEntry.insert(0, ampVAR)
    ampOutEntry.config(state=DISABLED)
    
    velOutEntry.config(state=NORMAL)
    velOutEntry.delete(0, END)
    velOutEntry.insert(0, velVAR)
    velOutEntry.config(state=DISABLED)
    
    freqOutEntry.config(state=NORMAL)
    freqOutEntry.delete(0, END)
    freqOutEntry.insert(0, freqVAR)
    freqOutEntry.config(state=DISABLED)
    
    energyOutEntry.config(state=NORMAL)
    energyOutEntry.delete(0, END)
    energyOutEntry.insert(0, energy)
    energyOutEntry.config(state=DISABLED)
    
    periodOutEntry.config(state=NORMAL)
    periodOutEntry.delete(0, END)
    periodOutEntry.insert(0, period)
    periodOutEntry.config(state=DISABLED)
    
    if varNonSelect.get() == "Wl":
        if wlUnit.get() == "m":
            wlEntry.config(state=NORMAL)
            wlEntry.delete(0, END)
            wlEntry.insert(0, wlVAR)
            wlEntry.config(state=DISABLED)
            PlotGraph()
        elif wlUnit.get() == "nm":
            wlEntry.config(state=NORMAL)
            wlEntry.delete(0, END)
            wlEntry.insert(0, (wlVAR *(10**9)) )
            wlEntry.config(state=DISABLED)
            PlotGraph()
        else:
            wlEntry.config(state=NORMAL)
            wlEntry.delete(0, END)
            wlEntry.insert(0, (wlVAR *(10**6)) )
            wlEntry.config(state=DISABLED)
            PlotGraph()
    elif varNonSelect.get() == "Vel":
        velEntry.config(state=NORMAL)
        velEntry.delete(0, END)
        velEntry.insert(0, velVAR)
        velEntry.config(state=DISABLED)
        PlotGraph()
    elif varNonSelect.get() == "Freq":
        freqEntry.config(state=NORMAL)
        freqEntry.delete(0, END)
        freqEntry.insert(0, freqVAR)
        freqEntry.config(state=DISABLED)
        PlotGraph()
    else:
        print("Error has occured")
        PlotGraph()
        
    
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
        ampMeter.select()
        velSelectRB.select()
        wlEntry.delete(0, END)
        freqEntry.delete(0, END)
        velEntry.delete(0, END)
        ampEntry.delete(0, END)
        wlEntry.insert(0, 700)
        freqEntry.insert(0, 428274940000000)
        velEntry.insert(0, 299792458)
        ampEntry.insert(0, 1.0)
        freqEntry.config(state=NORMAL)
        wlEntry.config(state=NORMAL)
        velEntry.config(state=DISABLED)
        PlotGraph()
        
    elif radioButtonSelect.get() == "Blue":
        freqEntry.config(state=NORMAL)
        wlEntry.config(state=NORMAL)
        velEntry.config(state=NORMAL)
        wlNano.select()
        ampMeter.select()
        velSelectRB.select()
        wlEntry.delete(0, END)
        freqEntry.delete(0, END)
        velEntry.delete(0, END)
        ampEntry.delete(0, END)
        wlEntry.insert(0, 460)
        freqEntry.insert(0, 651722734782609)
        velEntry.insert(0, 299792458)
        ampEntry.insert(0, 1.0)
        freqEntry.config(state=NORMAL)
        wlEntry.config(state=NORMAL)
        velEntry.config(state=DISABLED)
        PlotGraph()
        
    elif radioButtonSelect.get() == "Micro":
        print("micro")
        freqEntry.config(state=NORMAL)
        wlEntry.config(state=NORMAL)
        velEntry.config(state=NORMAL)
        wlMicro.select()
        ampMeter.select()
        velSelectRB.select()
        wlEntry.delete(0, END)
        freqEntry.delete(0, END)
        velEntry.delete(0, END)
        ampEntry.delete(0, END)
        wlEntry.insert(0, 1000)
        freqEntry.insert(0, 299792458000)
        velEntry.insert(0, 299792458)
        ampEntry.insert(0, 1.0)
        freqEntry.config(state=NORMAL)
        wlEntry.config(state=NORMAL)
        velEntry.config(state=DISABLED)
        PlotGraph()
        
    elif radioButtonSelect.get() == "Gamma":
        print("gamma")
        freqEntry.config(state=NORMAL)
        wlEntry.config(state=NORMAL)
        velEntry.config(state=NORMAL)
        wlNano.select()
        ampMeter.select()
        velSelectRB.select()
        wlEntry.delete(0, END)
        freqEntry.delete(0, END)
        velEntry.delete(0, END)
        ampEntry.delete(0, END)
        wlEntry.insert(0, 0.005)
        freqEntry.insert(0, 59958491600000000000)
        velEntry.insert(0, 299792458)
        ampEntry.insert(0, 1.0)
        freqEntry.config(state=NORMAL)
        wlEntry.config(state=NORMAL)
        velEntry.config(state=DISABLED)
        PlotGraph()
        
    elif radioButtonSelect.get() == "Custom":
        freqEntry.config(state=NORMAL)
        wlEntry.config(state=NORMAL)
        velEntry.config(state=NORMAL)
        wlMeter.select()
        ampMeter.select()
        freqSelectRB.select()
        wlEntry.delete(0, END)
        freqEntry.delete(0, END)
        velEntry.delete(0, END)
        ampEntry.delete(0, END)
        wlEntry.insert(0, 10.0)
        velEntry.insert(0, 1.0)
        ampEntry.insert(0, 1.0)
        freqEntry.config(state=DISABLED)
        wlEntry.config(state=NORMAL)
        velEntry.config(state=NORMAL)
        PlotGraph()


#Radiobutton Select Variable
varNonSelect = StringVar()
wlSelectRB = Radiobutton(root, variable=varNonSelect, value="Wl", bg="light grey", activebackground="light grey", command=SelectGrayedInput)#button for selecting wavelength
velSelectRB = Radiobutton(root, variable=varNonSelect, value="Vel", bg="light grey", activebackground="light grey", command=SelectGrayedInput)#button for selecting velocity
freqSelectRB = Radiobutton(root, variable=varNonSelect, value="Freq", bg="light grey", activebackground="light grey", command=SelectGrayedInput)#button for selecting frequency

wlSelectRB.place(x= root.winfo_screenwidth() *(8/100), y= root.winfo_screenheight() * (16.25/100) )
velSelectRB.place(x= root.winfo_screenwidth() *(8/100), y= root.winfo_screenheight() * (28.75/100) )
freqSelectRB.place(x= root.winfo_screenwidth() *(8/100), y= root.winfo_screenheight() * (41.25/100) )
freqSelectRB.select()

tooltips.bind_widget(wlSelectRB, balloonmsg="Set wavelength as the dependant variable")
tooltips.bind_widget(velSelectRB, balloonmsg="Set velocity as the dependant variable")
tooltips.bind_widget(freqSelectRB, balloonmsg="Set frequency as the dependant variable")

#wavelength
wlEntryVAR = StringVar()
wlLabel = Label(root, text='Wavelength', bg="light grey")#label
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
velLabel = Label(root, text="Velocity (m/s)", bg="light grey")#label
velLabel.place(x= (root.winfo_screenwidth() * (12.75/100)), y= (root.winfo_screenheight() * (25/100)) )
velEntry = Entry(root, bd="1", relief="solid", textvariable= velEntryVAR)#entry box
velEntry.place(x= root.winfo_screenwidth() * (11.5/100), y= root.winfo_screenheight() * (29/100) )
velEntryVAR.trace_add("write", callback=getVel)#constantly updating edits to velVAR (velEntry input)


#frequency input
freqEntryVAR = StringVar()
freqLabel = Label(root, text="Frequency (Hz)", bg="light grey")#label
freqLabel.place(x= (root.winfo_screenwidth() * (12.75/100)), y= (root.winfo_screenheight() * (37.5/100)) )#label
freqEntry = Entry(root, bd="1", relief="solid", textvariable= freqEntryVAR)#entry box
freqEntry.place(x= root.winfo_screenwidth() * (11.5/100), y= root.winfo_screenheight() * (41.5/100) )
freqEntryVAR.trace_add("write", callback=getFreq)#constantly updating edits to freqVAR (freqEntry input)


#amplitude input
ampEntryVAR = StringVar()
ampLabel = Label(root, text="Amplitude", bg="light grey")#label
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


wlOutEntry = Entry(root, bd="1", relief="solid")
wlOutEntry.place(x= root.winfo_screenwidth() * (32.5/100), y= root.winfo_screenheight() * (61.35/100))
ampOutEntry = Entry(root, bd="1", relief="solid")
ampOutEntry.place(x= root.winfo_screenwidth() * (32.5/100), y= root.winfo_screenheight() * (72.05/100))
velOutEntry = Entry(root, bd="1", relief="solid")
velOutEntry.place(x= root.winfo_screenwidth() * (32.5/100), y= root.winfo_screenheight() * (82.75/100))
freqOutEntry = Entry(root, bd="1", relief="solid")
freqOutEntry.place(x= root.winfo_screenwidth() * (47.5/100), y= root.winfo_screenheight() * (61.35/100))
energyOutEntry = Entry(root, bd="1", relief="solid")
energyOutEntry.place(x= root.winfo_screenwidth() * (47.5/100), y= root.winfo_screenheight() * (72.05/100))
periodOutEntry = Entry(root, bd="1", relief="solid")
periodOutEntry.place(x= root.winfo_screenwidth() * (47.5/100), y= root.winfo_screenheight() * (82.75/100))

wlOutLabel= Label(root, text="Wavelength (m)", bg="light grey")
wlOutLabel.place(x= root.winfo_screenwidth() * (39/100), y= root.winfo_screenheight() * (61.35/100))
ampOutLabel= Label(root, text="Amplitude (m)", bg="light grey")
ampOutLabel.place(x= root.winfo_screenwidth() * (39/100), y= root.winfo_screenheight() * (72.05/100))
velOutLabel= Label(root, text="Velocity (m/s)", bg="light grey")
velOutLabel.place(x= root.winfo_screenwidth() * (39/100), y= root.winfo_screenheight() * (82.75/100))
freqOutLabel= Label(root, text="Frequency (Hz)", bg="light grey")
freqOutLabel.place(x= root.winfo_screenwidth() * (54/100), y= root.winfo_screenheight() * (61.35/100))
energyOutLabel= Label(root, text="Photon Energy (eV)", bg="light grey")
energyOutLabel.place(x= root.winfo_screenwidth() * (54/100), y= root.winfo_screenheight() * (72.05/100))
periodOutLabel= Label(root, text="Period (s)", bg="light grey")
periodOutLabel.place(x= root.winfo_screenwidth() * (54/100), y= root.winfo_screenheight() * (82.75/100))


wlEntry.insert(0, 10.0)
velEntry.insert(0, 1.0)
freqEntry.insert(0, 0.0)
ampEntry.insert(0, 1.0)
SelectGrayedInput()


root.mainloop()



