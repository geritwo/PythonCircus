'''
TkWanderer Game view funcions
'''

from tkinter import *
from PIL import Image, ImageTk

class LevelDisplay:

    def __init__(self, area_dimensions):

        # Init area variables:
        self.tile_width = 72
        self.status_area_height = 20 # NOTE: If below game area. Not implemented.
        self.status_area_width = 160
        self.canvas_width = area_dimensions[1]*self.tile_width+self.status_area_width
        self.canvas_height = area_dimensions[0]*self.tile_width

        # Init canvas:
        self.root = Tk()
        self.root.title("*** TkWanderer Game ***")
        self.canvas = Canvas(self.root, width=self.canvas_width, height=self.canvas_height)
        self.canvas.pack()
        self.root.geometry("860x792+20+20")

        # Init imagery:
        self.floor_image = PhotoImage(file='./img/floor.png')
        self.wall_image = PhotoImage(file='./img/wall.png')
        self.hero_image = PhotoImage(file='./img/hero-down.png')

        self.hero_down = PhotoImage(file='./img/hero-down.png')
        self.hero_up = PhotoImage(file='./img/hero-up.png')
        self.hero_left = PhotoImage(file='./img/hero-left.png')
        self.hero_right = PhotoImage(file='./img/hero-right.png')

        self.boss = PhotoImage(file='./img/boss.png')
        self.skeleton = PhotoImage(file='./img/skeleton.png')


    # *** [ Display functions in tkinter mainloop ] ***

    def display_area(self, area_dimensions, area_floorplan):
        select_tile_pattern_display = {'0': self.floor_image, '1': self.wall_image}

        for row in range(area_dimensions[0]):
            for column in range(area_dimensions[1]):
                self.canvas.create_image(column*self.tile_width, row*self.tile_width, anchor=NW, image=select_tile_pattern_display[area_floorplan[row][column]])

    def display_hero(self, hero_position, heading):
        if heading == "Up":
            hero_heading_image = self.hero_up
        if heading == "Down":
            hero_heading_image = self.hero_down
        if heading == "Left":
            hero_heading_image = self.hero_left
        if heading == "Right":
            hero_heading_image = self.hero_right
        self.canvas.create_image(hero_position[0]*self.tile_width, hero_position[1]*self.tile_width, anchor=NW, image=hero_heading_image)

    def display_enemies(self, enemy_type, enemy_position):
        if enemy_type == 'Boss':
            enemy_view_image = self.boss
        if enemy_type == 'Skeleton':
            enemy_view_image = self.skeleton

        self.canvas.create_image(enemy_position[0]*self.tile_width, enemy_position[1]*self.tile_width, anchor=NW, image=enemy_view_image)

    def dislay_stats(self, hero_stats, enemy_stats, action):

        hero_stats_display = ' *** STATS ***\n\n Hero (Level {})\n\n | HP: {}/{} \n | DP: {} \n | SP: {}'.format(hero_stats[0], hero_stats[1], hero_stats[2], hero_stats[3], hero_stats[4])

        self.canvas.create_text(self.canvas_width-self.status_area_width, 0, text=hero_stats_display, anchor=NW, fill='white', width=self.status_area_width, font='14')

        enemy_stats_display = ' *** ENEMY ***\n\n | HP: {} \n | DP: {} \n | SP: {}'.format(enemy_stats[0], enemy_stats[1], enemy_stats[2])

        self.canvas.create_text(self.canvas_width-self.status_area_width, 160, text=enemy_stats_display, anchor=NW, fill='white', width=self.status_area_width, font='14')

        action_display = ' *** ACTION ***\n\n' + ' ' + action
        self.canvas.create_text(self.canvas_width-self.status_area_width, 280, text=action_display, anchor=NW, fill='white', width=self.status_area_width, font='14')


    # *** [ View control funcions ] ***
    def clear_display(self):
        self.canvas.delete('all')

    def show(self):
        self.root.mainloop()
