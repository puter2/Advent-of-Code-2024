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

    def isBlob(self,tab,x,y):
        for i in range(x,x+8):
            for j in range(y, y+8):
                if tab[i][j] != '0':
                    return False
        return True

    def findBlob(self,tab):
        '''
        find if table has an 7x7 block of 0's
        '''
        for i in range(len(tab)-8):
            for j in range(len(tab[0])-8):
                if self.isBlob(tab, i, j):
                    return True
        return False
    
    def show(self, data, time, width, height):
        positions = self.calculatePositions(data, time, width, height)
        res = [['.' for i in range(height)] for j in range(width)]
        print(len(positions.keys()))
        for key in positions.keys():
            res[key[0]][key[1]] = '0'
        #     # print(key)
        # res[0][1] = '0'
        # for row in res:
        #     print(''.join(row))
        if self.findBlob(res):
            with open('day 14\\outpus.txt','w') as file:
                for row in res:
                    file.write(''.join(row))
                    file.write('\n')
            input()


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