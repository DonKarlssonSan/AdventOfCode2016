def possible_triangles_vertically(input_string):
    possible_triangles_sum = 0
    rows = input_string.split('\n')
    for i in range(0, len(rows), 3):
        for col in range(0, 3):
            sides = [int(side) for side in [rows[i].split()[col], rows[i+1].split()[col], rows[i+2].split()[col]]]
            if sides[0] + sides[1] > sides[2] and sides[0] + sides[2] > sides[1] and sides[1] + sides[2] > sides[0]:
                possible_triangles_sum += 1

    return possible_triangles_sum
