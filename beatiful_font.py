"""
Nome: Beatiful_Color
Função: Estilizar sessões de um texto, com diversas cores e estilos
Autor: Állan Rocha
Data: 10/8/2017
"""

FONT_COLORS = {
    'style' : '',
    's': '',
    'black': '30',
    'b': '30',
    'red': '31',
    'r': '31',
    'green': '32',
    'g': '32',
    'yellow': '33',
    'y': '33',
    'blue': '34',
    'bl' : '34',
    'magenta': '35',
    'm': '35',
    'cyan': '36',
    'c': '36',
    'white': '37',
    'w': '37',
    'default': '38',
    'd': '38',
    'rgb' : '##'
}

STYLES = {
    "bold" : "1",
    "b" : "1",
    "light" : "2",
    "l" : "2",
    "italic": "3",
    "i" : "3",
    "underline" : "4",
    "u" : "4",
    "blink-slow" : "5",
    "bs" : "5",
    "blink-fast" : "6",
    "bf" : "6",
    "medium-line" : "9",
    "ml" : "9",
    "overline" : "53",
    "ov" : "53"
}

ANSI = "\033["
END = "\033[0m"

def beatiful_font(text):
    """
    Função que estiliza certas partes de um texto, de acordo com as cores e estilos
    definidos pelo programador
    """

    father = []
    ansi = []
    scala = -1

    for word in text.split(">"):
        start = word.find("<") + 1
        color = word[start:]
        tag = ""

        for style in color.split(" "):
            if style in STYLES:
                tag += STYLES[style] + ";"

        color = color.split(" ")[0]

        if color.find("rgb") != -1 and color.find("/") == -1:
            ansi_rgb_code = rgb_color(color)
            FONT_COLORS["rgb"] = ansi_rgb_code
            color = "rgb"

        if color in FONT_COLORS:
            tag_color = ANSI + tag
            if FONT_COLORS[color] == "":
                tag_color = tag_color[:len(tag_color) - 1] + "m"
            else:
                tag_color += FONT_COLORS[color] + "m"
            pre_text = word[:start - 1]
            ansi.extend([pre_text, tag_color])
            father.append(tag_color)
            scala += 1
        elif color[1:] in FONT_COLORS or color.find("rgb") != -1:
            pre_text = word[:start - 1]
            if scala - 1 < 0:
                ansi.extend([pre_text, END])
            else:
                ansi.extend([pre_text, END, father[scala - 1]])
            scala -= 1
        else:
            ansi.append(word)
    print(repr(ansi))
    return "".join(ansi)

def rgb_color(code):
    """
    Função que colore o texto com base no rgb
    """
    rgb = code.split(":")[1]
    ansi_code = ["38;2"]

    for color in rgb.split(","):
        ansi_code.append(color)
    return ";".join(ansi_code)

if __name__ == "__main__":
    print(beatiful_font("<b>Hello</b> <rgb:0,0,0>Programador</rgb> <y i>:)</y></s>"))
    