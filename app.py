from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '''
<html>
<head>
    <style>
        body {
            font-family: Arial, sans-serif;
        }
        h1 {
            color: #333;
            font-size: 36px;
        }
        h2 {
            color: #555;
            font-size: 28px;
        }
        center {
            margin-top: 50px;
        }
    </style>
</head>
<body>
<center>
<h1>Demo on GitOps with ArgoCD and Github Actions.</h1> <br>
<br>
<h2>deploying..</h2>
</center>
</body>
</html>
'''

if __name__ == '__main__':
    app.run(debug=True)
