import math
import cmath

a90 = math.pi/2
def walk(instructions):
    angle = a90
    pos = complex(0, 0)
    for instruction in instructions.split(', '):
        turn = instruction[0]
        if turn == 'L':
            angle += a90
        elif turn == 'R':
            angle -= a90
        length = int(instruction[1:])
        delta = cmath.rect(length, angle)
        pos += delta
    blocksAway = int(abs(pos.real) + abs(pos.imag))
    print('Blocks away: ' + str(blocksAway))

walk('R2, L3')
walk('R2, R2, R2')
walk('R5, L5, R5, R3')
walk('R3, L2, L2, R4, L1, R2, R3, R4, L2, R4, L2, L5, L1, R5, R2, R2, L1, R4, R1, L5, L3, R4, R3, R1, L1, L5, L4, L2, R5, L3, L4, R3, R1, L3, R1, L3, R3, L4, R2, R5, L190, R2, L3, R47, R4, L3, R78, L1, R3, R190, R4, L3, R4, R2, R5, R3, R4, R3, L1, L4, R3, L4, R1, L4, L5, R3, L3, L4, R1, R2, L4, L3, R3, R3, L2, L5, R1, L4, L1, R5, L5, R1, R5, L4, R2, L2, R1, L5, L4, R4, R4, R3, R2, R3, L1, R4, R5, L2, L5, L4, L1, R4, L4, R4, L4, R1, R5, L1, R1, L5, R5, R1, R1, L3, L1, R4, L1, L4, L4, L3, R1, R4, R1, R1, R2, L5, L2, R4, L1, R3, L5, L2, R5, L4, R5, L5, R3, R4, L3, L3, L2, R2, L5, L5, R3, R4, R3, R4, R3, R1')