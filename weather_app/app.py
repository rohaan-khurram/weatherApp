from flask import Flask, request, render_template, jsonify
import requests

app = Flask(__name__)
API_KEY = "74db3d2c371c4748baf162835251807"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_weather', methods=['POST'])
def get_weather():
    lat = request.json.get('lat')
    lon = request.json.get('lon')
    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={lat},{lon}&aqi=no"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return jsonify({
            "location": data['location']['name'],
            "temp_c": data['current']['temp_c']
        })
    else:
        return jsonify({"error": "Failed to fetch weather"}), 500

# if __name__ == '__main__':
#     # public_url = ngrok.connect(5000)
#     # print(f"🌐 Ngrok Public URL: {public_url}")
#     app.run(debug=True)
