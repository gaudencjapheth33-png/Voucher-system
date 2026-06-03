from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Voucher System Running"

if __name__ == "__main__":
    app.run()
