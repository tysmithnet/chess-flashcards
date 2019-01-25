import connexion

def home():
    return "hello world"

def moves():
    fen = connexion.request.get("fen")
    return fen

def openings():
    return "A00"

def openings_single():
    id = connexion.request.get("id")
    return id

app = connexion.FlaskApp(__name__)
app.add_api("swagger.yaml")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)