##Ayush kumar 202125,Prince Kumar 22378,Nishchay Sharma
##calculator
##used pygame module and its functions


import pygame

pygame.init()

a,b=720,375
calculator = pygame.display.set_mode((a,b))

white=(255,255,255)
orange=(255,165,0)
black=(0,0,0)
addx=(0,0)

pygame.display.set_caption("CALCULATOR")

font = pygame.font.SysFont('Ariel',30)

cal=[325,23]

t=False

l=[]
l0=[]
while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
        if i.type == pygame.MOUSEBUTTONDOWN:
            
            
            if addx[0]/2<=pointer[0]<addx[0]/2+75 and addx[1]<=pointer[1]<=addx[1]/2+75:
                l0.append("1")
            
                if t:
                    l0=[]
                    t=False
            
            
            if addx[0]/2+75<=pointer[0]<addx[0]/2+150 and addx[1]<=pointer[1]<=addx[1]/2+75:
                l0.append("2")
            
                if t:
                    l0=[]
                    t=False
            
            
            if addx[0]/2+150<=pointer[0]<addx[0]/2+225 and addx[1]<=pointer[1]<=addx[1]/2+75:
                l0.append("3")
            
                if t:
                    l0=[]
                    t=False
            
            
            if addx[0]/2+225<=pointer[0]<addx[0]/2+300 and addx[1]<=pointer[1]<=addx[1]/2+75:
                l0.append("4")
            
                if t:
                    l0=[]
                    t=False
            
            
            if addx[0]/2<=pointer[0]<addx[0]/2+75 and addx[1]+75<=pointer[1]<=addx[1]/2+150:
                l0.append("5")
            
                if t:
                    l0=[]
                    t=False
            
            
            if addx[0]/2+75<=pointer[0]<addx[0]/2+150 and addx[1]+75<=pointer[1]<=addx[1]/2+150:
                l0.append("6")
            
                if t:
                    l0=[]
                    t=False
            
            
            if addx[0]/2+150<=pointer[0]<addx[0]/2+225 and addx[1]+75<=pointer[1]<=addx[1]/2+150:
                l0.append("7")
            
                if t:
                    l0=[]
                    t=False
            
            
            if addx[0]/2+225<=pointer[0]<addx[0]/2+300 and addx[1]+75<=pointer[1]<=addx[1]/2+150:
                l0.append("8")
            
                if t:
                    l0=[]
                    t=False
            
            
            if addx[0]/2<=pointer[0]<addx[0]/2+75 and addx[1]+150<=pointer[1]<=addx[1]/2+225:
                l0.append("9")
            
                if t:
                    l0=[]
                    t=False
            
            
            if addx[0]/2+75<=pointer[0]<addx[0]/2+150 and addx[1]+150<=pointer[1]<=addx[1]/2+225:
                l0.append("0")
            
                if t:
                    l0=[]
                    t=False
            
            
            if addx[0]/2+150<=pointer[0]<addx[0]/2+225 and addx[1]+150<=pointer[1]<=addx[1]/2+225:
                l0.append("(")
            
                if t:
                    l0=[]
                    t=False
            
            
            if addx[0]/2+225<=pointer[0]<addx[0]/2+300 and addx[1]+150<=pointer[1]<=addx[1]/2+225:
                l0.append(")")
            
                if t:
                    l0=[]
                    t=False
            
            
            if addx[0]/2<=pointer[0]<addx[0]/2+75 and addx[1]+225<=pointer[1]<=addx[1]/2+300:
                l0.append("+")
            
                if t:
                    l0=[]
                    t=False
            
            
            if addx[0]/2+75<=pointer[0]<addx[0]/2+150 and addx[1]+225<=pointer[1]<=addx[1]/2+300:
                l0.append("-")
            
                if t:
                    l0=[]
                    t=False
            
            
            if addx[0]/2+150<=pointer[0]<addx[0]/2+225 and addx[1]+225<=pointer[1]<=addx[1]/2+300:
                l0.append("*")
            
                if t:
                    l0=[]
                    t=False
            
            
            if addx[0]/2+225<=pointer[0]<addx[0]/2+300 and addx[1]+225<=pointer[1]<=addx[1]/2+300:
                l0.append("/")
            
                if t:
                    l0=[]
                    t=False
            
            
            if addx[0]/2<=pointer[0]<addx[0]/2+75 and addx[1]+300<=pointer[1]<=addx[1]/2+375:
                l0.append(".")
            
                if t:
                    l0=[]
                    t=False
            
            
            if addx[0]/2+75<=pointer[0]<addx[0]/2+150 and addx[1]+300<=pointer[1]<=addx[1]/2+375:
                l0=[]
            
                if t:
                    l0=[]
                    t=False
            
            
            if addx[0]/2+150<=pointer[0]<addx[0]/2+225 and addx[1]+300<=pointer[1]<=addx[1]/2+375:
                l0.pop()
            
                if t:
                    l0=[]
                    t=False
            
            if addx[0]/2+225<=pointer[0]<addx[0]/2+300 and addx[1]+300<=pointer[1]<=addx[1]/2+375:
                t=True
        calculator.fill(white)
        pygame.display.update()
    pointer=pygame.mouse.get_pos()
    
    for i in range(len(l0)):
        if cal[0]+15*i<720:
            calculator.blit(font.render(l0[i],True,black),(325+15*i,cal[1]))
        if cal[0]+15*i>720:
            calculator.blit(font.render(l0[i],True,black),(325+15*i-395,cal[1]+(40)))
        if cal[0]+15*i>1110:
    
            calculator.blit(font.render("OVERFLOW",True,black),(325,105))
    if t:
        try:
            k=(str(eval("".join(l0))))
            calculator.blit(font.render(k,True,black),(325,105))
        except:
            calculator.blit(font.render("INVALID SYNTAX",True,black),(325,105))
    
    
    pygame.display.update()
    pygame.draw.rect(calculator, black, pygame.Rect(0, 0, 75, 75),  2, 0, 0, 0)
    pygame.draw.rect(calculator, black, pygame.Rect(75, 0, 75, 75),  2, 0, 0, 0)
    pygame.draw.rect(calculator, black, pygame.Rect(150, 0, 75, 75),  2, 0, 0, 0)
    pygame.draw.rect(calculator, black, pygame.Rect(225, 0, 75, 75),  2, 0, 0, 0,)
    pygame.draw.rect(calculator, black, pygame.Rect(0, 75, 75, 75),  2, 0, 0, 0)
    pygame.draw.rect(calculator, black, pygame.Rect(75, 75, 75, 75),  2, 0, 0, 0)
    pygame.draw.rect(calculator, black, pygame.Rect(150, 75, 75, 75),  2, 0, 0, 0)
    pygame.draw.rect(calculator, black, pygame.Rect(225, 75, 75, 75),  2, 0, 0, 0,)
    pygame.draw.rect(calculator, black, pygame.Rect(0, 150, 75, 75),  2, 0, 0, 0)
    pygame.draw.rect(calculator, black, pygame.Rect(75, 150, 75, 75),  2, 0, 0, 0)
    pygame.draw.rect(calculator, black, pygame.Rect(150, 150, 75, 75),  2, 0, 0, 0)
    pygame.draw.rect(calculator, black, pygame.Rect(225, 150, 75, 75),  2, 0, 0, 0,)
    pygame.draw.rect(calculator, black, pygame.Rect(0, 225, 75, 75),  2, 0, 0, 0)
    pygame.draw.rect(calculator, black, pygame.Rect(75, 225, 75, 75),  2, 0, 0, 0)
    pygame.draw.rect(calculator, black, pygame.Rect(150, 225, 75, 75),  2, 0, 0, 0)
    pygame.draw.rect(calculator, black, pygame.Rect(225, 225, 75, 75),  2, 0, 0, 0,)
    pygame.draw.rect(calculator, black, pygame.Rect(0, 300, 75, 75),  2, 0, 0, 0)
    pygame.draw.rect(calculator, black, pygame.Rect(75, 300, 75, 75),  2, 0, 0, 0)
    pygame.draw.rect(calculator, black, pygame.Rect(150, 300, 75, 75),  2, 0, 0, 0)
    pygame.draw.rect(calculator, black, pygame.Rect(225, 300, 75, 75),  2, 0, 0, 0,)
    
    calculator.blit(font.render("1",True,black),(34,23))
    calculator.blit(font.render("2",True,black),(109,23))
    calculator.blit(font.render("3",True,black),(184,23))
    calculator.blit(font.render("4",True,black),(259,23))
    calculator.blit(font.render("5",True,black),(34,98))
    calculator.blit(font.render("6",True,black),(109,98))
    calculator.blit(font.render("7",True,black),(184,98))
    calculator.blit(font.render("8",True,black),(259,98))
    calculator.blit(font.render("9",True,black),(34,173))
    calculator.blit(font.render("0",True,black),(109,173))
    calculator.blit(font.render("(",True,black),(184,173))
    calculator.blit(font.render(")",True,black),(259,173))
    calculator.blit(font.render("+",True,black),(34,248))
    calculator.blit(font.render("-",True,black),(109,248))
    calculator.blit(font.render("*",True,black),(184,248))
    calculator.blit(font.render("/",True,black),(259,248))
    calculator.blit(font.render(".",True,black),(34,323))
    calculator.blit(font.render("C",True,(255,0,0)),(109,323))
    calculator.blit(font.render("<",True,(255,0,0)),(184,323))
    calculator.blit(font.render("=",True,orange),(259,323))
