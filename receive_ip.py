from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/receive_ip', methods=['POST'])
def receive_ip():
    """Recevoir et afficher l'adresse IP envoyée par le client."""
    data = request.get_json()
    if 'ip' in data:
        ip = data['ip']
        print(f"Received IP: {ip}")
        return jsonify({"status": "success", "message": "IP received"}), 200
    else:
        return jsonify({"status": "error", "message": "No IP found in the request"}), 400


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=6666)  # Assurez-vous que le port correspond à celui du script d'envoi
