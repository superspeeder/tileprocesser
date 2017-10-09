import pygame

def construct_2d_list(width,height,placeholder=None):
  list_2d = []
  for row in height:
    list_2d.append([])
    for item in width:
      list_2d[-1].append(placeholder)
  return list_2d

class VMapMatrix2D(object):
  def __init__(self,width,height):
    self.width = width
    self.height = height
    self.dimensions = 2
  def as_list(self):
    return construct_2d_list(self.width,self.height)

class VirtualMap(object):
  def __init__(self, width, height):
    self.map = {}
    self.layers = []
    self.width, self.height = width, height
    
  def addLayer(self, name, depth):
    self.layers.append({'name':name, 'depth':depth})
    self.map[name] = VMapMatrix2D(width=self.width,height=self.height).as_list()

class Tile(pygame.sprite.Sprite):
  def __init__(self,x,y, image):
    self.image= image
    self.rect = self.image.get_rect()
    self.rect.x, self.rect.y = x,y
    self.pos = x,y
  
  def virtualmap(self, v_map, layer):
    v_map.insert(layer = layer, pos = self.pos, tile = self)

class TileProcesser(object):
  def __init__(self, filename, tilesize, name_or_name_dictionary, is_sheet, offset=0):
    self.tilesize = tilesize
    self.is_sheet = is_sheet
    self.filename = filename
    if is_sheet:
      self.names_dictionary = name_or_name_dictionary
      self.tiles = {}
    else:
      self.name = name_or_name_dictionary
    
  def load(self,alpha=False):
    if alpha:
      self.image = pygame.image.load(self.filename).convert_alpha()
    else:
      self.image = pygame.image.load(self.filename).convert()
    
    if self.is_sheet:
      for x in range(0,self.image.get_weight(),self.tilesize[0]):
        for y in range(0,self.image.get_height(),self.tilesize[1]):
          surface = pygame.Surface(self.tilesize)
          surface.blit(self.image, (0,0), (x*self.tilesize[0], y*self.tilesize[1], self.tilesize[0],self.tilesize[1])
          self.tiles[self.names_dictionary[(x,y)]] = Tile(surface
          
