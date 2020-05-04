from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)
print(__name__)



@app.route('/')
def mu_home():
	return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
	return render_template(page_name)




# Writing into a txt database
def write_to_file(data):
	with open('database.txt', mode='a') as database:
		email = data['email']
		subject= data['subject']
		message = data['message']

		file = database.write(f'\n{email} | {subject} | {message}')



# Writing into a csv database
def write_to_csv(data):
	with open('database.csv', mode='a', newline='') as database2:
		email = data['email']
		subject= data['subject']
		message = data['message']
		csv_writer = csv.writer(database2, delimiter='|', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([email, subject, message])


	
		


@app.route('/submit', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])	
def submit():
	if request.method == 'POST':  
		data = request.form.to_dict()
		
		#write_to_file(data)....for database.txt
		write_to_csv(data)    #...for database.csv

		return redirect('/thankyou.html')
	else:  
		return 'Oops! something went wrong!'