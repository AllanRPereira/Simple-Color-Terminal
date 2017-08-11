"""
Função: Definir funções para realização de operações com o cursor, usando
o terminal
Autor: Állan Rocha
"""

import sys
ANSI = "\033["

def cursor_move(direction="UP", lines=1):
    """
    Move o cursor de acordo com a direção e quantidade de linhas/colunas
    desejadas
    """
    directions = {"UP":"A", "DOWN":"B", "FORWARD": "C", "BACK":"D"}
    assert direction in directions
    sys.stdout.write("{}{}{}m".format(ANSI, lines, directions[direction]))

def next_line(position=1):
    """
    Move o cursor para a próxima linha, e o posiciona-o nessa linha
    """
    assert type(position) in (str, int)
    sys.stdout.write("{}{}{}m".format(ANSI, position, "E"))

def previous_line(position=1):
    """
    Move o cursor para a linha anterior, e o posiciona-o nessa linha
    """
    assert type(position) in (str, int)
    sys.stdout.write("{}{}{}m".format(ANSI, position, "F"))

def cursor_to_column(column=1):
    """
    Move o cursor para uma determinada coluna de uma linha
    """
    assert type(column) in (str, int)
    sys.stdout.write("{}{}{}m".format(ANSI, column, "G"))

def move_to_position(line=1, column=1):
    """
    Posiciona o cursor para as coordenada (line, column)
    """
    assert type(line) in (str, int)
    assert type(column) in (str, int)
    sys.stdout.write("{}{};{}{}m".format(ANSI, line, column, "H"))

def erase_in_terminal(mode="ALL_VIEW"):
    """
    Vários modos de limpar o terminal
    """
    cleans_mode = {"ALL" : "3", "ALL_VIEW" : "2", "CURSOR_END" : "1", "BEG_CURSOR" : "0"}
    assert mode in cleans_mode
    sys.stdout.write("{}{}{}".format(ANSI, cleans_mode[mode], "J"))

def erase_in_line(mode="ALL"):
    """
    Alguns modos para limpar uma linha de um terminal
    """
    line_clean_modes = {"ALL" : "2", "CURSOR_END" : "1", "BEG_CURSOR" : "0"}
    assert mode in line_clean_modes
    sys.stdout.write("{}{}{}".format(ANSI, line_clean_modes[mode], "K"))

def scroll_move(lines=40, mode="UP"):
    """
    Move o scroll para um terminada linha, tanto para cima,
    quanto para baixo
    """
    scroll_modes = {"UP" : "S", "DOWN": "T"}
    assert mode in scroll_modes
    sys.stdout.write("{}{}{}".format(ANSI, lines, scroll_modes[mode]))

def save_position():
    """
    Salva a posição do cursor na tela
    """
    sys.stdout.write("{}s".format(ANSI))

def restore_position():
    """
    Restaura a posição com base na posição salva
    """
    sys.stdout.write("{}u".format(ANSI))

def change_cursor_state(mode="SHOW"):
    """
    Altera certa característica do cursor
    """
    states = {"SHOW":"?25h", "HIDE":"?25l"}
    assert mode in states
    sys.stdout.write("{}{}".format(ANSI, states[mode]))

if __name__ == "__main__":
    change_cursor_state("HIDE")
    sys.stdout.write("Escondi seu cursor :D")
    