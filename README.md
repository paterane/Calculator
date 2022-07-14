# Calculator
Programmer: Peter Oo.

It is a `Simple GUI Calculator Program` written in `tkinter python`.

Complete python source file is uploaded, but we are here to learn the `basic mechanism`.

`Tkinter documents` provides useful resources starting from creating `windows form` to advanced.

In this simple GUI program, we have the following code parts....

```python
from tkinter import *
```
All the tkinter methods and classes can be imported using above code.
Creating a window for any widgets to be placed on it, the following codes are used,
```python
# Creating a windows form
win = Tk()
# infinite loop to display it until red cross button is hit.
# your statements
# your statements
# your statements!!!
win.mainloop()
```
The remaining statements belonged to windows form shall be coded inside the `win` object and its `mainloop`.
Basically, the calculator needs a display to show input mathematical expressions and output results. For that, Entry widgets are useful.
```python
# Creating an Entry display
txt = StringVar()                   # assigning txt as a buffer to store string data
display = Entry(win,
                textvariable=txt,   # works as a buffer to get data from entry or to set data to entry
                bg='white',         # background color
                fg='blue'           # foreground color
                font=('Arial', 12), # font style
                relief='groove',    # border style
                bd=5,               # border thickness
                justify='right',    # as normal calculator, we should set cursor at the right side the display
                width=30)
```
It's setting the required options for the display, but to show it on the windows, following code is added.
```python
display.pack()
```
We can use other methods like `.grid() or .place()`, too.

So, before we're not going any further, let's take a look back to winform base template.
We used simple template, but we would like to fix its **width and height**. For that, we can use the following methods..
```python
win.geometry('300x400+0+0') # the format is [width x height + 'x' coordinate + 'y' coordinate]
win.resizable(False, False)  # which make it unadjustable.
```
We can change **background color and menu title** using following statements
```python
win.title('Calculator')
win.config(bg='red')
```
So, it Looks like as below....

![Capture_1](https://user-images.githubusercontent.com/93751945/179067696-e1f1630a-23d3-4731-ad03-4bd12b70e4d6.PNG)

It is bloooooody.!

The next step, We are going to create the **buttons**....
```python
button_n = Button(frame,        # need to create a frame to layout buttons using .grid() methods
                  text='/',
                  font=('Arial', 12),
                  width=5,
                  height=2)
button_n.grid(row=0, column=0)
```
But, in the above codes, we need to create a frame to layout the buttons using `.grid()` methods properly, because `.grid()` methods cannot be mixed with `.pack()` methods in the same template.
We will have to go ahead and create a frame before the buttons are created. After that we will place the buttons on that master frame using `.grid()` methods.
```python
frame = Frame(win)    # on windows template
```
After that, We can create as many buttons as we want such as button_1,2,3,5,...,and so on by changing `row and column` to form a buttons layout.

So, the buttons layout should be like this....

![Capture_2](https://user-images.githubusercontent.com/93751945/179078002-43b137cf-9935-411c-97c3-78f8cc53847b.PNG)

Oops, numbers in my calculator are upside down. Anyway, it is great!

Then, when we hit the buttons, it should do something like printing data, or calling police station :joy::joy::joy:

We will need to add `command option` when we create the button widgets like....
```python
button_n = Button(frame,    
                  text='/',
                  font=('Arial', 12),
                  width=5,
                  height=2,
                  command=do_something)
button_n.grid(row=0, column=0)
```
So, when we hit the button, it will call `do_something` function. The functions can be defined outside `win` template and `win.mainloop()` like.....
```python
def do_something():
  txt.set('Hello world')
```
For now, I will call the function `do_something` when I hit `button C`. And It should display like this.....

![Capture_3](https://user-images.githubusercontent.com/93751945/179088656-f0a5038d-5b8f-45ab-bfc9-98625b16327d.PNG)

It is crazy!!! 😅😅😅

Well, as a final step, it is time to compile the source code to get executable file. For that, we will use pyinstaller, and following command will be typed in the command prompt.

`pyinstaller --noconfirm --windowed --icon "D:\Python\...\logo.ico" "D:\Python\...\calculator.py"`

And, Done, we are ready to play our own calculator.

![Capture_4](https://user-images.githubusercontent.com/93751945/179090014-32aa7491-83de-4764-8cfa-2b14f5518a35.PNG)

It is our final calculator design, so lovely....









