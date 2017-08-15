no_of_calls = 0
no_of_moves = 0         # No. of moves = 2^(n_disks) - 1


def move_disk(n_disks, start_peg, end_peg):
    # global no_of_moves
    # no_of_moves += 1
    print('Moving disk %d from peg %d --> peg %d' % (n_disks, start_peg, end_peg))


def towers_of_hanoi(n_disks, start_peg=1, end_peg=3):
    global no_of_calls
    no_of_calls += 1
    if n_disks:
        towers_of_hanoi(n_disks - 1, start_peg, 6 - start_peg - end_peg)
        move_disk(n_disks, start_peg, end_peg)
        towers_of_hanoi(n_disks - 1, 6 - start_peg - end_peg, end_peg)


if __name__ == '__main__':
    print("Tower of Hanoi solution for 3 disks: ")
    towers_of_hanoi(3)
    # print("Total moves =", no_of_moves)

    # no_of_calls, no_of_moves = 0, 0

    print("\nTower of Hanoi solution for 4 disks: ")
    towers_of_hanoi(4)
    # print("Total moves =", no_of_moves)
