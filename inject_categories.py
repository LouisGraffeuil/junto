import sqlite3 as sql3
from sys import stderr
import os.path

"""
Script pour injecter dans la base de données les themes et les types d'activités
"""

DB_NAME = 'database.db'
ACTIVITY_THEME = ["Les incontournables", "Découverte et culture", "Expérience authentique",
                  "Détente", "Sport & Loisirs", "Gastronomie"]
ACTIVITY_TYPE = ["Art", "Ateliers", "Aventure", "Balade", "Exposition", "Extrême",
                 "Fun", "Histoire", "Insolite", "Musique", "Mystère", "Nature",
                 "Spectacle", "Relaxation","Romantique"]

if (os.path.isfile(DB_NAME)):
	db = sql3.connect(DB_NAME)
	try:
		cursor = db.cursor()
		# injecting theme
		id_ = 1
		inject_theme = 'INSERT INTO activityTheme(id, theme) VALUES(?, ?)'
		cursor.execute(inject_theme, (0, ""))
		for aTheme in ACTIVITY_THEME:
			try:
				cursor.execute(inject_theme, (id_, aTheme))
			except:
				print('Theme <{}, {}> already exists in database.'.format(id_, aTheme), file=stderr)
			id_ += 1
		# injection type
		id_ = 1
		inject_type = 'INSERT INTO activityType(id, type) VALUES(?, ?)'
		cursor.execute(inject_type, (0, ""))
		for aType in ACTIVITY_TYPE:
			try:
				cursor.execute(inject_type, (id_, aType))
			except:
				print('Type <{}, {}> already exists in database.'.format(id_, aType), file=stderr)
			id_ += 1
		db.commit()
		db.close()
		print('Injection of thems and types is now over.')
	except:
		print('Something wen\'t wrong during injection, database has returned to its initial state.', file=stderr)
else:
	print('Database {} doesn\'t exists !'.format(DB_NAME), file=stderr)
