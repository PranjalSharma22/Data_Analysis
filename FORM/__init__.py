from flask import Flask,render_template,request
import pandas as pd
from pathlib import Path
app = Flask(__name__)
import xlsxwriter
@app.route('/',methods=['GET','POST'])
def homepage():	
	
	if request.method =='POST':
		config = Path('./pandas_simple13.xlsx') 
		if config.is_file(): 
			add()
		else:	
			# Create an new Excel file and add a worksheet.
			workbook = xlsxwriter.Workbook('pandas_simple13.xlsx')
			workbook.close()
			add()

	return render_template("index.html")
def add():
	first_name=request.form['first_name']
	last_name=request.form['last_name']
	print ("hello")	
	data = [{'First Name': first_name, 'Last Name': last_name}]
	df1=pd.DataFrame(data,columns=['First Name','Last Name'])	
	ex=pd.read_excel('pandas_simple13.xlsx')
	ex=ex.append(df1)
	ex.index = range(1,len(ex)+1)
	ex.to_excel('pandas_simple13.xlsx')


if __name__ == "__main__":
    app.run(debug=True)
