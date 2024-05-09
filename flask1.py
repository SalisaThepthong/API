from flask import Flask, request

app = Flask(__name__)

@app.route('/receive_json', methods=['POST'])
def receive_json():
    # ตรวจสอบว่ามี JSON body ที่ส่งมาหรือไม่
    if request.is_json:
        # รับข้อมูล JSON จาก body
        json_data = request.get_json()
        # พิมพ์ข้อมูล JSON ที่ได้รับ
        print(json_data)
        return 'Received JSON data successfully!', 200
    else:
        return 'Invalid JSON data', 400

if __name__ == '__main__':
    app.run(debug=True,port = 5000)
    #1. api post รับ json body แล้ว print ออกมา 
