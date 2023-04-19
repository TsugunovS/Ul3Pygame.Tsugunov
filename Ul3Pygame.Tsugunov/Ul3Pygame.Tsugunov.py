
from lib2to3 import pygram
import pygame,sys

pygame.init()
def Liikumine():
	global posX,posY
	if posX==0 and posY==0:
		sammX=1
		sammY=0
	if posX==X-mesilane.get_rect().width and posY<=Y-mesilane.get_rect().height:
		sammX=0
		sammY=1
	if posX<=X-mesilane.get_rect().width and posY==Y-mesilane.get_rect().height:
		sammX=1
		sammY=0
		sammX=-sammX
	if posX==0 and posY>=Y-mesilane.get_rect().height:
		sammX=0
		sammY=1
		sammY=-sammY
	ekraan.blit(mesilane,(posX,posY))
	ekraan.blit(mesilane,(posX,posY))
	pygame.display.flip()
	ekraan.fill(roosa)


def Postoronam():
	global sammX,sammY
	if posX>X-mesilane.get_rect().width or posX<0:
		sammX=-sammX
	if posY>Y-mesilane.get_rect().height or posY<0:
		sammY=-sammY
	ekraan.blit(mesilane,(posX,posY))
	ekraan.blit(mesilane,(posX,posY))
	pygame.display.flip()
	ekraan.fill(roosa)



#värvid
kollane=[255,255,10]
punane=[255,0,0]
hall=[200,200,200]
roosa=[255,150,255]
roheline=[100,255,100]


#ekraani suurus
X=640
Y=480
ekraan=pygame.display.set_mode([X,Y])
pygame.display.set_caption("Animatsion")
ekraan.fill(roheline)
kell=pygame.time.Clock()
mesilane=pygame.image.load("bee.png")
#mesilane=pygame.image.load("ghost.png")
posX=X-mesilane.get_rect().width
posY=Y-mesilane.get_rect().height
lõpp=False
sammX=5
sammY=5
while not lõpp:
	kell.tick(60)
	events=pygame.event.get()
	for i in pygame.event.get():
		if i.type==pygame.quit():
			sys.exit()
	Liikumine()
	Postoronam()
	#if posX==0 and posY==0:
	#	sammX=1
	#	sammY=0
	#if posX==X-mesilane.get_rect().width and posY<=Y-mesilane.get_rect().height:
	#	sammX=0
	#	sammY=1
	#if posX<=X-mesilane.get_rect().width and posY==Y-mesilane.get_rect().height:
	#	sammX=1
	#	sammY=0
	#	sammX=-sammX
	#if posX==0 and posY>=Y-mesilane.get_rect().height:
	#	sammX=0
	#	sammY=1
	#	sammY=-sammY
	#ekraan.blit(mesilane,(posX,posY))
	#posX+=sammX
	#posY+=sammY
	####################
	#if posX>X-mesilane.get_rect().width or posX<0:
	#	sammX=-sammX
	#if posY>Y-mesilane.get_rect().height or posY<0:
	#	sammY=-sammY
	####################
	#if posX==0 and posY==0:
	#	sammX=1
	#	sammY=0
	#if posX==X-mesilane.get_rect().width and posY<=Y-mesilane.get_rect().height:
	#	sammX=0
	#	sammY=1
	#if posX<=X-mesilane.get_rect().width and posY==Y-mesilane.get_rect().height:
	#	sammX=1
	#	sammY=0
	#	sammX=-sammX
	#if posX==0 and posY>=Y-mesilane.get_rect().height:
	#	sammX=0
	#	sammY=1
	#	sammY=-sammY
	ekraan.blit(mesilane,(posX,posY))
	posX+=sammX
	posY+=sammY
	ekraan.blit(mesilane,(posX,posY))
	pygame.display.flip()
	ekraan.fill(roosa)
pygame.quit()
