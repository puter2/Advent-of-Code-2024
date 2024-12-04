class Parser:

    def part1(self,s):
        tmp = ''
        res = 0
        for i in range(len(s)):
            if s[i] == 'm':
                tmp = s[i:i+12] #tmp = m***********
                if tmp[:4] != 'mul(':
                    continue
                #tmp = mul(********
                right_brace = tmp.find(')')
                if right_brace == -1:
                    continue
                tmp = tmp[:right_brace+1]   #tmp = mul( *** **** )
                #str.isdecimal()
                comma = tmp.find(',')
                if comma == -1:
                    continue
                if tmp[4:comma].isdecimal() and tmp[comma+1:-1].isdecimal():
                    val1 = int(tmp[4:comma])
                    val2 = int(tmp[comma+1:-1])
                    #print(val1,val2)
                    if 0<val1<1000 and 0<val2<1000:
                        res += val1 * val2
                #print(tmp)
        print(res)
        return res

    def part2(self,s):
        tmp = ''
        enabled = True
        res = 0
        for i in range(len(s)):
            if s[i] == 'd':
                if s[i:i+4] == 'do()':
                    enabled = True
                    #print('enabled')
                elif s[i:i+7] == "don't()":
                    #print('disabled')
                    enabled = False
                continue
            if s[i] == 'm' and enabled:
                tmp = s[i:i+12] #tmp = m***********
                if tmp[:4] != 'mul(':
                    continue
                #tmp = mul(********
                right_brace = tmp.find(')')
                if right_brace == -1:
                    continue
                tmp = tmp[:right_brace+1]   #tmp = mul( *** **** )
                #str.isdecimal()
                comma = tmp.find(',')
                if comma == -1:
                    continue
                if tmp[4:comma].isdecimal() and tmp[comma+1:-1].isdecimal():
                    val1 = int(tmp[4:comma])
                    val2 = int(tmp[comma+1:-1])
                    #print(val1,val2)
                    if 0<val1<1000 and 0<val2<1000:
                        res += val1 * val2
                #print(tmp,enabled)
        print(res)
        return res