# ekinter

ekinter is a much easier way to use tkinter. The setup process for tkinter's window is tedious, and can be hard to manage. Ekinter only passes 3 arguments to get it going.

## Setup

A setup for a window in tkinter might go something like this:

```py
from tkinter import *
tk = Tk()
tk.title('The best game!')
tk.resizable(0, 0)
tk.wm_attributes('-topmost', 1)
canvas = Canvas(tk, width=500, height=500, bd=0, highlightthickness=0)
canvas.pack()
tk.update()
```

Whilst in ekinter it would go something like this:

```py
from ekinter import *
window = Kint('The best game!', 500, 500)
```

Yep, it's really that easy! Adding objects to the window in tkinter and ekinter are the same, though.

Tkinter:

```py
from tkinter import *
tk = Tk()
tk.title('The best game!')
tk.resizable(0, 0)
tk.wm_attributes('-topmost', 1)
canvas = Canvas(tk, width=500, height=500, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

canvas.create_rectangle(10, 10, 50, 50, fill=yellow)
```

Ekinter:

```py
from ekinter import *
window = Kint('The best game!', 500, 500)

window.create_rectangle(10, 10, 50, 50, fill=yellow)
```

What are you waiting for? Create today!
(Add the ekinter file to C:\Users\<username>\AppData\Local\Programs\Python\Python37-32\Lib\site-packages on Windows)
