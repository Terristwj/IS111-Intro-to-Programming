def evaluate(expression):
    # modify the code below
    copied_str = expression
    copied_str = copied_str.replace("+", ";")
    copied_str = copied_str.replace("-", ";")
    copied_str = copied_str.replace("*", ";")
    copied_str = copied_str.replace("/", ";")

    nums_str = copied_str.split(";")
    nums = []
    for num in nums_str:
        nums.append(float(num))
    optrs = []

    valid_optrs = "+-/*"
    for ch in expression:
        if ch in valid_optrs:
            optrs.append(ch)

    # To debug
    # print(nums, optrs)

    while len(nums) != 1:
        if "*" in optrs or "/" in optrs:
            for i in range(len(optrs)):
                if optrs[i] == "*" or optrs[i] == "/":
                    if optrs[i] == "*":
                        calculate =  nums[i] * nums[i+1]
                    if optrs[i] == "/":
                        calculate =  nums[i] / nums[i+1]

                    nums.insert(i, calculate)
                    nums.remove(nums[i+1])
                    nums.remove(nums[i+1])
                    optrs.remove(optrs[i])
                    break
        else:
            for i in range(len(optrs)):
                if optrs[i] == "+" or optrs[i] == "-":
                    if optrs[i] == "+":
                        calculate =  nums[i] + nums[i+1]
                    if optrs[i] == "-":
                        calculate =  nums[i] - nums[i+1]

                    nums.insert(i, calculate)
                    nums.remove(nums[i+1])
                    nums.remove(nums[i+1])
                    optrs.remove(optrs[i])
                    break

    return nums[0]
