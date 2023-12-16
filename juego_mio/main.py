import random

import pygame as pg
from character import Character

pg.init()
screen_info = pg.display.Info()
height = screen_info.current_h
width = screen_info.current_w
screen = pg.display.set_mode((width, height))
initiate = True
p_one = Character("Player 1", 100, 0, 50, width / 8 * 6, 500, (255, 255, 0), 0, 0, 0, 0, [])
p_two = Character("Player 2", 100, 0, 50, 200, 500, (0, 0, 255), 0, 0, 0, 0, [])

clock = pg.time.Clock()

w_pressed = False
a_pressed = False
d_pressed = False
s_pressed = False
up_pressed = False
down_pressed = False
left_pressed = False
right_pressed = False
one_shoots = False
two_shoots = False
particulas = []
num_destellos = 150
for i in range(num_destellos):
    random_x = random.randint(0, width)
    random_y = random.randint(0, height)
    random_size = random.randint(5, 12)
    destello = random.randint(25, 200)
    particulas.append((random_x, random_y, random_size, destello))


def increase_speed(player):
    player.y_speed += player.y_acceleration
    player.x_speed += player.x_acceleration
    if player.y_speed > 10:
        player.y_speed = 10
    if player.y_speed < - 10:
        player.y_speed = - 10
    if player.x_speed > 10:
        player.x_speed = 10
    if player.x_speed < - 10:
        player.x_speed = - 10


def show_particles(particles):
    for m in range(num_destellos):
        particles[m] = (
            particles[m][0],
            particles[m][1],
            particles[m][2],
            particles[m][3] - 1
        )
        if particles[m][3] < 5:
            particles[m] = (
                random.randint(0, width),
                random.randint(0, height),
                random.randint(5, 12),
                random.randint(25, 200)
            )
        pg.draw.rect(screen, (particles[m][3], particles[m][3], particles[m][3]),
                     (particles[m][0], particles[m][1], particles[m][2], particles[m][2]))


