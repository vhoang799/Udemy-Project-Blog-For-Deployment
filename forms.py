from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL, Email, Length
from flask_ckeditor import CKEditorField

# WTForm for creating a blog post
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


# TODO: Create a RegisterForm to register new users
class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[
        DataRequired(message="Field is required."),
        Email(message="Must be a valid email address."), ])
    password = PasswordField("Password", validators=[
        DataRequired(message="Field is required."),
        Length(min=2, message="Password must be at least 2 characters long."),
    ])
    name = StringField("Name", validators=[
        DataRequired(message="Field is required."),
    ])
    submit = SubmitField("Submit")

# TODO: Create a LoginForm to login existing users
class LoginForm(FlaskForm):
    email = StringField("Email", validators=[
        DataRequired(message="Field is required."),
        Email(message="Must be a valid email address.")
    ])
    password = PasswordField("Password", validators=[
        DataRequired(message="Field is required."),
        Length(min=2, message="Password must be at least 2 characters long."),
    ])
    submit = SubmitField("Submit")

# TODO: Create a CommentForm so users can leave comments below posts
class CommentForm(FlaskForm):
    body = CKEditorField("Comment", validators=[
        DataRequired(message="Field is required."),
    ])
    submit = SubmitField("Submit")
