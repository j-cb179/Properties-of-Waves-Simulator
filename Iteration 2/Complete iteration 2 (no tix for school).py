from tkinter import *
import numpy as np
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)
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
    WaveGraph, wGraph = plt.subplots() #creates matplotlib Figure and an array of axes that the program can plot points on
    WaveGraph.set_figheight( (root.winfo_screenheight()/180) ) #sizes graph to window size
    WaveGraph.set_figwidth( (root.winfo_screenwidth()/120) ) #sizes graph to window size
    wGraph.set_ylabel("Amplitude (m)") # y axis title
    wGraph.set_xlabel("Time (s)") # x axis title
        
    if waveCanvas: waveCanvas.get_tk_widget().pack_forget() #replaces previous graph when new variables are used and new graph formed
    waveCanvas = FigureCanvasTkAgg(WaveGraph, master = waveFrame) #creates graph inside figure that can be embedded in tkinter
    waveCanvas.get_tk_widget().pack()
    wGraph.set_ylim(-(ampVAR+2), (ampVAR+2)) #sets the limits of the y-axis to be slightly greater than the amplitude of the wave
  
    def animation_fig(frame):
        global wlVAR
        global velVAR
        global ampVAR
        x = np.linspace(frame * velVAR, (frame +10) *velVAR, 800) #num1 = start point, num2 = end point, num3 = no. of generated coords
        y = ( np.sin(2*np.pi / wlVAR * x) *ampVAR) # y co-ordinates, models wave as sine wave
        sineWave.set_data(x, y) #sineWave is the name given to the line created by plotting the x and y variables
        wGraph.set_xlim(x.min(), x.max()) #sets a limit on the x-axis on either side of the created line to create an illusion of scrolling movement
        return sineWave, #the comma returns the full tuple with the sineWave variable included within it

    #The init function is the initialisation of the graph for each frame of animation to be placed on top of.
    def anim_init():
        sineWave.set_data([], [])#this sets the x and y values of anything plotted on the graph to blank to clear the graph
        return sineWave, #returns these empty values to the FuncAnimation function
    
    sineWave, = wGraph.plot([], []) #clears the plotted points of the graph ready to have the next set of points plotted
    animate = FuncAnimation(WaveGraph, animation_fig, init_func=anim_init, blit=True, interval=50 ) #animates the graph
    waveCanvas.draw() #draws the FuncAnimation onto the graph in the tkinter window


def getWl(var, index, mode):#whenever edit to wavelength input occurs ("write" trace)
    global wlVAR
    global wlUnit
    wlVAR = float(wlEntryVAR.get()) #value of wlEntry box
    if wlUnit.get() == "m":#check radiobutton value
        print(wlVAR)
        print(wlUnit.get())#prints unit alongside value to console
        wlCalculation()
    elif wlUnit.get() == "nm":#check radiobutton value
        print(wlVAR)
        print(wlUnit.get())
        wlVAR = float(wlVAR / 1000000000)#convert wl to correct unit for calculation (m)
        print(str(wlVAR)+"m")#prints wavelength as seen as in metres to console 
        wlCalculation()
    else:#check radiobutton value
        print(wlVAR)
        print(wlUnit.get())
        wlVAR = float(wlVAR / 1000000)#convert wl to correct unit for calculation (m)
        print(str(wlVAR)+"m")#prints wavelength as seen as in metres to console
        wlCalculation()


def getVel(var, index, mode):#whenever edit to velocity input occurs ("write" trace)
    global velVAR
    global gVelVAR
    velVAR = float(velEntryVAR.get())#value of velEntry
    print(velVAR)
    velCalculation()


def getFreq(var, index, mode):#whenever edit to frequency input occurs ("write" trace)
    global freqVAR
    global gFreqVAR
    freqVAR = float(freqEntryVAR.get())#value of freqEntry
    print(freqVAR)
    freqCalculation()


