
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
# t[0] = 10 #TypeError: 'tuple' object does not support item assignment

# ⿢
# t = (1, 2, [3, 4])
# t[2][0] = 99
# print(t) #(1, 2, [99, 4])

# ⿣
# t = (1,)
# print(type(t)) # <class 'tuple'>

# ⿤
# t = (1, 2, 3) + (4, 5)
# print(t) #(1, 2, 3, 4, 5)

# ⿥
# t = (10, 20, 30)
# print(20 in t) #True


# ---

# 🔹 SET

# ⿡
# s = {1, 2, 2, 3}
# print(s) #{1, 2, 3}

# ⿢
# a = {1, 2, 3}
# b = {3, 4, 5}
# print(a & b) # common/ intercept {3}
# print(a | b)  # union {1, 2, 3, 4, 5}

# ⿣
# s = set("banana")
# print(s) #{'a', 'n', 'b'}

# ⿤
# s = {1, 2, 3}
# s.add((4, 5))
# print(s) #{(4, 5), 1, 2, 3}

# ⿥
# s = {1, 2, 3}
# s.add([4, 5])
# print(s)


# ---

# 🔹 DICTIONARY
'''
dictionary.get(key, default_value)
It tries to find the value for the given key.

If the key exists, it returns its value.

If the key does NOT exist, it returns the default_value (if provided), else returns None.
'''


# ⿡
# d = {"a": 1, "b": 2}
# print(d.get("c")) #None
# print(d.get("c", "default value")) #default value

# print(d.get("c", 5)) #5

# ⿢
# d = {"x": 10, "y": 20}
# d["x"] += 5
# print(d) #{'x': 15, 'y': 20}

# ⿣
# d = {1: "one", True: "truth", 1.0: "hghgjg"}
# f = {1:"one"}
# print(f[1.0])
# print(d)

# ⿤
# d = {"a": 1, "b": 2}
# for k in d:
#     print(k)
# output: 
# a
# b

# ⿥
# d = {"a": [1, 2], "b": [3, 4]}
# print(d["a"][1]) #2