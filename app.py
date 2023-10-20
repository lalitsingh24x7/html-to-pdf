# app.py
from flask import Flask, request, send_file, Response
import pdfkit

app = Flask(__name__)

@app.route('/')
def index():
    # Replace the 'render_template' line with hardcoded HTML
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>HTML to PDF Converter</title>
    </head>
    <body>
        <h1>Convert HTML to PDF</h1>
        <form method="GET" action="/convert">
            <input type="text" name="url" placeholder="Enter URL">
            <input type="submit" value="Convert to PDF">
        </form>
    </body>
    </html>
    """
    return html_content

@app.route('/convert')
def convert_to_pdf():
    url = request.args.get('url')

    if url:
        # Use pdfkit to convert the webpage at the provided URL to PDF
        pdfkit.from_url(url, 'output.pdf')
        
        # Return the PDF as an attachment
        return send_file('output.pdf', as_attachment=True)
    else:
        return 'URL parameter is missing.'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
