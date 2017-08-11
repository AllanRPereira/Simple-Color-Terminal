# Ansi Terminal
## Objetivos
O objetivo desse projeto, é criar uma camada de abstração entre o programador, e as funcionalidades que os códigos de escape do ANSI proporcionam

## Como usar[PYTHON3]
O software é bem simples, e não há nenhum requerimento para que seja executado da maneira certa, sendo que basta apenas importar os arquivos do projeto e usar em suas aplicações, código para usar logo abaixo:

```
import beatiful_font
import cursor
```

Obs.: Software testado apenas no ambiente Linux

## Funcionalidades
### Cursor
Nesse arquivo concentram-se as funções responsáveis por manipular o cursor do Terminal, alterando tanto suas características, quanto sua posição na tela

Função              | Definição                            | Argumentos
------------------- | ------------------------------------ | -------------------------------------------------- |
cursor_move         | Move o curso para uma direção        | mode="UP","DOWN", "FORWARD", "BACK"                |
next_line           | Vai para a próxima linha             | column=int, str(number)                            |
previous_line       | Volta para a linha anterior          | column=int, str(number)                            |
cursor_to_column    | Vai para certa coluna da linha       | column=int, str(number)                            |
move_to_position    | Se move de acordo com as coordenadas | line=int e column=int                              |
erase_in_terminal   | Apaga certa parte do terminal        | mode="ALL", "ALL_VIEW", "CURSOR_END", "BEG_CURSOR" |
erase_in_line       | Apaga certa parte da linha           | mode="ALL", "CURSOR_END", "BEG_CURSOR"             |
scroll_move         | Move o scroll para certa direção     | lines=int, str(number), mode="UP", DOWN            |
save_position       | Salva a posição                      | Sem argumentos                                     |
restore_position    | Restaura a posição salva             | Sem argumentos                                     |
change_cursor_state | Muda o estado do cursor              | mode="SHOW", "HIDE"                                |


### Beatiful_Font
Nesse arquivo há a parte do software, que é responsável por colorir o seu texto, com as cores já disponíveis, e com as cores que você desejar utlizando o rgb!

#### Como usar
Para que estilize seus textos você deve usar uma ou mais das seguintes forma de escrita:

```python
import beatiful_font as bf
print(bf.beatiful_font("<red>Alerta, erro encontrado!!</red>"))

#Pode haver o aninhamento de cores

print(bf.beatiful_font("<red>Alerta, erro encontrado!! <blue>Erro Tal</blue></red>"))

#Vários modos de estilização

print(bf.beatiful_font("<red bold>Alerta, erro encontrado!! <blue i>Erro Tal</blue></red>"))

#Tag apenas para estilização

print(bf.beatiful_font("<style bold>Hello <s italic>World</s></style>"))

#RGB também disponível

print(bf.beatiful_font("<rgb:0,10,10 bold>Olá pessoal!!</rgb>"))
```

#### Regras 
Existem algumas regras para que a estilização funcione corretamente são elas:

* Toda cor deve ter um fechamento com o mesmo código de abertura
* Todas as estilizações devem estar separadas por espaço
* Não deve haver outros textos que estejam desse modo "\<texto>" 

Tabela de cores e estilos para seus textos:

Tags       | Cores Correspondentes |
---------- | --------------------- |
style, s   | Tag neutra            |
black, b   | Preto                 |
red, r     | Vermelho              |
green, g   | Verde                 |
yellow, y  | Amarelo               |
blue, bl   | Azul                  |
magenta, m | Roxo                  |
cyan, c    | Ciano                 |
white, w   | Branco                |
default, d | Padrão do Terminal    |
rgb        | RGB                   |

Estilos:

Styles          | Significados           |
--------------- | ---------------------- |
bold, b         | Mais intenso           |
light, l        | Mais suave             |
italic, i       | Inclinado              |
underline, u    | Linha abaixo           |
blink-slow, bs  | Pisca lentamente       |
blink-fast, bf  | Pisca rapidamente      |
medium-line, ml | Linha riscando no meio |
overline, ov    | Linha acima            |

