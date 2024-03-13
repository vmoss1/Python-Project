from flask import Flask, Blueprint, request, render_template
from app.models.image_model import db, ImageForm
from flask_login import current_user, login_required
from .config import Configuration
from app.routes.aws_helpers import (
    upload_file_to_s3, get_unique_filename)

# image_routes = Blueprint("images", __name__, url_prefix="")
# app.register_blueprint(image_routes)

app = Flask(__name__)
app.config.from_object(Configuration)

db.init_app(app)


@app.route("/", methods=["GET","POST"])
equired
def upload_image():
    form = ImageForm()

    if form.validate_on_submit():

        image = form.data["image"]
        image.filename = get_unique_filename(image.filename)
        upload = upload_file_to_s3(image)
        print(upload)

        if "url" not in upload:
        # if the dictionary doesn't have a url key
        # it means that there was an error when you tried to upload
        # so you send back that error message (and you printed it above)
            return render_template("post_form.html", form=form, errors=[upload])

        url = upload["url"]
        new_image = Post(image= url)
        db.session.add(new_image)
        db.session.commit()
        return redirect("/posts/all")

    if form.errors:
        print(form.errors)
        return render_template("post_image_form.html", form=form, errors=form.errors)

    return render_template("post_image_form.html", form=form, errors=None)
