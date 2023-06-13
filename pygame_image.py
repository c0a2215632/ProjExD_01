import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    kk_img = pg.image.load("ex01-20230613/fig/3.png") 
    kt_img = pg.transform.flip(kk_img, True,False)
    bg_img = pg.image.load("ex01-20230613/fig/pg_bg.jpg")
    ku_img = pg.transform.rotozoom(kk_img,10,1.0)
    
    l=[kt_img,ku_img]
    tmr = 0
    
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        
        screen.blit(bg_img, [0-tmr, 0])
        
        screen.blit(kt_img,[300,200])
        pg.display.update()
        tmr += 1        
        clock.tick(100)
        if tmr>=800:
            tmr=-800


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()