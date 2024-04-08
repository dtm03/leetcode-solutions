# Floyd-Algorithm
# Wenn Cycle existiert treffen sich slow und fast pointer
# Die Strecke vom Treffpunkt zum Cycleanfang ist gleich lang wie vom Anfang zum Cycleanfang
# p + c + c - x = p + c - x + p => p = x || p = vor dem Cycle, x = Abstand zum Cycleanfang, # C is Cycle-Länge

class Solution(object):
    def findDuplicate(self, nums):
        slow, fast = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow