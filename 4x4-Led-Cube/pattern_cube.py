from time import sleep
import RPi.GPIO as GPIO
import utility

delay = 0.2

def cube_4x4(layers, grid):
    utility.on_all_layers(layers)
    GPIO.output(grid[0][0], GPIO.LOW)
    GPIO.output(grid[0][3], GPIO.LOW)
    GPIO.output(grid[3][0], GPIO.LOW)
    GPIO.output(grid[3][3], GPIO.LOW)
    sleep(delay)
    utility.reset(layers, grid)


def cube_2x2(layers, grid):
    GPIO.output(layers[1], GPIO.HIGH)
    GPIO.output(layers[2], GPIO.HIGH)
    for i in range(1, 3):
        for j in range(1, 3):
            GPIO.output(grid[i][j], GPIO.LOW)
    sleep(delay)
    utility.reset(layers, grid)


def tuple_str(i, j):
    return "(" + str(i) + "," + str(j) + ")"


def cube_travel(layers, grid, pat):
    print "pat: " + str(pat)
    increase = False
    row_start = 0
    row_end = 3
    col_start = 0
    col_end = 3
    planes = layers[:]
    for k in range(0, 5):
        print str(increase) + ", " + tuple_str(row_start, col_start) + " :: " + tuple_str(row_end, col_end) + ", planes: " + ','.join(str(planes))

        utility.reset_grid(grid)
        for i in range(row_start, row_end + 1):
            GPIO.output(grid[i][col_start], GPIO.LOW)
            GPIO.output(grid[i][col_end], GPIO.LOW)
        for j in range(col_start, col_end + 1):
            GPIO.output(grid[row_start][j], GPIO.LOW)
            GPIO.output(grid[row_end][j], GPIO.LOW)

        utility.reset_layers(layers)
        for plane in planes:
            GPIO.output(plane, GPIO.HIGH)

        sleep(delay)

        if pat == 1:
            if increase:
                row_end = row_end + 1
                col_end = col_end + 1
                if len(planes) < 4:
                    planes.append(layers[len(planes)])
            else:
                row_end = row_end - 1
                col_end = col_end - 1
                planes.pop()

        elif pat == 2:
            if increase:
                row_start = row_start - 1
                col_start = col_start - 1
                if len(planes) < 4:
                    planes.insert(0, layers[3 - len(planes)])
            else:
                row_start = row_start + 1
                col_start = col_start + 1
                planes.pop(0)

        elif pat == 3:
            if increase:
                row_end = row_end + 1
                col_end = col_end + 1
                if len(planes) < 4:
                    planes.insert(0, layers[3 - len(planes)])
            else:
                row_end = row_end - 1
                col_end = col_end - 1
                planes.pop(0)

        elif pat == 4:
            if increase:
                row_start = row_start - 1
                col_start = col_start - 1
                if len(planes) < 4:
                    planes.append(layers[len(planes)])
            else:
                row_start = row_start + 1
                col_start = col_start + 1
                planes.pop()

        elif pat == 5:
            if increase:
                row_start = row_start - 1
                col_end = col_end + 1
                if len(planes) < 4:
                    planes.append(layers[len(planes)])
            else:
                row_start = row_start + 1
                col_end = col_end - 1
                planes.pop()

        elif pat == 6:
            if increase:
                row_end = row_end + 1
                col_start = col_start - 1
                if len(planes) < 4:
                    planes.insert(0, layers[3 - len(planes)])
            else:
                row_end = row_end - 1
                col_start = col_start + 1
                planes.pop(0)

        elif pat == 7:
            if increase:
                row_start = row_start - 1
                col_end = col_end + 1
                if len(planes) < 4:
                    planes.insert(0, layers[3 - len(planes)])
            else:
                row_start = row_start + 1
                col_end = col_end - 1
                planes.pop(0)

        elif pat == 8:
            if increase:
                row_end = row_end + 1
                col_start = col_start - 1
                if len(planes) < 4:
                    planes.append(layers[len(planes)])
            else:
                row_end = row_end - 1
                col_start = col_start + 1
                planes.pop()



        if row_start == row_end - 1 and col_start == col_end - 1:
            increase = not increase


def cube_pattern(layers, grid):
    for i in range(0, 1):
        cube_travel(layers, grid, 1)
        cube_travel(layers, grid, 2)
        cube_travel(layers, grid, 3)
        cube_travel(layers, grid, 4)
        cube_travel(layers, grid, 5)
        cube_travel(layers, grid, 6)
        cube_travel(layers, grid, 7)
        cube_travel(layers, grid, 8)
    for i in range(0, 4):
        cube_4x4(layers, grid)
        cube_2x2(layers, grid)
