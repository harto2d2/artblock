from guizero import App, Picture, PushButton, Window, Box


# Here are all the def, arranged properly
def open_window():
    window.show()
    window2.hide()

    for i in range(3, 14):
        str = f"window{i}.hide()"
        eval(str)
    app.hide()


def close_window():
    window.hide()
    app.show()

# the defs here are pretty self explanatory, as I open window two, the
# previous window we were on will close


def open_window2():
    window3.hide()
    window2.show()
    window.hide()
    app.hide()

    for i in range(3, 14):
        str = f"window2{i}.hide()"
        eval(str)


def close_window2():
    window2.hide()
    window.show()


def open_window3():
    window4.hide()
    window3.show()
    window2.hide()
    window.hide()
    app.hide()

    for i in range(3, 14):
        str = f"window2{i}.hide()"
        eval(str)


def close_window3():
    window3.hide()
    window2.show()
    app.hide()


def open_window4():
    window5.hide()
    window4.show()
    window3.hide()
    window2.hide()
    window.hide()
    app.hide()

    for i in range(3, 14):
        str = f"window2{i}.hide()"
        eval(str)


def close_window4():
    window4.hide()
    window3.show()
    window2.hide()
    window.hide()
    app.hide()


def open_window5():
    window8.hide()
    window7.hide()
    window6.hide()
    window5.show()
    window4.hide()
    window3.hide()
    window2.hide()
    window.hide()
    app.hide()

    for i in range(3, 14):
        str = f"window2{i}.hide()"
        eval(str)


def close_window5():
    window5.hide()
    window4.show()
    window3.hide()
    window2.hide()
    window.hide()
    app.hide()


def open_window6():
    window6.show()
    window5.hide()
    app.hide()

    for i in range(3, 14):
        str = f"window2{i}.hide()"
        eval(str)


def close_window6():
    window6.hide()
    window5.show()
    app.hide()


def open_window7():
    window7.show()
    window5.hide()
    app.hide()

    for i in range(3, 14):
        str = f"window2{i}.hide()"
        eval(str)


def close_window7():
    window7.hide()
    window5.show()
    app.hide()


def open_window8():
    window9.hide()
    window8.show()
    window7.hide()
    window6.hide()
    window5.hide()
    window4.hide()
    window3.hide()
    window2.hide()
    window.hide()
    app.hide()

    for i in range(3, 14):
        str = f"window2{i}.hide()"
        eval(str)


def close_window8():
    window8.hide()
    window5.show()
    window4.hide()
    window3.hide()
    window2.hide()
    window.hide()
    app.hide()


def open_window9():
    window10.hide()
    window9.show()
    window8.hide()
    window7.hide()
    window6.hide()
    window5.hide()
    window4.hide()
    window3.hide()
    window2.hide()
    window.hide()
    app.hide()

    for i in range(3, 14):
        str = f"window2{i}.hide()"
        eval(str)


def close_window9():
    window9.hide()
    window8.show()
    window5.hide()
    window4.hide()
    window3.hide()
    window2.hide()
    window.hide()
    app.hide()


# This function exits the whole app, including other windows
def exit():
    app.destroy()


def home():
    window.hide()
    window2.hide()
    window3.hide()
    window4.hide()
    window5.hide()
    window8.hide()
    window9.hide()
    app.show()

    for i in range(3, 14):
        str = f"app{i}.hide()"
        eval(str)


app = App(height=680, width=450)

box1 = Box(app, align="bottom", width=500, height=50)
window = Window(app, height=680, width=450)

box2 = Box(window, align="bottom", width=500, height=50)
window2 = Window(app, height=680, width=450)

box3 = Box(window2, align="bottom", width=500, height=50)
window3 = Window(app, height=680, width=450)

box4 = Box(window3, align="bottom", width=500, height=50)

window4 = Window(app, height=680, width=450)
box5 = Box(window4, align="bottom", width=500, height=50)

window5 = Window(app, height=680, width=450)
box6 = Box(window5, align="bottom", width=500, height=50)

window6 = Window(app, height=680, width=450)
box7 = Box(window6, align="bottom", width=500, height=50)

window7 = Window(app, height=680, width=450)
box8 = Box(window7, align="bottom", width=500, height=50)

window8 = Window(app, height=680, width=450)
box9 = Box(window8, align="bottom", width=500, height=50)

window9 = Window(app, height=680, width=450)
box10 = Box(window9, align="bottom", width=500, height=50)

window10 = Window(app, height=680, width=450)
box11 = Box(window10, align="bottom", width=500, height=50)

window11 = Window(app, height=680, width=450)
box12 = Box(window11, align="bottom", width=500, height=50)

window12 = Window(app, height=680, width=450)
box13 = Box(window12, align="bottom", width=500, height=50)

window13 = Window(app, height=500, width=500)
box14 = Box(window13, align="bottom", width=500, height=50)

window.hide()
for i in range(2, 14):
    str = f"window{i}.hide()"
    eval(str)

# Intro Image, the first page the user encounters
picture = Picture(app, image="img/dt-intro.gif", height=550, width=800)

