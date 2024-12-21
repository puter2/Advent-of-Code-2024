from record import Record

class Solver:

    def solve(self, data : list[Record]):
        pos = len(data) - 1
        while pos > 0:
            cur = data[pos]
            if cur.val != '.':
                if target := self.can_be_swapped(data, pos):
                    self.swap(data, pos, target)
                    data = self.merge_spaces(data)
                    # print(target)
                    # print(self.encode(data))
            pos -= 1
        return data
                    

    def merge_spaces(self, data : list[Record]):
        res = []
        i = 0
        while i < len(data):
            if data[i].val == '.':
                res.append(Record(data[i].amount, '.'))
                i += 1
                while i < len(data) and data[i].val == '.':
                    res[-1].amount += data[i].amount
                    i += 1
            else:
                res.append(data[i])
                i+=1
        return res

    def encode(self, data):
        res = ''
        for record in data:
            res += str(record.val) * record.amount
        return res


    def swap(self, data : list[Record], index, target_index):
        # print(data[index].val, data[index].amount, index)
        if data[index].amount == data[target_index].amount:
            tmp = data[index].val
            # print(tmp)
            data[index].val = '.'
            data[target_index].val = tmp
        else:
            put = data[index].copy()
            data[target_index].amount -= put.amount
            data.insert(target_index, put)
            data[index+1].val = '.'
        # print(self.encode(data))
        

    def can_be_swapped(self, data : list[Record], index):
        to_swap = data[index]
        for i in range(index):
            cur = data[i]
            if cur.val == '.' and cur.amount >= to_swap.amount:
                return i
        return 0

    def checksum(self, data : list[Record]):
        i = 0
        res = 0
        for record in data:
            if record.val != '.':
                for _ in range(record.amount):
                    res += i * record.val
                    i += 1
            else:
                i += record.amount
        return res