# coding: utf-8
# 作者: Charles
# 公众号: Charles的皮卡丘
# 场景类(墙、河流、树、冰)
import pygame
import random


# 石头墙
class Brick(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.brick = pygame.image.load('./images/scene/brick.png')
		self.rect = self.brick.get_rect()
		self.being = False


# 钢墙
class Iron(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.iron = pygame.image.load('./images/scene/iron.png')
		self.rect = self.iron.get_rect()
		self.being = False


# 冰
class Ice(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.ice = pygame.image.load('./images/scene/ice.png')
		self.rect = self.ice.get_rect()
		self.being = False


# 河流
class River(pygame.sprite.Sprite):
	def __init__(self, kind=None):
		pygame.sprite.Sprite.__init__(self)
		if kind is None:
			self.kind = random.randint(0, 1)
		self.rivers = ['./images/scene/river1.png', './images/scene/river2.png']
		self.river = pygame.image.load(self.rivers[self.kind])
		self.rect = self.river.get_rect()
		self.being = False


# 树
class Tree(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.tree = pygame.image.load('./images/scene/tree.png')
		self.rect = self.tree.get_rect()
		self.being = False


# 地图
class Map():
	def __init__(self, stage):
		self.brickGroup = pygame.sprite.Group()
		self.ironGroup  = pygame.sprite.Group()
		self.iceGroup = pygame.sprite.Group()
		self.riverGroup = pygame.sprite.Group()
		self.treeGroup = pygame.sprite.Group()
		if stage == 1:
			self.stage1()
		elif stage == 2:
			self.stage2()
		elif stage == 3:
			self.stage3()
	# 关卡一
	def stage3(self):
		for x in [2, 3, 6, 7, 18, 19, 22, 23]:
			for y in [2, 3, 4, 5, 6, 7, 8, 9, 10, 17, 18, 19, 20, 21, 22, 23]:
				self.brick = Brick()
				self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24
				self.brick.being = True
				self.brickGroup.add(self.brick)
		for x in [10, 11, 14, 15]:
			for y in [2, 3, 4, 5, 6, 7, 8, 11, 12, 15, 16, 17, 18, 19, 20]:
				self.brick = Brick()
				self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24
				self.brick.being = True
				self.brickGroup.add(self.brick)
		for x in [4, 5, 6, 7, 18, 19, 20, 21]:
			for y in [13, 14]:
				self.brick = Brick()
				self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24
				self.brick.being = True
				self.brickGroup.add(self.brick)
		for x in [12, 13]:
			for y in [16, 17]:
				self.brick = Brick()
				self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24
				self.brick.being = True
				self.brickGroup.add(self.brick)
		for x, y in [(11, 23), (12, 23), (13, 23), (14, 23), (11, 24), (14, 24), (11, 25), (14, 25)]:
			self.brick = Brick()
			self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24
			self.brick.being = True
			self.brickGroup.add(self.brick)
		for x, y in [(0, 14), (1, 14), (12, 6), (13, 6), (12, 7), (13, 7), (24, 14), (25, 14)]:
			self.iron = Iron()
			self.iron.rect.left, self.iron.rect.top = 3 + x * 24, 3 + y * 24
			self.iron.being = True
			self.ironGroup.add(self.iron)
	# 关卡二
	def stage2(self):
		for x in [2, 3, 6, 7, 18, 19, 22, 23]:
			for y in [2, 3, 4, 5, 6, 7, 8, 9, 10, 17, 18, 19, 20, 21, 22, 23]:
				self.brick = Brick()
				self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24
				self.brick.being = True
				self.brickGroup.add(self.brick)
		for x in [10, 11, 14, 15]:
			for y in [2, 3, 4, 5, 6, 7, 8, 11, 12, 15, 16, 17, 18, 19, 20]:
				self.brick = Brick()
				self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24
				self.brick.being = True
				self.brickGroup.add(self.brick)
		for x in [4, 5, 6, 7, 18, 19, 20, 21]:
			for y in [13, 14]:
				self.brick = Brick()
				self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24
				self.brick.being = True
				self.brickGroup.add(self.brick)
		for x in [12, 13]:
			for y in [16, 17]:
				self.brick = Brick()
				self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24
				self.brick.being = True
				self.brickGroup.add(self.brick)
		for x, y in [(11, 23), (12, 23), (13, 23), (14, 23), (11, 24), (14, 24), (11, 25), (14, 25)]:
			self.brick = Brick()
			self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24
			self.brick.being = True
			self.brickGroup.add(self.brick)
		for x, y in [(0, 14), (1, 14), (12, 6), (13, 6), (12, 7), (13, 7), (24, 14), (25, 14)]:
			self.iron = Iron()
			self.iron.rect.left, self.iron.rect.top = 3 + x * 24, 3 + y * 24
			self.iron.being = True
			self.ironGroup.add(self.iron)
	# 关卡三
	def stage1(self):
		for x in [2, 3, 6, 7,  18, 19, 22, 23]:
			for y in [18, 19, 20, 21, 22, 23, 24, 25]:
				self.brick = Brick()
				self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24
				self.brick.being = True
				self.brickGroup.add(self.brick)
		for x in [2, 3,  22, 23,]:
			for y in [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ]:
				self.river = River()
				self.river.rect.left, self.river.rect.top = 3 + x * 24, 3 + y * 24
				self.river.being = True
				self.riverGroup.add(self.river)
		for x in [4, 5, 20, 21,]:
			 for y in [22, 23, 24, 25]:
				 self.river = River()
				 self.river.rect.left, self.river.rect.top = 3 + x * 24, 3 + y * 24
				 self.river.being = True
				 self.riverGroup.add(self.river)
		for x in [12, 13]:
			for y in [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]:
				self.iron = Iron()
				self.iron.rect.left, self.iron.rect.top = 3 + x * 24, 3 + y * 24
				self.iron.being = True
				self.ironGroup.add(self.iron)
		for x ,y in [(0,15), (1,15),(24,15),(25,15) ]:
			self.iron = Iron()
			self.iron.rect.left, self.iron.rect.top = 3 + x * 24, 3 + y * 24
			self.iron.being = True
			self.ironGroup.add(self.iron)
		for x,y  in [(11,25), (11,24), (11,23), (12,23), (13,23), (14, 23), (14,24), (14,25)]:
			self.brick = Brick()
			self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24
			self.brick.being = True
			self.brickGroup.add(self.brick)
		for x in [4, 5, 6, 7, 18, 19, 20, 21]:
			for y in [14,15]:
				self.brick = Brick()
				self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24
				self.brick.being = True
				self.brickGroup.add(self.brick)
		for x ,y in [(7,4), (8,4), (17,4), (18,4)]:
			self.iron = Iron()
			self.iron.rect.left, self.iron.rect.top = 3 + x * 24, 3 + y * 24
			self.iron.being = True
			self.ironGroup.add(self.iron)
		for x in [6, 7, 8, 9, 16, 17, 18, 19]:
			for y in [5, 6, 7]:
				self.iron = Iron()
				self.iron.rect.left, self.iron.rect.top = 3 + x * 24, 3 + y * 24
				self.iron.being = True
				self.ironGroup.add(self.iron)
		for x in [8, 9, 10 ,11, 14, 15, 16, 17]:
			for y in [ 14, 15]:
				self.tree = Tree()
				self.tree.rect.left, self.tree.rect.top = 3 + x * 24, 3 + y * 24
				self.tree.being = True
				self.treeGroup.add(self.tree)
		for x in [8, 9, 10, 11, 14, 15, 16, 17]:
			for y in [16,17 ]:
				self.brick = Brick()
				self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24
				self.brick.being = True
				self.brickGroup.add(self.brick)
		for x in [4, 5, 6, 7 ,18, 19, 20, 21]:
			for y in [14, 15]:
				self.brick = Brick()
				self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24
				self.brick.being = True
				self.brickGroup.add(self.brick)
		for x in [10, 11, 14, 15]:
			for y in [12, 13]:
				self.brick = Brick()
				self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24
				self.brick.being = True
				self.brickGroup.add(self.brick)
		for x in [4, 5, 6, 7, 18, 19, 20, 21]:
			for y in [9, 10]:
				self.brick = Brick()
				self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24
				self.brick.being = True
				self.brickGroup.add(self.brick)




	def protect_home(self):
		for x, y in [(11, 23), (12, 23), (13, 23), (14, 23), (11, 24), (14, 24), (11, 25), (14, 25)]:
			self.iron = Iron()
			self.iron.rect.left, self.iron.rect.top = 3 + x * 24, 3 + y * 24
			self.iron.being = True
			self.ironGroup.add(self.iron)