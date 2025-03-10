n, k = map(int, input().split())

count = 0

nums = list(map(int, input().split()))

if len(nums) > n:
    nums = nums[:n]

for i in nums:

    if i >= nums[k - 1] and i > 0:
        count += 1

print(count)
