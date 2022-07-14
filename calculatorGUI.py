# Programmer: Peter Oo
# Location  : Yangon, Myanmar
# Finished date: Jul / 13 / 2022
# Issued date  : Jul / 15 / 2022
# This is an educational python programs, and free to be used or modified.

from tkinter import *
from random import randint


display_list = ['0']
del display_list[0]


# Functions
def press_one():
    display_list.append('1')
    tostring = ''.join(display_list)
    txt.set(tostring)


def press_two():
    display_list.append('2')
    tostring = ''.join(display_list)
    txt.set(tostring)


def press_three():
    display_list.append('3')
    tostring = ''.join(display_list)
    txt.set(tostring)


def press_four():
    display_list.append('4')
    tostring = ''.join(display_list)
    txt.set(tostring)


def press_five():
    display_list.append('5')
    tostring = ''.join(display_list)
    txt.set(tostring)


def press_six():
    display_list.append('6')
    tostring = ''.join(display_list)
    txt.set(tostring)


def press_seven():
    display_list.append('7')
    tostring = ''.join(display_list)
    txt.set(tostring)


def press_eight():
    display_list.append('8')
    tostring = ''.join(display_list)
    txt.set(tostring)


def press_nine():
    display_list.append('9')
    tostring = ''.join(display_list)
    txt.set(tostring)


def press_zero():
    display_list.append('0')
    tostring = ''.join(display_list)
    txt.set(tostring)


def press_decimal():
    display_list.append('.')
    tostring = ''.join(display_list)
    txt.set(tostring)


def press_add():
    display_list.append('+')
    tostring = ''.join(display_list)
    txt.set(tostring)


def press_sub():
    display_list.append('-')
    tostring = ''.join(display_list)
    txt.set(tostring)


def press_multiply():
    display_list.append('*')
    tostring = ''.join(display_list)
    txt.set(tostring)


def press_div():
    display_list.append('/')
    tostring = ''.join(display_list)
    txt.set(tostring)


def press_eq():
    display_var = display.get()
    try:
        txt.set(eval(display_var))
        display_list.clear()
        display_list.append(display.get())
    except SyntaxError:
        txt.set("Something went wrong!")


def press_clear():
    display_list.clear()
    display.delete(0, len(display.get()))


def press_del():
    if len(display_list) > 0:
        display_list.pop(len(display_list)-1)
        tostring = ''.join(display_list)
        txt.set(tostring)


def press_smiley():
    speech = randint(1, 5)
    dictionary = {1: 'Smiley is the best...',
                  2: 'Trial & Error makes thing perfect.',
                  3: 'Digital World!!!',
                  4: 'My first python GUI program!',
                  5: 'Be master in everything.'
                  }
    txt.set(dictionary[speech])


# Creating window form template
win = Tk()
win.title('Python Calculator')  # Giving windows form title name
icon = PhotoImage(file='calculator.png')  # Creating photoImage file for icon to be uploaded
win.iconphoto(True, icon)  # Display the icon on the windows form
win.iconbitmap(r'calculator.ico')
win.config(bg='black')  # Changing background color of windows base template
win.geometry('300x400')  # Sizing template as required.

win.resizable(False, False)

# Creating an Entry both for displaying output and input
txt = StringVar()
display = Entry(win,  # Entry is displayed on Windows form
                textvariable=txt,
                font=('Times New Roman', 14),
                bg='#f2f0e6',
                fg='blue',
                relief='ridge',     # Border style
                bd=10,
                width=30,  # Total width of the entry box
                justify='right',  # to set cursor position at left, right or center
                takefocus=False,  # Turn off taking focus by pressing tab key
                )
display.pack(pady=10)       # We have 3 methods .pack(), .place() & .grid() to display particular widget
display.bind('<Key>' and '<Button>', NONE)   # universal method .bind(Event Sequence, function(e) or NONE to do nothing)
# Creating a frame template for buttons
frame_one = Frame(win,
                  bg='black')
frame_one.pack()
frame_two = Frame(win,
                  bg='black')
