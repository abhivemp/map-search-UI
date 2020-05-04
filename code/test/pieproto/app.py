from flask import Flask, Markup, render_template

app = Flask(__name__)


labels = [
    'JAN', 'FEB', 'MAR', 'APR',
    'MAY', 'JUN', 'JUL', 'AUG',
    'SEP', 'OCT', 'NOV', 'DEC'
]

values = [
    967.67, 1190.89, 1079.75, 1349.19,
    2328.91, 2504.28, 2873.83, 4764.87,
    4349.29, 6458.30, 9907, 16297
]

colors = [
    "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA",
    "#ABCDEF", "#DDDDDD", "#ABCABC", "#4169E1",
    "#C71585", "#FF4500", "#FEDCBA", "#46BFBD"]


#after otag stuff
oTag = [('Java', 25), ('Python', 20), ('C++', 80), ('Psql', 35), ('C', 50)]



@app.route('/pie')
def pie():

    return render_template('pie.html', title='Articles on SRHub by Tags', max=17000, set=zip(oTag, colors))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
