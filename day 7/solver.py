class Solver:

    def solve(self,data):
        res = 0
        for row in data:
            if self.solveRow(row=row):
                print(row)
                res += int(row[0][0:-1])
        return res

    def solveRow(self,row):
        target = int(row[0][0:-1])
        nums = [int(el) for el in row[1:]]
        configuration = ['*'] * (len(nums) - 1)
        end = ['+'] * (len(nums) - 1)
        while configuration != end:
            #print(configuration)
            if self.testNoOrder(target, nums, configuration):
                return True
            else:
                self.nextConfig(configuration)
        return self.testNoOrder(target,nums,configuration)

    def nextConfig(self, configuration):
        for i in range(len(configuration)):
            if configuration[i] == '*':
                configuration[i] = '+'
                for j in range(i):
                    configuration[j] = '*'
                return


    def test(self, target, nums, configuration):
        i = 0
        tmp = nums.copy()
        tmp_conf = configuration.copy()
        stop = len(configuration)
        while i<stop:
            #print(i,stop)
            if tmp_conf[i] == '*':
                tmp_conf.pop(i)
                tmp[i] = tmp[i] * tmp[i + 1]
                tmp.pop(i+1)
                stop -= 1
            else:
                i += 1
        #     print(tmp)
        # print(sum(tmp))
        return target == sum(tmp)
                
    def testNoOrder(self, target, nums, configuration):
        res = nums[0]
        for i in range(len(configuration)):
            if configuration[i] == '*':
                res *= nums[i + 1]
            else:
                res += nums[i + 1]
        # print(nums, target, res, configuration)
        return target == res