class Solution(object):
    def averageWaitingTime(self, customers):
        prev = 0
        total = 0
        for c in customers:
            arrival = c[0]
            prep = c[1]
            if prev > arrival:
                total += prev - arrival
                prev += prep
            else:
                prev = arrival + prep
            total += prep

        return float(total) / len(customers)