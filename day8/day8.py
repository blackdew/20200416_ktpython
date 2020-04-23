from flask import Flask, render_template, request

app = Flask(__name__, template_folder="templates")
app.config['ENV'] = 'development'
app.config['DEBUG'] = True

@app.route('/')
def index():
    return "welcome, day8 class"

@app.route('/verify_jumin', methods=['get', 'post'])
def verify_jumin():
    result = ''
    
    if request.method == 'POST':
        verifies = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]
        jumin = request.form['jumin'].replace('-', '')
        jumin = [int(c) for c in list(jumin)]
        
        check_num = 0
        for i, num in enumerate(jumin[:-1]):
            check_num += num * verifies[i]
            
        check_num = 11 - (check_num % 11)
        
        if check_num == jumin[-1]:
            result = True
        else:
            result = False
    
    return render_template('template.html',
                            title='주민등록번호 검증기',
                            action='verify_jumin',
                            var_name='jumin',
                            placeholder='000000-0000000',
                            result=result)

app.run(port=8000)