def getAmp(var, index, mode):#whenever edit to amplitude input occurs ("write" trace)
    global ampVAR
    global ampUnit
    ampVAR = float(ampEntryVAR.get()) #value of ampEntry
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
        print("Dependent Variable Error has occured") #defensive design


def velCalculation():
    global wlVAR
    global velVAR
    global freqVAR
    global period
    if varNonSelect.get() == "Wl":
        wlVAR = velVAR / freqVAR #Use of the wl = vel / freq to find frequency
        period = float(1 / freqVAR) #Use of the period = 1 / frequency to find period
        Output()
    elif varNonSelect.get() == "Freq":
        freqVAR  = velVAR/wlVAR #Use of the wl = vel / freq to find frequency
        period = float(1 / freqVAR) #Use of the period = 1 / frequency to find period
        Output()
    else:
        print("Dependent Variable Error has occured") #defensive design
    

def freqCalculation():
    global wlVAR
    global velVAR
    global freqVAR
    global period
    if varNonSelect.get() == "Wl":
        wlVAR = velVAR / freqVAR #Use of the wl = vel / freq to find frequency
        period = float(1 / freqVAR) #Use of the period = 1 / frequency to find period
        Output()
    elif varNonSelect.get() == "Vel":
        velVAR = wlVAR * freqVAR #Use of the wl = vel / freq to find frequency
        period = float(1 / freqVAR) #Use of the period = 1 / frequency to find period
        Output()
    else:
        print("Dependent Variable Error has occured") #defensive design


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
    
    if varNonSelect.get() == "Wl": #check if wl is the dependent variable
        if wlUnit.get() == "m": #get to see wl unit
            wlEntry.config(state=NORMAL)
            wlEntry.delete(0, END) #empty wavelength entry box
            wlEntry.insert(0, wlVAR) #fill wavelength entry box with calculated variable
            wlEntry.config(state=DISABLED)
            PlotGraph()
        elif wlUnit.get() == "nm": #get to see wl unit
            wlEntry.config(state=NORMAL)
            wlEntry.delete(0, END) #empty wavelength entry box
            wlEntry.insert(0, (wlVAR *(10**9)) ) #fill wavelength entry box with calculated variable
            wlEntry.config(state=DISABLED)
            PlotGraph()
        else: #get to see wl unit
            wlEntry.config(state=NORMAL)
            wlEntry.delete(0, END) #empty wavelength entry box
            wlEntry.insert(0, (wlVAR *(10**6)) ) #fill wavelength entry box with calculated variable
            wlEntry.config(state=DISABLED)
            PlotGraph()
    elif varNonSelect.get() == "Vel": #check if vel is the dependent variable
        velEntry.config(state=NORMAL)
        velEntry.delete(0, END) #empty velocity entry box
        velEntry.insert(0, velVAR) #fill velocity entry box with calculated variable
        velEntry.config(state=DISABLED)
        PlotGraph()
    elif varNonSelect.get() == "Freq": #check if freq is the dependent variable
        freqEntry.config(state=NORMAL)
        freqEntry.delete(0, END) #empty frequency entry box
        freqEntry.insert(0, freqVAR) #fill frequency entry box with calculated variable
        freqEntry.config(state=DISABLED)
        PlotGraph()
    else:
        print("Output error has occured")#defensive design
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
        ampMeter.select()
        freqSelectRB.select()
        wlEntry.delete(0, END)
        freqEntry.delete(0, END)
        velEntry.delete(0, END)
        ampEntry.delete(0, END)
        wlEntry.insert(0, 700)
        velEntry.insert(0, 299792458)
        ampEntry.insert(0, 1.0)
        freqEntry.config(state=DISABLED)
        wlEntry.config(state=NORMAL)
        velEntry.config(state=NORMAL)
        wlNano.select()
        
    elif radioButtonSelect.get() == "Blue":
        freqEntry.config(state=NORMAL)
        wlEntry.config(state=NORMAL)
        velEntry.config(state=NORMAL)
        ampMeter.select()
        freqSelectRB.select()
        wlEntry.delete(0, END)
        freqEntry.delete(0, END)
        velEntry.delete(0, END)
        ampEntry.delete(0, END)
        wlEntry.insert(0, 460)
        velEntry.insert(0, 299792458)
        ampEntry.insert(0, 1.0)
        freqEntry.config(state=DISABLED)
        wlEntry.config(state=NORMAL)
        velEntry.config(state=NORMAL)
        wlNano.select()
        
    elif radioButtonSelect.get() == "Micro":
        freqEntry.config(state=NORMAL)
        wlEntry.config(state=NORMAL)
        velEntry.config(state=NORMAL)
        ampMeter.select()
        freqSelectRB.select()
        wlEntry.delete(0, END)
        freqEntry.delete(0, END)
        velEntry.delete(0, END)
        ampEntry.delete(0, END)
        wlEntry.insert(0, 1000)
        velEntry.insert(0, 299792458)
        ampEntry.insert(0, 1.0)
        freqEntry.config(state=DISABLED)
        wlEntry.config(state=NORMAL)
        velEntry.config(state=NORMAL)
        wlMicro.select()
        
    elif radioButtonSelect.get() == "Gamma":
        print("gamma")
        freqEntry.config(state=NORMAL)
        wlEntry.config(state=NORMAL)
        velEntry.config(state=NORMAL)
        ampMeter.select()
        freqSelectRB.select()
        wlEntry.delete(0, END)
        freqEntry.delete(0, END)
        velEntry.delete(0, END)
        ampEntry.delete(0, END)
        wlEntry.insert(0, 0.005)
        velEntry.insert(0, 299792458)
        ampEntry.insert(0, 1.0)
        freqEntry.config(state=DISABLED)
        wlEntry.config(state=NORMAL)
        velEntry.config(state=NORMAL)
        wlNano.select()
        
    elif radioButtonSelect.get() == "Custom":
        freqEntry.config(state=NORMAL)
        wlEntry.config(state=NORMAL)
        velEntry.config(state=NORMAL)
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
        wlMeter.select()


