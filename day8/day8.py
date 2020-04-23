import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, request

app = Flask(__name__, 
            template_folder="templates",
            static_folder="static")
app.config['ENV'] = 'development'
app.config['DEBUG'] = True

@app.route('/')
def index():
    return "welcome, day8 class"

@app.route('/crawler/naver/<word>')
def crawler_naver(word):
    result = ''

    url = f"https://search.naver.com/search.naver"
    query = {
        "where": "image",
        "sm": "tab_jum",
        "query": word
    }
    response = requests.get(url, params=query)
    soup = BeautifulSoup(response.content, 'html.parser')
    tags = soup.select('img._img')
    img_url = tags[0]['data-source']
    
    res_img = requests.get(img_url)
    filename = f'static/{word}0.jpg'
    with open(filename, 'wb') as f:
        f.write(res_img.content)
    
    return render_template('crawler.html', 
                           result=filename)


@app.route('/verify_jumin', methods=['get', 'post'])
def verify_jumin():
    result = ''
    
    if request.method == 'POST':
        verifies = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]
        jumin = request.form['jumin'].replace('-', '')
        jumin = [int(c) for c in list(jumin)]
        
        check = [num1 * num2 
                 for num1, num2 in zip(jumin[:-1], verifies)]
        check_num = 11 - (sum(check) % 11)
        
        if check_num % 10 == jumin[-1]:
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