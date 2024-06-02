class Solution(object):
    def maxSatisfied(self, customers, grumpy, minutes):
        # Calculate the initial sum of satisfied customers
        total_satisfied = sum(customers[i] for i in range(len(customers)) if grumpy[i] == 0)

        # Calculate the sum of additional customers when using the secret technique
        max_additional_satisfied = 0
        additional_satisfied = 0
        left = 0

        for right in range(len(customers)):
            if grumpy[right] == 1:
                additional_satisfied += customers[right]  # Count unsatisfied customers
            # Adjust the window size to minutes
            if right - left + 1 > minutes:
                if grumpy[left] == 1:
                    additional_satisfied -= customers[left]  # Remove leaving customer
                left += 1

            max_additional_satisfied = max(max_additional_satisfied, additional_satisfied)

        return total_satisfied + max_additional_satisfied
