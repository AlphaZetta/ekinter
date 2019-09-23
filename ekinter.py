from tkinter import *

class Kint:
	def __init__(self, title, width, height):
		tk = Tk()
		tk.title(title)
		tk.resizable(0, 0)
		tk.wm_attributes('-topmost', 1)
		canvas = Canvas(tk, width=width, height=height, bd=0, highlightthickness=0)
		canvas.pack()
		self.canvas = canvas
		tk.update()

	def create_arc(self, *args, **kw):
		self.canvas.create_arc(args, kw)

	def create_bitmap(self, *args, **kw):
		self.canvas.create_bitmap(args, kw)

	def create_image(self, *args, **kw):
		self.canvas.create_image(args, kw)

	def create_line(self, *args, **kw):
		self.canvas.create_line(args, kw)

	def create_oval(self, *args, **kw):
		self.canvas.create_oval(args, kw)

	def create_polygon(self, *args, **kw):
		self.canvas.create_polygon(args, kw)

	def create_rectangle(self, *args, **kw):
		self.canvas.create_rectangle(args, kw)

	def create_text(self, *args, **kw):
		self.canvas.create_text(args, kw)

	def bind_all(self, key, action):
		self.canvas.bind_all(key, action)