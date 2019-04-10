from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

page_header = """
    <!DOCTYPE html>

    <html>
        <head>
            <style>
                form {
                    background-color: #eee;
                    padding: 20px;
                    margin: 0 auto;
                    width: 540px;
                    font: 16px sans-serif;
                    border-radius: 10px;
                }
                textarea {
                    margin: 10px 0;
                    width: 540px;
                    height: 120px;
                }
            </style>
        </head>
        <body>
        """

form = """
        
            <form action='/' method="post">
                <label for="rotate-input">Rotate by: </label>
                <input id="rotate-input" type="text" name="rot" value="0" />
                <textarea name="text">
                </textarea>
                <input type="submit" />

            </form>
        """



page_footer = """
        </body>
    </html>


"""

@app.route("/")
def index():
    return page_header + form + page_footer

@app.route("/", methods=['POST'])
def encrypt():
    rotate = int(request.form["rot"])
    user_text = request.form["text"]
    
    encrypted_text = ""

    encrypted_text += rotate_string(user_text, rotate)
    

    return page_header + form + "<h1>" +encrypted_text + "</h1>" + page_footer

app.run()