frame_two.pack()
# Smiley ICON at free space
smiley = PhotoImage(file='smiley_50x50.png', )
# button for smiley
smiley_tag = Button(frame_two,
                    image=smiley,
                    command=press_smiley)
smiley_tag.grid(row=3, column=0)
# Creating buttons
one = Button(frame_two,  # button one
             text='1',
             font=('Times New Roman', 12),
             padx=20,
             pady=10,
             command=press_one,
             )
one.grid(row=2, column=0, padx=5, pady=5)
two = Button(frame_two,
             text='2',
             font=('Times New Roman', 12),
             padx=20,
             pady=10,
             command=press_two,
             )
two.grid(row=2, column=1, padx=5, pady=5)
three = Button(frame_two,
               text='3',
               font=('Times New Roman', 12),
               padx=20,
               pady=10,
               command=press_three,
               )
three.grid(row=2, column=2, padx=5, pady=5)
four = Button(frame_two,
              text='4',
              font=('Times New Roman', 12),
              padx=20,
              pady=10,
              command=press_four,
              )
four.grid(row=1, column=0, padx=5, pady=5)
five = Button(frame_two,
              text='5',
              font=('Times New Roman', 12),
              padx=20,
              pady=10,
              command=press_five,
              )
five.grid(row=1, column=1, padx=5, pady=5)
six = Button(frame_two,
             text='6',
             font=('Times New Roman', 12),
             padx=20,
             pady=10,
             command=press_six,
             )
six.grid(row=1, column=2, padx=5, pady=5)
seven = Button(frame_two,
               text='7',
               font=('Times New Roman', 12),
               padx=20,
               pady=10,
               command=press_seven,
               )
seven.grid(row=0, column=0, padx=5, pady=5)
eight = Button(frame_two,
               text='8',
               font=('Times New Roman', 12),
               padx=20,
               pady=10,
               command=press_eight,
               )
eight.grid(row=0, column=1, padx=5, pady=5)
nine = Button(frame_two,
              text='9',
              font=('Times New Roman', 12),
              padx=20,
              pady=10,
              command=press_nine,
              )
nine.grid(row=0, column=2, padx=5, pady=5)
zero = Button(frame_two,
              text='0',
              font=('Times New Roman', 12),
              padx=20,
              pady=10,
              command=press_zero,
              )
zero.grid(row=3, column=1, padx=5, pady=5)
decimal = Button(frame_two,
                 text='.',
                 font=('Times New Roman', 12),
                 padx=20,
                 pady=10,
                 command=press_decimal,
                 )
decimal.grid(row=3, column=2, padx=5, pady=5)
eq = Button(frame_two,
            text='=',
            font=('Times New Roman', 12),
            padx=20,
            pady=10,
            command=press_eq,
            )
eq.grid(row=3, column=3, padx=5, pady=5)
add = Button(frame_two,
             text='+',
             font=('Times New Roman', 12),
             padx=20,
             pady=10,
             command=press_add,
             )
add.grid(row=2, column=3, padx=5, pady=5)
sub = Button(frame_two,
             text='-',
             font=('Times New Roman', 12),
             padx=20,
             pady=10,
             command=press_sub,
             )
sub.grid(row=1, column=3, padx=5, pady=5)
multiply = Button(frame_two,
                  text='*',
                  font=('Times New Roman', 12),
                  padx=20,
                  pady=10,
                  command=press_multiply,
                  )
multiply.grid(row=0, column=3, padx=5, pady=5)
div = Button(frame_one,
             text='/',
             font=('Times New Roman', 12),
             padx=20,
             pady=5,
             command=press_div,
             )
div.grid(row=0, column=2, padx=5, pady=5)
delete = Button(frame_one,
                text='DEL',
                font=('Times New Roman', 12),
                padx=30,
                pady=5,
                command=press_del,
                )
delete.grid(row=0, column=0, padx=5, pady=5)
clear = Button(frame_one,
               text='clear',
               font=('Times New Roman', 12),
               padx=30,
               pady=5,
               command=press_clear,
               )
clear.grid(row=0, column=1, padx=5, pady=5)
# infinite Loop to display win form on the screen until 'red cross' button is hit.
win.mainloop()
