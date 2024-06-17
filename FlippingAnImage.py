class Solution(object):
    def flipAndInvertImage(self, image):
        if not image:
            return
        for row in image:
            # Reverse each row in place using list slicing
            row[:] = row[::-1]
            # Invert each pixel using bitwise XOR operation
            for i in range(len(row)):
                row[i] ^= 1
        return image