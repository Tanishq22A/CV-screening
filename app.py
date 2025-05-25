from flask import Flask, request, render_template
import pickle
import pdfplumber
import re

app = Flask(__name__)


clf = pickle.load(open("clf.pkl", "rb"))
tfidf = pickle.load(open("tfidf.pkl", "rb"))
label_encoder = pickle.load(open("label_encoder.pkl", "rb"))

def clean_resume(text):
    text = re.sub(r"http\S+\s*", " ", text)
    text = re.sub(r"RT|cc", " ", text)
    text = re.sub(r"#\S+", " ", text)
    text = re.sub(r"@\S+", " ", text)
    text = re.sub(r"[%s]" % re.escape("""!"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"""), " ", text)
    text = re.sub(r"[^\x00-\x7f]", r" ", text)
    text = re.sub(r"\s+", " ", text)
    return text

def extract_text(pdf_file):
    full_text = ""
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            full_text += page.extract_text() or ""
    return full_text

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        pdf = request.files["resume"]
        if pdf:
            text = extract_text(pdf)
            cleaned = clean_resume(text)
            vectorized = tfidf.transform([cleaned])
            pred_num = clf.predict(vectorized)[0]
            pred_label = label_encoder.inverse_transform([pred_num])[0]
            prediction = f"Predicted Resume Category: <strong>{pred_label}</strong>"
    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
