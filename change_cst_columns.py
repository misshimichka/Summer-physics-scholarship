import os


files = [i[2] for i in os.walk("data")][0]
for i in range(11):
    input_file = open("data/" + files[i]).readlines()
    s = [i.rstrip("\n") for i in input_file][2:]

    for j in range(len(s)):
        while s[j].count(" ") > 1:
            x = s[j].find(" ")
            s[j] = s[j][:x] + s[j][x + 1:]
        s[j] = s[j].replace(" ", "\t")

    f = open("data/" + files[i], "wt")
    for j in s:
        f.write(j)
        f.write("\n")
    f.close()
