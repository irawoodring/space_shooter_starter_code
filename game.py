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
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.__running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.__running = False
        return events
    
    def get_running(self):
        return self.__running
    
    def set_running(self, running):
        if isinstance(running, bool):
            self.__running = running

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
