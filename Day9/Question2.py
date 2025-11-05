
# 🔹 STRING

# ⿡
# s = "python"
# print(s[-1]) # n
# print(s[1:3]) # yt
# print(len(s)) # 6
# print(s[1:-1]) # s[1: len(s) - 1] => s[1:5] => ytho
# print(s[2:-3]) # s[2: len(s) - 3] => s[2:6-3] => s[2:3] => t

# s = "Business"
# print(s[5]) # e
# print(s[-4]) # n
# print(s[1:5]) # usin
# print(s[1:-2]) # usine
# print(s[:])
# print(s[ : : 2])
# print(s[::-1]) #ssenisuB


# ⿢
# s = "HELLO"
# # print(s.lower()) #hello
# # print(s.capitalize()) #Hello
# print(s.lower().capitalize()) #Hello

# f = "studio"
# print(f.upper()) #STUDIO
# print(f.capitalize()) #Studio

# ⿣
# s = "abc" * 3
# print(s) # abcabcabc

# ==
# ⿤
# s = "racecar"
# print(s[::-1]) #racecar
# print(s == s[::-1]) #True

# ⿥
# s = "hello world"
# print(s.replace("l", "L", 2)) # heLLo world


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