import sys, pygame, random, os
from JsonLoader import *

class Upgrades:

    bullet_damage_dictionary_level = {"1": "10", "2": "12", "3": "14","4": "16", "5": "18", "6": "20","7": "22", "8": "24", "9": "26"}

    bullet_amount_dictionary_level = {"1": "1", "2": "2", "3": "3"}

    bullet_fire_speed_dictionary_level = {"1": "15", "2": "14", "3": "13","4": "12", "5": "11", "6": "10","7": "9", "8": "8", "9": "7"}

    shield_dictionary_level = {"1": "1", "2": "1.2", "3": "1.4","4": "1.6", "5": "1.8", "6": "2"}

    def get_level_bullet_damage(self, current_level):
        level = self.bullet_damage_dictionary_level[current_level]
        return level

    def get_level_bullet_amount(self, current_level):
        level = self.bullet_amount_dictionary_level[current_level]
        return level

    def get_level_fire_speed(self, current_level):
        level = self.bullet_fire_speed_dictionary_level[current_level]
        return level

    def get_level_shield(self, current_level):
        level = self.shield_dictionary_level[current_level]
        return level

    #Prices of the upgrades compaired to their level

    bullet_damage_dictionary_price = {"1": "15", "2": "50", "3": "100","4": "200", "5": "350", "6": "500","7": "850", "8": "1200", "9": "1600"}

    bullet_amount_dictionary_price = {"1": "100", "2": "250", "3": "500"}

    bullet_fire_speed_dictionary_price = {"1": "15", "2": "50", "3": "100","4": "200", "5": "350", "6": "500","7": "850", "8": "1200", "9": "1600"}

    shield_dictionary_price = {"1": "15", "2": "50", "3": "100","4": "200", "5": "350", "6": "500"}

    def get_price_bullet_damage(self, current_level):
        price = self.bullet_damage_dictionary_price[current_level]
        return price

    def get_price_bullet_amount(self, current_level):
        price = self.bullet_amount_dictionary_price[current_level]
        return price

    def get_price_fire_speed(self, current_level):
        price = self.bullet_fire_speed_dictionary_price[current_level]
        return price

    def get_price_shield(self, current_level):
        price = self.shield_dictionary_price[current_level]
        return price


    def check_upgrade_bullet_damage(self):
        if int(JsonLoader.bullet_damage) < 9:
            if int(JsonLoader.get_coins(JsonLoader)) >= int(self.get_price_bullet_damage(self, JsonLoader.get_bullet_damage(JsonLoader))):
                JsonLoader.updateJsonFile(JsonLoader, 'subtract_coins', self.get_price_bullet_damage(self, JsonLoader.get_bullet_damage(JsonLoader)))
                JsonLoader.updateJsonFile(JsonLoader, 'upgrade_bullet_damage')

    def check_upgrade_bullet_amount(self):
        if int(JsonLoader.bullet_amount) < 3:
            if int(JsonLoader.get_coins(JsonLoader)) >= int(self.get_price_bullet_amount(self, JsonLoader.get_bullet_amount(JsonLoader))):
                JsonLoader.updateJsonFile(JsonLoader, 'subtract_coins', self.get_price_bullet_amount(self, JsonLoader.get_bullet_amount(JsonLoader)))
                JsonLoader.updateJsonFile(JsonLoader, 'upgrade_bullet_amount')   

    def check_upgrade_fire_speed(self):
        if int(JsonLoader.fire_speed) < 9:
            if int(JsonLoader.get_coins(JsonLoader)) >= int(self.get_price_fire_speed(self, JsonLoader.get_fire_speed(JsonLoader))):
                JsonLoader.updateJsonFile(JsonLoader, 'subtract_coins', self.get_price_fire_speed(self, JsonLoader.get_fire_speed(JsonLoader)))
                JsonLoader.updateJsonFile(JsonLoader, 'upgrade_fire_speed')  
    def check_upgrade_shield(self):
        if int(JsonLoader.shield) < 6:
            if int(JsonLoader.get_coins(JsonLoader)) >= int(self.get_price_shield(self, JsonLoader.get_shield(JsonLoader))):
                JsonLoader.updateJsonFile(JsonLoader, 'subtract_coins', self.get_price_shield(self, JsonLoader.get_shield(JsonLoader)))
                JsonLoader.updateJsonFile(JsonLoader, 'upgrade_shield')  