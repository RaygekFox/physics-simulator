import pygame
import sys
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock



pygame.init()
clock = pygame.time.Clock()


# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

scale = 1
properties = ["mass", "charge"]
forces = ["gravity", "electric"]
particles = ["proton", "electron"]



particle_properties = {(particle, prop): 0.0 for particle in particles for prop in properties}
property_forces = {(prop, force): [] for prop in properties for force in forces} #must be in the following format: [force at distance 0, distance where force is 0]



class Particle:
    def __init__(self):
        self.radius = 10
        self.x = 0
        self.y = 0
        self.x_vel = 0
        self.y_vel = 0
        self.fixed = False




# Game setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Physics Simulator")





while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()







pygame.display.flip()
clock.tick(FPS)



pygame.quit()
sys.exit()
