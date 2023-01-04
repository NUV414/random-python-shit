import turtle

tDraw = turtle.Turtle()
tDraw.pensize(10)
'''tDraw2 = turtle.Turtle()
tDraw2.pensize(4)
tDraw2.color("dark violet")
tDraw2.left(90)'''
'''tDraw3 = turtle.Turtle()
tDraw3.pensize(4)
tDraw3.color("red")
tDraw3.left(180)'''
'''tDraw4 = turtle.Turtle()
tDraw4.pensize(4)
tDraw4.color("lime")
tDraw4.left(270)'''
wn = turtle.Screen()

def read_rules(start,rules): #reads a dictionary containg rules formatted like {"variable": "goes to"}
	lst = list(start)
	outlst = []
	for element in lst:
		if element in rules:
			outlst.extend(list(rules.get(element)))
		else:
			outlst.extend(element)
	return outlst

def draw(order, t, start, angle, rules, size): #order controls how many times the rules are iterated, t is the turtle, start is the initial conditions
	outlst = start
	for i in range(order):
		outlst = read_rules(outlst, rules)
	for element in outlst:
		if element == "F" or element == "G":
			t.forward(size)
		elif element == "+":
			t.left(angle)
		elif element == "-":
			t.right(angle)

hilbertCurve =  {"A":"+BF-AFA-FB+", "B":"-AF+BFB+FA-"}
dragonCurve = {"F": "F+G", "G": "F-G"}
kochCurve = {"F": "F+F-F-F+F"} #for a snowflake set start to F--F--F, for normal just do F

draw(10, tDraw,start="F", angle=90 , rules= dragonCurve, size=10)
wn.mainloop()