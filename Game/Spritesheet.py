# This class handles sprite sheets
# This was taken from www.scriptefun.com/transcript-2-using
# sprite-sheets-and-drawing-the-background
# I've added some code to fail if the file wasn't found..
# Note: When calling images_at the rect is the format:
# (x, y, x + offset, y + offset)
#####This Class has been copy-pasted from 'https://www.pygame.org/wiki/Spritesheet'#####
import pygame 


class Spritesheet(object):

    def __init__(self,  filename):
        try:
            self.sheet = pygame.image.load(filename)
        except pygame.error:
            print('unable to load sprite sheet: ')
            raise SystemExit

    def image_at(self, rectangle):
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0,0), rect)
        color_key = image.get_at((0,0))
        image.set_colorkey(color_key)

        return image

    def images_at(self, rects):
        return [self.image_at(rect) for rect in rects]
