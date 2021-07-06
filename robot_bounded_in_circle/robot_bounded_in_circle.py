class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        position = [0,0]
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        d = 0
        
        for i in instructions:
            if i == "G":
                position[0] += directions[d][0]
                position[1] += directions[d][1]
            elif i == "L":
                d = d - 1 if d > 0 else 3
            else:
                d = d + 1 if d < 3 else 0
            
        return position == [0, 0] or d != 0
