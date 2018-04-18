import sqlite3 as sql3
from sys import stderr
import os.path

"""
Script pour créer la base de données
"""

DB_NAME = 'database.db'

if not (os.path.isfile(DB_NAME)):
	db = sql3.connect(DB_NAME)
	cursor = db.cursor()
	build_activities = '''CREATE TABLE activities(
					id TEXT PRIMARY KEY, 
					name TEXT,
					description TEXT,
					peopleMin INTEGER,
					peopleMax INTEGER ,
					priceMin DOUBLE,
					priceMax DOUBLE,
					activityThemeId TEXT,
					activityTypeId1 TEXT,
					activityTypeId2 TEXT,
					activityTypeId3 TEXT,
					activityTypeId4 TEXT,
					activityTypeId5 TEXT,
					activityTypeId6 TEXT,
					FOREIGN KEY(activityThemeId) REFERENCES activityTheme(id),
					FOREIGN KEY(activityTypeId1) REFERENCES activityType(id),
					FOREIGN KEY(activityTypeId2) REFERENCES activityType(id),
					FOREIGN KEY(activityTypeId3) REFERENCES activityType(id),
					FOREIGN KEY(activityTypeId4) REFERENCES activityType(id),
					FOREIGN KEY(activityTypeId5) REFERENCES activityType(id),
					FOREIGN KEY(activityTypeId6) REFERENCES activityType(id))'''
	# TODO ajouter plus de activityType si nécessaire
	build_wishes = '''CREATE TABLE wishes(
					id TEXT PRIMARY KEY,
					peopleGroupType TEXT,
					peopleNumber INTEGER,
					gender TEXT,
					ageRangeMin INTEGER,
					ageRangeMax INTEGER,
					name TEXT,
					mail TEXT,
					phone TEXT,
					budgetRangeMin INTEGER,
					budgetRangeMax INTEGER,
					accomodationName TEXT,
					activityDate DATE,
					activityDuration DOUBLE,
					activityThemeId1 TEXT,
					activityThemeId2 TEXT,
					activityThemeId3 TEXT,
					activityThemeId4 TEXT,
					activityThemeId5 TEXT,
					activityThemeId6 TEXT,
					activityTypeId1 TEXT,
					activityTypeId2 TEXT,
					activityTypeId3 TEXT,
					activityTypeId4 TEXT,
					activityTypeId5 TEXT,
					activityTypeId6 TEXT,
					activityTypeId7 TEXT,
					activityTypeId8 TEXT,
					activityTypeId9 TEXT,
					activityTypeId10 TEXT,
					activityTypeId11 TEXT,
					activityTypeId12 TEXT,
					activityTypeId13 TEXT,
					activityTypeId14 TEXT,
					activityTypeId15 TEXT,
					FOREIGN KEY(activityThemeId1) REFERENCES activityTheme(id),
					FOREIGN KEY(activityThemeId2) REFERENCES activityTheme(id),
					FOREIGN KEY(activityThemeId3) REFERENCES activityTheme(id),
					FOREIGN KEY(activityThemeId4) REFERENCES activityTheme(id),
					FOREIGN KEY(activityThemeId5) REFERENCES activityTheme(id),
					FOREIGN KEY(activityThemeId6) REFERENCES activityTheme(id),
					FOREIGN KEY(activityTypeId1) REFERENCES activityType(id),
					FOREIGN KEY(activityTypeId2) REFERENCES activityType(id),
					FOREIGN KEY(activityTypeId3) REFERENCES activityType(id),
					FOREIGN KEY(activityTypeId4) REFERENCES activityType(id),
					FOREIGN KEY(activityTypeId5) REFERENCES activityType(id),
					FOREIGN KEY(activityTypeId6) REFERENCES activityType(id),
					FOREIGN KEY(activityTypeId7) REFERENCES activityType(id),
					FOREIGN KEY(activityTypeId8) REFERENCES activityType(id),
					FOREIGN KEY(activityTypeId9) REFERENCES activityType(id),
					FOREIGN KEY(activityTypeId10) REFERENCES activityType(id),
					FOREIGN KEY(activityTypeId11) REFERENCES activityType(id),
					FOREIGN KEY(activityTypeId12) REFERENCES activityType(id),
					FOREIGN KEY(activityTypeId13) REFERENCES activityType(id),
					FOREIGN KEY(activityTypeId14) REFERENCES activityType(id),
					FOREIGN KEY(activityTypeId15) REFERENCES activityType(id))'''
	# TODO ajouter plus de activityType si nécessaire
	build_activityTheme = '''CREATE TABLE activityTheme(
								id TEXT PRIMARY KEY,
								theme TEXT)'''
	build_activityType = '''CREATE TABLE activityType(
									id TEXT PRIMARY KEY,
									type TEXT)'''
	cursor.execute(build_activityTheme)
	cursor.execute(build_activityType)
	cursor.execute(build_activities)
	cursor.execute(build_wishes)
	db.commit()
	db.close()
	print('File {} has been created.'.format(DB_NAME))
else:
	print('File {} already exists !'.format(DB_NAME), file=stderr)

