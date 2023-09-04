# get hexa number in a list
hex_num = "fc:94:b0:c1:e5:b0:98:7c:58:43:99:76:97:ee:9f:b7"
list_hex_num = hex_num.split(":")
list_binary_num = []
dic_move = {"00": [-1, -1], "01": [-1, 1], "10": [1, -1], "11": [1, 1]}
start_position = (4, 8)
symbol_dic = {0: ".", 1: "o", 2: "+", 3: "=", 4: "*", 5: "B", 6: "O", 7: "X", 8: "@", 9: "%", 10: "&", 11: "#", 12: "/", 13: "^", 14: "|"}

# get a list of pair bin number
for i in list_hex_num:
    binary_num = bin(int(i, 16))[2:].zfill(8)
    for j in range(len(binary_num) - 2, -1, -2):
        binary_num_pair = binary_num[j:j+2]
        list_binary_num.append(binary_num_pair)


# create chessboard
rows = 9
cols = 17
chessboard = [[" " for _ in range(cols)] for _ in range(rows)]

# create a dict with the number of steps passed in each cases of the chessboard
count_move = {}
position = start_position
for bin_pair in list_binary_num:
    if (bin_pair == "00" and position == (0, 0)) or (bin_pair == "01" and position == (8, 0)) or (bin_pair == "10" and position == (0, 16)) or (bin_pair == "11" and position == (8, 16)):
        position = position
    elif bin_pair == "00" and position[1] == 0:
        position = (position[0] + dic_move[bin_pair][0], 0)
    elif bin_pair == "00" and position[0] == 0:
        position = (0, position[1] + dic_move[bin_pair][1])
    elif bin_pair == "01" and position[1] == 16:
        position = (position[0] + dic_move[bin_pair][0], 16)
    elif bin_pair == "01" and position[0] == 0:
        position = (0, position[1] + dic_move[bin_pair][1])

    elif bin_pair == "10" and position[1] == 0:
        position = (position[0] + dic_move[bin_pair][0], 0)
    elif bin_pair == "10" and position[0] == 8:
        position = (8, position[1] + dic_move[bin_pair][1])
    elif bin_pair == "11" and position[0] == 8:
        position = (8, position[1] + dic_move[bin_pair][1])
    elif bin_pair == "11" and position[1] == 16:
        position = (position[0] + dic_move[bin_pair][0], 16)

    else:
        position = (position[0] + dic_move[bin_pair][0], position[1] + dic_move[bin_pair][1])
    if position in count_move:
        if count_move[position] == 14:
            count_move[position] = 0
        else:
            count_move[position] += 1
    else:
        count_move[position] = 1

# draw the chessboard
chessboard_row = len(chessboard)
chessboard_col = len(chessboard[0])

for i in range(chessboard_row):
    for j in range(chessboard_col):
        if (i, j) in count_move:
            chessboard[i][j] = symbol_dic[count_move[(i, j)] - 1]
        else:
            pass


chessboard[start_position[0]][start_position[1]] = "S"
chessboard[position[0]][position[1]] = "E"


# shaping the final chess board
chessboard.insert(16, ["+","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","+"])
chessboard.insert(0, ["+","-","-","-","[","C","O","D","I","N","G","A","M","E","]","-","-","-","+"])
for i in range(1, chessboard_row + 1):
    chessboard[i].insert(0, "|")
    chessboard[i].insert(chessboard_col + 1, "|")

for row in chessboard:
    print("".join(row))