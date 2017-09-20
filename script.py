import xlrd
import webbrowser
import os
html_start = """
<table>
"""
html_row = "<tr>"
workbook = xlrd.open_workbook('data.xlsx',encoding_override='cp1252')
sheet = workbook.sheet_by_index(0)
html_file = open("report.html","w")
html_file.write(html_start)
for i in range(sheet.nrows):
	html_file.write("<tr>")
	for j in range(sheet.ncols):
		html_file.write("<td>")
		
		if sheet.cell(i,j).value == xlrd.empty_cell.value:
			html_file.write('<p> &#10005 </p>')
		else:
			html_file.write('<p> &#10004 </p>')
		html_file.write("</td>")
		
webbrowser.open(os.path.join(os.path.dirname(__file__), 'report.html'))


		
			


