import robot_kinemat_model
import Tkinter as tk
import matplotlib
matplotlib.use('TkAgg')

from numpy import arange, sin, pi
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D

#Initializes & Populates GUI

def mOpen():

	global f
	global a
	global arm1 
	global arm2
	global arm3
	global canvas
	global input_vars
	global end_effector

	angle_in = []
	input_vars = []
	#output_vars = []
	marker = []
	output = []
	output_labels = [0,0,0]
	slider=[]
	end_effector = [tk.DoubleVar(),tk.DoubleVar(),tk.DoubleVar()]


	output_labels[0] = tk.Label(root1, text='X Position')
	output_labels[1] = tk.Label(root1, text='Y Position')
	output_labels[2] = tk.Label(root1, text='Z Position')
	ee_label = tk.Label(root1, text='End Effector Position in Global Coords')

	for ii in range(0, 3):
		input_vars.append(tk.DoubleVar())
		#output_vars.append(tk.DoubleVar())

		angle_label = "Angle " + str(ii + 1)
		marker.append(tk.Label(root1, text=angle_label))

	 	angle_in.append(tk.Entry(root1, textvariable=input_vars[ii]))
	 	#outputs.append(tk.Label(root1, textvariable=output_vars[ii]))

	 	slider.append(tk.Scale(root1, from_=-90, to=90, orient="horizontal", variable=input_vars[ii], command=updateScale))
	 	output.append(tk.Label(root1, textvariable=end_effector[ii]))

	 	marker[ii].grid(column=ii, row=0)
	 	angle_in[ii].grid(column=ii, row=1)
	 	#outputs[ii].grid(column=ii, row=2)
	 	slider[ii].grid(column = ii, row=2)
	 	output[ii].grid(column = 1, row = 4+ii)
	 	output_labels[ii].grid(column = 0, row = 4+ii)


	#output = tk.Label(root1, textvariable=end_effector[0])#variable=end_effector)
	#output.grid(column=1, row=3)
	#def updatelabels(event):
	#	for ii in range(0,3):
	#		output_vars[ii].set(input_vars[ii].get())

	# for ii in range(0,3):
	# 	angle_in[ii].bind('<Return>', updatelabels)

	ee_label.grid(column = 1, row=3)

	f = Figure(figsize=(5,4), dpi=100)
	a = f.add_subplot(111, projection='3d')
	(arm1, arm2, arm3, eop) = robot_kinemat_model.calc_arm_pos(input_vars[0].get(),input_vars[1].get(),input_vars[2].get())
	a.plot(arm1['x'],arm1['y'], arm1['z'])
	a.plot(arm2['x'],arm2['y'], arm2['z'])
	a.plot(arm3['x'],arm3['y'], arm3['z'])
	axes = f.gca()
	axes.set_xlim([-300,300])
	axes.set_ylim([200,-200])
	axes.set_zlim([0,350])

	canvas=FigureCanvasTkAgg(f,master=root1)
	canvas.show()
	canvas.get_tk_widget().grid(column=4, row=0, rowspan=8)

	for ii in range(0,3):
		angle_in[ii].bind('<Return>', updateScale)

def updateScale(event):
	(arm1, arm2, arm3, eop) = robot_kinemat_model.calc_arm_pos(input_vars[0].get(),input_vars[1].get(),input_vars[2].get())
	a.clear()
	a.plot(arm1['x'],arm1['y'], arm1['z'])
	a.plot(arm2['x'],arm2['y'], arm2['z'])
	a.plot(arm3['x'],arm3['y'], arm3['z'])
	axes = f.gca()
	axes.set_xlim([-300,300])
	axes.set_ylim([200,-200])
	axes.set_zlim([0,350])
	canvas.show()
	end_effector[0].set(eop[0,0].round(decimals=1))
	end_effector[1].set(eop[1,0].round(decimals=1))
	end_effector[2].set(eop[2,0].round(decimals=1))

root1 = tk.Tk()
mOpen()
root1.wm_title('Kinematic Model of a Robot with 3 rotary Joints')
root1.mainloop()
