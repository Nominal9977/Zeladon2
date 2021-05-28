import random 

class Pet:

    

    def __init__(self,name):

        self.name = name
        self.x = 0
        self.y = 0
        self.dir = 0

        self.happiness = 5
        self.hunger = 5
        self.is_alive = True
        self.health = 10
        self.energy = 5
    def eat(self):

        if self.is_alive:
            g = random.randint(1,10)
            print( self.name + " eats food")
            if g == 7:
                print("oh no " + self.name + " got food poising and has died")
                self.is_alive = False 

            elif g == 3:
                d = random.randint(10,20)
                print (self.name + " has eaten the best food of his life +" + str(d) + " health")
                
                self.health += d

        else:
            print(self.name + " is dead")  
         
    def sleep(self):
        if self.is_alive:
            e = random.randint(7,7)
            print(self.name + " goes ' zzzzzzzzzzzzzzz....'")
            if e == 7:
                g = random.randint(1,5)
                print( self.name + " had the best sleep of his lfe + " + str(g)+ " energy")
                self.energy += g

        

        
        else:
            print(self.name + " is dead")  

    def play(self):
        if self.is_alive:
            g = random.randint (1,3)
            print(self.name + " goes ' yippee!'")
            if g == 1:
              r = random.randint (1,5)

              print( self.name + " has diecied to go on a walk -" + str(r) + " energy")

              self.energy -=r
              if self.energy < 0:
                    self.is_alive = False 
                

            elif g == 2:
                t = random.randint (1,6)
                print( self.name + "'s dog ran away so he had to chase it -" + str(t) + " energy")

                self.energy -=t

                if self.energy < 0:
                    self.is_alive = False 

            elif g == 3:
                h = random.randint(1,7)
                print( self.name + " diecied to go swiming -" + str(h) + " energy")
                if self.energy < 0:
                    self.is_alive = False 
                
            
        else:
            print(self.name + " is dead") 
    def rotate_right(self):
    
         if self.is_alive:
            self.dir +=1

            if self.dir > 3:
                self.dir =0

                print(self.name + " turns to right")
         else:
            print(self.name + " is dead") 

    def rotate_left(self):

        if self.is_alive:

            self.dir -=1
            if self.dir > -2:
                self.dir =0

                print(self.name + " turns to left")
        else:
            print(self.name + " is dead") 

    def kill(self,other):
        if self.is_alive:
           other.is_alive = False
           print(self.name + " kills " + other.name + ".")
           print(other.name + " goes 'AHHHHHHHHHHHH how could you'")

        else:
            print(self.name + " is dead") 



      

    def move(self):
        if self.is_alive:
            if self.dir==0:
                self.y+=1

            elif self.dir==1:
                self.x +=1

            elif self.dif == 2:
                self.y -= 1

            elif self.dir == 3:
                self.x -=1
            print(self.name + " moved forward.")
        else:
            print(self.name + " is dead")


    def attack(self, other):
        if self.is_alive:
            if other.is_alive:
                    d = random.randint(1,10)
                    c = random.randint(1,10)
                    print(self.name + " attacks " + other.name + ".")

                    if c == 10:
                        print(" critical hit!!")

                        d *= 2
                   
                    other.health -=d

                   
                  
                    print(other.name + " takes " + str(d) + " damage.")
                    print(other.name + " goes ' ahhhhhh how could you'")
                    
                    if other.health <=0:
                        other.is_alive = False
                        print(other.name + " has died ")
            else:
                print("why are we atacking a dead man?")
        else:
            print(self.name + " is dead")


        
        


# testing funtions #
p1=Pet("bob")
p2=Pet("mike")
p1.eat()
p1.sleep()
p2.attack(p1)
p1.eat()
p2.attack(p1)
p2.sleep()
p2.play()




 

    
        
        
         

    

        
        
