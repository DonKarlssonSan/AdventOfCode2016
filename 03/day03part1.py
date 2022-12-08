def possible_triangles(input_string):
    possible_triangles_sum = 0
    triangles = input_string.split('\n')
    for triangle in triangles:
        sides = [int(side) for side in triangle.split()]
        if sides[0] + sides[1] > sides[2] and sides[0] + sides[2] > sides[1] and sides[1] + sides[2] > sides[0]:
            possible_triangles_sum += 1
    return possible_triangles_sum