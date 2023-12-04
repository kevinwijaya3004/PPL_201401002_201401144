import os
from keras.models import load_model
from flask import Flask, render_template, request

app = Flask(__name__)
model = load_model('model/saved_model.h5', compile=False)
model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict')
def predict():
    return render_template('predict.html')

@app.route('/result', methods=['GET', 'POST'])
def result():
    age = int(request.form['age'])
    gender = 0 if request.form['gender'] == 'Male' else 1

    polyuria = polydipsia = w_loss = weakness = polyphagia = g_thrush = 0
    v_blurring = itching = irritability = d_healing = p_paresis = 0
    m_stiffness = alopecia = obesity = 0

    if request.form.get('polyuria'): polyuria = 1
    if request.form.get('polydipsia'): polydipsia = 1
    if request.form.get('sudden_weight_loss'): w_loss = 1
    if request.form.get('weakness'): weakness = 1
    if request.form.get('polyphagia'): polyphagia = 1
    if request.form.get('genital_thrush'): g_thrush = 1
    if request.form.get('visual_blurring'): v_blurring = 1
    if request.form.get('itching'): itching = 1
    if request.form.get('irritability'): irritability = 1
    if request.form.get('delayed_healing'): d_healing = 1
    if request.form.get('partial_paresis'): p_paresis = 1
    if request.form.get('muscle_stiffness'): m_stiffness = 1
    if request.form.get('alopecia'): alopecia = 1
    if request.form.get('obesity'): obesity = 1

    features = [
        age, gender, polyuria, polydipsia, w_loss, weakness,
        polyphagia, g_thrush, v_blurring, itching, irritability,
        d_healing, p_paresis, m_stiffness, alopecia, obesity
    ]

    prediction = model.predict([features])
    classes = False if prediction[0] < 0.5 else True

    print(f'features: {features}')
    print(f'prediction: {prediction[0]}')

    return render_template('predict.html', result=classes)

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv('PORT', default=5000))
