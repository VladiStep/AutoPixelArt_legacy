# coding=utf-8

from __future__ import print_function
try:
	import cv2, time, sys, os, random, ctypes, traceback, math
	import win32api as w1
	import win32con as w2
	import win32gui as w3
	import win32console as w4
	import numpy as np
	from colorama import init, Fore, Back, Style
	from getpass import getuser
	from msvcrt import getch, kbhit
		
	t = 0.75
	dir = 0
	prev_item = [0,0]
	exp_open = False
	colors_dict = ((((18, 18, 18), 'coal_block'), ((20, 18, 29), 'obsidian'), ((25, 22, 22), 'black_wool'), ((37, 22, 16), 'black_terracotta'), ((38, 67, 137), 'lapis_block'), ((45, 28, 12), 'spruce_log'), ((46, 56, 141), 'blue_wool'), ((46, 110, 137), 'cyan_wool'), ((52, 40, 23), 'dark_oak_log'), ((53, 70, 27), 'green_wool'), ((57, 42, 35), 'gray_terracotta'), ((61, 39, 18), 'dark_oak_planks'), ((64, 64, 64), 'gray_wool'), ((65, 174, 56), 'lime_wool'), ((74, 59, 91), 'blue_terracotta'), ((76, 83, 42), 'green_terracotta'), ((77, 51, 35), 'brown_terracotta'), ((79, 50, 31), 'brown_wool'), ((83, 83, 83), 'bedrock'), ((86, 91, 91), 'cyan_terracotta'), ((87, 67, 26), 'jungle_log'), ((97, 219, 213), 'diamond_block'), ((99, 160, 143), 'prismarine_bricks'), ((102, 81, 49), 'oak_log'), ((103, 77, 46), 'spruce_planks'), ((103, 117, 52), 'lime_terracotta'), ((105, 99, 89), 'acacia_log'), ((106, 138, 201), 'light_blue_wool'), ((111, 54, 52), 'netherrack'), ((113, 108, 137), 'light_blue_terracotta'), ((118, 70, 86), 'purple_terracotta'), ((125, 125, 125), 'stone'), ((126, 61, 181), 'purple_wool'), ((126, 124, 122), 'gravel'), ((130, 131, 131), 'andesite'), ((134, 96, 67), 'dirt'), ((135, 106, 97), 'light_gray_terracotta'), ((143, 61, 46), 'red_terracotta'), ((143, 118, 69), 'glowstone'), ((149, 88, 108), 'magenta_terracotta'), ((150, 52, 48), 'red_wool'), ((150, 92, 66), 'terracotta'), ((153, 113, 98), 'granite'), ((154, 110, 77), 'jungle_planks'), ((154, 161, 161), 'light_gray_wool'), ((156, 127, 78), 'oak_planks'), ((158, 164, 176), 'clay'), ((161, 78, 78), 'pink_terracotta'), ((161, 83, 37), 'orange_terracotta'), ((169, 88, 33), 'red_sand'), ((169, 91, 51), 'acacia_planks'), ((171, 27, 9), 'redstone_block'), ((177, 166, 39), 'yellow_wool'), ((179, 80, 188), 'magenta_wool'), ((179, 179, 182), 'diorite'), ((186, 133, 35), 'yellow_terracotta'), ((194, 195, 84), 'sponge'), ((195, 179, 123), 'birch_planks'), ((208, 132, 153), 'pink_wool'), ((209, 178, 161), 'white_terracotta'), ((219, 125, 62), 'orange_wool'), ((219, 211, 160), 'sand'), ((219, 219, 219), 'iron_block'), ((221, 221, 221), 'white_wool'), ((236, 233, 226), 'quartz_block'), ((249, 236, 78), 'gold_block')), #1.8
	(((117, 6, 7), 'nether_wart_block'), ((224, 220, 200), 'bone_block')), #1.10
	(((8, 10, 15), 'black_concrete'), ((21, 119, 136), 'cyan_concrete'), ((25, 26, 31), 'black_concrete_powder'), ((35, 137, 198), 'light_blue_concrete'), ((36, 147, 157), 'cyan_concrete_powder'), ((44, 46, 143), 'blue_concrete'), ((54, 57, 61), 'gray_concrete'), ((70, 73, 166), 'blue_concrete_powder'), ((73, 91, 36), 'green_concrete'), ((74, 180, 213), 'light_blue_concrete_powder'), ((76, 81, 84), 'gray_concrete_powder'), ((94, 168, 24), 'lime_concrete'), ((96, 59, 31), 'brown_concrete'), ((97, 119, 44), 'green_concrete_powder'), ((100, 31, 156), 'purple_concrete'), ((125, 84, 53), 'brown_concrete_powder'), ((125, 125, 115), 'light_gray_concrete'), ((125, 189, 41), 'lime_concrete_powder'), ((131, 55, 177), 'purple_concrete_powder'), ((142, 32, 32), 'red_concrete'), ((154, 154, 148), 'light_gray_concrete_powder'), ((168, 54, 50), 'red_concrete_powder'), ((169, 48, 159), 'magenta_concrete'), ((192, 83, 184), 'magenta_concrete_powder'), ((207, 213, 214), 'white_concrete'), ((213, 101, 142), 'pink_concrete'), ((224, 97, 0), 'orange_concrete'), ((225, 227, 227), 'white_concrete_powder'), ((227, 131, 31), 'orange_concrete_powder'), ((228, 153, 181), 'pink_concrete_powder'), ((232, 199, 54), 'yellow_concrete_powder'), ((240, 175, 21), 'yellow_concrete')), #1.12
	(((96, 76, 49), 'stripped_dark_oak_log'), ((115, 89, 52), 'stripped_spruce_log'), ((141, 106, 83), 'brown_mushroom_block'), ((166, 85, 29), 'smooth_red_sandstone'), ((171, 132, 84), 'stripped_jungle_log'), ((174, 92, 59), 'stripped_acacia_log'), ((177, 144, 86), 'stripped_oak_log'), ((196, 176, 118), 'stripped_birch_log'), ((207, 204, 194), 'mushroom_stem'), ((218, 210, 158), 'smooth_sandstone')), #1.13
	(((8, 10, 15), 'black_concrete'), ((15, 10, 24), 'obsidian'), ((16, 15, 15), 'coal_block'), ((20, 21, 25), 'black_wool'), ((21, 119, 136), 'cyan_concrete'), ((21, 137, 145), 'cyan_wool'), ((25, 26, 31), 'black_concrete_powder'), ((30, 67, 140), 'lapis_block'), ((35, 137, 198), 'light_blue_concrete'), ((36, 147, 157), 'cyan_concrete_powder'), ((37, 22, 16), 'black_terracotta'), ((42, 203, 87), 'emerald_block'), ((44, 46, 143), 'blue_concrete'), ((53, 57, 157), 'blue_wool'), ((54, 57, 61), 'gray_concrete'), ((57, 42, 35), 'gray_terracotta'), ((58, 37, 16), 'spruce_log'), ((58, 175, 217), 'light_blue_wool'), ((60, 46, 26), 'dark_oak_log'), ((62, 68, 71), 'gray_wool'), ((66, 43, 20), 'dark_oak_planks'), ((70, 73, 166), 'blue_concrete_powder'), ((73, 91, 36), 'green_concrete'), ((74, 59, 91), 'blue_terracotta'), ((74, 180, 213), 'light_blue_concrete_powder'), ((76, 81, 84), 'gray_concrete_powder'), ((76, 83, 42), 'green_terracotta'), ((77, 51, 35), 'brown_terracotta'), ((84, 109, 27), 'green_wool'), ((85, 67, 25), 'jungle_log'), ((85, 85, 85), 'bedrock'), ((86, 91, 91), 'cyan_terracotta'), ((94, 168, 24), 'lime_concrete'), ((96, 59, 31), 'brown_concrete'), ((96, 76, 49), 'stripped_dark_oak_log'), ((97, 38, 38), 'netherrack'), ((97, 119, 44), 'green_concrete_powder'), ((98, 237, 228), 'diamond_block'), ((99, 171, 158), 'prismarine_bricks'), ((100, 31, 156), 'purple_concrete'), ((103, 96, 86), 'acacia_log'), ((103, 117, 52), 'lime_terracotta'), ((109, 85, 50), 'oak_log'), ((112, 185, 25), 'lime_wool'), ((113, 108, 137), 'light_blue_terracotta'), ((114, 3, 2), 'nether_wart_block'), ((114, 71, 40), 'brown_wool'), ((114, 84, 48), 'spruce_planks'), ((115, 89, 52), 'stripped_spruce_log'), ((118, 70, 86), 'purple_terracotta'), ((121, 42, 172), 'purple_wool'), ((125, 84, 53), 'brown_concrete_powder'), ((125, 125, 115), 'light_gray_concrete'), ((125, 125, 125), 'stone'), ((125, 189, 41), 'lime_concrete_powder'), ((131, 55, 177), 'purple_concrete_powder'), ((131, 127, 126), 'gravel'), ((134, 96, 67), 'dirt'), ((135, 106, 97), 'light_gray_terracotta'), ((136, 136, 136), 'andesite'), ((142, 32, 32), 'red_concrete'), ((142, 142, 134), 'light_gray_wool'), ((143, 61, 46), 'red_terracotta'), ((149, 88, 108), 'magenta_terracotta'), ((149, 103, 85), 'granite'), ((149, 111, 81), 'brown_mushroom_block'), ((152, 94, 67), 'terracotta'), ((154, 154, 148), 'light_gray_concrete_powder'), ((160, 39, 34), 'red_wool'), ((160, 115, 80), 'jungle_planks'), ((160, 166, 179), 'clay'), ((161, 78, 78), 'pink_terracotta'), ((161, 83, 37), 'orange_terracotta'), ((162, 130, 78), 'oak_planks'), ((168, 54, 50), 'red_concrete_powder'), ((168, 90, 50), 'acacia_planks'), ((169, 48, 159), 'magenta_concrete'), ((171, 131, 84), 'glowstone'), ((171, 132, 84), 'stripped_jungle_log'), ((174, 92, 59), 'stripped_acacia_log'), ((175, 24, 5), 'redstone_block'), ((177, 144, 86), 'stripped_oak_log'), ((181, 97, 31), 'smooth_red_sandstone'), ((186, 133, 35), 'yellow_terracotta'), ((188, 188, 188), 'diorite'), ((189, 68, 179), 'magenta_wool'), ((190, 102, 33), 'red_sand'), ((192, 83, 184), 'magenta_concrete_powder'), ((192, 175, 121), 'birch_planks'), ((196, 176, 118), 'stripped_birch_log'), ((203, 196, 185), 'mushroom_stem'), ((207, 213, 214), 'white_concrete'), ((209, 178, 161), 'white_terracotta'), ((213, 101, 142), 'pink_concrete'), ((219, 207, 163), 'sand'), ((220, 220, 220), 'iron_block'), ((223, 214, 170), 'smooth_sandstone'), ((224, 97, 0), 'orange_concrete'), ((225, 227, 227), 'white_concrete_powder'), ((227, 131, 31), 'orange_concrete_powder'), ((228, 153, 181), 'pink_concrete_powder'), ((229, 225, 207), 'bone_block'), ((232, 199, 54), 'yellow_concrete_powder'), ((233, 236, 236), 'white_wool'), ((235, 229, 222), 'quartz_block'), ((237, 141, 172), 'pink_wool'), ((240, 118, 19), 'orange_wool'), ((240, 175, 21), 'yellow_concrete'), ((246, 208, 61), 'gold_block'), ((248, 197, 39), 'yellow_wool'))) #1.14
	colors_for_ver = []
	version = -1
	blocks = 0
	percents = 0
	upd_blocks_clr = ''
	h_count = [0,0]
	init()
	ctypes.windll.kernel32.SetConsoleTitleA('AutoPixelArt')
	
	def on_exit(sig):
		try:
			slow(False)
			w3.SendMessage(h, w2.WM_KEYUP, ord('A'), 3223191553)
			w3.SendMessage(h, w2.WM_KEYUP, ord('D'), 3223322625)
			w3.SendMessage(h, w2.WM_KEYUP, ord('X'), 0xC02D0001)
			for i1 in range(1,10):
				lParamUp = int('0xC00'+str(1+i1)+'0001',16)
				w3.SendMessage(h, w2.WM_KEYUP, 0x00000030+i1, hex(lParamUp))
			w3.SendMessage(h, w2.WM_KEYUP, 0x00000039, 0xC00A0001)
			w3.SendMessage(h, w2.WM_SETFOCUS, 0, 0)
		except Exception as e:
			print(Fore.RED+u'Произошла ошибка. Подробности в error.log.'+Style.RESET_ALL)
			file = open('error.log', 'w')
			file.write(traceback.format_exc())
			file.close()
			print(u'(Нажмите Enter для завершения)',end='')
			raw_input()
	
	def getClosestBlock(inp_color):
		minError = 99999
		curError = 0
		for i in range(len(colors_for_ver)):
			curError = math.sqrt(math.pow(inp_color[0]-colors_for_ver[i][0][0], 2) + math.pow(inp_color[1]-colors_for_ver[i][0][1], 2) + math.pow(inp_color[2]-colors_for_ver[i][0][2], 2))
			if curError < minError:
				minError = curError
				best_block = colors_for_ver[i][1]
		return best_block
	
	def blendImages(image_1,image_2,x1,y1):
		y2 = y1 + image_1.shape[0]
		x2 = x1 + image_1.shape[1]
		alpha_s = image_1[:, :, 3] / 255.0
		alpha_l = 1.0 - alpha_s
		for c in range(0, 3):
			image_2[y1:y2, x1:x2, c] = (alpha_s * image_1[:, :, c] + alpha_l * image_2[y1:y2, x1:x2, c])
	
	def selectItem(number1,number2):
		lParamDown1 = 0
		lParamDown2 = 0
		sleeped = False
		if 1 <= number2 <= 8:
			lParamDown2 = int('0x000'+str(1+number2)+'0001',16)
			lParamUp2 = int('0xC00'+str(1+number2)+'0001',16)
		if number2 == 9:
			lParamDown2 = 0x000A0001
			lParamUp2 = 0xC00A0001
		if 1 <= number1 <= 8:
			lParamDown1 = int('0x000'+str(1+number1)+'0001',16)
			lParamUp1 = int('0xC00'+str(1+number1)+'0001',16)
		if number1 == 9:
			lParamDown1 = 0x000A0001
			lParamUp1 = 0xC00A0001
		if lParamDown1 == 0 or lParamDown2 == 0:
			print(u'(Хоть и это сообщение никогда не выведется, но)') 
			print(Fore.RED+u'Неверное число в selectItem()'+Style.RESET_ALL)
			print(u'(Нажмите Enter для завершения)')
			raw_input()
			sys.exit()
		global prev_item
		if np.array_equal(prev_item,[0,0]):
			if len(colors) > 9:
				w3.SendMessage(h, w2.WM_KEYDOWN, ord('X'), 0x002D0001)
				w3.SendMessage(h, w2.WM_KEYDOWN, 0x00000030+number2, lParamDown2)
				w3.SendMessage(h, w2.WM_KEYUP, 0x00000030+number2, lParamUp2)
				time.sleep(0.15)
				w3.SendMessage(h, w2.WM_KEYUP, ord('X'), 0xC02D0001)
			w3.SendMessage(h, w2.WM_KEYDOWN, 0x00000030+number1, lParamDown1)
			w3.SendMessage(h, w2.WM_KEYUP, 0x00000030+number1, lParamUp1)
			if len(colors) <= 9: time.sleep(0.15)
			prev_item = (number1, number2)
		else:
			if len(colors) > 9:
				if prev_item[1] != number2:
					w3.SendMessage(h, w2.WM_KEYDOWN, ord('X'), 0x002D0001)
					w3.SendMessage(h, w2.WM_KEYDOWN, 0x00000030+number2, lParamDown2)
					w3.SendMessage(h, w2.WM_KEYUP, 0x00000030+number2, lParamUp2)
					time.sleep(0.15)
					sleeped = True
					w3.SendMessage(h, w2.WM_KEYUP, ord('X'), 0xC02D0001)
			if prev_item[0] != number1:
				w3.SendMessage(h, w2.WM_KEYDOWN, 0x00000030+number1, lParamDown1)
				w3.SendMessage(h, w2.WM_KEYUP, 0x00000030+number1, lParamUp1)
			if not sleeped: time.sleep(0.15)
			prev_item = (number1, number2)
	
	def rightClick():
		w3.SendMessage(h, w2.WM_RBUTTONDOWN, w2.MK_RBUTTON, 0)
		time.sleep(0.01)
		w3.SendMessage(h, w2.WM_RBUTTONUP, w2.MK_RBUTTON, 0)
	
	def mouseDown():
		w3.SendMessage(h, w2.WM_RBUTTONDOWN, w2.MK_RBUTTON, 0)
	
	def mouseUp():
		w3.SendMessage(h, w2.WM_RBUTTONUP, w2.MK_RBUTTON, 0)
	
	def updateStat():
		global blocks, percents, upd_blocks_clr
		blocks += 1
		percents = '{0:.3f}'.format((float(blocks)/blocks_total) * 100).replace('.',',')
		upd_blocks = u'Поставлено блоков: {} / {}. ({}%)'.format(blocks,blocks_total,percents)
		upd_blocks_clr = '\b' * len(upd_blocks)
		print(upd_blocks_clr,end='')
		print(upd_blocks,end='')
	
	def pressKey(key):
		if key == 'space':
			w3.SendMessage(h, w2.WM_KEYDOWN, w2.VK_SPACE, 0x00390001)
			time.sleep(0.1)
			w3.SendMessage(h, w2.WM_KEYUP, w2.VK_SPACE, 0xC0390001)
			time.sleep(0.1)
	
	def keyDown(key):
		if key == 'w':
			w3.SendMessage(h, w2.WM_KEYDOWN, ord('W'), 1114113)
		if key == 'a':
			w3.SendMessage(h, w2.WM_KEYDOWN, ord('A'), 1966081)
		if key == 's':
			w3.SendMessage(h, w2.WM_KEYDOWN, ord('S'), 2031617)
		if key == 'd':
			w3.SendMessage(h, w2.WM_KEYDOWN, ord('D'), 1075838977)
	
	def keyUp(key):
		if key == 'w':
			w3.SendMessage(h, w2.WM_KEYUP, ord('W'), 3222339585)
		if key == 'a':
			w3.SendMessage(h, w2.WM_KEYUP, ord('A'), 3223191553)
		if key == 's':
			w3.SendMessage(h, w2.WM_KEYUP, ord('S'), 3223257089)
		if key == 'd':
			w3.SendMessage(h, w2.WM_KEYUP, ord('D'), 3223322625)
	
	def slow(isSlow):
		if isSlow: w3.SendMessage(h, w2.WM_KEYDOWN, ord('Z'), 0x002C0001)
		else: w3.SendMessage(h, w2.WM_KEYUP, ord('Z'), 0xC02C0001)
	
	def mouseCallback(event, x, y, flags, param):
		if event == cv2.EVENT_LBUTTONDOWN:
			if x < im_color.shape[1]-1: selectedColor = y // 100 * 9 + x // 100
			else: selectedColor = y // 100 * 9 + x // 100 - 1
			if selectedColor < len(colors):
				color_mask = cv2.inRange(im_view, (int(colors[selectedColor][2]),int(colors[selectedColor][1]),int(colors[selectedColor][0])), (int(colors[selectedColor][2]),int(colors[selectedColor][1]),int(colors[selectedColor][0])))
				cv2.imshow(basename, color_mask)
		if event == cv2.EVENT_LBUTTONUP:
			cv2.imshow(basename, im_view)
	
	def enumHandler(hwnd, param):
		global h_temp, h_count
		if 'Minecraft' in w3.GetWindowText(hwnd) and ver in w3.GetWindowText(hwnd) and 'GL' in w3.GetClassName(hwnd):
			if w3.GetWindowPlacement(hwnd)[1] == 1 or w3.GetWindowPlacement(hwnd)[1] == 3:
				h_temp = hwnd
				h_count[0] += 1
			else:
				if h_count[0] == 0: h_temp = hwnd
				h_count[1] += 1
		return True
	
	h_self = w4.GetConsoleWindow()
	if len(sys.argv) < 2:
		print(Style.BRIGHT+Fore.GREEN+u'Использование: py AutoPixelArt.py <имя картинки>, или просто перетащите картинку на программу'+Style.RESET_ALL)
		print(u'(Нажмите Enter для завершения)',end='')
		raw_input()
	else:
		if not os.path.exists(sys.argv[1]):
			print(Fore.RED+u'Неверное имя файла.'+Style.RESET_ALL)
			print(u'(Нажмите Enter для завершения)',end='')
			raw_input()
		else:
			im = cv2.imread(sys.argv[1])
			if im is None:
				print(Fore.RED+u'Указанный файл повреждён или не является картинкой.'+Style.RESET_ALL)
				print(u'(Нажмите Enter для завершения)',end='')
				raw_input()
			else:
				im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
				os.system('cls')
				height, width, _ = im.shape
				print(Style.BRIGHT+Fore.YELLOW+u'AutoPixelArt, версия 1.94.'+Style.RESET_ALL)
				print(Style.BRIGHT+Fore.YELLOW+u'Автор'+Style.RESET_ALL+' - '+Style.BRIGHT+Fore.CYAN+u'vk.com/vladstep2001'+Style.RESET_ALL+'\n')
				print(Style.BRIGHT+Fore.GREEN+u'Картинка загружена. '+Style.RESET_ALL+u'Ширина - ' + str(width) + u', высота - '+str(height)+u'.')
				print(u'Кол-во необходимых блоков - ' + str(width*height) + u'.')
				blocks_total = width * height
				colors = np.unique(im.reshape(-1, im.shape[2]), axis=0)
				if len(colors) > 81:
					print(Fore.RED+u'В указанной картинке больше 81 цвета.'+Style.RESET_ALL)
					print(u'(Нажмите Enter для завершения)',end='')
					raw_input()
					sys.exit()
				print(u'Кол-во цветов - ' + str(len(colors)) + u'.' + '\n')
				if len(colors) > 9 and len(colors) < 82:
					username = getuser()
					if os.path.isfile(u'C:\\Users\\'+username.decode('1251')+u'\\AppData\\Roaming\\.minecraft\\hotbar.nbt'):
						exp_open = True
						os.startfile(u'C:\\Users\\'+username.decode('1251')+u'\\AppData\\Roaming\\.minecraft\\')
						print(Fore.RED+u'Так как количество цветов больше 9'+Style.BRIGHT+Fore.GREEN+u', я открыл папку, где '+Fore.YELLOW+u'(по-умолчанию)'+Fore.GREEN+u' расположен файл hotbar.'+Style.RESET_ALL)
						print(Fore.RED+u'Сохраните его куда-нибудь, чтобы не потерять "Сохранённые инструменты"(1.12+!),'+Style.BRIGHT+Fore.GREEN+u' потом закроете Minecraft, и замените hotbar назад.'+Style.RESET_ALL+'\n')
					else:
						print(Fore.RED+u'Так как количество цветов больше 9'+Style.BRIGHT+Fore.GREEN+u', я хотел открыть папку, где '+Fore.YELLOW+u'(по-умолчанию)'+Fore.GREEN+u' расположен файл hotbar.'+Style.RESET_ALL)
						print(Fore.RED+u'Так как я его там не нашёл, вы должны сами найти её, и тот файл.'+Style.RESET_ALL)
						print(Fore.RED+u'Сохраните его куда-нибудь, чтобы не потерять "Сохранённые инструменты"(1.12+!),'+Style.BRIGHT+Fore.GREEN+u' потом закроете Minecraft, и замените hotbar назад.'+Style.RESET_ALL+'\n')
				prev_clr = im[height-1][0]
				avg_time = 0.2 + 0.01 + 0.3 + 0.15 * (width*height) + 0.2 * (height-1) + (t-0.15) * height + (t-0.15+0.01) * (width-1) * height + 0.2 * height + 0.01 * (width * height - 1) + 0.506 * height
				print(u'Приблизительное время стройки в минутах - ' + Style.BRIGHT+Fore.RED + '{0:.2f}'.format(avg_time/60).replace('.',',') + Style.RESET_ALL + u'.' + '\n')
				print(u'(По какой-то причине, эмуляция нажатия Shift не работает, поэтому,'+Fore.RED+u' надо поставить Z в качестве кнопки приседания'+Style.RESET_ALL+u')' + '\n')
				while kbhit(): getch() #Очистить буфер ввода
				print(u'Использовать '+Style.BRIGHT+Fore.RED+u'п'+Style.NORMAL+Fore.YELLOW+u'а'+Style.BRIGHT+Fore.YELLOW+u'л'+Fore.GREEN+u'и'+Fore.CYAN+u'т'+Fore.BLUE+u'р'+Fore.MAGENTA+u'у'+Style.RESET_ALL+u' для версии: ', end='')
				ver = raw_input().replace(' ','')
				if 8 <= int(ver.split('.')[1]) <= 9: version = 0
				if 10 <= int(ver.split('.')[1]) <= 11: version = 1
				if int(ver.split('.')[1]) == 12: version = 2
				if int(ver.split('.')[1]) == 13: version = 3
				if int(ver.split('.')[1]) == 14: version = 4
				if version == -1:
					print(Style.BRIGHT+Fore.YELLOW+u'Для этой версии у меня нет палитры, поэтому вам придётся подбирать цвета самостоятельно.'+Style.RESET_ALL)
				else:
					for ver_i in range(version+1):
						if ver_i == 4:
							colors_for_ver = colors_dict[ver_i]
							break
						colors_for_ver += colors_dict[ver_i]
				if len(colors) > 9 and len(colors) < 82:
					im_color = np.zeros((((len(colors)-1)//9+1)*100+1,901,3), np.uint8)
					for i2 in range((len(colors)-1)//9+1):
						for i in range(9):
							if i+i2*9 > len(colors)-1: break
							if i == 0:
								if version != -1:
									color_str = getClosestBlock(colors[i+i2*9])
									rendered_title = cv2.imread('rendered_titles/'+color_str+'.png',cv2.IMREAD_UNCHANGED)
								cv2.rectangle(im_color, (0, i2*100), (100, i2*100+100), (int(colors[i+i2*9][2]),int(colors[i+i2*9][1]),int(colors[i+i2*9][0])), -1)
								cv2.rectangle(im_color, (0, i2*100), (100, i2*100+100), (128, 128, 128), 3)
								color_mask = cv2.inRange(im, (int(colors[i+i2*9][0]),int(colors[i+i2*9][1]),int(colors[i+i2*9][2])), (int(colors[i+i2*9][0]),int(colors[i+i2*9][1]),int(colors[i+i2*9][2])))
								color_count = cv2.countNonZero(color_mask)
								text_size = cv2.getTextSize(str(color_count), cv2.FONT_HERSHEY_SIMPLEX, 0.71, 2)[0]
								if version != -1:
									text_size_1 = rendered_title.shape[1]
								if not (125 <= colors[i+i2*9][0] <= 130) and not (125 <= colors[i+i2*9][1] <= 130) and not (125 <= colors[i+i2*9][2] <= 130):
									cv2.putText(im_color, str(color_count), (((i*100+51) - text_size[0] / 2), 57+100*i2), cv2.FONT_HERSHEY_SIMPLEX, 0.71, (int(255-colors[i+i2*9][2]),int(255-colors[i+i2*9][1]),int(255-colors[i+i2*9][0])), 2)
									if version != -1:
										rendered_title[np.where((rendered_title==[255,255,255,255]).all(axis=2))] = [int(255-colors[i+i2*9][2]),int(255-colors[i+i2*9][1]),int(255-colors[i+i2*9][0]),255]
								else:
									cv2.putText(im_color, str(color_count), (((i*100+51) - text_size[0] / 2), 57+100*i2), cv2.FONT_HERSHEY_SIMPLEX, 0.71, (255,255,255), 2)
								if version != -1:
									blendImages(rendered_title,im_color,((i*100+51) - text_size_1 / 2),(70+100*i2))
							else:
								if version != -1:
									color_str = getClosestBlock(colors[i+i2*9])
									rendered_title = cv2.imread('rendered_titles/'+color_str+'.png',cv2.IMREAD_UNCHANGED)
								cv2.rectangle(im_color, (i*100+1, i2*100), (i*100+100, i2*100+100), (int(colors[i+i2*9][2]),int(colors[i+i2*9][1]),int(colors[i+i2*9][0])), -1)
								cv2.rectangle(im_color, (i*100+1, i2*100), (i*100+100, i2*100+100), (128,128,128), 3)
								color_mask = cv2.inRange(im, (int(colors[i+i2*9][0]),int(colors[i+i2*9][1]),int(colors[i+i2*9][2])), (int(colors[i+i2*9][0]),int(colors[i+i2*9][1]),int(colors[i+i2*9][2])))
								color_count = cv2.countNonZero(color_mask)
								text_size = cv2.getTextSize(str(color_count), cv2.FONT_HERSHEY_SIMPLEX, 0.71, 2)[0]
								if version != -1:
									text_size_1 = rendered_title.shape[1]
								if not (125 <= colors[i+i2*9][0] <= 130) and not (125 <= colors[i+i2*9][1] <= 130) and not (125 <= colors[i+i2*9][2] <= 130):
									cv2.putText(im_color, str(color_count), (((i*100+51) - text_size[0] / 2), 57+100*i2), cv2.FONT_HERSHEY_SIMPLEX, 0.71, (int(255-colors[i+i2*9][2]),int(255-colors[i+i2*9][1]),int(255-colors[i+i2*9][0])), 2)
									if version != -1:
										rendered_title[np.where((rendered_title==[255,255,255,255]).all(axis=2))] = [int(255-colors[i+i2*9][2]),int(255-colors[i+i2*9][1]),int(255-colors[i+i2*9][0]),255]
								else:
									cv2.putText(im_color, str(color_count), (((i*100+51) - text_size[0] / 2), 57+100*i2), cv2.FONT_HERSHEY_SIMPLEX, 0.71, (255,255,255), 2)
								if version != -1:
									blendImages(rendered_title,im_color,((i*100+51) - text_size_1 / 2),(70+100*i2))
					name = u'Список слотов (в сохранённых инструментах):'.encode('1251')
					cv2.namedWindow(name)
					cv2.setMouseCallback(name,mouseCallback)
					cv2.imshow(name, im_color)
				else:
					im_color = np.zeros((101,len(colors)*100+1,3), np.uint8)
					for i in range(len(colors)):
						if i == 0:
							if version != -1:
								color_str = getClosestBlock(colors[i])
								rendered_title = cv2.imread('rendered_titles/'+color_str+'.png',cv2.IMREAD_UNCHANGED)
							cv2.rectangle(im_color, (0, 0), (100, 100), (int(colors[i][2]),int(colors[i][1]),int(colors[i][0])), -1)
							cv2.rectangle(im_color, (0, 0), (100, 100), (128, 128, 128), 3)
							color_mask = cv2.inRange(im, (int(colors[i][0]),int(colors[i][1]),int(colors[i][2])), (int(colors[i][0]),int(colors[i][1]),int(colors[i][2])))
							color_count = cv2.countNonZero(color_mask)
							text_size = cv2.getTextSize(str(color_count), cv2.FONT_HERSHEY_SIMPLEX, 0.71, 2)[0]
							if version != -1:
								text_size_1 = rendered_title.shape[1]
							if not (125 <= colors[i][0] <= 130) and not (125 <= colors[i][1] <= 130) and not (125 <= colors[i][2] <= 130):
								cv2.putText(im_color, str(color_count), (((50 - text_size[0] / 2 + 1), 56)), cv2.FONT_HERSHEY_SIMPLEX, 0.71, (int(255-colors[i][2]),int(255-colors[i][1]),int(255-colors[i][0])), 2)
								if version != -1:
									rendered_title[np.where((rendered_title==[255,255,255,255]).all(axis=2))] = [int(255-colors[i][2]),int(255-colors[i][1]),int(255-colors[i][0]),255]
							else:
								cv2.putText(im_color, str(color_count), (((50 - text_size[0] / 2 + 1), 56)), cv2.FONT_HERSHEY_SIMPLEX, 0.71, (255,255,255), 2)
							if version != -1:
								blendImages(rendered_title,im_color,(50 - text_size_1 / 2 + 1),70)
						else:
							if version != -1:
								color_str = getClosestBlock(colors[i])
								rendered_title = cv2.imread('rendered_titles/'+color_str+'.png',cv2.IMREAD_UNCHANGED)
							cv2.rectangle(im_color, (i*100+1, 0), (i*100+100, 100), (int(colors[i][2]),int(colors[i][1]),int(colors[i][0])), -1)
							cv2.rectangle(im_color, (i*100+1, 0), (i*100+100, 100), (128,128,128), 3)
							color_mask = cv2.inRange(im, (int(colors[i][0]),int(colors[i][1]),int(colors[i][2])), (int(colors[i][0]),int(colors[i][1]),int(colors[i][2])))
							color_count = cv2.countNonZero(color_mask)
							text_size = cv2.getTextSize(str(color_count), cv2.FONT_HERSHEY_SIMPLEX, 0.71, 2)[0]
							if version != -1:
								text_size_1 = rendered_title.shape[1]
							if not (125 <= colors[i][0] <= 130) and not (125 <= colors[i][1] <= 130) and not (125 <= colors[i][2] <= 130):
								cv2.putText(im_color, str(color_count), (((i*100+51) - text_size[0] / 2), 55), cv2.FONT_HERSHEY_SIMPLEX, 0.71, (int(255-colors[i][2]),int(255-colors[i][1]),int(255-colors[i][0])), 2)
								if version != -1:
									rendered_title[np.where((rendered_title==[255,255,255,255]).all(axis=2))] = [int(255-colors[i][2]),int(255-colors[i][1]),int(255-colors[i][0]),255]
							else:
								cv2.putText(im_color, str(color_count), (((i*100+51) - text_size[0] / 2), 55), cv2.FONT_HERSHEY_SIMPLEX, 0.71, (255,255,255), 2)
							if version != -1:
								blendImages(rendered_title,im_color,((i*100+51) - text_size_1 / 2),70)
					name = u'Список слотов:'.encode('1251')
					cv2.namedWindow(name)
					cv2.setMouseCallback(name,mouseCallback)
					cv2.imshow(name, im_color)
				if width <= 400: scale = 400/width
				else: scale = 1
				im_view = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
				basename = os.path.basename(sys.argv[1])
				cv2.namedWindow(basename, flags=cv2.WINDOW_NORMAL)
				cv2.resizeWindow(basename,int(round(im_view.shape[1]*scale)),int(round(im_view.shape[0]*scale)))
				cv2.imshow(basename, im_view)
				if exp_open: cv2.waitKey(1000)
				try:
					w3.ShowWindow(h_self, w2.SW_SHOWNORMAL)
					w3.SetForegroundWindow(h_self)
				except: None
				print(Style.BRIGHT+Fore.YELLOW+u'Зажмите ЛКМ на слоте, чтобы посмотреть, где этот цвет на рисунке.'+Style.RESET_ALL)
				print(Style.BRIGHT+Fore.YELLOW+u'(Для правильного прерывания строительства, закройте это окно)'+Style.RESET_ALL+'\n')
				if cv2.waitKey(0) == w2.VK_ESCAPE: sys.exit()
				cv2.destroyAllWindows()
				for y in range(height):
					if (y+1)%2 == 0: y_mod = 0
					else: y_mod = 1
					for x in range(width):
						if (x+y_mod)%2 == 0: im_view[y,x] = [255,255,255]
						else: im_view[y,x] = [204,204,204]
				time.sleep(0.5)
				try:
					w3.BringWindowToTop(h_self)
					w3.ShowWindow(h_self, w2.SW_SHOW)
					w3.SetForegroundWindow(h_self)
				except: None
				while kbhit(): getch()
				print(u'Введите версию Minecraft: ', end='')
				ver = raw_input().replace(' ','')
				if len(colors) > 9:
					if ver.split('.')[0] == '1':
						if (int(ver.split('.')[1]) < 12):
							print(Style.BRIGHT+Fore.RED+u'Как я написал выше, "Сохранённые инструменты" появились с версии 1.12 (17w06a)!'+Style.RESET_ALL)
							print(u'(Нажмите Enter для завершения)',end='')
							raw_input()
							sys.exit()
					else:
						if ver[2:3] == 'w':
							if int(ver[:2]) < 17:
								print(Style.BRIGHT+Fore.RED+u'Как я написал выше, "Сохранённые инструменты" появились с версии 1.12 (17w06a)!'+Style.RESET_ALL)
								print(u'(Нажмите Enter для завершения)',end='')
								raw_input()
								sys.exit()
						else:
							print(Style.BRIGHT+Fore.RED+u'Вы неправильно написали версию Minecraft!'+Style.RESET_ALL)
							print(u'(Нажмите Enter для завершения)',end='')
							raw_input()
							sys.exit()
				try:
					w3.EnumWindows(enumHandler, 0)
				except: None
				if h_count[0]+h_count[1] == 0:
					print(Fore.RED+u'Окно не найдено.'+Style.RESET_ALL)
					print(u'(Нажмите Enter для завершения)',end='')
					raw_input()
					sys.exit()
				if (h_count[0] > 1 or h_count[1] > 1) and h_count[0] != 1:
					print(Style.BRIGHT+Fore.YELLOW+u'Открыто два (или более) окна Minecraft одной версии. Оставьте видимым нужный вам Minecraft, и нажмите Enter.'+Style.RESET_ALL, end='')
					raw_input()
					h_count = [0,0]
					try:
						w3.EnumWindows(enumHandler, 0)
					except: None
					if h_count[0]+h_count[1] == 0:
						print(Style.BRIGHT+Fore.RED+u'Зачем вы закрыли ВСЕ окна?'+Style.RESET_ALL)
						print(u'(Нажмите Enter для завершения)',end='')
						raw_input()
						sys.exit()
					if (h_count[0] > 1 or h_count[1] > 1) and h_count[0] != 1:
						print(Style.BRIGHT+Fore.RED+u'Ничего не изменилось: скрыто/открыто два (или более) окна, нужно чтобы только ОДНО окно осталось видимым! Сделайте как нужно, и нажмите Enter.'+Style.RESET_ALL)
						raw_input()
						h_count = [0,0]
						try:
							w3.EnumWindows(enumHandler, 0)
						except: None
						if h_count[0]+h_count[1] == 0:
							print(Style.BRIGHT+Fore.RED+u'Зачем вы закрыли ВСЕ окна?')
							print(u'(Нажмите Enter для завершения)',end='')
							raw_input()
							sys.exit()
						if (h_count[0] > 1 or h_count[1] > 1) and h_count[0] != 1:
							sys.exit()
						elif h_count[0] == 1: h = h_temp
					elif h_count[0] == 1: h = h_temp
				elif h_count[0]+h_count[1] > 1:
					print(Style.BRIGHT+Fore.YELLOW+u'У вас открыто два (или более) окна одной версии Minecraft. Когда вы нажмёте Enter, нужным окном будет считаться несвёрнутое окно.'+Style.RESET_ALL)
					raw_input()
					h_count = [0,0]
					try:
						w3.EnumWindows(enumHandler, 0)
					except: None
					if h_count[0]+h_count[1] == 0:
						print(Style.BRIGHT+Fore.RED+u'Зачем вы закрыли ВСЕ окна?'+Style.RESET_ALL)
						print(u'(Нажмите Enter для завершения)',end='')
						raw_input()
						sys.exit()
					h = h_temp
				else: h = h_temp
				for i in range(len(colors)):
					if np.array_equal(im[height-1][0],colors[i]):
						color = i % 9 + 1
						hotbar = i // 9 + 1
				print(Style.BRIGHT+Fore.GREEN+u'Показывать процесс строительства в отдельном окне '+Fore.RED+u'(без него работает стабильнее)'+Fore.GREEN+u'?(y/n) '+Style.RESET_ALL, end='')
				show_progress = raw_input()
				print(Style.BRIGHT+Fore.GREEN+u'Заблокировать клавиатуру и мышь на время строительства?(y/n) '+Style.RESET_ALL, end='')
				block = raw_input()
				if block == 'y' or block == 'Y': print(Style.BRIGHT+Fore.RED+u'(Чтобы убрать блокировку, нажмите Ctrl + Alt + Delete)'+Style.RESET_ALL)
				if (block == 'y' or block == 'Y') and (show_progress == 'y' or show_progress == 'Y'):
					name = u'Построено:'.encode('1251')
					cv2.namedWindow(name, flags=cv2.WINDOW_NORMAL)
					cv2.resizeWindow(name,int(round(im_view.shape[1]*scale)),int(round(im_view.shape[0]*scale)))
					cv2.imshow(name, im_view)
				print(Fore.YELLOW+u'Начну через: '+Style.BRIGHT,end='')
				for i in reversed(range(1,11)):
					if i == 9: print(' '*2+'\b'*2,end='')
					if i > 3:
						print(Fore.YELLOW+str(i),end='')
						if block == 'y' or block == 'Y': cv2.waitKey(1000)
						else: time.sleep(1)
						print('\b'*len(str(i)),end='')
					else:
						print(Fore.RED+str(i),end='')
						if block == 'y' or block == 'Y': cv2.waitKey(1000)
						else: time.sleep(1)
						print('\b'*len(str(i)),end='')
				print(Style.RESET_ALL+'\b'*14+' '*14)
				if not w3.IsWindow(h):
					print(Style.BRIGHT+Fore.RED+u'Вы закрыли Minecraft.'+Style.RESET_ALL)
					print(u'(Нажмите Enter для завершения)',end='')
					raw_input()
					sys.exit()
				if block == 'y' or block == 'Y':
					ctypes.windll.user32.BlockInput(True)
					block_error = w1.GetLastError()
					if block_error != 0:
						print(Fore.RED+u'При блокировке клавиатуры и мыши произошла ошибка, номер ошибки - '+str(block_error)+u'. '+Style.BRIGHT+u'Если "Запуск от имени администратора" не поможет, то отправьте этот номер автору скрипта!'+Style.RESET_ALL)
						print(u'(Нажмите Enter для завершения)',end='')
						raw_input()
						sys.exit()
				else: 
					w3.SendMessage(h, w2.WM_KILLFOCUS, 0, 0)
					w3.ShowWindow(h, w2.SW_MINIMIZE)
					time.sleep(1)
					if (show_progress == 'y' or show_progress == 'Y'):
						name = u'Построено:'.encode('1251')
						cv2.namedWindow(name, flags=cv2.WINDOW_NORMAL)
						cv2.resizeWindow(name,int(round(im_view.shape[1]*scale)),int(round(im_view.shape[0]*scale)))
						cv2.imshow(name, im_view)
				w1.SetConsoleCtrlHandler(on_exit, True)
				prev_time = time.time()
				slow(True)
				selectItem(color,hotbar)
				pressKey('space')
				rightClick()
				updateStat()
				if (show_progress == 'y' or show_progress == 'Y'):
					im_view[height-1][0] = np.flip(im[height-1][0])
					cv2.imshow(name,im_view)
					cv2.waitKey(1)
				keyDown('d')
				time.sleep(0.3)
				for y in range(height):
					if y != 0:
						for i in range(len(colors)):
							if np.array_equal(im[height-y-1][x],colors[i]): 
								color = i % 9 + 1
								hotbar = i // 9 + 1
						selectItem(color,hotbar)
						pressKey('space')
						rightClick()
						updateStat()
						if (show_progress == 'y' or show_progress == 'Y'):
							im_view[height-y-1][x] = np.flip(im[height-y-1][x])
							cv2.imshow(name,im_view)
							cv2.waitKey(1)
							time.sleep(0.199)
						else: time.sleep(0.2)
					if dir == 0:
						keyUp('a')
						keyDown('d')
						time.sleep(t)
						for x in range(width):
							prev_time1 = time.time()
							if x != 0:
								for i in range(len(colors)):
									if np.array_equal(im[height-1-y][x],colors[i]):
										color = i % 9 + 1
										hotbar = i // 9 + 1
								prev_time1 = time.time()
								selectItem(color,hotbar)
								rightClick()
								updateStat()
								if (show_progress == 'y' or show_progress == 'Y'):
									im_view[height-y-1][x] = np.flip(im[height-y-1][x])
									cv2.imshow(name,im_view)
									cv2.waitKey(1)
									time.sleep(abs(t+0.029-float('{0:.2f}'.format(time.time()-prev_time1))))
								else: time.sleep(abs(t+0.03-float('{0:.2f}'.format(time.time()-prev_time1))))
					else:
						keyUp('d')
						keyDown('a')
						time.sleep(t)
						for x in reversed(range(width)):
							prev_time1 = time.time()
							if x != width-1:
								for i in range(len(colors)):
									if np.array_equal(im[height-1-y][x],colors[i]): 
										color = i % 9 + 1
										hotbar = i // 9 + 1
								prev_time1 = time.time()
								selectItem(color,hotbar)
								rightClick()
								updateStat()
								if (show_progress == 'y' or show_progress == 'Y'):
									im_view[height-y-1][x] = np.flip(im[height-y-1][x])
									cv2.imshow(name,im_view)
									cv2.waitKey(1)
									time.sleep(abs(t+0.029-float('{0:.2f}'.format(time.time()-prev_time1))))
								else: time.sleep(abs(t+0.03-float('{0:.2f}'.format(time.time()-prev_time1))))
					if dir == 0: dir = 1
					else: dir = 0
				slow(False)
				keyUp('a')
				keyUp('d')
				ctypes.windll.user32.BlockInput(False)
				print(upd_blocks_clr,end='')
				print(Style.BRIGHT+Fore.GREEN+u'Готово! На это ушло минут: ' + '{0:.2f}'.format((time.time()-prev_time)/60).replace('.',',')+u'.          '+Style.RESET_ALL)
				print(u'(Нажмите Enter для завершения)',end='')
				if (show_progress == 'y' or show_progress == 'Y'): cv2.destroyAllWindows()
				w3.ShowWindow(h, w2.SW_SHOWNORMAL)
				if block != 'y' and block != 'Y':
					w3.SendMessage(h, w2.WM_SETFOCUS, 0, 0)
				time.sleep(1)
				try:
					w3.SetActiveWindow(h_self)
					w3.ShowWindow(h_self, w2.SW_SHOWNORMAL)
					w3.SetForegroundWindow(h_self)
				except: None
				raw_input()
except Exception as e:
	print(Fore.RED+u'Произошла ошибка. Подробности в error.log.'+Style.RESET_ALL)
	file = open('error.log', 'w')
	file.write(traceback.format_exc())
	file.close()
	print(u'(Нажмите Enter для завершения)',end='')
	raw_input()