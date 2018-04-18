class Activity:
	def __init__(self, id, name, description, peopleMin, peopleMax,
	             priceMin, priceMax, activityTheme, activityType):
		self.id = id
		self.name = name
		self.description = description
		self.peopleMin = peopleMin
		self.peopleMax = peopleMax
		self.priceMin = priceMin
		self.priceMax = priceMax
		self.activityTheme = activityTheme
		self.activityType = activityType

	def database_format(self):
		ret = Activity(self.id, self.name, self.description, self.peopleMin, self.peopleMax,
		               self.priceMin, self.priceMax, self.activityTheme, self.activityType)
		# add 0 => None to match database format
		for i in range(0, 6 - len(ret.activityType)):
			ret.activityType.append(0)
		return ret

def build_from_database(row):
	id = row[0]
	name = row[1]
	description = row[2]
	peopleMin = row[3]
	peopleMax = row[4]
	priceMin = row[5]
	priceMax = row[6]
	activityTheme = row[7]
	activityType = list()
	for r in range(8, len(row)):
		if row[r]!='':
			activityType.append(row[r])
	return Activity(id, name, description, peopleMin, peopleMax, priceMin, priceMax, activityTheme, activityType)