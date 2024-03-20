from CanPlaceFlower import Solution as CanPlaceFlower

def main():

    # Create an instance of the Solution class from CanPlaceFlower module
    solution_instance = CanPlaceFlower()

    # Call the canPlaceFlowers method on the instance
    result = solution_instance.canPlaceFlowers([1, 0, 0, 0, 1], 1)
    print(result)

    # print(CanPlaceFlower().canPlaceFlowers([1, 0, 0, 0, 1], 1))

if __name__ == "__main__":
    main()