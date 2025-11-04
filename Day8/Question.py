# 🧾 PYTHON DATATYPE QUESTIONS (LIST / STRING / TUPLE / SET / DICT)

# 🔹 LIST


# a = [1, 2, 3]
# b = a.copy()
# c = b
# b.append(4)
# print(a) # [1, 2, 3]
# print(b) # [1, 2, 3, 4]
# c.append(6)
# print(c) #[1, 2, 3, 4, 6]
# print(b) #[1, 2, 3, 4, 6]

# ⿢
# nums = [1, 2, 3] * 2
# print(nums)  #[1, 2, 3, 1, 2, 3]

# ⿣
# lst = [1, [2, 3], 4]
# print(lst[0])  # 1
# print(lst[1])  # [2, 3]
# print(lst[1][0]) # 2

# ⿤
# a = [10, 20, 30]
# print(a[0]) # 10
# print(a[-1]) # a[len(a) - 1] = a[3 - 1] = a[2]  ==> 30

# ⿥
# x = [1, 2, 3]
# print(x.pop(1)) # 2
# print(x)  # [1, 3]


# ---

# 🔹 STRING

# ⿡
# s = "python"
# print(s[1:-1])

# ⿢
# s = "HELLO"
# print(s.lower().capitalize())

# ⿣
# s = "abc" * 3
# print(s)

# ⿤
# s = "racecar"
# print(s == s[::-1])

# ⿥
# s = "hello world"
# print(s.replace("l", "L", 2))


# ---

# 🔹 TUPLE

# ⿡
# t = (1, 2, 3)
# t[0] = 10

# ⿢
# t = (1, 2, [3, 4])
# t[2][0] = 99
# print(t)

# ⿣
# t = (1,)
# print(type(t))

# ⿤
# t = (1, 2, 3) + (4, 5)
# print(t)

# ⿥
# t = (10, 20, 30)
# print(20 in t)


# ---

# 🔹 SET

# ⿡
# s = {1, 2, 2, 3}
# print(s)

# ⿢
# a = {1, 2, 3}
# b = {3, 4, 5}
# print(a & b)

# ⿣
# s = set("banana")
# print(s)

# ⿤
# s = {1, 2, 3}
# s.add((4, 5))
# print(s)

# ⿥
# s = {1, 2, 3}
# s.add([4, 5])


# ---

# 🔹 DICTIONARY

# ⿡
# d = {"a": 1, "b": 2}
# print(d.get("c", 5))

# ⿢
# d = {"x": 10, "y": 20}
# d["x"] += 5
# print(d)

# ⿣
# d = {1: "one", True: "truth", 1.0: "float"}
# print(d)

# ⿤
# d = {"a": 1, "b": 2}
# for k in d:
# print(k)

# ⿥
# d = {"a": [1, 2], "b": [3, 4]}
# print(d["a"][1])