from flask import Flask, render_template

app = Flask(__name__, template_folder="templates")
app.config['ENV'] = 'development'
app.config['DEBUG'] = True

@app.route('/')
def index():
    return "welcome, day8 class"

@app.route('/verify_jumin', methods=['get', 'method'])
def verify_jumin():
    result = ''
    
    return render_template('template.html',
                            title='주민등록번호 검증기',
                            action='verify_jumin',
                            var_name='jumin',
                            placeholder='000000-0000000',
                            result=result)

app.run(port=8000)