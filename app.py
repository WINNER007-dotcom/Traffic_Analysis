from flask import Flask, render_template
import traffic_analysis

app = Flask(__name__)

@app.route('/')
def home():
    # Run analysis code before rendering page
    traffic_analysis.run_analysis()
    return render_template("index.html")

if __name__ == '_main_':
    app.run(debug=True)