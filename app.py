from flask import Flask, render_template
from flask_wtf import FlaskForm
from werkzeug.utils import secure_filename
from flask_wtf.file import FileField
from wtforms import SubmitField
from wtforms.validators import InputRequired
from prediction import predict_tumor_class, model, labels
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = 'abcd1234'
app.config['IMAGE_FOLDER'] = 'static/image'

if not os.path.exists(app.config['IMAGE_FOLDER']):
    os.makedirs(app.config['IMAGE_FOLDER'])

class UploadFileForm(FlaskForm):
    file = FileField("File", validators=[InputRequired()])
    submit = SubmitField("Predict")

@app.route('/', methods=['GET', 'POST'])
def upload():
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data
        print(file.filename)
        input_file_path = os.path.join(app.config['IMAGE_FOLDER'], secure_filename(file.filename))
        file.save(input_file_path)
        predicted_class, confidence = predict_tumor_class(model, input_file_path, labels)
        return render_template('predict.html', file=file, predicted_class=predicted_class, confidence=confidence)
    
    return render_template('home.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)

