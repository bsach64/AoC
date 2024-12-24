text = [line.strip().split(':') for line in open("7.txt").readlines()]
text = [
            [
                int(line[0]), [int(x) for x in line[1].split(' ') if x.strip()]
            ] for line in text
       ]


def dfs(target, nums):
    if len(nums) == 1:
        if nums[0] == target:
            return True
        return False

    x, y = nums[0], nums[1]
    concat = int(str(x) + str(y))
    return dfs(target, [x * y] + nums[2:]) or dfs(target, [x + y] + nums[2:]) or dfs(target, [concat] + nums[2:])


res = 0

for line in text:
    if dfs(line[0], line[1]):
        res += line[0]

print(res)
