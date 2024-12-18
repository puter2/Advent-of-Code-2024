class Solver:

    def isValid(self, order : dict, sample : list):
        processed = [sample[0]]
        for page in sample[1:]:
            if order.get(page):
                for rule in order.get(page):
                    if rule in processed:
                        return False
            processed.append(page)
        return True

    def getMiddle(self, sample):
        return int(sample[len(sample) // 2])