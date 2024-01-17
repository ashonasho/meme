from flask import Flask, render_template, request, Response
import requests

app = Flask(__name__)

@app.route('/')
def index():
    # Sample data to pass to the template
    image_url = request.args.get('image_url', '')
    rect_color = request.args.get('rect_color', '#000000')  # Default black color

    return render_template('index.html', image_url=image_url, rect_color=rect_color)

@app.route('/proxy')
def proxy():
    # Get the image URL from query parameters
    image_url = request.args.get('image_url')
    if not image_url:
        return "Image URL not provided", 400

    try:
        response = requests.get(image_url)
        # Additional checks can be added here (like status code or content type)
        return Response(response.content, content_type=response.headers['Content-Type'])
    except requests.exceptions.RequestException as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(debug=True)
