import pygame as pg
import random
# 구현해야 할 기능 
# 게임 초기 세팅
# 타이머, 점수판
# 일정시간마다 토끼가 나온다. (랜덤한 위치에서)
# 이벤트 망치가 토끼에 닿으면 사라지고 점수 획득
# 시간제한 -> 성공/실패

pg.init()

screen = pg.display.set_mode((800, 600))
background_img = pg.image.load("pygame_pract/whack_a_mole_game/src/background.png")
mole_img = pg.image.load("pygame_pract/whack_a_mole_game/src/mole.png")
running = True
score = 0
font = pg.font.SysFont("nanumbarungothic", 50)
mole_pos = [(35, 70), (210, 70), (380, 70), (550, 70), (35, 210), (210, 210), (380, 210), (550, 210), (35, 340), (210, 340), (380, 340), (550, 340)]


while running:
    time = pg.time.get_ticks() // 1000
    time_text = font.render(str(time), True, (0, 0, 0), None)
    score_text = font.render(str(score), True, (0, 0, 0), None)
    moles = []
    check_time = True
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            if mole.collidepoint(event.pos):
                score += 1
                moles.remove(mole) 
                break

    if time // 1000 % 2 == 0:
        if check_time == True:
            add_mole = screen.blit(mole_img, random.choice(mole_pos))
            pg.display.update() 
            pg.time.wait(2000)
            moles.append(add_mole)
            check_time = False
    else:
        check_time = True
    
    for mole in moles:
        screen.blit(mole_img,mole)
        pg.display.update()
    
    if time > 20:
            if score >= 10:
                print("victory")
                running = False
            else:
                print("lose")
                running = False
                
    screen.blit(background_img, background_img.get_rect())
    screen.blit(time_text, (680, 55))
    screen.blit(score_text, (55, 55))

    pg.display.update() 

pg.quit()
