from bottle import Bottle, run, template
app = Bottle()

@app.route('/')
def update():
    with open('file.txt', 'r') as file:
        text = file.read()
    return template('update.tpl', text=text)


