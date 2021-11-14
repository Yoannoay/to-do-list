from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired


class TaskForm(FlaskForm):
    description = StringField("Task Description", validators=[DataRequired()])
    submit = SubmitField("Add Task")

class TaskDesc(FlaskForm):
    taskselect = IntegerField("Task ID", validators= [DataRequired()])
    description = StringField("New Task Description", validators=[DataRequired()])

    submit = SubmitField("Confirm change")
    

