class Solver:

    def part1(self,data):
        safe = 0
        for report in data:
            decreasing, ascending = True, True
            for i in range(len(report)-1):
                if decreasing:
                    if report[i] >= report[i+1] or abs(report[i]-report[i+1]) > 3:
                        decreasing = False
                if ascending:
                    if report[i] <= report[i+1] or abs(report[i]-report[i+1]) > 3:
                        ascending = False
            if ascending or decreasing:
                safe += 1
                #print(report)
        return safe