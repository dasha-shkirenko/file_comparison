import sys
from itertools import zip_longest as izip_longest
import xlrd

# 676

def compare_reports(f1, f2):
    file1 = xlrd.open_workbook(f1)
    file2 = xlrd.open_workbook(f2)

    sheet1 = file1.sheet_by_index(0)
    sheet2 = file2.sheet_by_index(0)

    for rownum in range(min(sheet1.nrows, sheet2.nrows)):
        if rownum < sheet1.nrows:
            row_rb1 = sheet1.row_values(rownum)
            row_rb2 = sheet2.row_values(rownum)

            for colnum, (c1, c2) in enumerate(izip_longest(row_rb1, row_rb2)):
                if c1 != c2:
                    print(
                        "Row: {} Col: '{}' : \n {}: {} \n {}: {} \n".format(
                            rownum + 1,
                            sheet1.cell_value(0, colnum),
                            f1,
                            c1,
                            f2,
                            c2,
                        )
                    )
                    if sheet1.nrows != sheet2.nrows:
                        print('From row #{} reports start differentiating.'.format(sheet1.nrows))
                        return
        else:
            print("Row {} missing".format(rownum + 1))


if __name__ == '__main__':
    _, f1, f2 = sys.argv
    compare_reports(f1, f2)