from flask import Flask, request, jsonify

app = Flask(__name__)

# IP data တွေကို သိမ်းထားမယ့် နေရာ (ယာယီမှတ်ဉာဏ်ထဲမှာ သိမ်းတာပါ)
# တကယ်လို့ ဖုန်းအလိုက် သိမ်းချင်ရင် Dictionary သုံးလို့ရပါတယ်
device_ips = {
    "phone1": "none",
    "phone2": "none",
    "phone3": "none",
    "phone4": "none",
    "phone5": "none"
}

@app.route('/')
def home():
    return "IP Control Center is Running!"

# IP update လုပ်ရန် Link: /update?id=phone1&ip=1.1.1.1
@app.route('/update', methods=['GET'])
def update_ip():
    device_id = request.args.get('id')
    new_ip = request.args.get('ip')
    
    if device_id in device_ips:
        device_ips[device_id] = new_ip
        return f"Updated {device_id} to {new_ip}", 200
    return "Invalid Device ID", 400

# IP အားလုံးကို ပြန်ကြည့်ရန် Link: /get-all
@app.route('/get-all', methods=['GET'])
def get_all_ips():
    return jsonify(device_ips)

if __name__ == '__main__':
    app.run(debug=True)
