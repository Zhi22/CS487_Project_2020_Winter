import random as rd
import math
import sys

def convert(unique):
    tmp = []
    result = []
    for _ in range(7):
        tmp.append('A')
        result.append('A')
    i = 6
    cnt = 0
    j = 0
    while(unique > 0):
        rem = unique % 26
        tmp[i] = chr(65 + rem)
        unique = math.floor(unique / 26)
        i -= 1
        cnt += 1

    while(j <= cnt):
        result[j] = tmp[i]
        j += 1
        i += 1
    return ''.join(result)

def generate_relation(MAXTUPLE):
    tuples = []
    tuples.append('{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}\n'.format(
        'unique1','unique2','two','four','ten','twenty',
        'onePercent','tenPercent','twentyPercent','fifty_Percent','unique3',
        'evenOnePercent','oddOnePercent','stringu1','stringu2','string4'))

    following_char = ""
    for _ in range(45):
        following_char += "x"
    unique = rd.sample(range(MAXTUPLE), MAXTUPLE)
    for row in range(MAXTUPLE):
        unique1 = unique[row]
        unique2 = row
        two = unique1 % 2
        four = unique1 % 4
        ten = unique1 % 10
        twenty = unique1 % 20
        onePercent = unique1 % 100
        tenPercent = unique1 % 10
        twentyPercent = unique1 % 5
        fifty_Percent = unique1 % 2
        unique3 = unique1
        evenOnePercent = onePercent * 2
        oddOnePercent = onePercent * 2 + 1
        stringu1 = convert(unique1) + following_char
        stringu2 = convert(unique2) + following_char
        string4 = ''.join([chr(65 + (row % 4 * 7))] * 4) + following_char +"xxx"

        tuples.append('{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}\n'.format(
        unique1,unique2,two,four,ten,twenty,
        onePercent,tenPercent,twentyPercent,fifty_Percent,unique3,
        evenOnePercent,oddOnePercent,stringu1,stringu2,string4)
        )
    return tuples

def write_out_csv(tuples):
    with open("output.csv", 'w') as file:
        for row in tuples:
            file.write(row)

def main(cmd_args):
    if len(cmd_args) > 1:
        MAXTUPLE = int(cmd_args[1])
        tuples = generate_relation(MAXTUPLE)
        write_out_csv(tuples)
    else:
        return

if __name__== "__main__":
    main(sys.argv)