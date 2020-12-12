"""
Before you can give the destination to the captain, you realize that the actual action meanings were printed on the back of the instructions the whole time.

Almost all of the actions indicate how to move a waypoint which is relative to the ship's position:

Action N means to move the waypoint north by the given value.
Action S means to move the waypoint south by the given value.
Action E means to move the waypoint east by the given value.
Action W means to move the waypoint west by the given value.
Action L means to rotate the waypoint around the ship left (counter-clockwise) the given number of degrees.
Action R means to rotate the waypoint around the ship right (clockwise) the given number of degrees.
Action F means to move forward to the waypoint a number of times equal to the given value.
The waypoint starts 10 units east and 1 unit north relative to the ship. The waypoint is relative to the ship; that is, if the ship moves, the waypoint moves with it.

For example, using the same instructions as above:

F10 moves the ship to the waypoint 10 times (a total of 100 units east and 10 units north), leaving the ship at east 100, north 10. The waypoint stays 10 units east and 1 unit north of the ship.
N3 moves the waypoint 3 units north to 10 units east and 4 units north of the ship. The ship remains at east 100, north 10.
F7 moves the ship to the waypoint 7 times (a total of 70 units east and 28 units north), leaving the ship at east 170, north 38. The waypoint stays 10 units east and 4 units north of the ship.
R90 rotates the waypoint around the ship clockwise 90 degrees, moving it to 4 units east and 10 units south of the ship. The ship remains at east 170, north 38.
F11 moves the ship to the waypoint 11 times (a total of 44 units east and 110 units south), leaving the ship at east 214, south 72. The waypoint stays 4 units east and 10 units south of the ship.
After these operations, the ship's Manhattan distance from its starting position is 214 + 72 = 286.

Figure out where the navigation instructions actually lead. What is the Manhattan distance between that location and the ship's starting position?

Your puzzle answer was 52866
"""

class Waypoint():
    def __init__(self):
        self.ns = 1
        self.ew = 10

    def update_waypoint(self, action, count):
        if action == "N":
            self.ns += steps
        if action == "S":
            self.ns -= steps
        if action == "E":
            self.ew += steps
        if action == "W":
            self.ew -= steps
        if action == "R":
            self.rotate_right( steps // 90 )
        if action == "L":
            self.rotate_left( steps // 90 )

    def rotate_right(self, turn_count):
        for i in range(turn_count):
            # invert the value of east/west and store in north/south
            # value in north/south becomes east/west
            temp = self.ns
            self.ns = 0 - self.ew
            self.ew = temp

    def rotate_left(self, turn_count):
        for i in range(turn_count):
            # invert the value of north/south and store in east/west
            # value in east/west becomes north/south
            temp = self.ns
            self.ns = self.ew
            self.ew = 0 - temp

    def get_ns(self):
        return self.ns

    def get_ew(self):
        return self.ew

class Ship():

    def __init__(self):
        self.ns = 0 # north/south pos
        self.ew = 0 # east/west pos
        self.waypoint = Waypoint()

    def preform_action(self, action, steps):
        if action == "F":
            self.ns += steps * self.waypoint.get_ns()
            self.ew += steps * self.waypoint.get_ew()
        else:
            self.waypoint.update_waypoint(action, steps)

    def manhattan_distance(self):
        return abs(self.ns) + abs(self.ew)


f = open("input.txt", "r")

ship = Ship()
for line in f:
    action = line[0]
    steps = int(line[1:].strip())
    ship.preform_action(action, steps)

print(ship.manhattan_distance())