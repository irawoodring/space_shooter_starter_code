""""""
import pygame
from collideable import PowerupType, UtilityFunctions


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, manager):
        super().__init__()
        self.__assets = {}
        self.__load_assets()
        self.image = self.__assets['regular_image']
        self.rect = self.image.get_rect(center=(x, y))

        # Student to do

    def __load_assets(self):
        # Load images
        self.__assets['regular_image'] = pygame.image.load("./assets/ship.png").convert_alpha()
        self.__assets['shielded_image'] = pygame.image.load("./assets/shielded_ship.png").convert_alpha()
        self.__assets['invincible_image'] = pygame.image.load("./assets/ship2.png").convert_alpha()
        # Load sound effects
        self.__assets['sfx_fire'] = pygame.mixer.Sound("./assets/sfx_laser1.ogg")
        self.__assets['sfx_damage'] = pygame.mixer.Sound("./assets/sfx_twoTone.ogg")

    def update(self, dt):
        # Student to do
        pass

        # Collision with an enemy code
        hits = pygame.sprite.spritecollide(self, self.__manager.get_group('enemies'), False)
        if hits:
            if self.__shield:
                self.__shield = False
                self.image = self.__assets['regular_image']
            elif not self.__invincible:
                self.__health -= 10
                if self.__health <= 0:
                    self.__lives -= 1
                    self.__health = 100
            hits[0].kill()
            self.__assets['sfx_damage'].play()
        # PUT NEW CODE BELOW HERE

        hits = pygame.sprite.spritecollide(self, self.__manager.get_group('powerups'), False)
        if hits:
            pwr_type = hits[0].get_type()
            if pwr_type == PowerupType.CLEAR:
                self.__manager.clear_enemies()
            elif pwr_type == PowerupType.HEALTH:
                self.__health += 100
            elif pwr_type == PowerupType.SHIELD:
                self.image = self.__assets['shielded_image']
                self.__shield = True
            elif pwr_type == PowerupType.INVINCIBLE:
                self.__invincible = True
                self.__invincible_timer = 0
                self.image = self.__assets['invincible_image']
            hits[0].kill()

        # Student to do
        pass

    def get_invincible(self):
        # Student to do
        pass
    
    def get_health(self):
        # Student to do
        pass
    
    def get_lives(self):
        # Student to do
        pass


class PlayerLaser(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("./assets/playerLaser.png").convert_alpha()  # preserves transparency
        self.rect = self.image.get_rect(center=(x, y))
        self.__speed = 1000

    def update(self, dt):
        self.rect.y -= self.__speed * dt

        if self.rect.y < 0:
            self.kill()