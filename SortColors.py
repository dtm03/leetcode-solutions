class Solution(object):
    def sortColors(self, nums):
        def quicksort(arr, low, high):
            if low < high:
                # Partition the array and get the pivot index
                pi = partition(arr, low, high)

                # Recursively sort the elements before and after partition
                quicksort(arr, low, pi - 1)
                quicksort(arr, pi + 1, high)

        def median_of_three(arr, low, high):
            mid = (low + high) // 2
            if arr[low] > arr[mid]:
                arr[low], arr[mid] = arr[mid], arr[low]
            if arr[low] > arr[high]:
                arr[low], arr[high] = arr[high], arr[low]
            if arr[mid] > arr[high]:
                arr[mid], arr[high] = arr[high], arr[mid]
            return mid

        def partition(arr, low, high):
            mid = median_of_three(arr, low, high)
            # Use the median of three as the pivot
            arr[mid], arr[high] = arr[high], arr[mid]
            pivot = arr[high]
            i = low - 1

            for j in range(low, high):
                if arr[j] <= pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]

            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            return i + 1

        return quicksort(nums, 0, len(nums) - 1)


# Another solution using the Dutch National Flag algorithm
        class Solution(object):
            def sortColors(self, nums):
                low, mid, high = 0, 0, len(nums) - 1

                while mid <= high:
                    if nums[mid] == 0:
                        nums[low], nums[mid] = nums[mid], nums[low]
                        low += 1
                        mid += 1
                    elif nums[mid] == 1:
                        mid += 1
                    else:  # nums[mid] == 2
                        nums[high], nums[mid] = nums[mid], nums[high]
                        high -= 1