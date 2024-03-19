class Solution(object):
    def sortByBits(self, arr):
        bit_count_map = {}

        for num in arr:
            bit_count = bin(num).count('1')
            if bit_count in bit_count_map:
                bit_count_map[bit_count].append(num)
            else:
                bit_count_map[bit_count] = [num]

        result = []

        for bit_count, nums in sorted(bit_count_map.items()):
            result.extend(sorted(nums))

        return result

    '''
        dror1 = list(arr)
        dror1.sort(key=lambda x: (bin(x).count('1'), x))
        return dror1
    '''