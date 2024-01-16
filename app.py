from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    # Sample data to pass to the template
    image_url = request.args.get('image_url', '')
    text = request.args.get('text', '')
    rect_color = request.args.get('rect_color', '#FFFFFF')  # Red color
    text_bottom = request.args.get('text', '')
    text_color= request.args.get('rect_color', '#FFFFFF')

    return render_template('index.html', image_url=image_url, text=text,rect_color=rect_color,text_bottom=text_bottom, text_color= text_color)

if __name__ == '__main__':
    app.run(debug=True)