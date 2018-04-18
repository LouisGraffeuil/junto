import sqlite3 as sql3
from sys import stderr
import os.path

import Activity

"""
Script pour injecter dans la base de données des activités de demo
"""

DB_NAME = 'database.db'

activity1 = Activity.Activity("0",
                     "name1",
                     "name1 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
                     1,
                     20,
                     0,
                     50,
                     str(0),
                     [str(0), str(1), str(2)])

activity2 = Activity.Activity("1",
                              "name2",
                              "name2 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
                              1,
                              20,
                              50,
                              100,
                              str(2),
                              [str(3), str(4), str(5)])

activity3 = Activity.Activity("2",
                              "name3",
                              "name3 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
                              3,
                              4,
                              150,
                              200,
                              str(2),
                              [str(3), str(4)])

activities = [activity1.database_format(), activity2.database_format(), activity3.database_format()]

if (os.path.isfile(DB_NAME)):
	db = sql3.connect(DB_NAME)
	try:
		cursor = db.cursor()
		# injecting activities
		inject_activity = '''INSERT INTO activities(
							id, 
							name,
							description,
							peopleMin,
							peopleMax,
							priceMin,
							priceMax,
							activityThemeId,
							activityTypeId1,
							activityTypeId2,
							activityTypeId3,
							activityTypeId4,
							activityTypeId5,
							activityTypeId6
					) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
		for a in activities:
			try:
				cursor.execute(inject_activity, (a.id, a.name, a.description, a.peopleMin, a.peopleMax, a.priceMin,
				                                 a.priceMax, a.activityTheme,
				                                 a.activityType[0], a.activityType[1], a.activityType[2],
				                                 a.activityType[3], a.activityType[4], a.activityType[5]))
			except:
				print('Activity <{}, {}, ...> already exists in database.'.format(a.id, a.name), file=stderr)

		db.commit()
		db.close()
		print('Injection of demonstration activities is now over.')
	except:
		print('Something wen\'t wrong during injection, database has returned to its initial state.', file=stderr)
else:
	print('Database {} doesn\'t exists !'.format(DB_NAME), file=stderr)