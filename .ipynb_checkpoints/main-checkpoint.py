# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from flask import Flask,request,render_template

app=Flask(__name__,template_folder='templates')

@app.route('/')

def index():
    # Main page
    return render_template('index.html')

@app.route('/',methods=['Get','Post'])

def add():
     a=request.args.get('a')
     b=request.args.get('b')
     return str(int(a)+int(b))
if __name__ == '__main__':
    app.run()
