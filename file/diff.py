#!/usr/bin/python

def readLineFrom(file_path):
    with open(file_path, "r") as file_handle:
        line = file_handle.readline()
        while line:
            yield line
            line = file_handle.readline()
    yield None


def getLineNum(file_path):
    import os
    cmd = "wc -l ".format(file_path)
    os.system(cmd)
    #return_code, cmd_output = commands.getstatusoutput(cmd)
    #print(cmd_output)

def diff(line1, line2, line_idx, diff_num, precision_range=1e-5):
    if type(line1) == str:
        if line1 != line2:
            print("{} diff:line1:{}line2:{}".format(line_idx, line1, line2))
            diff_num += 1
    elif type(line1) == float:
        if abs(line1-line2) > precision_range:
            print("{} diff:line1:{}line2:{}".format(line_idx, line1, line2))
            diff_num += 1
    else:
        pass
        #print("{}".format(line_idx))
    return diff_num
        

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("usage: python {} FILE1_PATH FILE2_PATH\n".format(sys.argv[0]))
        exit(-1)

    # init
    file1_path = sys.argv[1]
    file2_path = sys.argv[2]

    #file1_line_num = getLineNum(file1_path)
    #file2_line_num = getLineNum(file2_path)
    precision_range = 1e-5

    # read
    reader1 = readLineFrom(file1_path)
    reader2 = readLineFrom(file2_path)

    line1 = reader1.next()
    line2 = reader2.next()

    line_idx = 1
    diff_num = 0

    while True:
        diff_num = diff(line1, line2, line_idx, diff_num, precision_range)

        line1 = reader1.next()
        line2 = reader2.next()
        line_idx += 1

        if line1 == None or line2 == None:
           break 

    print("line1:{}".format(line1))
    print("line2:{}".format(line2))
    print("diff_num:{}".format(diff_num))
    print("all_point:{}".format(line_idx+1))
    print("diff_rate:{}".format(float(diff_num)/(line_idx)))
