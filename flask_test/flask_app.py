from flask import Flask, render_template, request
my_app = Flask('stock_pricer')

year = 2019 #input
#predicted_value = my_trained_model.predict(input_year) #output
#predicted_price = 12356
@my_app.route('/')
def show_predict_stock_form():
    return render_template('predictorform.html')
@my_app.route('/results', methods=['POST'])
def results():
    form = request.form
    if request.method == 'POST':
        #write your function that loads the model
        #model = get_model() #you can use pickle to load the trained model
        #year = request.form['year']
        year = 2019
        #predicted_stock_price = model.predict(year)
        predicted_stock_price = 123456
        return render_template('resultsform.html', year=year,   predicted_price=predicted_stock_price)

if __name__ == '__main__':
    my_app.run("localhost", "9999", debug=True)
    #my_app.run()
