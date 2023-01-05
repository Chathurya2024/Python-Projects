#move()
#turn_left()
#jump()
#(x,y) =  (1,1)  (x,y) =(13,1)
def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move() 
    elif front_is_clear():
        move()
    else:
        turn_left()

      


   #if wall_on_right():
    #    turn_left()
     #   turn_left()
      #  turn_left()
        

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
