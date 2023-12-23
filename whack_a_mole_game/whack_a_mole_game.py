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
background_img = pg.image.load("whack_a_mole_game/src/background.png")
mole_img = pg.image.load("whack_a_mole_game/src/mole.png")
running = True
score = 0
font = pg.font.SysFont("nanumbarungothic", 50)
mole_pos = [(25, 45), (200, 45), (370, 45), (540, 45), (25, 175), (200, 175), (370, 175), (540, 175), (25, 305), (200, 305), (370, 305), (540, 305)]

while running:
    time = pg.time.get_ticks() // 1000

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            score += 1

        if time >= 10:
            if score >= 20:
                print("victory")
                running = False
            else:
                print("lose")
                running = False

    time_text = font.render(str(time), True, (0, 0, 0), None)
    score_text = font.render(str(score), True, (0, 0, 0), None)
    
    screen.blit(background_img, background_img.get_rect())
    screen.blit(time_text, (680, 55))
    screen.blit(score_text, (55, 55))

    pg.display.update() 
    pg.time.wait(1000)


pg.quit()
