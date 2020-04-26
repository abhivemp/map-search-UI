from flask import Flask, render_template
import psycopg2

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
	con = psycopg2.connect("dbname='Project' user='osc' password='osc'")
	cur = con.cursor()
	cur.execute("""SELECT * FROM pietags order by count DESC""")
	cats = cur.fetchall()
	cur.close
	return render_template('index.html', cats=cats)

@app.route('/Data')
def Data():
	con = psycopg2.connect("dbname='Project' user='osc' password='osc'")

	# cur = con.cursor()
	# cur.execute("SELECT tables.table_catalog, tables.table_name, tables.table_type FROM  INFORMATION_SCHEMA.tables WHERE table_schema='public' AND table_type = 'BASE TABLE' ORDER BY tables.table_name;")
	# oTables = cur.fetchall()
	# cur.close

	cur = con.cursor()
	cur.execute("SELECT * From article order by posting_date DESC")
	arts = cur.fetchmany(size = 9)
	cur.close

	cur = con.cursor()
	cur.execute("SELECT * From mm order by posting_date DESC")
	mults = cur.fetchmany(size = 9)
	cur.close

	return render_template('data.html', arts=arts, mults=mults)


@app.route('/Data/Category/<category>')
def CatData(category):
	con = psycopg2.connect("dbname='Project' user='osc' password='osc'")
	cur = con.cursor()
	cur.execute("""SELECT * FROM content WHERE category = (%s); """, (category,))
	dcat = cur.fetchall()
	cur.close

	return render_template('catData.html', dcat=dcat, cat=category)

@app.route('/Data/County/<county>')
def CountData(county):
	con = psycopg2.connect("dbname='Project' user='osc' password='osc'")
	cur = con.cursor()
	cur.execute("""SELECT * FROM content WHERE location = (%s); """, (county,))
	cont = cur.fetchall()
	cur.close

	return render_template('cData.html', cont=cont, count=county)

if __name__ == '__main__':
	app.run()