while initiate:
    square_one = pg.Rect(p_one.posx, p_one.posy, p_one.height, p_one.height)
    square_two = pg.Rect(p_two.posx, p_two.posy, p_two.height, p_two.height)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            initiate = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                initiate = False

            if event.key == pg.K_w:
                p_one.y_acceleration = - 0.3
                w_pressed = True
            if event.key == pg.K_d:
                p_one.x_acceleration = 0.3
                d_pressed = True
            if event.key == pg.K_s:
                p_one.y_acceleration = 0.3
                s_pressed = True
            if event.key == pg.K_a:
                p_one.x_acceleration = - 0.3
                a_pressed = True
            if event.key == pg.K_UP:
                p_two.y_acceleration = - 0.3
                up_pressed = True
            if event.key == pg.K_RIGHT:
                p_two.x_acceleration = 0.3
                right_pressed = True
            if event.key == pg.K_DOWN:
                p_two.y_acceleration = 0.3
                down_pressed = True
            if event.key == pg.K_LEFT:
                p_two.x_acceleration = - 0.3
                left_pressed = True
            if event.key == pg.K_SPACE:
                one_shoots = True
            if event.key == pg.K_KP_0:
                two_shoots = True

        if event.type == pg.KEYUP:
            if event.key == pg.K_w and w_pressed:
                if p_one.y_speed < 0:
                    p_one.y_acceleration = 0.3
                w_pressed = False
            if event.key == pg.K_s and s_pressed:
                if p_one.y_speed > 0:
                    p_one.y_acceleration = - 0.3
                s_pressed = False
            if event.key == pg.K_a and a_pressed:
                if p_one.x_speed < 0:
                    p_one.x_acceleration = 0.3
                a_pressed = False
            if event.key == pg.K_d and d_pressed:
                if p_one.x_speed > 0:
                    p_one.x_acceleration = - 0.3
                d_pressed = False
            if event.key == pg.K_UP and up_pressed:
                if p_two.y_speed < 0:
                    p_two.y_acceleration = 0.3
                up_pressed = False
            if event.key == pg.K_DOWN and down_pressed:
                if p_two.y_speed > 0:
                    p_two.y_acceleration = - 0.3
                down_pressed = False
            if event.key == pg.K_LEFT and left_pressed:
                if p_two.x_speed < 0:
                    p_two.x_acceleration = 0.3
                left_pressed = False
            if event.key == pg.K_RIGHT and right_pressed:
                if p_two.x_speed > 0:
                    p_two.x_acceleration = - 0.3
                right_pressed = False

    if 0.4 > p_one.y_speed > -0.4 and not w_pressed and not s_pressed:
        p_one.y_speed = 0
        p_one.y_acceleration = 0
    if 0.4 > p_one.x_speed > -0.4 and not a_pressed and not d_pressed:
        p_one.x_speed = 0
        p_one.x_acceleration = 0
    if 0.4 > p_two.y_speed > -0.4 and not up_pressed and not down_pressed:
        p_two.y_speed = 0
        p_two.y_acceleration = 0
    if 0.4 > p_two.x_speed > -0.4 and not left_pressed and not right_pressed:
        p_two.x_speed = 0
        p_two.x_acceleration = 0

    increase_speed(p_one), increase_speed(p_two)
    screen.fill((0, 0, 0))

    if (
            p_one.posx < p_two.posx + p_two.height and
            p_one.posx + p_one.height > p_two.posx and
            p_one.posy < p_two.posy + p_two.height and
            p_one.posy + p_one.height > p_two.posy
    ):

        # Calcular superposición en ambas direcciones
        overlap_x = min(p_one.posx + p_one.height, p_two.posx + p_two.height) - max(p_one.posx,
                                                                                    p_two.posx)
        overlap_y = min(p_one.posy + p_one.height, p_two.posy + p_two.height) - max(p_one.posy,
                                                                                    p_two.posy)

        # Ajustar posiciones en consecuencia
        if overlap_x < overlap_y:
            if p_one.posx < p_two.posx:
                p_one.posx -= overlap_x
                p_two.posx += overlap_x
            else:
                p_one.posx += overlap_x
                p_two.posx -= overlap_x
        else:
            if p_one.posy < p_two.posy:
                p_one.posy -= overlap_y
                p_two.posy += overlap_y
            else:
                p_one.posy += overlap_y
                p_two.posy -= overlap_y

        if overlap_x < overlap_y:  # the collision occurs from the sides
            if p_one.x_acceleration != 0 and p_two.x_acceleration == 0:
                aux = p_one.x_speed
                aux2 = p_one.x_acceleration
                p_one.x_speed = p_two.x_speed
                p_two.x_speed = aux
                p_two.x_acceleration = -aux2
                if not a_pressed and not d_pressed:
                    p_two.x_acceleration = aux2
                else:
                    if p_one.x_acceleration < 0 and left_pressed:
                        p_two.x_acceleration = -aux2
                    elif p_one.x_acceleration < 0 and right_pressed:
                        p_two.x_acceleration = aux2
                    elif p_one.x_acceleration > 0 and right_pressed:
                        p_two.x_acceleration = aux2
                    elif p_one.x_acceleration > 0 and left_pressed:
                        p_two.x_acceleration = -aux2

            elif p_two.x_acceleration != 0 and p_one.x_acceleration == 0:
                aux = p_two.x_speed
                aux2 = p_two.x_acceleration
                p_two.x_speed = p_one.x_speed
                p_one.x_speed = aux
                p_one.x_acceleration = -aux2
                if not left_pressed and not right_pressed:
                    p_one.x_acceleration = aux2
                else:
                    if p_two.x_acceleration < 0 and a_pressed:
                        p_one.x_acceleration = -aux2
                    elif p_two.x_acceleration < 0 and d_pressed:
                        p_one.x_acceleration = aux2
                    elif p_two.x_acceleration > 0 and d_pressed:
                        p_one.x_acceleration = aux2
                    elif p_two.x_acceleration > 0 and a_pressed:
                        p_one.x_acceleration = -aux2

            elif p_two.x_acceleration != 0 and p_one.x_acceleration != 0:
                if p_two.x_acceleration > 0:
                    if p_one.x_acceleration < 0:  # 1-> <-2
                        print("1, 2")
                        if (p_two.x_speed > 0 > p_one.x_speed) or (  # 2-> <-1  # 2-> 1->
                                p_two.x_speed < 0 > p_one.x_speed):  # # 2<- <-1 / 1<- 2<-
                            print(p_two.x_speed > 0 > p_one.x_speed)
                            print(p_two.x_speed > 0 < p_one.x_speed)
                            print(p_two.x_speed < 0 > p_one.x_speed)
                            aux = p_two.x_speed
                            p_two.x_speed = p_one.x_speed
                            p_one.x_speed = aux
                            print(1)
                        elif p_two.x_speed < 0 < p_one.x_speed:  # 1 -> <-2
                            aux = p_two.x_speed
                            aux2 = p_two.x_acceleration
                            p_two.x_speed = p_one.x_speed
                            p_two.x_acceleration = p_one.x_acceleration
                            p_one.x_speed = aux
                            p_one.x_acceleration = aux2
                            print("2")
                        elif p_two.x_speed > 0 < p_one.x_speed:
                            aux = p_two.x_speed
                            p_two.x_speed = p_one.x_speed
                            p_one.x_speed = aux
                            p_two.x_acceleration = p_one.x_acceleration

                    elif p_one.x_acceleration > 0:
                        print("3, 4")
                        if (p_two.x_speed < 0 > p_one.x_speed) or (  # 1<- 2<- / 2<- 1<-
                                p_two.x_speed > 0 < p_one.x_speed):  # 1-> 2-> / 2-> 1->
                            print(p_two.x_speed < 0 > p_one.x_speed)
                            print(p_two.x_speed > 0 < p_one.x_speed)
                            aux = p_two.x_speed
                            p_two.x_speed = p_one.x_speed
                            p_one.x_speed = aux
                            print(3)
                        elif p_two.x_speed > 0 > p_one.x_speed:  # 1-> <-2
                            print(p_two.x_speed > 0 > p_one.x_speed)
                            aux = p_two.x_speed
                            aux2 = p_two.x_acceleration
                            p_two.x_speed = p_one.x_speed
                            p_two.x_acceleration = p_one.x_acceleration
                            p_one.x_speed = aux
                            p_one.x_acceleration = -aux2
                            print(4)
                        elif p_two.x_speed < 0 < p_one.x_speed:
                            print(p_two.x_speed < 0 < p_one.x_speed)
                            aux = p_two.x_speed
                            p_two.x_speed = p_one.x_speed
                            p_one.x_speed = aux
                            p_two.x_acceleration = -p_two.x_acceleration
                            print(4.5)

                elif p_two.x_acceleration < 0:
                    if p_one.x_acceleration > 0:  # 1-> <-2
                        print("5, 6")
                        if (p_one.x_speed > 0 > p_two.x_speed) or (  # 1-> <-2
                                p_one.x_speed > 0 < p_two.x_speed) or (  # 1-> 2->
                                p_one.x_speed < 0 > p_two.x_speed):  # 2<- <-1 / 1<- 2<-
                            print(p_one.x_speed > 0 > p_two.x_speed)
                            print(p_one.x_speed > 0 < p_two.x_speed)
                            print(p_one.x_speed < 0 > p_two.x_speed)
                            aux = p_one.x_speed
                            p_one.x_speed = p_two.x_speed
                            p_two.x_speed = aux
                            print(5)
                        elif p_one.x_speed < 0 < p_two.x_speed:  # 2 -> <-1
                            aux = p_one.x_speed
                            aux2 = p_one.x_acceleration
                            p_one.x_speed = p_two.x_speed
                            p_one.x_acceleration = p_two.x_acceleration
                            p_two.x_speed = aux
                            p_two.x_acceleration = aux2
                            print("6")

                    elif p_one.x_acceleration < 0:
                        print("7, 8")
                        if (p_one.x_speed < 0 > p_two.x_speed) or (  # 1<- 2<- / 2<- 1<-
                                p_one.x_speed > 0 < p_two.x_speed):  # 1-> 2-> / 2-> 1->
                            print(p_one.x_speed < 0 > p_two.x_speed)
                            print(p_one.x_speed > 0 < p_two.x_speed)
                            aux = p_one.x_speed
                            p_one.x_speed = p_two.x_speed
                            p_two.x_speed = aux
                            print(7)
                        elif p_one.x_speed < 0 < p_two.x_speed:  # 2-> <-1
                            print(p_one.x_speed < 0 < p_two.x_speed)
                            aux = p_one.x_speed
                            aux2 = p_one.x_acceleration
                            p_one.x_speed = p_two.x_speed
                            p_one.x_acceleration = p_two.x_acceleration
                            p_two.x_speed = aux
                            p_two.x_acceleration = -aux2
                            print(8)
                        elif p_one.x_speed > 0 > p_two.x_speed:
                            print(p_one.x_speed > 0 > p_two.x_speed)
                            aux = p_two.x_speed
                            p_two.x_speed = p_one.x_speed
                            p_one.x_speed = aux
                            p_one.x_acceleration = -p_one.x_acceleration
                            print(8.5)

        if overlap_x > overlap_y:  # the collition occurs either from the top or from the bottom
            if p_one.y_acceleration != 0:
                aux = p_one.y_speed
                aux2 = p_one.y_acceleration
                p_one.y_speed = p_two.y_speed
                p_two.y_speed = aux
                p_two.y_acceleration = -aux2
                if not w_pressed and not s_pressed:
                    p_two.y_acceleration = aux2
                else:
                    if p_one.y_acceleration < 0 and up_pressed:
                        p_two.y_acceleration = -aux2
                    elif p_one.y_acceleration < 0 and down_pressed:
                        p_two.y_acceleration = aux2
                    elif p_one.y_acceleration > 0 and down_pressed:
                        p_two.y_acceleration = aux2
                    elif p_one.y_acceleration > 0 and up_pressed:
                        p_two.y_acceleration = -aux2

            elif p_two.y_acceleration != 0:
                aux = p_two.y_speed
                aux2 = p_two.y_acceleration
                p_two.y_speed = p_one.y_speed
                p_one.y_speed = aux
                p_one.y_acceleration = -aux2
                if not up_pressed and not down_pressed:
                    p_one.y_acceleration = aux2
                else:
                    if p_two.y_acceleration < 0 and w_pressed:
                        p_one.y_acceleration = -aux2
                    elif p_two.y_acceleration < 0 and s_pressed:
                        p_one.y_acceleration = aux2
                    elif p_two.y_acceleration > 0 and s_pressed:
                        p_one.y_acceleration = aux2
                    elif p_two.y_acceleration > 0 and w_pressed:
                        p_one.y_acceleration = -aux2

            elif p_two.y_acceleration != 0 and p_one.y_acceleration != 0:
                if p_two.y_acceleration > 0:
                    if p_one.y_acceleration < 0:  # 1-> <-2
                        print("1, 2")
                        if (p_two.y_speed > 0 > p_one.y_speed) or (  # 2-> <-1  # 2-> 1->
                                p_two.y_speed < 0 > p_one.y_speed):  # # 2<- <-1 / 1<- 2<-
                            print(p_two.y_speed > 0 > p_one.y_speed)
                            print(p_two.y_speed > 0 < p_one.y_speed)
                            print(p_two.y_speed < 0 > p_one.y_speed)
                            aux = p_two.y_speed
                            p_two.y_speed = p_one.y_speed
                            p_one.y_speed = aux
                            print(1)
                        elif p_two.y_speed < 0 < p_one.y_speed:  # 1 -> <-2
                            aux = p_two.y_speed
                            aux2 = p_two.y_acceleration
                            p_two.y_speed = p_one.y_speed
                            p_two.y_acceleration = p_one.y_acceleration
                            p_one.y_speed = aux
                            p_one.y_acceleration = aux2
                            print("2")
                        elif p_two.y_speed > 0 < p_one.y_speed:
                            aux = p_two.y_speed
                            p_two.y_speed = p_one.y_speed
                            p_one.x_speed = aux
                            p_two.y_acceleration = p_one.y_acceleration

                    elif p_one.y_acceleration > 0:
                        print("3, 4")
                        if (p_two.y_speed < 0 > p_one.y_speed) or (  # 1<- 2<- / 2<- 1<-
                                p_two.y_speed > 0 < p_one.y_speed):  # 1-> 2-> / 2-> 1->
                            print(p_two.y_speed < 0 > p_one.y_speed)
                            print(p_two.y_speed > 0 < p_one.y_speed)
                            aux = p_two.y_speed
                            p_two.y_speed = p_one.y_speed
                            p_one.y_speed = aux
                            print(3)
                        elif p_two.y_speed > 0 > p_one.y_speed:  # 1-> <-2
                            print(p_two.y_speed > 0 > p_one.y_speed)
                            aux = p_two.y_speed
                            aux2 = p_two.y_acceleration
                            p_two.y_speed = p_one.y_speed
                            p_two.y_acceleration = p_one.y_acceleration
                            p_one.y_speed = aux
                            p_one.y_acceleration = -aux2
                            print(4)
                        elif p_two.y_speed < 0 < p_one.y_speed:
                            print(p_two.y_speed < 0 < p_one.y_speed)
                            aux = p_two.y_speed
                            p_two.y_speed = p_one.y_speed
                            p_one.y_speed = aux
                            p_two.y_acceleration = -p_two.y_acceleration
                            print(4.5)

                elif p_two.y_acceleration < 0:
                    if p_one.y_acceleration > 0:  # 1-> <-2
                        print("5, 6")
                        if (p_one.y_speed > 0 > p_two.y_speed) or (  # 1-> <-2
                                p_one.y_speed > 0 < p_two.y_speed) or (  # 1-> 2->
                                p_one.y_speed < 0 > p_two.y_speed):  # 2<- <-1 / 1<- 2<-
                            print(p_one.y_speed > 0 > p_two.y_speed)
                            print(p_one.y_speed > 0 < p_two.y_speed)
                            print(p_one.y_speed < 0 > p_two.y_speed)
                            aux = p_one.y_speed
                            p_one.y_speed = p_two.y_speed
                            p_two.y_speed = aux
                            print(5)
                        elif p_one.y_speed < 0 < p_two.y_speed:  # 2 -> <-1
                            aux = p_one.y_speed
                            aux2 = p_one.y_acceleration
                            p_one.y_speed = p_two.y_speed
                            p_one.y_acceleration = p_two.y_acceleration
                            p_two.y_speed = aux
                            p_two.y_acceleration = aux2
                            print("6")

                    elif p_one.y_acceleration < 0:
                        print("7, 8")
                        if (p_one.y_speed < 0 > p_two.y_speed) or (  # 1<- 2<- / 2<- 1<-
                                p_one.y_speed > 0 < p_two.y_speed):  # 1-> 2-> / 2-> 1->
                            print(p_one.y_speed < 0 > p_two.y_speed)
                            print(p_one.y_speed > 0 < p_two.y_speed)
                            aux = p_one.y_speed
                            p_one.y_speed = p_two.y_speed
                            p_two.y_speed = aux
                            print(7)
                        elif p_one.y_speed < 0 < p_two.y_speed:  # 2-> <-1
                            print(p_one.y_speed < 0 < p_two.y_speed)
                            aux = p_one.y_speed
                            aux2 = p_one.y_acceleration
                            p_one.y_speed = p_two.y_speed
                            p_one.y_acceleration = p_two.y_acceleration
                            p_two.y_speed = aux
                            p_two.y_acceleration = -aux2
                            print(8)
                        elif p_one.y_speed > 0 > p_two.y_speed:
                            print(p_one.y_speed > 0 > p_two.y_speed)
                            aux = p_two.y_speed
                            p_two.y_speed = p_one.y_speed
                            p_one.y_speed = aux
                            p_one.y_acceleration = -p_one.y_acceleration
                            print(8.5)

    if d_pressed or w_pressed or a_pressed or s_pressed:
        if d_pressed:
            p_one.x_acceleration = 0.3
        if w_pressed:
            p_one.y_acceleration = - 0.3
        if a_pressed:
            p_one.x_acceleration = - 0.3
        if s_pressed:
            p_one.y_acceleration = 0.3
    else:
        if p_one.x_speed > 0:
            p_one.x_acceleration = - 0.3
        elif p_one.x_speed < 0:
            p_one.x_acceleration = 0.3
        if p_one.y_speed > 0:
            p_one.y_acceleration = - 0.3
        elif p_one.y_speed < 0:
            p_one.y_acceleration = 0.3

    if up_pressed or down_pressed or left_pressed or right_pressed:
        if up_pressed:
            p_two.y_acceleration = - 0.3
        if down_pressed:
            p_two.y_acceleration = 0.3
        if right_pressed:
            p_two.x_acceleration = 0.3
        if left_pressed:
            p_two.x_acceleration = - 0.3
    else:
        if p_two.x_speed > 0:
            p_two.x_acceleration = - 0.3
        elif p_two.x_speed < 0:
            p_two.x_acceleration = 0.3
        if p_two.y_speed > 0:
            p_two.y_acceleration = - 0.3
        elif p_two.y_speed < 0:
            p_two.y_acceleration = 0.3

    if one_shoots:
        p_one.attack()
        # print(p_one.bullets_shot)
        one_shoots = False
    if two_shoots:
        p_two.attack()
        # print(p_two.bullets_shot)
        two_shoots = False

    for i in range(len(p_one.bullets_shot) - 1, -1, -1):
        if (
                p_two.posx < p_one.bullets_shot[i][2] + p_one.bullets_shot[i][-1] and
                p_two.posx + p_two.height > p_one.bullets_shot[i][2] and
                p_two.posy < p_one.bullets_shot[i][3] + p_one.bullets_shot[i][-1] and
                p_two.posy + p_two.height > p_one.bullets_shot[i][3]
        ):
            p_two.recieve_attack(10)
            p_one.height += 5
            p_one.bullets_shot.pop(i)

    for i in range(len(p_two.bullets_shot) - 1, -1, -1):
        if (
                p_one.posx < p_two.bullets_shot[i][2] + p_two.bullets_shot[i][-1] and
                p_one.posx + p_one.height > p_two.bullets_shot[i][2] and
                p_one.posy < p_two.bullets_shot[i][3] + p_two.bullets_shot[i][-1] and
                p_one.posy + p_one.height > p_two.bullets_shot[i][3]
        ):
            p_one.recieve_attack(10)
            p_two.height += 5
            p_two.bullets_shot.pop(i)

    random_x = random.randint(0, width)
    random_y = random.randint(0, height)
    random_size = random.randint(5, 12)
    p_one.move_vertically(p_one.y_speed, height, w_pressed, s_pressed)
    p_one.move_horizontally(p_one.x_speed, width, a_pressed, d_pressed)
    p_two.move_vertically(p_two.y_speed, height, up_pressed, down_pressed)
    p_two.move_horizontally(p_two.x_speed, width, left_pressed, right_pressed)
    show_particles(particulas)
    pg.draw.rect(screen, p_one.color, (p_one.posx, p_one.posy, p_one.height, p_one.height))
    pg.draw.rect(screen, p_two.color, (p_two.posx, p_two.posy, p_two.height, p_two.height))
    for i in range(len(p_one.bullets_shot)):
        print(p_one.bullets_shot)
        p_one.bullets_shot[i] = (
            p_one.bullets_shot[i][0],
            p_one.bullets_shot[i][1],
            p_one.bullets_shot[i][2] + p_one.bullets_shot[i][0],
            p_one.bullets_shot[i][3] + p_one.bullets_shot[i][1],
            p_one.bullets_shot[i][4],
            p_one.bullets_shot[i][5]
        )
        pg.draw.rect(screen, (243, 255, 51), (
            p_one.bullets_shot[i][2], p_one.bullets_shot[i][3], p_one.bullets_shot[i][4], p_one.bullets_shot[i][5]))
    for i in range(len(p_one.bullets_shot) - 1, -1, -1):
        if p_one.bullets_shot[i][2] + p_one.height < 0 or p_one.bullets_shot[i][2] > width or p_one.bullets_shot[i][3] < 0 or p_one.bullets_shot[i][3] > height:
            p_one.bullets_shot.pop(i)

    #  jugador 2
    for i in range(len(p_two.bullets_shot)):
        print(p_two.bullets_shot)
        p_two.bullets_shot[i] = (
            p_two.bullets_shot[i][0],
            p_two.bullets_shot[i][1],
            p_two.bullets_shot[i][2] + p_two.bullets_shot[i][0],
            p_two.bullets_shot[i][3] + p_two.bullets_shot[i][1],
            p_two.bullets_shot[i][4],
            p_two.bullets_shot[i][5]
        )
        pg.draw.rect(screen, (0, 0, 255), (
            p_two.bullets_shot[i][2], p_two.bullets_shot[i][3], p_two.bullets_shot[i][4], p_two.bullets_shot[i][5]))
    for i in range(len(p_two.bullets_shot) - 1, -1, -1):
        if p_two.bullets_shot[i][2] + p_two.height < 0 or p_two.bullets_shot[i][2] > width or p_two.bullets_shot[i][3] < 0 or p_two.bullets_shot[i][3] > height:
            p_two.bullets_shot.pop(i)

    clock.tick(144)

    pg.display.update()
