import tkinter as tk
from tkinter import font

class Frame1(tk.Frame):
	def __init__(self, master, *args, **kwargs):
		tk.Frame.__init__(self, master, *args, **kwargs)

		self.container = tk.Frame(self, bg='#121212', padx=80, pady=100)

		self.logo = tk.PhotoImage(file=r'images\head5.png', height=225, width=360)
		self.labelLogo = tk.Label(self.container, image=self.logo, bd=0)
		self.labelLogo.grid(row=0, column=0)

		self.btnimg = tk.PhotoImage(file=r'images\signup6.png')
		self.btnimg2 = tk.PhotoImage(file=r'images\login.png')

		from .Frame3 import Frame3
		from .Frame4 import Frame4
		self.login = tk.Button(
			self.container,
			border=0,
			background='#121212',
			activebackground='#121212',
			image=self.btnimg2,
			command=lambda: self.master.show_frame(Frame3)
		)
		self.login.grid(row=2, column=0, pady=10)

		from .Frame2 import Frame2
		self.login = tk.Button(
			self.container,
			border=0,
			background='#121212',
			activebackground='#121212',
			image=self.btnimg,
			command=lambda: self.master.show_frame(Frame2)
		)
		self.login.grid(row=1, column=0)

		self.container.grid(row=0, column=0, sticky='nsew')

		self.grid_rowconfigure(0, weight=1)
		self.grid_columnconfigure(0, weight=1)
		
		self.appHighlightFont = font.Font(
			family='lineto circular',
			size=14
		)

		self.appHighlightFont2 = font.Font(
			family='lineto circular',
			size=12
		)

		self.verify = tk.Label(
			self.container,
			border=0,
			text="Amplify team Welcomes you!",
			background='#121212',
			# activebackground='#121212',
			foreground='white',
			# activeforeground='white',
			font=self.appHighlightFont2,
			
		)
		self.verify.grid(
			row=6,
			column=0,
			sticky='news',
			padx=2,
			pady=5,
			ipadx=20,
			ipady=10
		)
