class Character:
    def __init__(self, name, health, score, height, posx, posy, color, x_speed, y_speed, x_acceleration, y_acceleration, bullets_shot):
        self.name = name
        self.health = health
        self.score = score
        self.height = height
        self.posx = posx
        self.posy = posy
        self.color = color
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.x_acceleration = x_acceleration
        self.y_acceleration = y_acceleration
        self.bullets_shot = bullets_shot

    '''self.bullets_shot.append((20, 0, self.posx + self.height, self.posy + self.height / 2 - 5))'''
    def attack(self):
        if self.x_speed != 0 or self.y_speed != 0:
            self.bullets_shot.append((self.x_speed * 2, self.y_speed * 2, self.posx + self.height / 2 - 8.5, self.posy + self.height / 2 - 8.5, 17, 17))
        else:
            print("move to shoot!")

        print(f"{self.name} attacks!!")

    def recieve_attack(self, height):
        self.height -= height
        self.posx += height / 2
        self.posy += height / 2

    def move_horizontally(self, x_speed, height, left, right):
        if height - self.height > self.posx > 0:
            self.posx += x_speed
        else:
            if self.posx >= height - self.height:
                self.posx = height - self.height - 1
            if self.posx <= 0:
                self.posx = 1
            self.x_speed = -self.x_speed
            if not left and not right:
                if self.x_speed < 0 and self.x_acceleration < 0 or self.x_speed > 0 and self.x_acceleration > 0:
                    self.x_acceleration = - self.x_acceleration

    def move_vertically(self, y_speed, height, up, down):
        if height - self.height > self.posy > 0:
            self.posy += y_speed
        else:
            if self.posy <= 0:
                self.posy = 1
            if self.posy >= height - self.height:
                self.posy = height - self.height - 1
            self.y_speed = -self.y_speed
            if not up and not down:
                self.y_acceleration = -self.y_acceleration
