#  MapSearch (CSC 315)


## Overview
The module is a prototype to demonstrate an upgraded landing page of [NJSR Hub](https://srhub.org/). The prototype allows users to search content based on their location or trending tags of the content. 

## How it works

### See all Articles
<img src="https://github.com/CSC-315/cab-srhub-group-10/blob/master/docs/images/articlechoose.gif" alt="drawing" width="600"/>

<br>

### See content curated to location
<img src="https://github.com/CSC-315/cab-srhub-group-10/blob/master/docs/images/mapchoose.gif" alt="drawing" width="600"/>

<br>


### You can even see content based on their tags
<img src="https://github.com/CSC-315/cab-srhub-group-10/blob/master/docs/images/piechart.gif" alt="drawing" width="600"/>

<br>


## Installation and Usage
See wiki system requirements before installing

Setup Postgres Database
Preferably do this outside the repository. 

```
$ createdb <dbname>
$ sudo -u postgresql
$ alter role <username> superuser
$ psql <dbname>
$ \i path/to/repo/cab-srhub-group-10/code/postgres/DB_setup.sql
```
If you don't have `pipenv` in the pip
```
$ pip install pipenv
```
Then
```
$ cd code/site/
```

Enter the virtual environment
```
$ pipenv shell
$ pipenv install
```

Access the website
```
$ cd Flask
```

Run the Flask script
```
$ python app.py
```
Open Google Chrome and access the prototype via localhost. After running the flask app, you can see your locahost address

<img src="https://github.com/CSC-315/cab-srhub-group-10/blob/master/docs/images/localhost%20example.PNG" alt="drawing" width="500"/>



Developed by:

[Kevin Williams](https://www.linkedin.com/in/willik39/)
[Yash Dhayal](https://github.com/dhayalytcnj)
[Abhi Vempati](https://github.com/abhivemp) 
[Zahir Johnson](https://github.com/ZahirJohnson00)
