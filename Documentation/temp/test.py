from openpyxl import load_workbook

#load excel file
workbook = load_workbook('499a.xlsx')

#open workbook
sheet = workbook.active

#modify the desired cell
print(sheet["A1"].value)

