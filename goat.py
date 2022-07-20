from cs1graphics import*
from time import sleep

class Goat(Layer):

    def __init__(self,furColor='brown'):
        """This class creates an instance of a goat and performs
        some traditional and some less traditional actions that
        a real goat would perform.

        Some of these methods include,standing,walking,sitting,eating.
        Some of the less traditional actions include changing fur colr,
        eye color and tail color at will.The fur color of every goat can
        be defaulted at the call of the class and the refernce point of e
        very goat instance is the center of the ellipse that forms the trunk."""
        
        super().__init__()

        
        self._neck=Path(Point(50,50),Point(75,75))               #The goat's neck is a Path
        self._neck.setBorderWidth(4)
        self._neck.moveTo(-45,-20)
        self.add(self._neck)
 
        self._horns=Layer()                                      #Goat's horns
        self._horns1=Path(Point(55,50),Point(70,30))
        self._horns1.setBorderWidth(3)
        self._horns1.moveTo(-55,-30)
        self._horns2=Path(Point(70,50),Point(70,40))
        self._horns2.setBorderWidth(3)
        self._horns2.moveTo(-41,-49)
        self._horns.add(self._horns1)
        self._horns.add(self._horns2)
        self._hornleft=self._horns.clone()
        self._hornleft.flip()
        self._hornleft.moveTo(-100,0)
        self.add(self._horns)
        self.add(self._hornleft)

        self._leg1=Path(Point(25,50),Point(25,25))             #Goat's legs
        self._leg1.setBorderWidth(4)
        self._leg1.moveTo(20,40)
        self._leg2=self._leg1.clone()
        self._leg2.moveTo(-10,40)
        self.add(self._leg1)
        self.add(self._leg2)
        
        self._trunk=Ellipse(75,40)                             #Creates the trunk of the goat
        self._trunk.setFillColor(furColor)
        self.add(self._trunk)
 
        self._goathead=Ellipse(35,25)                          #Creates the goat's head
        self._goathead.moveTo(-50,-25)
        self._goathead.setFillColor(furColor)
        self._goathead.setBorderColor('transparent')
        self.add(self._goathead)

        self._eye=Layer()                                       #Creates the goat's eye
        self._white=Circle(3,Point(-60,-30))
        self._white.setFillColor('white')
        self._black=Circle(1,Point(-60,-30))
        self._black.setFillColor('black')
        self._eye.add(self._white)
        self._eye.add(self._black)
        self.add(self._eye)

        self._tail=Circle(5,Point(40,0))                         #Creates the goat's tail
        self._tail.setFillColor('Black')
        self.add(self._tail)
        
        self._chatbubble=Layer()                                  #Creates the chatbubble for speech
        self._bubble=Ellipse(95,50)
        self._bubble.setFillColor('lightcyan')
        self._bubble.moveTo(100,10)
        self._attach=Polygon(Point(175,100),Point(185,50),Point(195,100))
        self._attach.rotate(145)
        self._attach.setFillColor('lightcyan')
        self._attach.move(-55,-95)
        self._cover=Circle(5)
        self._cover.setFillColor('transparent')
        self._cover.setBorderColor('transparent')
        self._cover.move(126,30)
        self._cover.setDepth(40)
        self._chatbubble.add(self._cover)
        self._chatbubble.add(self._attach)
        self._chatbubble.add(self._bubble)
        self._chatbubble.setDepth(2)
        self._chatbubble.moveTo(10000,-90)
        self.add(self._chatbubble)

        self._words=Text('',12,Point(-900,-60))                     #Creates the text
        self._words.setDepth(2)
        self.add(self._words)
        #initial instances of added methods
        self.spoken=False 
        self.alreadyRight=False
        self.alreadyLeft=True                                       #every goat originally faces the left
        self.eaten=False
        self.seated=False

    def toggleSpeak(self,text):
        """This function allows the user to potray speech between the animals.

        It contols all the semantics of speech by first assessing what
        direction the animal is facing before adding text and a chatbubble
        that correspondings with the animal's line of visiion"""
        
        if self.alreadyLeft==True:                                   #positions chatbubble depending on the current direction the goat is facing
            if self.spoken==False:
                self._words.moveTo(-100,-80)
                self._chatbubble.moveTo(-200,-90)
                self._words.setMessage(text)
                self.spoken=True
            else:
                self._words.moveTo(-10000,-80)
                self._chatbubble.moveTo(-10000,-90)
                self.spoken=False
        elif self.alreadyRight==True:
            self._chatbubble.flip()
            if self.spoken==False:
                self._words.moveTo(100,-80)
                self._chatbubble.moveTo(200,-90)
                
                self._words.setMessage(text)
                self.spoken=True
            else:
                self._words.moveTo(-10000,-80)
                self._chatbubble.moveTo(-10000,-90)
                self.spoken=False
                
    def toggleEat(self,time=1):                                 #initial number of head roatations is 1
        """This function allows the user to show a
            simulation of the animals eating.

            It does thid by rotating and flipping various
            parts of the goat's head"""
        if self.alreadyLeft==True:                              #performs the rotation based on the direction the goat is facing
            if self.eaten==True:                                #animals cannot perform consecutive eating actions
                self._neck.flip()
                self._neck.move(-20,-30)
                self._goathead.move(0,-60)
                self._eye.move(0,-66)
                self._horns1.move(0,-63)
                self._horns2.move(0,-63)
                self._hornleft.move(0,-63)
                self._eaten=False
                
            else:
                self._neck.flip()
                self._neck.move(20,30)
                self._goathead.move(0,60)
                self._eye.move(0,66)
                self._horns1.move(0,63)
                self._horns2.move(0,63)
                self._hornleft.move(0,63)
                for i in range(time):                           #to support the alternating head rotations
                    if i%2==0:
                        self._goathead.rotate(20)
                    else:
                        self._goathead.rotate(-20)
                    sleep(0.2)
                self.eaten=True
        else:
            if self.eaten==True:
                self._neck.flip()
                self._neck.move(20,-30)
                self._goathead.move(0,-60)
                self._eye.move(0,-66)
                self._horns1.move(0,-63)
                self._horns2.move(0,-63)
                self._hornleft.move(0,-63)
                self._eaten=False
                
            else:
                self._neck.flip()
                self._neck.move(-20,30)
                self._goathead.move(0,60)
                self._eye.move(0,66)
                self._horns1.move(0,63)
                self._horns2.move(0,63)
                self._hornleft.move(0,63)
                for i in range(time):
                    if i%2==0:
                        self._goathead.rotate(20)
                    else:
                        self._goathead.rotate(-20)
                    sleep(0.2)
                self.eaten=True

    def toggleSit(self):
        """This function allows the user to show a
            simulation of the animals eating.

            It does thid by moving various
            parts of the goat's body and rotating its
            legs depending on which direction it's facing"""
        if self.seated==False:                            #Can only sit if its not already sitted
            self._neck.move(0,30)
            self._goathead.move(0,30)
            self._eye.move(0,33)
            self._horns1.move(0,33)
            self._horns2.move(0,33)
            self._hornleft.move(0,33)
            self._trunk.move(0,20)
            self._tail.move(0,20)
            if self.alreadyLeft==True:
                self._leg1.rotate(-90)
                self._leg2.rotate(-90)
            else:
                self._leg1.rotate(90)
                self._leg2.rotate(90)
        else:                                               #If it's already sitted,it goes back to standing position
            self._neck.move(0,-30)
            self._goathead.move(0,-30)
            self._eye.move(0,-33)
            self._horns1.move(0,-33)
            self._horns2.move(0,-33)
            self._hornleft.move(0,-33)
            self._trunk.move(0,-20)
            self._tail.move(0,-20)
            if self.alreadyLeft==True:
                self._leg1.rotate(90)
                self._leg2.rotate(90)
            else:
                self._leg1.rotate(-90)
                self._leg2.rotate(-90)
    

    def changeFurColor(self,color):
        """This function allows the user to change
            the fur color of the goat"""
        self._trunk.setFillColor(color)
        self._goathead.setFillColor(color)

    def changeEyeColor(self,color):
         """This function allows the user to change
            the eye color of the goat"""
         self._white.setFillColor(color)
        
    def changeTailColor(self,color):
         """This function allows the user to change
            the tail color of the goat"""
         self._tail.setFillColor(color)
        
    def walkLeft(self,steps):
        """This function allows the user to animate
            the goat walking towards the left"""
        for i in range(steps):
            if i%2==0:                                  #To alternate the leg rotation
                self._leg1.rotate(-20)
                self._leg2.rotate(20)
                self.move(-15,0)
            else:
                self._leg1.rotate(20)
                self._leg2.rotate(-20)
                self.move(-15,0)
            sleep(0.1)
            
    def walkRight(self,steps):
        """This function allows the user to animate
            the goat walking towards the right"""
        for i in range(steps):
            if i%2==0:
                self._leg1.rotate(20)                  #same as walkLeft but different angle
                self._leg2.rotate(-20)
                self.move(10,0)
            else:
                self._leg1.rotate(-20)
                self._leg2.rotate(20)
                self.move(10,0)
            sleep(0.2)
            
    def toggleLookRight(self):
        """This function allows the user to change
            the goat's line of vision to the right"""
        if self.alreadyRight==False:         
            self._goathead.move(100,0)
            self._tail.move(-80,0)
            self._eye.move(120,0)
            self._neck.move(90,0)
            self._neck.flip()
            self._horns.move(100,0)
            self._hornleft.move(100,0)
            self.alreadyRight=True
            self.alreadyLeft=False
        else:                                                #if its already facing right nothing changes
            pass
        
    def toggleLookLeft(self):
        """This function allows the user to change
            the goat's line of vision to the left"""
        if self.alreadyLeft==False:
            self._goathead.move(-100,0)
            self._tail.move(80,0)
            self._eye.move(-120,0)
            self._neck.move(-90,0)
            self._neck.flip()
            self._horns.move(-100,0)
            self._hornleft.move(-100,0)
            self.alreadyRight=False
            self.alreadyLeft=True
        else:
            pass                                        #if its already facing left nothing changes


