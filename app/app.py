from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <title>Hello Flask</title>
        <style>
            body {
                background: linear-gradient(135deg, #f6d365 0%, #fda085 100%);
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                color: #ffffff;
                text-align: center;
                padding-top: 100px;
            }
            h1 {
                font-size: 4em;
                margin-bottom: 0.2em;
                text-shadow: 2px 2px 4px #000000;
            }
            p {
                font-size: 1.5em;
                color: #f0f0f0;
                text-shadow: 1px 1px 2px #000000;
            }
            .card {
                background-color: rgba(255, 255, 255, 0.2);
                padding: 2em;
                border-radius: 15px;
                box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
                display: inline-block;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>🚀 Hello World DTCC Poc!</h1>
            <p>Welcome to your colorful Flask application.</p>
        </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
