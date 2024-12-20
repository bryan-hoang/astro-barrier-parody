# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 17:13:47 2018

@author: Liam, Bryan, Eden
"""

import arcade

asset_path = "./assets"

SCREEN_WIDTH = 800


class Target(arcade.AnimatedTimeSprite):
    def __init__(self, scale, center_x, center_y):
        # take x and y vars from AnimatedTimeSprite)
        super().__init__(scale=scale, center_x=center_x, center_y=center_y)
        self.textures.append(
            arcade.load_texture(f"{asset_path}/astro_barrier_target.png")
        )
        self.textures.append(
            arcade.load_texture(f"{asset_path}/red_target.png", scale=0.5)
        )
        self.change_x = 0

    def update(self):
        if self.left <= 0:
            self.change_x = 5
        if self.right >= SCREEN_WIDTH:
            self.change_x = -5
        self.set_position(self.center_x + self.change_x, self.center_y)
