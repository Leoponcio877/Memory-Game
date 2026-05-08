from random import shuffle
from turtle import (
    up, down, goto, color, begin_fill, end_fill,
    forward, left, write, clear, update,
    setup, hideturtle, tracer, onscreenclick, ontimer, done,
    shape, addshape, Turtle
)
from freegames import path

GRID_COLS   = 8
GRID_ROWS   = 8
TILE_SIZE   = 50
GRID_ORIGIN = -200
FONT_SIZE   = 20

SYMBOLS = [
    '@', '#', '*', '[', '+', '-', '_', '%',
    '$', '^', '&', '', '🐷', '🐸', '🐙', '🦋',
    '🌸', '🌞', '⭐', '🍕', '🍦', '🎈', '🎵', '🚀',
    '🌈', '🔥', '💎', '🍀', '🎯', '🏆', '🦄', '🌙',
]

tiles = SYMBOLS * 2
shuffle(tiles)

state = {
    'mark': None,
    'taps': 0,
}

hide = [True] * 64

def all_uncovered():
    """Return True if all tiles are uncovered."""
    return not any(hide)

counter = Turtle(visible=False)
counter.up()
counter.goto(-200, 180)

scorer = Turtle(visible=False)

def square(x, y):
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for _ in range(4):
        forward(TILE_SIZE)
        left(90)
    end_fill()


def index(x, y):
    col = int((x - GRID_ORIGIN) // TILE_SIZE)
    row = int((y - GRID_ORIGIN) // TILE_SIZE)
    return col + row * GRID_COLS


def xy(count):
    col = count % GRID_COLS
    row = count // GRID_COLS
    return col * TILE_SIZE + GRID_ORIGIN, row * TILE_SIZE + GRID_ORIGIN


def center_xy(count):
    x, y = xy(count)
    cx = x + TILE_SIZE // 2 - FONT_SIZE // 2
    cy = y + TILE_SIZE // 2 - FONT_SIZE // 2
    return cx, cy

def tap(x, y):
    """Update mark and hidden tiles based on tap."""

    state['taps'] += 1

    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None


def draw():
    "Draw image and tiles."
    clear()
    goto(0, 0)
    shape(car)
    

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 2, y)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))
       

    counter.clear()
    counter.write(f'Taps: {state["taps"]}', font=('Arial', 16, 'normal'))
    
    if all_uncovered():
       up()
       goto(-80, 0)
       color('green')
       write('You won!', font=('Arial', 30, 'normal'))

    update()
    ontimer(draw, 100)





def all_uncovered():
    return not any(hide)


#    ontimer(draw, 100)


car = path('car.gif')
setup(420, 420, 370, 0)
addshape(car)
shape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
