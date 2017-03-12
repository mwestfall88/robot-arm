import Tkinter as tk

root1 = tk.Tk()
angle_in = []
input_vars = []
output_vars = []
marker = []
outputs = []

angle_label = "angle"

#Initializes & Populates GUI
for ii in range(0, 3):
	input_vars.append(tk.DoubleVar())
	output_vars.append(tk.DoubleVar())

	angle_label = "angle " + str(ii + 1)
	marker.append(tk.Label(root1, text=angle_label))

 	angle_in.append(tk.Entry(root1, textvariable=input_vars[ii]))
 	outputs.append(tk.Label(root1, textvariable=output_vars[ii]))

 	marker[ii].grid(column=ii, row=0)
 	angle_in[ii].grid(column=ii, row=1)
 	outputs[ii].grid(column=ii, row=2)


w = tk.Scale(root1, from_=0, to_=90, orient="horizontal")
w.grid(column = 0, columnspan=3, row=3)

def updatelabels(event):
	for ii in range(0,3):
		output_vars[ii].set(input_vars[ii].get())

for ii in range(0,3):
	angle_in[ii].bind('<Return>', updatelabels)

root1.mainloop()

# root1 = tk.Tk()
# x = tk.StringVar()
# var2 = tk.StringVar()
# label1 = tk.Label(root1, text='Enter Something')
# entry1 = tk.Entry(root1, textvariable = x)
# label3 = tk.Label(root1, textvariable = var2)


# label1.pack(side=tk.TOP)
# entry1.pack()
# label3.pack(side=tk.BOTTOM)

# def showentry(event):
# 	print(entry1.get())

# def assignlabel(event):
# 	var2.set(x.get())
# 	print(var2)
# 	return var2

# entry1.bind('<Return>', assignlabel)

# root1.mainloop()

# root2 = tk.Tk()
# label2 = tk.Label(root2, text='Choose a button')
# buttonstr = tk.StringVar()

# buttonA = tk.Radiobutton(root2, text="Button A", variable=buttonstr, value='ButtonA string')
# buttonB = tk.Radiobutton(root2, text="Button B", variable=buttonstr, value="ButtonB string")
# buttonC = tk.Radiobutton(root2, text="Button C", variable=buttonstr, value="ButtonC string")

# def showstr(event=None):
# 	print(buttonstr.get())

# buttonA.config(command=showstr)
# buttonB.config(command=showstr)
# buttonC.config(command=showstr)


# label2.grid(column=0, row=0)
# buttonA.grid(column=0, row=1)
# buttonB.grid(column=0, row=2)
# buttonC.grid(column=0, row=3)

# buttonA.select()
# root2.mainloop()



# root1.mainloop()
#Entry
#Text
#Buttom
#Radiobutton
#Checkbutton

#label
#photoimage
#listbox
#menu