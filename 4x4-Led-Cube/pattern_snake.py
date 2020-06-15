from time import sleep
import RPi.GPIO as GPIO
import utility
from random import randrange

delay = 0.3
delay_captured = 0.07
snake = []


def tuple_str(i, j):
    return str(i) + "," + str(j)


def print_snake():
    print "~~ snake :"
    for (i, j) in snake:
        print "(" + tuple_str(i, j) + ") "


def captured(grid):
    for n in range(0, 2):
        for (i, j) in snake:
            GPIO.output(grid[i][j], GPIO.HIGH)
        sleep(delay_captured)
        for (i, j) in snake:
            GPIO.output(grid[i][j], GPIO.LOW)
        sleep(delay_captured)


def get_empty_positions():
    print "get_empty_positions"
    empty_pos = []
    for i in range(0, 4):
        for j in range(0, 4):
            empty = True
            for s_pos in snake:
                s_i, s_j = s_pos
                if (s_i == i) and (s_j == j):
                    empty = False
                    break
            if empty:
                empty_pos.append((i, j))
    return empty_pos


def init(grid):
    del snake[:]
    GPIO.output(grid[1][1], GPIO.LOW)
    GPIO.output(grid[1][2], GPIO.LOW)
    GPIO.output(grid[1][3], GPIO.LOW)
    snake.append((1, 1))
    snake.append((1, 2))
    snake.append((1, 3))
    sleep(delay)


def next_insect(grid):
    print "place next insect"
    empty_pos = get_empty_positions()
    next = randrange(0, 16 - len(snake))
    i, j = empty_pos[next]
    print("%% NEXT INSECT : " + tuple_str(i, j))
    GPIO.output(grid[i][j], GPIO.LOW)
    return i, j


def is_snake_pos(i, j):
    for (s_i, s_j) in snake:
        if s_i == i and s_j == j:
            return True
    return False


def capture(insect_i, insect_j, grid):
    print ("capturing " + tuple_str(insect_i, insect_j) + " .....")
    while True:
        print_snake()
        s_i, s_j = snake[0]
        print "Head : " + tuple_str(s_i, s_j)
        if s_i == insect_i:
            if s_j == insect_j:
                print "*** captured ***"
                break
            elif s_j < insect_j:
                if is_snake_pos(s_i, s_j + 1):
                    if s_i + 1 < 4:
                        s_i = s_i + 1
                    else:
                        s_i = s_i - 1
                else:
                    s_j = s_j + 1
            else:
                if is_snake_pos(s_i, s_j - 1):
                    if s_i + 1 < 4:
                        s_i = s_i + 1
                    else:
                        s_i = s_i - 1
                else:
                    s_j = s_j - 1
        elif s_i < insect_i:
            if is_snake_pos(s_i + 1, s_j):
                if s_j + 1 < 4:
                    s_j = s_j + 1
                else:
                    s_j = s_j - 1
            else:
                s_i = s_i + 1
        else:
            if is_snake_pos(s_i - 1, s_j):
                if s_j + 1 < 4:
                    s_j = s_j + 1
                else:
                    s_j = s_j - 1
            else:
                s_i = s_i - 1
        print ("next move : " + tuple_str(s_i, s_j))
        snake.insert(0, (s_i, s_j))
        # if s_i == insect_i and s_j == insect_j and False:
        #     print ""
        # else:
        prev_i, prev_j = snake.pop()
        print "prev : " + tuple_str(prev_i, prev_j)
        GPIO.output(grid[prev_i][prev_j], GPIO.HIGH)
        GPIO.output(grid[s_i][s_j], GPIO.LOW)
        sleep(delay)


def snake_game(layers, grid):
    utility.reset(layers, grid)
    GPIO.output(layers[3], GPIO.HIGH)
    init(grid)
    for insects in range(0, 30):
        insect_i, insect_j = next_insect(grid)
        captured(grid)
        capture(insect_i, insect_j, grid)
    utility.reset(layers, grid)
