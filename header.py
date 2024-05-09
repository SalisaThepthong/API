from flask import Flask, request

app = Flask(__name__)

@app.route('/receive_header_data', methods=['POST'])
def receive_header_data():
    # เข้าถึงข้อมูลของ header ของคำขอ
    headers = request.headers
    print('Request Headers:')
    # วนลูปและพิมพ์ค่า key-value ของ headers ทั้งหมด
    for key, value in headers.items():
        print(f'{key}: {value}')
    return 'Received Header data successfully!', 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)

#http://127.0.0.1:5000/receive_header_data