if __name__=='__main__':
    paper=Canvas(725,500,'skyblue')
    sun=Circle(45,Point(725,0))
    sun.setFillColor('yellow')
    paper.add(sun)
    grass=Rectangle(875,250,Point(375,375))
    grass.setFillColor('green')
    grass.setBorderColor('green')
    paper.add(grass)
    
    mike=Goat('black')
    mike.moveTo(200,380)
    paper.add(mike)
    roger=Goat()
    roger.moveTo(400,380)
    paper.add(roger)
    sabrina=Goat('white')
    sabrina.moveTo(600,380)
    sabrina.scale(1.15)
    paper.add(sabrina)
    lola=Goat('Tomato')
    lola.changeEyeColor('green')
    lola.scale(1.2)
    lola.moveTo(100,380)
    paper.add(lola)
    
    sleep(1)
    roger.changeTailColor('maroon')
    sleep(1)
    mike.changeEyeColor('red')
    mike.toggleLookRight()
    sleep(1)
    roger.toggleSpeak('I am hungry')
    sleep(1)
    roger.toggleSpeak('')
    mike.toggleSpeak('same')
    sleep(1)
    mike.toggleSpeak('')
    sleep(1)
    mike.toggleSpeak('let us get food')
    sleep(1)
    mike.toggleSpeak('')
    mike.toggleLookLeft()
    roger.toggleSpeak('alright!')
    sleep(1)
    roger.toggleSpeak('')
    mike.toggleLookLeft()
    sleep(0.1)
    mike.walkLeft(23)
    roger.walkLeft(30)
    sabrina.changeFurColor('sienna')
    sleep(1)
    sabrina.toggleSpeak('Where u going?')
    sleep(1)
    sabrina.toggleSpeak('')
    lola.toggleLookRight()
    sabrina.toggleSpeak("There's food here")
    sleep(1)
    sabrina.toggleSpeak('')
    lola.toggleSpeak('exactly!')
    sleep(1)
    lola.toggleSpeak('')
    sabrina.toggleEat(6)
    lola.toggleEat(6)
    sleep(1)
    lola.toggleSpeak('time to rest')
    sabrina.toggleEat()
    lola.toggleEat()
    sleep(1)
    lola.toggleSpeak('')
    sabrina.toggleSit()
    lola.toggleSit()
    
    
    
   
    
    
