class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = list(zip(position, speed))  # O(n)
        cars.sort(reverse=True)            # O(n log n)

        carFleets = []
        for pos, speed in cars:
            time = (target - pos) / speed
            if not carFleets or time > carFleets[-1]:
                carFleets.append(time)

        return len(carFleets)

# ChatGPT: The key idea is: when a car catches the fleet ahead, don't replace/remove the fleet's time. The fleet continues at the slower car's time.

# Idea-2 using sort and stack - is not correct cause got logic errors
# We need to consider that faster car can get slower and then it has to go same speed as slower car!

# Algorithm:
# stack = []
# sorted tuple array of cars by position: sorted[{0:1}, {3:3}, {5:1}, {8:4}, {10:2}]
# loop sorted cars:
#   - check stack:
#       -- get top car time and sorted car time
#       -- compare topTime <= sortTime:
#           if true -> pop from stack
#   - append sorted car to stack
# return length of stack

# Input: target=12, position=[10,8,0,5,3], speed=[2,4,1,1,3]

# 1 -> sortedStack[{0:1}, {3:3}, {5:1}, {8:4}, {10:2}]
# 2 -> loop sorted:
#   if stack is not empty - compare times of top vs sorted[i]
#   else - put to stack
# 3 -> return len of stack

# cars = list(zip(position, speed))  # O(n)
# cars.sort()                        # O(n log n)

# carFleets = []
# for tup in cars:
#     if carFleets:
#         top = carFleets[-1]
#         topTime = (target - top[0]) / top[1]
#         sortTime = (target - tup[0]) / tup[1]
#         if topTime <= sortTime:
#             carFleets.pop()
#     carFleets.append(tup)

# return len(carFleets)
# -------------------------------------------------

# Idea-1 using dict -> is not correct cause I did not consider
# that faster car can get slower and then it has to go same speed as slower car!

# 1 - need to find each car's time to get to target
# formula: (target - position) / speed = time
# 2 - need to count car fleets
# check time is in stack if yes, increase it by 1
# and the len of stack would be count of car fleets
# -------------------------------------------------

# Error case:
# Input: target=12, position=[10,8,0,5,3], speed=[2,4,1,1,3]

# car[0] = 12 - 10 = 2 / 2 = 1
# car[1] = 12 - 8 = 4 / 4 = 1
# car[2] = 12 - 0 = 12 / 1 = 12
# car[3] = 12 - 5 = 7 / 1 = 7
# car[4] = 12 - 3 = 9 / 3 = 3
# My output: 4, but expected: 3

# Success cases:
# Input: target = 10, position = [1,4], speed = [3,2]

# car[0]: 1 miles
#   leftToTarget -> target - position: 10 - 1 = 9 miles
#   time -> target / speed: 3 -> 9 / 3 = 3 hours
# car[1]: 4 miles
#   leftToTarget -> target - position: 10 - 4 = 6 miles
#   time -> target / speed: 2 -> 6 / 2 = 3 hours

# car[0] and car[1] -> 1 car fleet

# result car fleets: 1
# --------------------

# Input: target = 10, position = [4,1,0,7], speed = [2,2,1,1]

# car[0]: 4 miles
#   leftToTarget -> target - position: 10 - 4 = 6 miles
#   time -> target / speed: 2 -> 6 / 2 = 3 hours
# car[1]: 1 miles
#   leftToTarget -> target - position: 10 - 1 = 9 miles
#   time -> target / speed: 2 -> 9 / 2 = 4.5 hours
# car[2]: 0 miles
#   leftToTarget -> target - position: 10 - 0 = 10 miles
#   time -> target / speed: 1 -> 10 / 1 = 10 hours
# car[3]: 7 miles
#   leftToTarget -> target - position: 10 - 7 = 3 miles
#   time -> target / speed: 1 -> 3 / 1 = 3 hours

# car[0] and car[3] -> 1 car fleet
# car[1] -> 1 car fleet
# car[2] -> 1 car fleet

# result car fleets: 1 + 1 + 1 = 3
