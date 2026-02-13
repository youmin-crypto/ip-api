from flask import Flask, request, jsonify

app = Flask(__name__)

# IP တွေကို စာရင်း (List) အနေနဲ့ သိမ်းမယ်
device_ips = {
    "phone1": [],
    "phone2": [],
    "phone3": [],
    "phone4": [],
    "phone5": []
}

@app.route('/update', methods=['GET'])
def update_ip():
    device_id = request.args.get('id')
    new_ip = request.args.get('ip')
    
    if device_id in device_ips:
        # IP အသစ်ကို စာရင်းထဲမှာ ထပ်တိုး (Append) လုပ်မယ်
        # အကယ်၍ IP က ရှိပြီးသားဆိုရင် ထပ်မထည့်အောင် စစ်လို့ရပါတယ်
        if new_ip not in device_ips[device_id]:
            device_ips[device_id].append(new_ip)
        return f"Added {new_ip} to {device_id} list", 200
    return "Invalid Device ID", 400

# IP အားလုံးကို ပြန်ကြည့်ရန် Link: /get-all
@app.route('/get-all', methods=['GET'])
def get_all_ips():
    return jsonify(device_ips)

if __name__ == '__main__':
    app.run(debug=True)
