from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    nama = "Ian Wahyu"
    hobi = ["Coding", "Gaming", "Membaca"]
    return render_template("index.html", nama=nama, hobi=hobi)

if __name__ == "__main__":
    app.run(debug=True)