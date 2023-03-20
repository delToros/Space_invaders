import pygame as pg, random
import pygame.event


class Missile(pg.sprite.Sprite):
    """Class for missile launch"""
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.image.load("assets/missile.png")
        self.rect = self.image.get_rect()
        self.rect.midbottom = (x, y)
        self.velocity = 5

    def update(self):
        self.fly()

    def fly(self):
        self.rect.y -= self.velocity
        if self.rect.y < 0:
            self.kill()



class Player(pg.sprite.Sprite):
    """Class defining player"""
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.image.load("assets/player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.velocity = 5

    def update(self):
        self.move()

    def move(self):
        """Moving player"""
        self.keys = pg.key.get_pressed()
        if self.keys[pg.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.velocity
            self.image = pg.image.load("assets/player-left.png")
        # else:
        #     self.image = pg.image.load("assets/player.png")

        elif self.keys[pg.K_RIGHT] and self.rect.right < 600:
            self.rect.x += self.velocity
            self.image = pg.image.load("assets/player-right.png")
        else:
            self.image = pg.image.load("assets/player.png")


class Lives(pg.sprite.Sprite):
    """Class for missile launch"""
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.image.load("assets/lives.png")
        self.rect = self.image.get_rect()
        self.rect.midbottom = (x, y)


class EnemyMissile(pg.sprite.Sprite):
    """Class for missile launch"""
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.image.load("assets/enemy-missile.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocity = 5


    def update(self):
        self.fly()

    def fly(self):
        self.rect.y += self.velocity
        if self.rect.y > 910:
            self.kill()



class Enemy(pg.sprite.Sprite):
    """Class for enemy"""
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.image.load('assets/enemy1.png')
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.velocity = 2

    def update(self):
        self.move()
        # self.fire()

    def move(self):
        """Move enemy"""
        self.rect.x += self.velocity

    def change_direction(self):
        self.velocity *= -1

    # def fire(self):
    #     num = random.randint(1, 2)
    #     if num == 2:
    #         print('yeah')
    #         mis = EnemyMissile(self.rect.centerx, self.rect.centery)
    #         mis.update()


class Enemy2(pg.sprite.Sprite):
    """Class for enemy"""
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.image.load('assets/enemy2.png')
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.velocity = 2

    def update(self):

        self.move()

    def move(self):
        """Move enemy"""
        self.rect.x += self.velocity

    def change_direction(self):
        self.velocity *= -1