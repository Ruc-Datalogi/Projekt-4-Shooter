import sys, pygame, random, os

class Upgrades:


    bullet_damage_dictionary = {"1": "15", "2": "50", "3": "100","4": "200", "5": "350", "6": "500","7": "850", "8": "1200", "9": "1600"}

    bullet_amount_dictionary = {"1": "15", "2": "50", "3": "100","4": "200", "5": "350", "6": "500","7": "850", "8": "1200", "9": "1600"}

    bullet_fire_speed_dictionary = {"1": "15", "2": "50", "3": "100","4": "200", "5": "350", "6": "500","7": "850", "8": "1200", "9": "1600"}

    shield_dictionary = {"1": "15", "2": "50", "3": "100","4": "200", "5": "350", "6": "500","7": "850", "8": "1200", "9": "1600"}

    def get_price_bullet_damage(self, current_level):
        price = self.bullet_damage_dictionary[current_level]
        return price

    def get_price_bullet_amount(self, current_level):
        price = self.bullet_amount_dictionary[current_level]
        return price

    def get_price_fire_speed(self, current_level):
        price = self.bullet_fire_speed_dictionary[current_level]
        return price

    def get_price_shield(self, current_level):
        price = self.shield_dictionary[current_level]
        return price