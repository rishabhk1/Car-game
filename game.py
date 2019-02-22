import pygame,time,random
pygame.init()
white=(255,255,255)
black=(0,0,0)
green=(0,255,0)
red=(255,0,0)
blue=(179,255,255)
light_green=(0,200,0)
light_red=(200,0,0)
display_w=800
display_h=600
display=pygame.display.set_mode((display_w,display_h))
pygame.display.set_caption('Race')
clock=pygame.time.Clock()
carimg=pygame.image.load('racecar.png')
x_change=0
pause=False
def buttons(text,x,y,xb,yb,c,lc,f=None):
        mouseb=pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()

        if x+xb > mouseb[0] > x and y+yb > mouseb[1] > y:
            pygame.draw.rect(display,lc,(x,y,xb,yb))
            if click[0]==1 and f!=None :
                f()
        else:
            pygame.draw.rect(display,c,(x,y,xb,yb))
        esmalltext=pygame.font.Font('freesansbold.ttf',25)
        textsurface,textrect=text_objects(text,esmalltext)
        textrect.center=((x+(xb/2)),(y+(yb/2)))#to center the text
        display.blit(textsurface,textrect)
        pygame.display.update()

def unpause():
    global pause
    pause=False

def intro():
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()

        display.fill(white)
        smalltext=pygame.font.Font('freesansbold.ttf',75)
        textsurface,textrect=text_objects('Game',smalltext)
        textrect.center=((display_w/2),(display_h/2))#to center the text
        display.blit(textsurface,textrect)

        buttons('GO',150,450,100,50,green,light_green,gameloop)
        buttons('Exit',550,450,100,50,red,light_red,quit)
        pygame.display.update()
        clock.tick(20)

def end():
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()

        display.fill(white)
        smalltext=pygame.font.Font('freesansbold.ttf',75)
        textsurface,textrect=text_objects('You crashed',smalltext)
        textrect.center=((display_w/2),(display_h/2))#to center the text
        display.blit(textsurface,textrect)

        buttons('Again',150,450,100,50,green,light_green,gameloop)
        buttons('Exit',550,450,100,50,red,light_red,quit)
        pygame.display.update()
        clock.tick(20)

def paused():
    while pause:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()

        display.fill(white)
        smalltext=pygame.font.Font('freesansbold.ttf',75)
        textsurface,textrect=text_objects('You Paused',smalltext)
        textrect.center=((display_w/2),(display_h/2))#to center the text
        display.blit(textsurface,textrect)

        buttons('Continue',150,450,130,50,green,light_green,unpause)
        buttons('Exit',550,450,100,50,red,light_red,quit)
        pygame.display.update()
        clock.tick(20)

def score(c):
    font=pygame.font.SysFont(None,25)
    text=font.render('Score :'+str(c),True,black)
    display.blit(text,(0,0))

def things(tx,ty,tw,th,color):
    pygame.draw.rect(display,color,[tx,ty,tw,th])


def text_objects(text,font):
    textsurface=font.render(text,True,black)
    return textsurface,textsurface.get_rect()

def message_display(text):
    largetext=pygame.font.Font('freesansbold.ttf',50)
    textsurface,textrect=text_objects(text,largetext)
    textrect.center=((display_w/2),(display_h/2))#to center the text
    display.blit(textsurface,textrect)#to place the text on the screen
    pygame.display.update()
    end()

def crash():
    message_display('YOU CRASHED')

def car(x,y):
    display.blit(carimg,(x,y)) #add the image on screen

def gameloop():
    #crashed = False #for every game
    global pause
    x=(display_w*0.45)# these claculation to put the car at a certain position
    y=(display_h*0.8)#we put these in loop bcoz it is  position at start of game
    x_change=0
    count=0
    x_thing=random.randrange(0,display_w)
    x_thing1=random.randrange(0,display_w)
    y_thing=y_thing1=-400
    tspeed=7
    tspeed1=10
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    x_change=-5
                elif event.key==pygame.K_RIGHT:
                    x_change=5
                elif  event.key==pygame.K_p:
                    pause=True
                    paused()
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                    x_change=0
        x+=x_change
        display.fill(white) #to make the background white
        car(x,y)
        score(count)
        things(x_thing,y_thing,100,100,blue)# to display the image
        things(x_thing1,y_thing1,100,100,blue)
        y_thing+=tspeed
        y_thing1+=tspeed1
        if x<0 or x>display_w-70:
            count-=1
            crash()
        if y_thing>display_h:
            x_thing=random.randrange(0,display_w)
            y_thing=-100
            count+=1
        if y_thing1>display_h:
            x_thing1=random.randrange(0,display_w)
            y_thing1=-100
            count+=1

        if y_thing+100>y:
            if x_thing<x and x_thing+100>x or x_thing<x+70 and x_thing+100>x+70:
                    count-=1
                    crash()
        if y_thing1+100>y:
            if x_thing1<x and x_thing1+100>x or x_thing1<x+70 and x_thing1+100>x+70:
                    count-=1
                    crash()

        pygame.display.update()#responsible to change the display
        clock.tick(60) # no of frames per sec

intro()
gameloop()
pygame.quit()
quit()
