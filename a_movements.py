from v_cubes import char_cube, cube_to_graphics, graphics_to_cube


class Movement:
    left = [char_cube[0][i][:] for i in range(0, 3)]
    front = [char_cube[1][i][:] for i in range(0, 3)]
    right = [char_cube[2][i][:] for i in range(0, 3)]
    back = [char_cube[3][i][:] for i in range(0, 3)]
    down = [char_cube[4][i][:] for i in range(0, 3)]
    up = [char_cube[5][i][:] for i in range(0, 3)]

    def type(direction):
        match(direction):
            case "up":
                Movement.move('U', [[5, i, j, 2-j, i] for i in range(0, 3) for j in range(0, 3)],
                              [[j, 0, i, 0, i]
                                  for i in range(0, 3) for j in range(0, 4)],
                              [Movement.up],
                              [Movement.front, Movement.right, Movement.back, Movement.left])
            case "up prime":
                Movement.move('U\'', [[5, i, j, j, 2-i] for i in range(0, 3) for j in range(0, 3)],
                              [[j, 0, i, 0, i]
                                  for i in range(0, 3) for j in range(0, 4)],
                              [Movement.up],
                              [Movement.back, Movement.left, Movement.front, Movement.right])
            case "down":
                Movement.move('D', [[4, i, j, 2-j, i] for i in range(0, 3) for j in range(0, 3)],
                              [[j, 2, i, 2, i]
                                  for i in range(0, 3) for j in range(0, 4)],
                              [Movement.down],
                              [Movement.back, Movement.left, Movement.front, Movement.right])
            case "down prime":
                Movement.move('D\'', [[4, i, j, j, 2-i] for i in range(0, 3) for j in range(0, 3)],
                              [[j, 2, i, 2, i]
                                  for i in range(0, 3) for j in range(0, 4)],
                              [Movement.down],
                              [Movement.front, Movement.right, Movement.back, Movement.left])
            case "left":
                Movement.move('L', [[0, i, j, 2-j, i] for i in range(0, 3) for j in range(0, 3)],
                              [[j[0], i, j[1], j[2], j[3]] for i in range(0, 3) for j in list(
                                  zip([3, 5, 1, 4], [2, 0, 0, 0], [2-i, 2-i, i, i], [0, 2, 0, 0]))],
                              [Movement.left],
                              [Movement.down, Movement.back, Movement.up, Movement.front])
            case "left prime":
                Movement.move('L\'', [[0, i, j, j, 2-i] for i in range(0, 3) for j in range(0, 3)],
                              [[j[0], i, j[1], j[2], j[3]] for i in range(0, 3) for j in list(
                                  zip([3, 5, 1, 4], [2, 0, 0, 0], [2-i, i, i, 2-i], [0, 0, 0, 2]))],
                              [Movement.left],
                              [Movement.up, Movement.front, Movement.down, Movement.back])
            case "right":
                Movement.move('R', [[2, i, j, 2-j, i] for i in range(0, 3) for j in range(0, 3)],
                              [[j[0], i, j[1], j[2], j[3]] for i in range(0, 3) for j in list(
                                  zip([3, 5, 1, 4], [0, 2, 2, 2], [2-i, i, i, 2-i], [2, 2, 2, 0]))],
                              [Movement.right],
                              [Movement.up, Movement.front, Movement.down, Movement.back])
            case "right prime":
                Movement.move('R\'', [[2, i, j, j, 2-i] for i in range(0, 3) for j in range(0, 3)],
                              [[j[0], i, j[1], j[2], j[3]] for i in range(0, 3) for j in list(
                                  zip([3, 5, 1, 4], [0, 2, 2, 2], [2-i, 2-i, i, i], [2, 0, 2, 2]))],
                              [Movement.right],
                              [Movement.down, Movement.back, Movement.up, Movement.front])
            case "front":
                Movement.move('F', [[1, i, j, 2-j, i] for i in range(0, 3) for j in range(0, 3)],
                              [[j[0], j[1], j[2], j[3], j[4]] for i in range(0, 3) for j in list(
                                  zip([0, 5, 2, 4], [i, 2, i, 0], [2, i, 0, i], [0, 2-i, 2, 2-i], [i, 2, i, 0]))],
                              [Movement.front],
                              [Movement.down, Movement.left, Movement.up, Movement.right])
            case "front prime":
                Movement.move('F\'', [[1, i, j, j, 2-i] for i in range(0, 3) for j in range(0, 3)],
                              [[j[0], j[1], j[2], j[3], j[4]] for i in range(0, 3) for j in list(
                                  zip([0, 5, 2, 4], [i, 2, i, 0], [2, i, 0, i], [2, i, 0, i], [2-i, 0, 2-i, 2]))],
                              [Movement.front],
                              [Movement.up, Movement.right, Movement.down, Movement.left])
            case "back":
                Movement.move('B', [[3, i, j, 2-j, i] for i in range(0, 3) for j in range(0, 3)],
                              [[j[0], j[1], j[2], j[3], j[4]] for i in range(0, 3) for j in list(
                                  zip([0, 5, 2, 4], [i, 0, i, 2], [0, i, 2, i], [0, i, 2, i], [2-i, 2, 2-i, 0]))],
                              [Movement.back],
                              [Movement.up, Movement.right, Movement.down, Movement.left])
            case "back prime":
                Movement.move('B\'', [[3, i, j, j, 2-i] for i in range(0, 3) for j in range(0, 3)],
                              [[j[0], j[1], j[2], j[3], j[4]] for i in range(0, 3) for j in list(
                                  zip([0, 5, 2, 4], [i, 0, i, 2], [0, i, 2, i], [2, 2-i, 0, 2-i], [i, 0, i, 2]))],
                              [Movement.back],
                              [Movement.down, Movement.left, Movement.up, Movement.right])

    def move(direction, side_rotations, sides_changes, movement_rotations, movement_changes):
        for side_rotation in side_rotations:
            char_cube[side_rotation[0]][side_rotation[1]][side_rotation[2]
                                                          ] = movement_rotations[0][side_rotation[3]][side_rotation[4]]

        for i, movement in enumerate(movement_changes):
            for sides_change in [sides_changes[i], sides_changes[i+4], sides_changes[i+8]]:
                char_cube[sides_change[0]][sides_change[1]][sides_change[2]
                                                            ] = movement[sides_change[3]][sides_change[4]]
        Movement.update_cube()
        return direction

    def refresh():
        Movement.left = [char_cube[0][i][:] for i in range(0, 3)]
        Movement.front = [char_cube[1][i][:] for i in range(0, 3)]
        Movement.right = [char_cube[2][i][:] for i in range(0, 3)]
        Movement.back = [char_cube[3][i][:] for i in range(0, 3)]
        Movement.down = [char_cube[4][i][:] for i in range(0, 3)]
        Movement.up = [char_cube[5][i][:] for i in range(0, 3)]

    def update_cube():
        cube_to_graphics()
        graphics_to_cube()
        Movement.refresh()
