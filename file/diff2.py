
def getFileLines(file_path):
    with open(file_path) as file_handle:
        file_line_list = file_handle.readlines()
        print("[INFO] LOC:{} PATH:{}".format(len(file_line_list), file_path))
        return file_line_list


def diffLists(file1_list, file2_list, precision_range=1e-5):

    if len(file1_list) < len(file2_list):
        short_len = len(file1_list)
    else:
        short_len = len(file2_list)

    diff_num = 0
    sum_num = short_len

    for idx in xrange(short_len):

        try:
            line1 = float(file1_list[idx].strip())
            line2 = float(file2_list[idx].strip())
        except:
            line1 = file1_list[idx].strip()
            line2 = file2_list[idx].strip()

        if type(line1) == str and type(line2) == str:
            if line1 != line2:
                diff_num += 1
                print("idx:{} diff_num:{} line1:{} line2:{}".format(idx, diff_num, line1, line2))
        if type(line1) == float and type(line2) == float:
            if abs(line1-line2)>precision_range:
                diff_num += 1
                print("idx:{} diff_num:{} line1:{} line2:{}".format(idx, diff_num, line1, line2))

    diff_rate = float(diff_num)/sum_num

    print("[INFO] precision_range:{}".format(precision_range))
    print("[INFO] diff_num:{}".format(diff_num))
    print("[INFO] sum_num:{}".format(sum_num))
    print("[INFO] diff_rate:{}".format(diff_rate))

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("usage: python {} FILE1 FILE2".format(sys.argv[0]))
        exit(-1)

    file1_path = sys.argv[1]
    file2_path = sys.argv[2]
    precision_range = 1e-1

    file1_line_list = getFileLines(file1_path)
    file2_line_list = getFileLines(file2_path)

    diffLists(file1_line_list, file2_line_list, precision_range)
