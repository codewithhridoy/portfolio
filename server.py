from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def dynamic_page(page_name):
    return render_template(page_name)



def write_to_csv(data):
    with open('database.csv', mode='a') as database:
        name = data['name']
        email = data['email']
        message = data['message']

        csv_writer = csv.writer(database, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name,email,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return 'Something Went Wrong! Try Again!!'


    # return render_template('login.html', error=error)


if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)