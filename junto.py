from flask import Flask, redirect, url_for, render_template, request, abort
from sys import stderr
import sqlite3 as sql3
import os.path

import Activity

app = Flask(__name__)

DB_NAME = 'database.db'

# choix du questionnaire
PEOPLE_TYPE = ["Solo", "Couple", "Famille", "Amis", "Groupe (minimum 7 personnes)"]
ACTIVITY_THEME = ["Les incontournables", "Découverte et culture", "Expérience authentique",
                  "Détente", "Sport & Loisirs", "Gastronomie"]
ACTIVITY_TYPE = ["Art", "Ateliers", "Aventure", "Balade", "Exposition", "Extrême",
                 "Fun", "Histoire", "Insolite", "Musique", "Mystère", "Nature", "Spectacle", "Relaxation",
                 "Romantique"]
ACTIVITY_DURATION = ["1h", "1h30", "2h", "2h30", "3h", "Toute la journée"]
GENDER = ["un homme", "une femme"]
AGE_RANGE = ["18 - 25", "26 - 35", "34 - 45", "46 - 55", "56 - 65", "65+"]
BUDGET_RANGE = ["Moins de 5€", "Entre 5€ et 15€", "Entre 15€ et 30€", "Entre 30€ et 60€",
                "Entre 60€ et 80€", "Autour de 100€", "Plus de 150€"]

def obtain_activities():
	ret = list()
	if (os.path.isfile(DB_NAME)):
		db = sql3.connect(DB_NAME)
		try:
			cursor = db.cursor()
			query = '''select a.id, a.name, a.description, a.peopleMin, a.peopleMax, a.priceMin, a.priceMax, 
					th.theme, ty1.type, ty2.type, ty3.type, ty4.type, ty5.type, ty6.type
					from activities a, activityTheme th, activityType ty1, activityType ty2, 
					activityType ty3, activityType ty4, activityType ty5, activityType ty6
					where a.activityThemeId=th.id and a.activityTypeId1=ty1.id and a.activityTypeId2=ty2.id 
					and a.activityTypeId3=ty3.id and a.activityTypeId4=ty4.id and a.activityTypeId5=ty5.id 
					and a.activityTypeId6=ty6.id'''
			result = cursor.execute(query).fetchall()
			for r in result:
				ret.append(Activity.build_from_database(r))
		except:
			print('Something wen\'t wrong during queying.', file=stderr)
	else:
		print('Database {} doesn\'t exists !'.format(DB_NAME), file=stderr)
	return ret

def sort_activities(activities, wish):
	# TODO algo de tri des activités en fonction du formulaire à implémenter
	return activities;

@app.route('/')
@app.route('/index.html')
def index():
	return render_template('index.html')

@app.route('/experience.html')
def experience():
	return render_template('experience.html')

@app.route('/partenaire.html')
def partenaire():
	return render_template('partenaire.html')


@app.route('/about.html')
def about():
	return render_template('about.html')

@app.route('/questionnaire.html')
def questionnaire():
	return render_template('questionnaire.html', PEOPLE_TYPE=PEOPLE_TYPE, ACTIVITY_THEME=ACTIVITY_THEME,
	                       ACTIVITY_TYPE=ACTIVITY_TYPE, ACTIVITY_DURATION=ACTIVITY_DURATION, GENDER=GENDER,
	                       AGE_RANGE=AGE_RANGE, BUDGET_RANGE=BUDGET_RANGE)


@app.route('/suggestion.html', methods=['GET', 'POST'])
def suggestion():
	if request.method=="POST":
		# si questionnaire valide ajouter dans la base
		activities = obtain_activities()
		sorted_activities = sort_activities(activities, None)

		return render_template("suggestion.html", activities=sorted_activities)
	else:
		return redirect(request.host_url)


if __name__ == '__main__':
	app.run(host="0.0.0.0")
