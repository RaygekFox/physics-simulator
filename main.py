import pygame
import sys

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
property_forces = {(prop, force): [] for prop in properties for force in forces}


particle_properties[("proton", "mass")] = 1.6726219e-27
particle_properties[("proton", "charge")] = 1.60217663e-19
particle_properties[("electron", "mass")] = 9.1093837e-31
particle_properties[("electron", "charge")] = -1.60217663e-19

print(particle_properties[("proton", "mass")] * particle_properties[("electron", "mass")])



class Particle:
    def __init__(self):
        self.radius = 10
        self.x = 0
        self.y = 0
        self.x_vel = 0
        self.y_vel = 0




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
