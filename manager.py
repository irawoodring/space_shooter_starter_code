import pygame
from collideables import ObjectSpawner
from starfield import StarField
from hud_elements import HudElement
from player import Player


class GameManager:
    def __init__(self, engine):
        pass

    def __setup_groups(self):
        # Add sprite groups
        self.add_group('all')
        self.add_group('enemies')
        self.add_group('projectiles')
        self.add_group('powerups')
        self.__groups['starfield'] = StarField()
        
        self.add_object(self.__player)
        self.add_object(self.__object_spawner)

    def __setup_hud(self):
        self.__score_hud = HudElement("Score: 0", self.__hud_font, (100, 20))
        self.__time_hud = HudElement("Time: 0", self.__hud_font, (400, 20))
        self.__health_hud = HudElement("Health: 100", self.__hud_font, (700, 20))
        self.__lives_hud = HudElement("Lives: 3", self.__hud_font, (900, 20))
        self.add_object(self.__score_hud)
        self.add_object(self.__time_hud)
        self.add_object(self.__health_hud)
        self.add_object(self.__lives_hud)

    def update(self, dt):
        self.__time += dt
        self.__time_hud.change_text(f"Time: {self.__time:.2f}")
        self.__health_hud.change_text(f"Health: {self.__player.health}")
        self.__lives_hud.change_text(f"Lives: {self.__player.lives}")

        self.__elapsed_time += dt
        if self.__elapsed_time >= 10.0:
            self.__elapsed_time -= 10.0
            self.__speed_multiplier += 0.1
        if self.__player.lives < 0:
            self.__engine.running = False
