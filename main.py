from screen_rect import *
from controls_colliding import ai_movement, obj_user_movement

pg.init()


while run:
    clock.tick(FPS)
    #those lines ables us to terminate the program and some other functionality
    for event in pg.event.get():
        if event.type == pg.QUIT:   
            run = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                run = False
            if event.key == pg.K_0:
                rects = random_squares(1)

    keys_pressed = pg.key.get_pressed()
    obj_main3.move(keys_pressed)

    screen.fill(background)

    obj_main3.draw(screen)

    for id, rect in enumerate(rects):   #this is an awesome built-in method :)
        rect.move_bot(id, velocity=3)
        rect.draw(screen) 

        
    

        

    pg.display.flip() #how is it diffrent from update?


pg.quit()
