# Floyd's Cycle Detection Algorithm: Calculates the squares of digits once and twice and if they meet it's a cycle

class Solution(object):
    def isHappy(self, n):
        slow = n
        fast = n
        while True:
            slow = self.square_sum_of_digits(slow)  # Move slow pointer once
            fast = self.square_sum_of_digits(self.square_sum_of_digits(fast))  # Move fast pointer twice
            if slow == 1 or fast == 1:
                return True  # If either pointer reaches 1, the number is happy
            if slow == fast:
                return False  # If pointers meet, there's a cycle and the number is not happy

    def square_sum_of_digits(self, n):
        square_sum = 0
        while n > 0:
            digit = n % 10
            square_sum += digit ** 2
            n //= 10
        return square_sum