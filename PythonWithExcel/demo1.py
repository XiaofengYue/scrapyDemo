import xlsxwriter


workbook = xlsxwriter.Workbook('Example01.xlsx')
worksheet = workbook.add_worksheet()


Titles = input('请输入首行内容，空格隔开\n').split(' ')
list_edges = []


def writeDataWith_BadSituation():
    # order
    worksheet.write(0, 0, '序号')
    row = 0
    col = 1
    allNums = 1
    repeat = 1
    # WriteTitles
    for title in Titles:
        worksheet.write(row, col, title)
        col += 1
        edges = input('请输入' + title + '边界' + '(空格隔开)\n').split(' ')
        allNums *= len(edges)
        list_edges.append(edges)
    # write order
    for i in range(allNums):
        worksheet.write(1 + i, 0, 1 + i)
    worksheet.write(row, col, '期望')
    row = 1
    col = 1

    for i in range(len(Titles)):
        # 除以一个数后的总数量
        row = 1
        allNums //= len(list_edges[i])
        # 遍历这个数的边界
        for _ in range(repeat):
            for j in range(len(list_edges[i])):
                for k in range(allNums):
                    worksheet.write(row, col + i, list_edges[i][j])
                    row += 1
        repeat *= len(list_edges[i])


writeDataWith_BadSituation()

workbook.close()
