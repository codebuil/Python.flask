from flask import Flask
app = Flask(__name__)

htmlss="""
<html>
<head>
<title>
{{%title}}
</title>
<body>
{{%body}}
<body>
</head>
</html>
"""
titless="F.L.A.S.K."
titles="{{%title}}"
bodyss="<h1>F.L.A.S.K.</h1>"
bodys="{{%body}}"
@app.route("/")
def hello_world():
    h=htmlss
    h=h.replace(titles,titless)
    h=h.replace(bodys,bodyss)
    return h



app.run()
