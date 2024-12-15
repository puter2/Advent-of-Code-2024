from robot import Robot

class Solver:

    def calculatePositions(self, data, time, width, height):
        positions = {}
        for robot in data:
            tmp = Robot()
            tmp.setPos(robot['p'])
            tmp.setVel(robot['v'])
            tmp.move(time, width, height)
            pos = tmp.getPos()
            if positions.get(pos):
                positions[pos] += 1
            else:
                positions[pos] = 1
        return positions
            
    def part1(self, data, time, width, height):
        positions = self.calculatePositions(data, time, width, height)
        q1, q2, q3, q4 = 0,0,0,0
        middle_row = height // 2
        middle_column = width // 2
        for key, val in positions.items():
            if key[0] < middle_column:
                if key[1] < middle_row:
                    q2 += val
                    print(key, '2')
                elif key[1] > middle_row:
                    q3 += val
                    print(key, '3')
            elif key[0] > middle_column:
                if key[1] < middle_row:
                    q1 += val
                    print(key, '1')
                elif key[1] > middle_row:
                    q4 += val
                    print(key, '4')
        print(q1,q2,q3,q4)
        return q1 * q2 * q3 * q4        