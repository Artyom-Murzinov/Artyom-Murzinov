from scipy import interpolate
import numpy
from math import *


class UFG:
    """Этот класс выдает уголы под которыми необходимо повернуть фрезерную поворотную голову UFG"""
    """спомощью модуля scipy, строится сплайн по точкам и возвращает знаечение которое находится между точек"""
    '''Список табличный'''
    def __init__(self, cornerX, cornerZ):
        self.cornerX = cornerX
        self.cornerZ = cornerZ
        self.w_list = []
        self.a3g_list = []
        self.a2g_list = []
        self.a1g_list = []
        self.a_list = []   #--- X
        self.a1l_list = [] #--- A
        self.a2l_list = []
        self.a3l_list = [] #--- C

        
    def __str__(self):
        return UFG.calculation_angles(self)

    def making_list(self):
        '''Заполняю списки данными'''
        with open('telegram_bot/file_document/UFG.txt', 'r', encoding='utf8') as word:
            for i in word:
                # w_list
                wl = ''.join(i).split(' ')[7]
                y = float(f'{wl.split('°')[0]}.{wl.split('°')[-1][:-2]}')
                y2 = str(y)
                if len(y2.split('.')[-1]) == 2:
                    y1 = str(int(y2.split('.')[-1])/60)
                else:
                    y1 = str(int(y2.split('.')[-1])/6)
                y = float(f'{y2.split('.')[0]}.{y1.split('.')[-1]}')
                self.w_list.append(y)

                # a3d_list
                a3d = ''.join(i).split(' ')[6]
                y = float(f'{a3d.split('°')[0]}.{a3d.split('°')[-1][:-1]}')
                y2 = str(y)
                if len(y2.split('.')[-1]) == 2:
                    y1 = str(int(y2.split('.')[-1])/60)
                else:
                    y1 = str(int(y2.split('.')[-1])/6)
                y = float(f'{y2.split('.')[0]}.{y1.split('.')[-1]}')
                self.a3g_list.append(y)

                # a2d_list
                a2d = ''.join(i).split(' ')[5]
                y = float(f'{a2d.split('°')[0]}.{a2d.split('°')[-1][:-1]}')
                y2 = str(y)
                if len(y2.split('.')[-1]) == 2:
                    y1 = str(int(y2.split('.')[-1])/60)
                else:
                    y1 = str(int(y2.split('.')[-1])/6)
                y = float(f'{y2.split('.')[0]}.{y1.split('.')[-1]}')
                self.a2g_list.append(y)

            # a1d_list
                a1d = ''.join(i).split(' ')[4]
                y = float(f'{a1d.split('°')[0]}.{a1d.split('°')[-1][:-1]}')
                y2 = str(y)
                if len(y2.split('.')[-1]) == 2:
                    y1 = str(int(y2.split('.')[-1])/60)
                else:
                    y1 = str(int(y2.split('.')[-1])/6)
                y = float(f'{y2.split('.')[0]}.{y1.split('.')[-1]}')
                self.a1g_list.append(y)

            # a2l_list
                a2l = ''.join(i).split(' ')[1]
                y = float(f'{a2l.split('°')[0]}.{a2l.split('°')[-1][:-1]}')
                y2 = str(y)
                if len(y2.split('.')[-1]) == 2:
                    y1 = str(int(y2.split('.')[-1])/60)
                else:
                    y1 = str(int(y2.split('.')[-1])/6)
                y = float(f'{y2.split('.')[0]}.{y1.split('.')[-1]}')
                self.a2l_list.append(y)

            # Ось С
                a3l = ''.join(i).split(' ')[0]
                y = float(f'{a3l.split('°')[0]}.{a3l.split('°')[-1][:-1]}')
                y2 = str(y)
                if len(y2.split('.')[-1]) == 2:
                    y1 = str(int(y2.split('.')[-1])/60)
                else:
                    y1 = str(int(y2.split('.')[-1])/6)
                y = float(f'{y2.split('.')[0]}.{y1.split('.')[-1]}')
                self.a3l_list.append(y)

            # Задаваемый угол
                al = ''.join(i).split(' ')[3]
                x = float(f'{al.split('°')[0]}.{al.split('°')[-1][:-1]}')
                x2 = str(x)
                if len(x2.split('.')[-1]) == 2:
                    x1 = str(int(x2.split('.')[-1])/60)
                else:
                    x1 = str(int(x2.split('.')[-1])/6)
                x = float(f'{x2.split('.')[0]}.{x1.split('.')[-1]}')
                self.a_list.append(x)

                # Ось А
                a1l = ''.join(i).split(' ')[2]
                z = float(f'{a1l.split('°')[0]}.{a1l.split('°')[-1][:-1]}')
                z2 = str(z)
                if len(z2.split('.')[-1]) == 2:
                    z1 = str(int(z2.split('.')[-1])/60)
                else:
                    z1 = str(int(z2.split('.')[-1])/6)
                z = float(f'{z2.split('.')[0]}.{z1.split('.')[-1]}')
                self.a1l_list.append(z)

    def projecting_spline(self, list_a, list_b, list_c, corner):
        '''Создаю сплайн исходя из данных, затем находим нужное число исходя из сплайна'''
        list_a = numpy.array(list_a)
        list_b = numpy.array(list_b)
        list_c = numpy.array(list_c)
        Cheights_smooth = interpolate.splrep(list_c, list_a)
        Aheights_smooth = interpolate.splrep(list_c, list_b)
        Cheights = interpolate.splev(corner, Cheights_smooth)
        Aheights = interpolate.splev(corner, Aheights_smooth)
        return Cheights,  Aheights    


    def calculation_angles(self):
        '''Основной код запрашивает углы плоскости, и возвращает уже результат нужного
        поворота головы'''
        UFG.making_list(self)
        #cornerX = float(input('Введите угол вокруг оси X: '))
        #cornerZ = float(input('Введите угол вокруг оси Z: '))
        variable = 180
        if -90 <= self.cornerX <= 90 and -90 <= self.cornerZ <= 90: 
            if self.cornerX < 0:
                self.cornerX *= -1
                variable = 0
            corner1, corner2 = UFG.projecting_spline(self, self.a3l_list, self.a1l_list, self.a_list, self.cornerX)
            return f'C = {round(corner1.item() -variable - self.cornerZ, 3)}, A = {round(corner2.item(), 3)}'
        else:
            return f"Угол вокруг оси 'X' и 'Z' должен быть не более 90° и не менее -90°"

