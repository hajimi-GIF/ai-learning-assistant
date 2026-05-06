# Example: Using AI to solve a simple problem

def two_sum(nums, target):
    hashmap = {}
    for i, num in enumerate(nums):
        if target - num in hashmap:
            return [hashmap[target - num], i]
        hashmap[num] = i

# Simulated AI-assisted result
if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print("Result:", two_sum(nums, target))
