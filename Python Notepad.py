from tkinter import *

def WriteFile():
	try:
		file = open("notepadFile.txt", "a")
		#file.writelines("Hello! ")
	except FileDoesNotExit:
		print("Cannot write file")
	finally:
		file.close()

def OpenFile(txtBox1):
	txtBox1.delete("1.0", END)
	try:
		file = open("notepadFile.txt", "r")
		text = ""
		for x in file:
			text += x
		txtBox1.insert(END, text)
	except IOError:
		print("Cannot open file")
	finally:
		file.close()

def AppendFile(text):
	try:
		file = open("notepadFile.txt", "a")
		#text = "This is append text.\n"
		file.writelines(text)
		print("Appending done!\n")
	except IOError:
		print("Cannot append file")
	finally:
		file.close()

class Windows(Frame):
	def __init__(self, master=None):
		Frame.__init__(self)
		self.option_add('*Font', 'arial 20 bold')
		self.pack(expand = YES, fill = BOTH)
		self.master.title('TK Windows')
		#self.master.geometry("900x500")

		lbl1 = Label(self, text = "THE TEXT FROM TEXT FILE.", font="Courilla, 14", bg = "white", fg = "black", bd=5)
		lbl1.pack(side = TOP, expand = NO, fill = BOTH)
		
		# Creating text box to show contents from text file
		txtBox1 = Text(self, height = 10, width = 500, bd = 1, bg = "black", fg = "white", font="Courilla, 11")
		txtBox1.pack(side = TOP, expand=YES, fill = BOTH)
		
		WriteFile()
		
		OpenFile(txtBox1)
		
		# Scrollbar for txtBox1
		scrollbar1 = Scrollbar(txtBox1)
		scrollbar1.pack(side = RIGHT, fill = Y)
		scrollbar1.config(command = txtBox1.yview)
		txtBox1.config(yscrollcommand = scrollbar1.set)
		
		lbl2 = Label(self, text = "ENTER SOMETHING!", font="Courilla, 14", bg = "black", fg = "white", bd=5)
		lbl2.pack(side = TOP, expand = NO, fill = BOTH)
		
		# Creating text box to append the text into text file
		txtBox2 = Text(self, height = 10, width = 500, bd = 1, bg = "white", fg = "black", font="Courilla, 11")
		txtBox2.pack(side = TOP, expand = YES, fill = BOTH)
		
		# Scrollbar for txtBox2
		scrollbar2 = Scrollbar(txtBox2)
		scrollbar2.pack(side = RIGHT, fill = Y)
		scrollbar2.config(command = txtBox2.yview)
		txtBox2.config(yscrollcommand = scrollbar2.set)
		
		def enter_text():
			text = txtBox2.get("1.0", END)
			AppendFile(text)
			OpenFile(txtBox1)

		# Adding Enter button
		btn = Button(self, text = "ENTER", bd = 5, bg = "black", fg = "white", command = enter_text)
		btn.pack(side = TOP, expand = NO, fill = BOTH)

# Start the GUI
root = Tk()

root.geometry("800x500")

app = Windows(root)

root.mainloop()

