# SLIDING WINDOW!!
# When the right index finds an element outside of the window,
# move the left index up until the right element can be included!!

def longestOnes(nums, k):
    longest = 0
    left_index = 0
    zeroes = 0
    for right_index in range(len(nums)):
        if nums[right_index] == 0:
            if zeroes == k:
                while nums[left_index] != 0:
                    left_index += 1
                left_index += 1
            else:
                zeroes += 1
        longest = max(longest, right_index - left_index + 1)

    return longest

print("3:", longestOnes([0,1,1,0], 1))
print("7:", longestOnes([0,0,0,0,1,1,0,1,1,0], 3))
