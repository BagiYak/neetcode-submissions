class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        
        # Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
        # reversed sorted = [(10, 2), (8, 4), (5, 1), (3, 3), (0, 1)]
        sortedCars = sorted(zip(position, speed), key=lambda car: car[0], reverse=True)

        # save only times to output, cause we loop cars from nearst to target

        # ex. 10:2 -> (12 - 10) / 2 = 1 hour
        # i = 0 -> check is there output -> false -> append(iTime) to output
        # output[1]

        # ex. 8:4 -> (12 - 8) / 4 = 1 hour
        # i = 1 -> compare top time output[-1] with i car time
        # 1 hour > 1 hour -> false -> don't append iTime to output
        # output[1]

        # ex. 5:1 -> (12 - 5) / 1 = 7 hour
        # i = 2 -> compare top time output[-1] with i car time
        # 7 hour > 1 hour -> true -> append(iTime) to output
        # output[1, 7]

        # i = 3 -> compare top time output[-1] with i car time
        # 3 hour > 7 hour -> false -> don't append iTime to output
        # output[1, 7]

        # i = 4 -> compare top time output[-1] with i car time
        # 12 hour > 1 hour -> true -> append(iTime) to output
        # output[1, 7, 3, 12]

        # return lenth of output times = 3

        output = []

        for i in range(len(sortedCars)):

            iCarTime = (target - sortedCars[i][0]) / sortedCars[i][1]
            if not output or iCarTime > output[-1]:
                output.append(iCarTime)

        return len(output)