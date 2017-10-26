#! python3

"""
Table Printer
Prints a list as table.

"""


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


columnWidths = [0]*len(tableData[1])
print(columnWidths)

for rownum in range(len(tableData)) :
    for colnum in range(len(columnWidths)) :
        if int(columnWidths[colnum]) < len(tableData[rownum][colnum]):
            columnWidths[colnum]=len(tableData[rownum][colnum])


for rownum in range(len(tableData)) :
    for colnum in range(len(columnWidths)) :
        print((tableData[rownum][colnum]).ljust(columnWidths[colnum],"-")+" ", end="")

    print('\n')
