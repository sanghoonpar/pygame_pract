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
hammer_img = pg.image.load("pygame_pract/whack_a_mole_game/src/hammer.png")
hammer_img = pg.transform.scale(hammer_img, (150, 150))
running = True
vic_img = pg.image.load("pygame_pract/whack_a_mole_game/src/victory.jpg")
los_img = pg.image.load("pygame_pract/whack_a_mole_game/src/lose.jfif")
vic_img = pg.transform.scale(vic_img, (400, 400))
los_img = pg.transform.scale(los_img, (400, 400))
score = 0
font = pg.font.SysFont("nanumbarungothic", 50)
mole_pos = [(35, 70), (210, 70), (380, 70), (550, 70), (35, 210), (210, 210), (380, 210), (550, 210), (35, 340), (210, 340), (380, 340), (550, 340)]
check_time = True
moles = []
pg.mouse.set_visible(False)

while running:
    screen.blit(background_img, background_img.get_rect())
    time = pg.time.get_ticks() // 1000
    time_text = font.render(str(time), True, (0, 0, 0), None)
    score_text = font.render(str(score), True, (0, 0, 0), None)

    # 이벤트 처리
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEBUTTONDOWN:
            for mole in moles:
                if mole.collidepoint(event.pos):
                    score += 1
                    moles.remove(mole)
                    break

    # 2초에 한번씩 두더지 생성
    if ((time % 2) == 0) and check_time == True:
            add_mole = screen.blit(mole_img, random.choice(mole_pos))
            moles.append(add_mole)
            check_time = False
            print(add_mole)
    elif ((time % 2) == 1):
        check_time = True


    for mole in moles:
        screen.blit(mole_img, mole)


    if time > 20:
        if score >= 10:
            pg.time.delay(500)
            screen.blit(vic_img, (200,150))
            pg.display.update()
            pg.time.delay(3000)
            running = False
        else:
            pg.time.delay(500)
            screen.blit(los_img, (200,150))
            pg.display.update()
            pg.time.delay(3000)
            running = False

    screen.blit(time_text, (680, 55))
    screen.blit(score_text, (55, 55))
    screen.blit(hammer_img, pg.mouse.get_pos())
    pg.display.update()

pg.quit()