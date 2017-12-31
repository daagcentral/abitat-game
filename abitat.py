from time import sleep
class Board:
    
    def __init__(self, width, height):
        self.width = width #this tells you the width of the board ur playing with.
        self.height = height # and this tells u the height.
        W = self.width 
        H = self.height #assigns width and height to a variable
        self.data = [[' ']*W for row in range(H)] #self.data is the board

    def __repr__(self): # what this whole function does is show how the board is displayed, how it is represented.
        W = self.width
        H = self.height
        s = ''
        for r in range(H):
            s += '|'
            for c in range(W):
                 s += self.data[r][c] + ' |'
            s += '\n'

        s = s+ W*'|[]' + '|'
        s += '\n'        

        return s     



    def clear(self): # this function clears the board (idk if it works)
        self.data = [[' ']*self.width for row in range(self.height)]

    def movingThing(self): # this function is what controls the moving thing.
        H = self.height
        w = self.width
        ox = "[]" # this is the representation of the box
        a = 0   
        while True: 
            # this infinite loop checks whether the space next to the position 
            # the current box is and if it is free, moves it to the right
                
                
            if self.data[H][a] == ' ':
                self.data[H][a] = ox
                self.data[H][a-1] = ' '
                
            if a==w+1: # this tests whether or not the box runs out of space and is responsible for the "boincing back" of the box
                break
            a += 1
            print(self) # this prints to show the thing move per loop. 
        
                
        while True:
            # this is the same exact thing except it handles the backward movement of the bounce
            # i feel like running these 2 while loops in another infinate loop will help animate the for/backward movement of the block
                
            if self.data[H][a-1] == ' ':
                self.data[H][a-1] = ox
                self.data[H][a-2] = ' '
                
            if a==1:
                break
            a -= 1
            print(self)
        
            
    

  
    def winsFor(self):
        for i in range(self.width):
            for I in range(self.height):
                if self.data[0][I] == '[]':
                    return True
        return False 

 

    def hostGame(self):
        # this is supposed to stich the whole game together
        # HOWEVER, it's not working. Help!
        print("Welcome to Abitat game (Remade)!")
        print()
        print(self)
        print()
        while True: 
            
            print(self.movingThing)
            sleep(0.05)
