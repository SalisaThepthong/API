from flask import Flask, request

app = Flask(__name__)

@app.route('/receive_form_data', methods=['POST'])
def receive_form_data():
    form_data = request.form
    print('Form data:', form_data)
    return 'Received Form data successfully!', 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
#http://127.0.0.1:5000/receive_form_data