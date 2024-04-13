import matplotlib
matplotlib.use('Agg')

from flask import Flask, request, send_file
import matplotlib.pyplot as plt
from io import BytesIO
from math import *
import numpy as np
import re

app = Flask(__name__)

@app.route('/')
def index():
    return send_file('index.html')

@app.route('/plot', methods=['POST'])
def plot():
    function_input = request.get_json()['function']
    x = np.linspace(-10, 10, 1000)
    if not re.match(r'^[a-zA-Z0-9_()+\-*/\s\^%\.]+$', function_input):
        return 'Invalid function input.', 400
    
    namespace = {'x': x, 'sin': np.sin, 'cos': np.cos, 'tan': np.tan, 'exp': np.exp}
    try:
        y = eval(function_input, {}, namespace)
        if np.isscalar(y):
            y = np.full_like(x, y) 
        elif len(y) != len(x):
            raise ValueError('Invalid function output size.')
    except Exception as e:
        return f'Error evaluating function: {str(e)}', 400
    plt.clf()
    
    plt.plot(x, y, color='#007bff')
    
    plt.xlabel('$x$')
    plt.ylabel('$y$')
    plt.title('Plot of ' + function_input)
    
    img_buffer = BytesIO()
    plt.savefig(img_buffer, format='png')
    plt.close()

    img_buffer.seek(0)
    return send_file(img_buffer, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)