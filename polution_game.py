# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 14:30:15 2022
"""

# Importing the library
import pygame
from pygame.locals import *
import sys
import time
import math

import matplotlib.pyplot as plt

# Initializing Pygame
pygame.init()
  
# Initializing surface
surface = pygame.display.set_mode((400,300))
  
# Initializing Color
green = (0, 255, 0)
red = (255, 0, 0)
white = (255, 255, 255)

# Drawing Rectangle
pygame.draw.rect(surface, green, pygame.Rect(30, 30, 60, 60))
pygame.draw.rect(surface, green, pygame.Rect(30, 93, 60, 60))
pygame.draw.rect(surface, green, pygame.Rect(93, 30, 60, 60))
pygame.draw.rect(surface, green, pygame.Rect(93, 93, 60, 60))
pygame.display.flip()

global factories, emissions

class Factory:
    def __init__(self, em, x, y, _id, sub, policy):
        self.polution = 0
        self.emissions = em
        self.x = x
        self.y = y
        self._id = _id
        self.subsidies = sub
        self.profit = 0
        self.policy = policy
        self.emis_temp = 0

    def Produce(self, polution_cost_from_neigh):
        polution_costs_to_neigh = 0
        # short term profit
        self.stp = 0
        # subtract the environmental policy costs
        if self.policy == True:
            temp = self.subsidies - 3
            self.emissions = math.ceil(self.emissions /2)
        else:
            temp = self.subsidies - 1
            polution_costs_to_neigh = 1
        
        self.emis_temp = self.emis_temp + self.emissions 
        
        self.stp = temp - polution_cost_from_neigh
        
        if self.polution < 255:
            self.profit = self.profit + self.stp
            print("Factory ", self._id, " accuired ", self.stp, " for a total profit of ", self.profit)
        else:
            print("Ecosystem ", self._id, " is dead, nothing lives here long enough to produce profits.")        
        self.polution = self.polution + self.emissions
    
        return polution_costs_to_neigh
    
    def neighbour_polutants(self, amount):
        self.polution = self.polution + amount
        if self.polution > 255:
            self.polution = 255
        

def update_tile(factory):    
    r = factory.polution
    
    died = False
    to_polute_neigh = 0
    if r > 255:
        r = 255
        to_polute_neigh = factory.emissions
        died = True
        print("Tile ", factory._id, " has max polution - ecosystem destroyed.")
    
    g = 255 - factory.polution
    if g < 0:
        g = 0
    color = (r, g, 0)
    #print(color)
    pygame.draw.rect(surface, color, pygame.Rect(factory.x, factory.y, 60, 60))
    
    return died, to_polute_neigh

def draw_letter(surface, x, y, _id):
    # create a font object.
    # 1st parameter is the font file
    # which is present in pygame.
    # 2nd parameter is size of the font
    font = pygame.font.Font('freesansbold.ttf', 32)
     
    # create a text surface object,
    # on which text is drawn on it.
    text = font.render(_id, True, white, None)
     
    # create a rectangular object for the
    # text surface object
    textRect = text.get_rect()
     
    # set the center of the rectangular object.
    #textRect.center = (35 // 2, 60 // 2)
    textRect.x = x
    textRect.y = y
    
    # copying the text surface object
    # to the display surface object
    # at the center coordinate.
    surface.blit(text, textRect)    
     
def print_policies(factories):
    print("Current ppolicies: ")
    for f in factories:
        if f.policy:
            print("Factory ", f._id, " has active policy.")
        else:
            print("Factory ", f._id, " has passive policy.")
    
def main():
    global factories, emissions, emis_temp

    # remember # of active policies per iteration
    policies = []

    # long term profits per iteration
    ltps = []

    # short term profits per iteration
    stps = []   
    
    # individual profits per iteration
    ips = [[] for i in range(0, 4)]

    # number of total rounds
    rounds = []
    
    # total emissions per iteration (avg)
    emissions = []

    # get all possible combinations of factories and their policies
    mask0 = 0x01
    mask1 = 0x02
    mask2 = 0x04
    mask3 = 0x08
    for cnt in range(0, 16):
        factories = []
        factories.append(Factory(5, 30, 30, 'A', 5, cnt & mask0))
        factories.append(Factory(5, 93, 30, 'B', 5, cnt & mask1))
        factories.append(Factory(5, 30, 93, 'C', 5, cnt & mask2))
        factories.append(Factory(5, 93, 93, 'D', 5, cnt & mask3))
        
        print_policies(factories)
    
        # game loop
        t0 = time.clock()
        t1 = time.clock()
        
        # reset emissions counter
        emis_temp = 0
        
        _round = 0
        while True:
            #print(t1 - t0)
            #if------------------------------------------------------------------------------
            #if t1 - t0 > 1:
            end_cnt = 0

            for i in range(0, len(factories)):
                fs = [x for j,x in enumerate(factories) if j != i]
                neigh_polution = 0
                for f in fs:
                    if f.policy == False:
                        neigh_polution = neigh_polution + 1
                
                polution_costs_to_neigh = factories[i].Produce(neigh_polution)
                
                died, polution_trickle = update_tile(factories[i])
                print(polution_trickle)
                if died:
                    end_cnt = end_cnt + 1
                
                # polution starts creeping out of current tile to neighbouring ones
                if polution_trickle > 0:
                    temp = polution_trickle // 3
                    
                    for f in fs:
                        f.neighbour_polutants(temp)
                draw_letter(surface, factories[i].x, factories[i].y, factories[i]._id)
            
            pygame.display.flip()
            _round = _round + 1
            t0 = time.clock()
        
            # Simulation ends here - when no factories are operational
            if end_cnt == len(factories):
                # long term profit
                ltp = 0
                # short term profit
                stp = 0
                
                # emssions counter
                em_temp = 0
                
                num_active_policies = 0
                for i in range(0, len(factories)):
                    # individual profit
                    ips[i].append(factories[i].stp)
                    
                    ltp = ltp + factories[i].profit
                    stp = stp + factories[i].stp
                    
                    em_temp = em_temp + factories[i].emis_temp
                    
                    if factories[i].policy:
                        num_active_policies = num_active_policies + 1
                ltps.append(ltp)
                stps.append(stp)
                policies.append(num_active_policies)
                
                emissions.append(em_temp / 4)
                
                rounds.append(_round)
                
                print("All factories are out of bussiness.")
                print("At least one ecosystem survived for ", _round, " rounds")
                break
            print("------------------Next round-------------------------")
        
            # event loop
            for event in pygame.event.get():
               if event.type == QUIT:
                   pygame.quit()
                   sys.exit()
        #end if--------------------------------------------------------------------------         
        t1 = time.clock()
    pygame.quit()
    #sys.exit()
    fig, ax = plt.subplots(5)
    fig.tight_layout()
    
    ax[0].plot(range(0, 16), ltps)
    ax[0].set_title("(Overall - Sum) Long term profits per iteration")

    ax[1].plot(range(0, 16), stps)
    ax[1].set_title("(Overall - Sum) Short term profits per iteration")

    ax[2].plot(range(0, 16), policies)
    ax[2].set_title("# of active policies per iteration")
    
    ax[3].plot(range(0, 16), rounds)
    ax[3].set_title("# of rounds per iteration")
    
    ax[4].plot(range(0, 16), emissions)
    ax[4].set_title("Emissions")
    #----------------------------------------------------------------------
    fig, ax = plt.subplots(2, 2)
    fig.tight_layout()
    ax[0 ,0].plot(range(0, 16), ips[0])
    ax[0, 0].set_title("Individual profits for factory #0")

    ax[0, 1].plot(range(0, 16), ips[1])
    ax[0, 1].set_title("Individual profits for factory #1")

    #plt.plot(range(0, 16), profits)
    ax[1, 0].plot(range(0, 16), ips[2])
    ax[1, 0].set_title("Individual profits for factory #2")
    
    #plt.plot(range(0, 16), profits)
    ax[1, 1].plot(range(0, 16), ips[3])
    ax[1, 1].set_title("Individual profits for factory #3")
main()