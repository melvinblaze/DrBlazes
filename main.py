from flask import Flask, render_template, request
import csv
app = Flask(__name__)

@app.route("/")
def my_home():
    return render_template("index.html")

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)


def write_file(data):
    with open('database.txt', mode='a') as database:
        date = data['date']
        name = data['name']
        email = data['email']
        subject = data['subject']
        message = data['message']
        file =database.write(f' \n {date},{name}, {email}, {subject}, \"{message}\"')

def write_csv(data):
    with open('database.csv', mode='a',newline='') as database2:
        date = data['date']
        name = data['name']
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2,delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([date,name, email,subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_file(data)
        write_csv(data)
        return render_template('/thankyou.html')
    else:
        return 'Some thing went wrong try again later'