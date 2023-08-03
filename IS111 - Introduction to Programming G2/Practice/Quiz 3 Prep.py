# Q1
# def extract(chars, parity):
#     string = ""
#     n = len(chars)
#     for i in range(n):
#         if i % 2 == parity:
#             string += chars[i]
#     return string
# chars = ['p', 'c', 'y', 'o', 't', 'b', 'h', 'r', 'o', 'a', 'n']
# print(extract(chars, 0))
# print(extract(chars, 1))
# Output: Python, Cobra


# Q2
# def get_max(a,b):
#     new_list = []
#     n = 1         len(a)
#     for i in range(n):
#         num = max(2,3)
#         new_list.4
#     return new_list
# num1 = [3,5,6]
# num2 = [7,2,5]
# num3 = get_max(num1,num2)
# print(num3)
# Output: [7, 6, 5]
# Answer: len(a), a[i], b[i], append(num)

# Q3
# def modify(nums):
#     new_nums = nums
#     for i in range(len(new_nums)):
#         new_nums[i] += 1
#     return new_nums
# nums1 = [3,6,5]
# nums2 = modify(nums1)
# print(nums1)
# print(nums2)
# Output: 
# Line1: [4, 7, 6]
# Line2: [4, 7, 6]


# Q4
# def count_scores(scores, threshold):
#     count = 0
#     for score in scores:
#         if score > threshold:
#             count += 1
#     return count

# scores = [80, 45, 70, 55]
# print(count_scores(scores, 50))
# print(count_scores(scores, 90))
# Output: 
# Line1: 3
# Line2: 0