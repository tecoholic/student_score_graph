from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed


class CSVUploadForm(FlaskForm):
    csvfile = FileField(
        "CSV Mark Sheet",
        validators=[FileRequired(), FileAllowed(["csv"], "CSV Files only!")],
    )
