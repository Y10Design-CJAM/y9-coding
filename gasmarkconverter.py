import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Gas Mark Converter")
root.minsize(300, 300)
root.geometry("1000x700")

style = ttk.Style()
style.configure('TNotebook', tabposition='nw') #'nw' as in compass direction
# style.configure('lefttab.TNotebook', tabposition='ws')

# Create your variables to store data that is typed in by the user 
number1 = tk.StringVar()
number2 = tk.StringVar()
number3 = tk.StringVar()

# Helper Functions

def pressBtn1():
    num1 = (number1.get())
    result = (int(num1) * 14) + 121
    label2.config(text="Result is %d" % result + " ""°C")

def pressBtn2():
    num1 = (number1.get())
    result = (int(num1) * 25) + 250
    label2.config(text="Result is %d" % result + " ""°F")
def pressBtn3():
	num2 = (number2.get())
	result = (int(num2) - 121) / 14
	label4.config(text="Result is %d" % result + " ""Gas Marks")
def pressBtn4():
	num2 = (number2.get())
	result = (int(num2) * 9/5) + 32
	label4.config(text="Result is %d" % result + " ""°F")
def pressBtn5():
	num3 = (number3.get())
	result = (int(num3) - 250) / 25
	label6.config(text="Result is %d" % result + " ""Gas Marks")
def pressBtn6():
	num3 = (number3.get())
	result = (int(num3) - 32) * 5/9
	label6.config(text="Result is %d" % result + " ""°C")

planner = ttk.Notebook(root, width=1000, height=650)

# Create the frames of different colours that are 200*200 pixels in dimensions

######################################## Start Frame 1 ###################################

tab1 = tk.Frame(planner, bg='#EFEFEF', width=200, height=200)

label_1 = tk.Label (tab1,
	text="Gas Mark - is a temepature scale used on gas ovens in the United Kingdom, Ireland and some other Commonwealth countries")
label_1.config(font=("Courier", 13), bg='#EFEFEF', fg='Orange')
label_1.grid(row=1,column=2)
label_2 = tk.Label(tab1, text = 'Gas Mark Converter')
label_2.config(font=("Courier", 25), bg='#EFEFEF', fg='#2DC0DA')
label_2.grid(row=3,column=2)
label_3 = tk.Label(tab1, text = 'Gas Mark')
label_3.config(font=("Courier", 18), bg='#EFEFEF', fg='Orange')
label_3.grid(row=5,column=2)

# Here we create a label to tell the user what the answer is
label2 = tk.Label(tab1, text="Answer is:")
label2.config(font=("Courier", 14), bg='#EFEFEF', fg='Orange')
label2.grid(row=7, column=2)

# Here we create a textbox for data entry
# "number1" will store this information that will be used by the "pressBtn1" helper function
entryNum1 = tk.Entry(tab1, textvariable=number1)
entryNum1. grid(row=9,column=2)

# Here we create a button
button1 = tk.Button(tab1, text="Celsius", command = pressBtn1)
button1.config(font=("Courier", 15), fg='Orange')
button1.grid(row=10, column=2)

# Here we create another button
button2 = tk.Button(tab1, text="Fahrenheit", command = pressBtn2)
button2.config(font=("Courier", 15), fg='Orange')
button2.grid(row=11, column=2)

######################################## End Frame 1 ###################################

# These frames have not been implemented yet
tab2 = tk.Frame(planner, bg='#EFEFEF', width=200, height=200)
label_4 = tk.Label (tab2,
	text="Celsius - also known as the centrigrade system, is a temepature scale used by the International System of Units")
label_4.config(font=("Courier", 13), bg='#EFEFEF', fg='Orange')
label_4.grid(row=1,column=2)
label_5 = tk.Label(tab2, text = "Celsius Converter")
label_5.config(font=("Courier", 25), bg='#EFEFEF', fg='#2DC0DA')
label_5.grid(row=3,column=2)
label_6 = tk.Label(tab2, text = 'Celsius')
label_6.config(font=("Courier", 18), bg='#EFEFEF', fg='Orange')
label_6.grid(row=5,column=2)

label4 = tk.Label(tab2, text="Answer is:")
label4.config(font=("Courier", 14), bg='#EFEFEF', fg='Orange')
label4.grid(row=7,column=2)
entryNum2 = tk.Entry(tab2, textvariable=number2)
entryNum2.grid(row=9,column=2)

button3 = tk.Button(tab2, text="Gas Mark", command = pressBtn3)
button3.config(font=("Courier", 15), fg='Orange')
button3.grid(row=10,column=2)

button4 = tk.Button(tab2, text="Fahrenheit", command = pressBtn4)
button4.config(font=("Courier", 15), fg='Orange')
button4.grid(row=11,column=2)



tab3 = tk.Frame(planner, bg='#EFEFEF', width=200, height=200)
label_7 = tk.Label (tab3,
	text="Fahrenheit - is a temperature scale based on one proposed in 1724 by German physicist Daniel Gabriel Fahrenheit")
label_7.config(font=("Courier", 13), bg='#EFEFEF', fg='Orange')
label_7.grid(row=1,column=2)
label_8 = tk.Label(tab3, text = "Fahrenheit Converter")
label_8.config(font=("Courier", 25), bg='#EFEFEF', fg='#2DC0DA')
label_8.grid(row=3,column=2)
label_9 = tk.Label(tab3, text='Fahrenheit')
label_9.config(font=("Courier", 18), bg='#EFEFEF', fg='Orange')
label_9.grid(row=5,column=2)

label6 = tk.Label(tab3, text="Answer is:")
label6.config(font=("Courier", 14), bg='#EFEFEF', fg='Orange')
label6.grid(row=7,column=2)
entryNum3 = tk.Entry(tab3, textvariable=number3)
entryNum3.grid(row=9,column=2)

button5 = tk.Button(tab3, text="Gas Mark", command = pressBtn5)
button5.config(font=("Courier", 15), fg='Orange')
button5.grid(row=10,column=2)

button6 = tk.Button(tab3, text="Celsius", command = pressBtn6)
button6.config(font=("Courier", 15), fg='Orange')
button6.grid(row=11,column=2)


# Add the tabs/frames to the notebook object called "planner" 
# Referred to Stack Overflow for assistance

planner.add(tab1, text='Gas Marks')
planner.add(tab2, text='Celsius')
planner.add(tab3, text='Fahrenheit')


# Tabs will be added to the "top" of the "frame"
#planner.pack(side=tk.TOP)
planner.grid(row = 0, column = 0)

root.mainloop()
