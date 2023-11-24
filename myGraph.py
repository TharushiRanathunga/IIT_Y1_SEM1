from graphics import *   #import the graphics.py module (must be in the same folder this file)


#OPEN THE WINDOW
win = GraphWin("My First Graphics Window", 800, 600)#open a window object called "win" with size and title 
win.setBackground("Mint Cream")# Set the background colour of the window

#creating first heading
my_heading = Text(Point(100, 30), 'My Heading') 
my_heading.draw(win)
my_heading.setTextColor("grey")
my_heading.setSize(20)
my_heading.setStyle("bold")
my_heading.setFace("helvetica")

#creating sub heading
my_sub_heading = Text(Point(105, 70), 'My Sub heading')
my_sub_heading.setTextColor("grey")
my_sub_heading.setSize(16)
my_sub_heading.setStyle("bold")
my_sub_heading.setFace("helvetica")
my_sub_heading.draw(win)

#creating first circle
aCircle = Circle(Point(150,300), 90)
aCircle.setFill("darkolivegreen3")
aCircle.setWidth(0)
aCircle.draw(win)

#creating the second circle
b_Circle = Circle(Point(400,300), 140)
b_Circle.setFill("Lime")
b_Circle.setWidth(0)
b_Circle.draw(win)

#creating the Third circle
c_Circle = Circle(Point(650,300), 170)
c_Circle.setFill("mediumaquamarine")
c_Circle.setWidth(0)
c_Circle.draw(win)

#adding text to first circle
circle1_text = Text(Point(150, 300), "90")
circle1_text.setTextColor("white")
circle1_text.setSize(30)
circle1_text.setStyle("bold")
circle1_text.setFace("helvetica")
circle1_text.draw(win)

#adding text to second circle
circle2_text = Text(Point(400, 300), "140")
circle2_text.setTextColor("white")
circle2_text.setSize(30)
circle2_text.setStyle("bold")
circle2_text.setFace("helvetica")
circle2_text.draw(win)

#adding text to third circle
circle3_text = Text(Point(650, 300), "170")
circle3_text.setTextColor("white")
circle3_text.setSize(30)
circle3_text.setStyle("bold")
circle3_text.setFace("helvetica")
circle3_text.draw(win)

win.getMouse()
win.close()