# the button in the intro, still the first page
bottom_button0 = PushButton(box1,
                            image="img/right arrow.png",
                            align="center",
                            height=40,
                            width=100,
                            command=open_window2)


# this is the second page
picture1 = Picture(window2,
                   image="img/First Page.png",
                   height=640,
                   width=450)

# the buttons of the 2nd page, this is WINDOW2
bottom_button1 = PushButton(box3,
                            image="img/left arrow.png",
                            align="left",
                            height=40,
                            width=100,
                            command=home)

bottom_button2 = PushButton(box3,
                            image="img/right arrow.png",
                            align="right",
                            height=40,
                            width=100,
                            command=open_window3)

# ---------------------------------------------------------------------------

# 3rd page, this is WINDOW3
picture2 = Picture(window3,
                   image="img/second.png",
                   height=640,
                   width=450)

bottom_button3 = PushButton(box4,
                            image="img/left arrow.png",
                            align="left",
                            height=40,
                            width=100,
                            command=open_window2)

bottom_button4 = PushButton(box4,
                            image="img/home2.png",
                            align="left",
                            height=40,
                            width=230,
                            command=home)
bottom_button5 = PushButton(box4,
                            image="img/right arrow.png",
                            align="left",
                            height=40,
                            width=100,
                            command=open_window4)

# ---------------------------------------------------------------------------

# 4th page, this is WINDOW4
picture3 = Picture(window4,
                   image="img/third.png",
                   height=640,
                   width=450)

bottom_button6 = PushButton(box5,
                            image="img/left arrow.png",
                            align="left",
                            height=40,
                            width=100,
                            command=open_window3)

bottom_button7 = PushButton(box5,
                            image="img/home2.png",
                            align="left",
                            height=40,
                            width=230,
                            command=home)
bottom_button8 = PushButton(box5,
                            image="img/right arrow.png",
                            align="left",
                            height=40,
                            width=100,
                            command=open_window5)

# ----------------------------------------------------------------------
# 5th page, this WINDOW5

button1 = PushButton(window5,
                     image="img/aspiring.png",
                     height=310,
                     width=440,
                     command=open_window6)

button2 = PushButton(window5,
                     image="img/experienced.png",
                     align="bottom",
                     height=310,
                     width=440,
                     command=open_window7)

# -----------------------------------------------------------------------
# this is the same page, this is still WINDOW 5
bottom_button9 = PushButton(box6,
                            image="img/left arrow.png",
                            align="left",
                            height=40,
                            width=100,
                            command=open_window4)

bottom_button10 = PushButton(box6,
                             image="img/home2.png",
                             align="left",
                             height=40,
                             width=230,
                             command=home)
bottom_button11 = PushButton(box6,
                             image="img/right arrow.png",
                             align="left",
                             height=40,
                             width=100,
                             command=open_window8)

# ----------------------------------------------------------
# the page the user is directed to after clicking the aspiring button,
# this is WINDOW 6

picture4 = Picture(window6,
                   image="img/Aspiring Page.png",
                   height=640,
                   width=450)

bottom_button13 = PushButton(box7,
                             image="img/left arrow.png",
                             align="left",
                             height=40,
                             width=100,
                             command=open_window5)
# -------------------------------------------------------------
# the page the user is directed to after clicking the experienced button,
# this is WINDOW 7

picture5 = Picture(window7,
                   image="img/Experienced Page.png",
                   height=640,
                   width=450)

bottom_button14 = PushButton(box8,
                             image="img/left arrow.png",
                             align="left",
                             height=40,
                             width=100,
                             command=open_window5)

# -------------------------------------------------------------

# filename, the text file for the page that talks about my personal
# exprience regarding artblock
with open("advice.txt", "r") as f:
    while True:
        file_eof = f.readline()
        print(file_eof)
        if file_eof == '':
            print('End Of File')
            break
        path = "img/" + file_eof + '.jpg'
        path2 = "'str' + path + 'str'"
        print(path, path2)

# -------------------------------------------------------------

# this is the page after the page with the buttons, so after WINDOW 5,
# this is WINDOW8

picture6 = Picture(window8,
                   image="img/Personal Experience Page.png",
                   height=640,
                   width=450)

bottom_button15 = PushButton(box9,
                             image="img/left arrow.png",
                             align="left",
                             height=40,
                             width=100,
                             command=open_window5)

bottom_button16 = PushButton(box9,
                             image="img/home2.png",
                             align="left",
                             height=40,
                             width=230,
                             command=home)
bottom_button17 = PushButton(box9,
                             image="img/right arrow.png",
                             align="left",
                             height=40,
                             width=100,
                             command=open_window9)

# -------------------------------------------------------
# this is WINDOW 9, the last page

picture7 = Picture(window9,
                   image="img/last.png",
                   height=640,
                   width=450)

bottom_button24 = PushButton(box10,
                             image="img/left arrow.png",
                             align="left",
                             height=40,
                             width=100,
                             command=open_window8)

bottom_button25 = PushButton(box10,
                             image="img/home2.png",
                             align="left",
                             height=40,
                             width=230,
                             command=home)

app.display()
