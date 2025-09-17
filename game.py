"""Core game loop logic.  Updates and
draws objects after setting up the screen.
"""
import sys
import pygame
from manager import GameManager


class GameEngine:    
    def __init__(self, width=1024, height=768, title="Louis' Revenge"):
        pygame.init()
        pygame.mixer.init() 
       
        self.__screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)

        # Add a game manager and player object
        self.__manager = GameManager(self)
        self.__clock = pygame.time.Clock()
        self.__running = True

    def handle_events(self):
        # Student to do
        pass
    
    def get_running(self):
        # Student to do
        pass
    
    def set_running(self, running):
        # Student to do
        pass

    def run(self):
        # Uncomment these lines if you want music!
        #pygame.mixer.music.load("./assets/cosmic_annihilation.mp3")
        #pygame.mixer.music.set_volume(0.3)
        #pygame.mixer.music.play(-1)
        while self.__running:
            # Student to do
            pass


if __name__ == "__main__":
    game = GameEngine(1024, 768, "Louie's Revenge")
    game.run()