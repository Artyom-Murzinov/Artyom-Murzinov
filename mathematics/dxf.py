import ezdxf
from ezdxf.addons.text2path import Kind, explode
from ezdxf.enums import TextEntityAlignment
import math
from ezdxf.addons.drawing import matplotlib
import configparser
from ezdxf.fonts import fonts
config = configparser.ConfigParser()
config.read("settings.ini")
ezdxf.options.support_dirs = config['core']["support_dirs"]
fonts.build_system_font_cache()


class TextEngraving:
    def __init__(self, dictory):
        list_shrift = ["ГОСТ тип А.ttf", "T-FlexA.ttf", "AmericanTypewriter.ttc", "PTSans.ttc", "GOST 26.008-85.ttf"]
        self.fonts = list_shrift[int(dictory["fonts"])]
        self.text_position = (float(dictory["text_position"].split(',')[0]), float(dictory["text_position"].split(',')[1]))  #расположение в системе координат
        if int(dictory["text_alignments"]) == 1:
            self.location = TextEntityAlignment.BOTTOM_LEFT
        if int(dictory["text_alignments"]) == 2:
            self.location = TextEntityAlignment.TOP_LEFT
        if int(dictory["text_alignments"]) == 3:
            self.location = TextEntityAlignment.TOP_CENTER
        if int(dictory["text_alignments"]) == 4:
            self.location = TextEntityAlignment.TOP_RIGHT
        if int(dictory["text_alignments"]) == 5:
            self.location = TextEntityAlignment.BOTTOM_RIGHT
        if int(dictory["text_alignments"]) == 6:
            self.location = TextEntityAlignment.BOTTOM_CENTER

        self.doc = ezdxf.new("AC1032", setup=True)
        self.msp = self.doc.modelspace()
        self.text_circle = dictory["text_circle"] #прямое или по окружности
        self.text_content = dictory["text_content"] #текст
        self.text_size = float(dictory["text_size"])        #высота символов
        self.shag = float(dictory["shag"])             #между символами
        self.angle = float(dictory["angle"]) #угол
        self.oblique = float(dictory['oblique']) # наклон
        #FONT = fonts.FontFace(family=self.fonts)
        # Радиус окружности
        if dictory["text_circle"] == 1:
            self.radius = dictory["radius"]           #радиус 
        self.doc.styles.new("myStandard", dxfattribs = {'font': self.fonts})


    def __str__(self):
        return TextEngraving.generating_code(self)

    def func_grav(dxf_poli, text):
        engraving = explode(dxf_poli, kind=4)
        for coordinates in engraving:
            if coordinates.dxftype() =="LWPOLYLINE":
                text += f"G0 X{round(coordinates[0][0], 4)} Y{round(coordinates[0][1], 4)}\n"
                text += f"G0 Z#1\n"
                text += f"G1 Z-[#2]\n"
                for coordinat in coordinates:
                    text += f"G1 X{round(coordinat[0], 4)} Y{round(coordinat[1], 4)}\n"
                text += f"G0 Z#1\n"
            if coordinates.dxftype() =="SPLINE":
                text += f"G0 X{coordinates.control_points[0][0]} Y{coordinates.control_points[0][1]}\n"
                text += f"G0 Z#1\n"
                text += f"G1 Z-[#2]\n"
                for coordinat in coordinates.control_points:
                    text+= f"G1 X{coordinat[0]} Y{coordinat[1]}\n"
                text += f"G0 Z#1\n"
        return text


    def generating_code(self):
        text = f"% \nT1M6 \nS3000M3 \nF600 \nD1H1 \nG43 \n"
        text += f"#1 = 2 (Bezopasnji pod'ezd) \n"
        text += f"#2 = 0.1 (glubina frezerowaniya) \n"
        if self.text_circle == 0:
            dxf_poli = self.msp.add_text(self.text_content, rotation=self.angle, dxfattribs = {
                'height': self.text_size,
                'style': "myStandard",
                'width': self.shag,
                'oblique': 15
            }).set_placement(self.text_position)
            text = TextEngraving.func_grav(dxf_poli, text)
        if self.text_circle == 1:    
            num_chars = len(self.text_content)
    # Угол между символами
            if self.shag == 0:
                angle_step = 360 / num_chars
            else:
                angle_step = self.shag
      
    # Добавляем текст по окружности
            for char in self.text_content:
                x = self.text_position[0] + self.radius * math.cos(math.radians(self.angle))  # Вычисляем x-координату
                y = self.text_position[1] + self.radius * math.sin(math.radians(self.angle))  # Вычисляем y-координату
                self.msp.add_text(char, rotation=self.angle-90, dxfattribs = {
                    'height': self.text_size,
                    'style' : "myStandard"}).set_placement((x, y), align = TextEntityAlignment.CENTER)
                self.angle -= angle_step 
            for dxf_poli in self.msp:
                if dxf_poli.dxftype() =="TEXT": 
                    text = TextEngraving.func_grav(dxf_poli, text)
        matplotlib.qsave(self.doc.modelspace(), 'your.png')
        text += f"G0 Z200 \nM30 \n%"
        return text