#Radiobutton Select Variable
varNonSelect = StringVar()
wlSelectRB = Radiobutton(root, variable=varNonSelect, value="Wl", bg="light grey", activebackground="light grey", command=SelectGrayedInput)#button for selecting wavelength
velSelectRB = Radiobutton(root, variable=varNonSelect, value="Vel", bg="light grey", activebackground="light grey", command=SelectGrayedInput)#button for selecting velocity
freqSelectRB = Radiobutton(root, variable=varNonSelect, value="Freq", bg="light grey", activebackground="light grey", command=SelectGrayedInput)#button for selecting frequency

wlSelectRB.place(x= root.winfo_screenwidth() *(8/100), y= root.winfo_screenheight() * (16.25/100) )
velSelectRB.place(x= root.winfo_screenwidth() *(8/100), y= root.winfo_screenheight() * (28.75/100) )
freqSelectRB.place(x= root.winfo_screenwidth() *(8/100), y= root.winfo_screenheight() * (41.25/100) )
freqSelectRB.select()

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
redLightRadioB = Radiobutton(root, variable=radioButtonSelect, text="Red Light", value="Red", bg="light grey", activebackground="light grey", command=SelectWaveInput) #radiobutton
blueLightRadioB = Radiobutton(root, variable=radioButtonSelect, text="Blue Light",value="Blue", bg="light grey", activebackground="light grey", command=SelectWaveInput) #radiobutton
microWaveRadioB = Radiobutton(root, variable=radioButtonSelect, text="Microwave",value="Micro", bg="light grey", activebackground="light grey", command=SelectWaveInput) #radiobutton
gammaWaveRadioB = Radiobutton(root, variable=radioButtonSelect, text="Gamma ray",value="Gamma", bg="light grey", activebackground="light grey", command=SelectWaveInput) #radiobutton
customWaveRadioB = Radiobutton(root, variable=radioButtonSelect, text="Custom",value="Custom", bg="light grey", activebackground="light grey", command=SelectWaveInput) #radiobutton
customWaveRadioB.select() #select a button when program is run
redLightRadioB.place(x= root.winfo_screenwidth() * (75/100), y= root.winfo_screenheight() * (62.4/100) )
blueLightRadioB.place(x= root.winfo_screenwidth() * (75/100), y= root.winfo_screenheight() * (68.8/100) )
microWaveRadioB.place(x= root.winfo_screenwidth() * (75/100), y= root.winfo_screenheight() * (75.2/100) ) 
gammaWaveRadioB.place(x= root.winfo_screenwidth() * (75/100), y= root.winfo_screenheight() * (81.6/100) )
customWaveRadioB.place(x= root.winfo_screenwidth() * (82.5/100), y= root.winfo_screenheight() * (72/100) )


