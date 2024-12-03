class Reader:

    def read(self,filepath):
        '''
        read data from file
        '''
        data = []
        with open(filepath) as file:
            for line in file.readlines():
                tmp = []
                for val in line.split():
                    tmp.append(int(val))
                data.append(tmp)
        return data