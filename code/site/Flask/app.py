# Flask HQ

from flask import Flask, render_template
import psycopg2

app = Flask(__name__)
app.debug = True

# THESE VARIABLES CONTROL THE LOGIN TO THE DB, CHANGE IF NECESSARY
uname = 'Project'
use = 'osc'
pawrd = 'osc'


# psql queries for the index home page
# Selects data from the pietags view to the MapCats view and 
# orders the article occurences from greatest to least.
# passes both queries to index.html
@app.route('/')
def index():
	con = psycopg2.connect("dbname=" + uname + " user="+ use + " password=" + pawrd)
	cur = con.cursor()
	cur.execute("""SELECT * FROM pietags order by count DESC""")
	cats = cur.fetchall()
	cur.close

	cur = con.cursor()
	cur.execute("""SELECT * FROM MapCats order by count DESC""")
	counts = cur.fetchall()
	cur.close

	return render_template('index.html', cats=cats, counts=counts)

# queries for data and retrieval
# selects from article table and shows order from recently uploaded
# passes both articles and multimedia content to display most 
# recent content
@app.route('/Data')
def Data():
	con = psycopg2.connect("dbname=" + uname + " user="+ use + " password=" + pawrd)

	cur = con.cursor()
	cur.execute("SELECT * From article order by posting_date DESC")
	arts = cur.fetchmany(size = 9)
	cur.close

	cur = con.cursor()
	cur.execute("SELECT * From mm order by posting_date DESC")
	mults = cur.fetchmany(size = 9)
	cur.close

	return render_template('data.html', arts=arts, mults=mults)

# category retrieval
# selects article/mulitmedia based on category selected 
# loads the data/content for the category selected on that pie chart 
@app.route('/Data/Category/<category>')
def CatData(category):
	con = psycopg2.connect("dbname=" + uname + " user="+ use + " password=" + pawrd)
	cur = con.cursor()
	cur.execute("""SELECT * FROM article WHERE category = (%s); """, (category,))
	dcat = cur.fetchall()
	cur.execute("""SELECT * FROM mm WHERE category = (%s); """, (category,))
	dcat += cur.fetchall()
	cur.close

	dcat.sort(key=lambda data:data[3], reverse = True)

	return render_template('catData.html', dcat=dcat, cat=category)

#retrieve by county
# selects article/multimedia based on county selected 
@app.route('/Data/County/<county>')
def CountData(county):
	con = psycopg2.connect("dbname=" + uname + " user="+ use + " password=" + pawrd)
	cur = con.cursor()
	cur.execute("""SELECT * FROM article WHERE location = (%s); """, (county,))
	cont = cur.fetchall()
	cur.execute("""SELECT * FROM mm WHERE location = (%s); """, (county,))
	cont += cur.fetchall()
	cur.close

	cont.sort(key=lambda data:data[3], reverse = True)

	return render_template('cData.html', cont=cont, count=county)

if __name__ == '__main__':
	app.run()