wlOutEntry = Entry(root, bd="1", relief="solid") #entry box creation
wlOutEntry.place(x= root.winfo_screenwidth() * (32.5/100), y= root.winfo_screenheight() * (61.35/100))
ampOutEntry = Entry(root, bd="1", relief="solid") #entry box creation
ampOutEntry.place(x= root.winfo_screenwidth() * (32.5/100), y= root.winfo_screenheight() * (72.05/100))
velOutEntry = Entry(root, bd="1", relief="solid") #entry box creation
velOutEntry.place(x= root.winfo_screenwidth() * (32.5/100), y= root.winfo_screenheight() * (82.75/100))
freqOutEntry = Entry(root, bd="1", relief="solid") #entry box creation
freqOutEntry.place(x= root.winfo_screenwidth() * (47.5/100), y= root.winfo_screenheight() * (61.35/100))
energyOutEntry = Entry(root, bd="1", relief="solid") #entry box creation
energyOutEntry.place(x= root.winfo_screenwidth() * (47.5/100), y= root.winfo_screenheight() * (72.05/100))
periodOutEntry = Entry(root, bd="1", relief="solid") #entry box creation
periodOutEntry.place(x= root.winfo_screenwidth() * (47.5/100), y= root.winfo_screenheight() * (82.75/100))

wlOutLabel= Label(root, text="Wavelength (m)", bg="light grey") #label creation
wlOutLabel.place(x= root.winfo_screenwidth() * (39/100), y= root.winfo_screenheight() * (61.35/100))
ampOutLabel= Label(root, text="Amplitude (m)", bg="light grey") #label creation
ampOutLabel.place(x= root.winfo_screenwidth() * (39/100), y= root.winfo_screenheight() * (72.05/100))
velOutLabel= Label(root, text="Velocity (m/s)", bg="light grey") #label creation
velOutLabel.place(x= root.winfo_screenwidth() * (39/100), y= root.winfo_screenheight() * (82.75/100))
freqOutLabel= Label(root, text="Frequency (Hz)", bg="light grey") #label creation
freqOutLabel.place(x= root.winfo_screenwidth() * (54/100), y= root.winfo_screenheight() * (61.35/100))
energyOutLabel= Label(root, text="Photon Energy (eV)", bg="light grey") #label creation
energyOutLabel.place(x= root.winfo_screenwidth() * (54/100), y= root.winfo_screenheight() * (72.05/100))
periodOutLabel= Label(root, text="Period (s)", bg="light grey") #label creation
periodOutLabel.place(x= root.winfo_screenwidth() * (54/100), y= root.winfo_screenheight() * (82.75/100))


wlEntry.insert(0, 10.0)
velEntry.insert(0, 1.0)
freqEntry.insert(0, 0.0)
ampEntry.insert(0, 1.0)
SelectGrayedInput()


root.mainloop()
