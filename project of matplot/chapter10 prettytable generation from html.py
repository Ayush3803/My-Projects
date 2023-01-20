from prettytable import from_html_one
with open("table.html","r")as fp:
    html=fp.read()
x=from_html_one(html)
print(x)
