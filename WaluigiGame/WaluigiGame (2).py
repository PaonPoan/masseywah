from pygame import *
init()
screen = display.set_mode((800,600))
mixer.music.load("waluigi funk.mp3")
mixer.music.play(-1)
display.set_caption("WAH")
bg=Rect(0,0,800,600)
titlePic = image.load("pics/title.png")
##gamePic = image.load("Waluigi.jpg")
##gamePic = transform.smoothscale(gamePic,screen.get_size())
instructionsPic = image.load("pics/helpscreen.png")
goodend=image.load("pics/happy end.png")
badend=image.load("pics/sad end.png")
qR=image.load("pics/qright.png")
qW=image.load("pics/qwrong.png")
q1=image.load("pics/q1.png")
q2=image.load("pics/q2.png")
q3=image.load("pics/q3.png")
q4=image.load("pics/q4.png")
q5=image.load("pics/q5.png")
playbutton = Rect(380,415,180,170)
helpbutton = Rect(600,415,180,170)
playhover=image.load("pics/play.png")
helphover=image.load("pics/help.png")
nose=Rect(343,154,58,100)
nosehover=image.load("pics/nose.png")
qa=Rect(20,500,43,100)
qc=Rect(23,543,43,100)
q1b=Rect(192,500,43,100)
q1d=Rect(209,543,43,100)
q2b=Rect(256,503,43,100)
q2d=Rect(256,556,43,100)
q3b=Rect(500,503,43,100)
q3d=Rect(500,545,43,100)
q4b=Rect(253,500,43,100)
q4d=Rect(253,557,43,100)
q5b=Rect(286,500,43,100)
q5d=Rect(286,547,43,100)
right = 0
wrong = 0
def game():
    global question
    global right
    global wrong
    running = True
    screen.blit(q1,(0,0))
    while running:
        for evnt in event.get():
            if evnt.type == QUIT:
                running = False
        mx,my = mouse.get_pos()
        mb = mouse.get_pressed()
        if qc.collidepoint(mx,my) and mb[0]==1:
            question = 1
            screen.blit(qR,(0,0))
            right=1
        elif q1b.collidepoint(mx,my) and mb[0]==1 or qa.collidepoint(mx,my) and mb[0]==1 or q1d.collidepoint(mx,my) and mb[0]==1:
            question=1 
            screen.blit(qW,(0,0))
            wrong=1
        if nose.collidepoint(mx,my) and mb[0]==1 and question==1:
            return "question 2"   
        display.flip()       
    return "Menu"
def question2():
    global question
    global right
    global wrong
    running = True
    screen.blit(q2,(0,0))
    while running:
        for evnt in event.get():
            if evnt.type == QUIT:
                running = False
        mx,my = mouse.get_pos()
        mb = mouse.get_pressed()
        if qc.collidepoint(mx,my) and mb[0]==1:
            question = 2
            screen.blit(qR,(0,0))
            right+=1
        elif q2b.collidepoint(mx,my) and mb[0]==1 or qa.collidepoint(mx,my) and mb[0]==1 or q2d.collidepoint(mx,my) and mb[0]==1:
            question=2 
            screen.blit(qW,(0,0))
            wrong+=1
        if nose.collidepoint(mx,my) and mb[0]==1 and question==2:
            return "question 3"
        display.flip()
    return "Menu"
def question3():
    global question
    global right
    global wrong
    running = True
    screen.blit(q3,(0,0))
    while running:
        for evnt in event.get():
            if evnt.type == QUIT:
                running = False
        mx,my = mouse.get_pos()
        mb = mouse.get_pressed()
        if qc.collidepoint(mx,my) and mb[0]==1:
            question=3
            screen.blit(qR,(0,0))
            right+=1
        elif q3b.collidepoint(mx,my) and mb[0]==1 or qa.collidepoint(mx,my) and mb[0]==1 or q3d.collidepoint(mx,my) and mb[0]==1:
            question=3 
            screen.blit(qW,(0,0))
            wrong+=1
        if nose.collidepoint(mx,my) and mb[0]==1 and question==3:
            return "question 4"
        display.flip()
    return "Menu"
def question4():
    global question
    global right
    global wrong
    running = True
    screen.blit(q4,(0,0))
    while running:
        for evnt in event.get():
            if evnt.type == QUIT:
                running = False
        mx,my = mouse.get_pos()
        mb = mouse.get_pressed()
        if qc.collidepoint(mx,my) and mb[0]==1:
            question=4
            screen.blit(qR,(0,0))
            right+=1
        elif q4b.collidepoint(mx,my) and mb[0]==1 or qa.collidepoint(mx,my) and mb[0]==1 or q4d.collidepoint(mx,my) and mb[0]==1:
            question=4 
            screen.blit(qW,(0,0))
            wrong+=1
        if nose.collidepoint(mx,my) and mb[0]==1 and question==4:
            return "question 5"
        display.flip()
    return "Menu"
def question5():
    global question
    global right
    global wrong
    running = True
    screen.blit(q5,(0,0))
    while running:
        for evnt in event.get():
            if evnt.type == QUIT:
                running = False
        mx,my = mouse.get_pos()
        mb = mouse.get_pressed()
        if qc.collidepoint(mx,my) and mb[0]==1:
            question=5
            screen.blit(qR,(0,0))
            right+=1
        elif q5b.collidepoint(mx,my) and mb[0]==1 or qa.collidepoint(mx,my) and mb[0]==1 or q5d.collidepoint(mx,my) and mb[0]==1:
            question=5
            screen.blit(qW,(0,0))
            wrong+=1
        if nose.collidepoint(mx,my) and mb[0]==1 and question==5:
            if wrong==0:
                screen.blit(goodend,(0,0))
            else:
                screen.blit(badend,(0,0))
        display.flip()
    return "Menu"
    
def instructions():
    running = True
    screen.blit(instructionsPic,(0,0))
    while running:
        for evnt in event.get():
            if evnt.type == QUIT:
                running = False
        display.flip()       
    return "Menu" 
def menu():
    global question
    global right
    global wrong
    right=0
    wrong=0
    #options = ["Instructions"]
    running = True
    while running:
        for evt in event.get():
            print(evt)
            if evt.type==QUIT:
                return "Exit"
        mx,my = mouse.get_pos()
        mb = mouse.get_pressed()
        screen.blit(titlePic,(0,0))
        if playbutton.collidepoint(mx,my):
            screen.blit(playhover,(358,405))
        if playbutton.collidepoint(mx,my) and mb[0]==1:
            return "Game"
        if helpbutton.collidepoint(mx,my):
            screen.blit(helphover,(575,402))
        if helpbutton.collidepoint(mx,my) and mb[0]==1:
            return "Instructions"
        display.flip()    
frame = "Menu"
while frame!="Exit":
    if frame == "Menu":
        frame = menu()
    if frame == "Game":
        frame = game()
    if frame == "Instructions":
        frame = instructions()
    if frame == "question 2":
        frame = question2()
    if frame == "question 3":
        frame = question3()
    if frame == "question 4":
        frame = question4()
    if frame == "question 5":
        frame = question5()

quit()
