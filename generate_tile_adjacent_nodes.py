

upper_left = [(1, 2), (1, 4), (1, 6), (3, 1), (3, 3), (3, 5), (3, 7), (5, 0), (5, 2), (5, 4), (5, 6), (5, 8), (7, 1), (7, 3), (7, 5), (7, 7), (9, 2), (9, 4), (9, 6) ]

for x,y in upper_left:
    res = ""
    res += "node_" + str(x) + "_" + str(y) + ","
    res += "node_" + str(x - 1) + "_" + str(y + 1) + ","
    res += "node_" + str(x) + "_" + str(y + 2) + ","
    res += "node_" + str(x + 1) + "_" + str(y + 2) + ","
    res += "node_" + str(x + 2) + "_" + str(y + 1) + ","
    res += "node_" + str(x + 1) + "_" + str(y)
    print(res)


upper_left = [(1, 2), (1, 4), (1, 6), (3, 1), (3, 3), (3, 5), (3, 7), (5, 0), (5, 2), (5, 4), (5, 6), (5, 8), (7, 1), (7, 3), (7, 5), (7, 7), (9, 2), (9, 4), (9, 6) ]

for x,y in upper_left:
    res = ""
    res += "node_" + str(x) + "_" + str(y) + ","
    res += "node_" + str(x - 1) + "_" + str(y + 1) + ","
    res += "node_" + str(x) + "_" + str(y + 2) + ","
    res += "node_" + str(x + 1) + "_" + str(y + 2) + ","
    res += "node_" + str(x + 2) + "_" + str(y + 1) + ","
    res += "node_" + str(x + 1) + "_" + str(y)
    print(res)
