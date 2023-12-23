import pygame as pg

pg.init()

screen = pg.display.set_mode((600, 600))
pg.display.set_caption("나만의 캐릭터 움직임")

running = True

background_img = pg.image.load("풀밭.png")
character_img = pg.image.load("images.jfif")
character_img = pg.transform.scale(character_img,(100,100))

character_img_pos = [0,0]

while running:
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT or event.key == pg.K_a:
                character_img_pos[0] -= 5
            elif  event.key == pg.K_RIGHT or event.key == pg.K_d:
                character_img_pos[0] += 5
            elif event.key == pg.K_UP or event.key == pg.K_w:
                character_img_pos[1] -= 5
            elif event.key == pg.K_DOWN or event.key == pg.K_s:
                character_img_pos[1] += 5
        elif event.type == pg.QUIT:
            running = False
    screen.blit(background_img, background_img.get_rect())
    screen.blit(character_img, character_img_pos)
    pg.display.update()
pg.quit()