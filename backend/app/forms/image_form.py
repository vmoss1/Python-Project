from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import SubmitField
from app.aws_helpers import ALLOWED_EXTENSIONS
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class ImageForm(FlaskForm):
    image = FileField(
        "Image File",
        validators=[FileRequired(),
        FileAllowed(list(ALLOWED_EXTENSIONS))])
    submit = SubmitField("Create Post")
