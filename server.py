import torch
from flask import Flask, request
from transformers import RobertaForSequenceClassification, RobertaTokenizer, AdamW


def load_model():
    model = RobertaForSequenceClassification.from_pretrained('roberta-base')
    model.load_state_dict(torch.load('./model_bert.pth', map_location="cpu"))
    model.eval()
    return model


def predict(review):
    sequence = tokenizer(review, return_tensors="pt", max_length=512, truncation=True)['input_ids']

    logits = model(sequence)[0]

    probabilities = torch.softmax(logits, dim=1).detach().cpu().tolist()[0]

    proba_pos = round(probabilities[1], 2)
    proba_neg = round(probabilities[0], 2)
    if proba_pos > proba_neg:
        return '<label style="color: green"> Positive review'
    else:
        return '<label style="color: red"> Negative review'


model = load_model()
tokenizer = RobertaTokenizer.from_pretrained("roberta-base")

app = Flask(__name__)

html_form = """
    <h2>Please, input your review:</h2>
    
    <form action="/transform" method="post" enctype="text/html">
    <textarea name="review" style="width:250px;height:150px;"></textarea>
    </br>
    <input type="submit" id="submit-form" class="hidden" />
    </form>
"""

@app.route('/')
def form():
    return """
      <html>
        <body>
          {}
        </body>
      </html>
    """.format(html_form)


@app.route('/transform', methods=["POST"])
def transform_view():
    review = request.form["review"]
    if not review:
        return "No review"
    output = predict(review)
    return """
      <html>
        <body>
          {}
          <br><br>
          <h2>Review: {}</h2>
          <br>
          <h2>Answer: {}</h2>
        </body>
      </html>
    """.format(html_form, review, output)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False)
