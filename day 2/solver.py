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
    
    def isDecreasing(self, report):
        for i in range(len(report) - 1):
            if report[i] <= report[i + 1] or report[i] - report[i + 1] > 3:
                return i
        return -1
    
    def isIncreasing(self, report):
        for i in range(len(report) - 1):
            if report[i] >= report[i + 1] or report[i + 1] - report[i] > 3:
                return i
        return -1
    
    def part2(self, data):
        safe = 0
        for report in data:
            decr_err = self.isDecreasing(report)
            incr_err = self.isIncreasing(report)
            if decr_err == -1 or incr_err == -1:
                safe += 1
            else:
                if (self.isDecreasing(report[:decr_err] + report[decr_err+1:]) == -1 or 
                    self.isDecreasing(report[:decr_err+1] + report[decr_err+2:]) == -1 or
                    self.isIncreasing(report[:incr_err] + report[incr_err+1:]) == -1 or
                    self.isIncreasing(report[:incr_err+1] + report[incr_err+2:]) == -1
                    ):
                    safe += 1
            print(report, safe)
        return safe