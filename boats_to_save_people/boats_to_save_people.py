class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i = 0
        j = len(people) - 1
        boats = len(people)
        while i < j:
            if people[i] + people[j] <= limit:
                boats -= 1
                i += 1
            j -= 1
        return boats
