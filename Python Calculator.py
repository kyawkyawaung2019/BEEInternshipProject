from tkinter import *

# Creating frame for calculator
def iCalculator(source, side):
	storeObject = Frame(source, borderwidth = 0, bd = 0, bg = "black")
	storeObject.pack(side = side, expand = YES, fill = BOTH)
	return storeObject
	
# Creating button
def button(source, side, bg, fg, text, command = None):
	storeObject = Button(source, text = text, bg = bg, fg = fg, command = command)
	storeObject.pack(side = side, expand = YES, fill = BOTH)
	return storeObject
	
class Window(Frame):
	def __init__(self, master=None):
		Frame.__init__(self)
		self.option_add('*Font', 'arial 20')
		self.pack(expand = YES, fill = BOTH)
		self.master.title('Python Calculator')
		
		# Adding Display Widget
		display = StringVar()
		Entry(self, relief = RIDGE, textvariable = display, justify = 'right', bd = 1, bg = "white", font="arial, 25").pack(side=TOP, expand=YES, fill=BOTH)

		# Adding Clear Button Widgets
		for clearButton in (["CX"]):
			erase = iCalculator(self, TOP)
			for ichar in clearButton:
				if ichar == 'C':
					button(erase, LEFT, 'white', 'black', ichar, lambda storeObject = display, q = ichar: storeObject.set(''))
				else:
					button(erase, LEFT, 'red', 'white', ichar, self.app_exit)

		# Adding Numbers And Symbols Widgets
		for numButton in ("789/","456*","123-","0.+"):
			functionNum = iCalculator(self, TOP)
			for iEquals in numButton:
				button(functionNum, LEFT, 'black', 'white', iEquals, lambda storeObject = display, q = iEquals: storeObject.set(storeObject.get() + q))

		# Adding Equal Button
		Equalbutton = iCalculator(self, TOP)
		for iEquals in "=":
			if iEquals == '=':
				btniEquals = button(Equalbutton, LEFT, 'white', 'black', iEquals)
				btniEquals.bind('<ButtonRelease - 1 >', lambda e,s=self, storeObject = display: s.calculator(storeObject), '+')
			else:
				btniEquals = button(Equalbutton, LEFT, 'white', 'black', iEquals, lambda storeObject=display, s='%s' %iEquals:storeObject.set(storeObject.get()+s))
				
	# Applying Evenet Trigger On Widgetts
	def calculator(self, display):
		try:
			display.set(eval(display.get()))
		except:
			display.set("ERROR")
	
	def app_exit(self):
		exit()

# Start the GUI
root = Tk()

root.geometry("300x500")

app = Window(root)
root.mainloop()
'''
if __name__ == '__main__':
	app().mainloop()
'''
