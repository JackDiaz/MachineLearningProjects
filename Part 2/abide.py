rulesin = [('year', '194'), ('year', '195'), ('year', '196'), ('year', '197'), 
('genre', 'Film-Noir'), ('genre', 'War')]

import pickle
import math
mode = 4

def sat(tup):
	global rulesin
	for r in rulesin:
		if r[0] == 'gen' and tup[0] == r[1]:
			return True
		elif r[0] == 'age' and tup[1] == str(r[1]):
			return True
		elif r[0] == 'occ' and tup[2] == str(r[1]):
			return True
		elif r[0] == 'zip' and tup[3][0] == str(r[1]):
			return True
		elif r[0] == 'year' and tup[4][0:3] == r[1]:
			return True
		elif r[0] == 'genre':
			if r[1] in tup[5]:
				return True
		elif r[0] == 'time' and tup[7] == str(r[1]):
			return True
	return False


users = {}
movies = {}
pos = {}
neg = {}
inp = 'testing3.dat'
f = open('users.dat', 'r')
for line in f:
	(uid,gen,age,occ,zipc) = line.strip('\n').split("::")
	users[uid] = [gen,age,occ,zipc]
f.close()

f = open('movies.dat', 'r')
for line in f:
	(mid, nameyear, genres) = line.strip('\n').split("::")
	genres = genres.split('|')
	year = nameyear[len(nameyear)-5:len(nameyear)-1]
	name = nameyear[0:len(nameyear)-7]
	movies[mid] = [year]+[genres]+[mid]
f.close()
spCons = ["Gender", "Age", "Occupation", "Zip", "Year", "Action", "Adventure", "Animation", 
"Children's", "Comedy", "Crime", "Documentary", "Drama", "Fantasy", "Film-Noir", 
"Horror", "Musical", "Mystery", "Romance", "Sci-Fi", "Thriller", "War", "Western", "MovieID"]
f = open(inp, 'r')
g = open('output3.dat', 'w')
tuples = []
tp = 0.0
tn = 0.0
fp = 0.0
fn = 0.0
for line in f:
	(uid,mid,time) = line.strip('\n').split("::")
	time = math.floor(float(time)/(31556900.0))
	tup = users[uid]+movies[mid]+[time]
	if sat(tup):
		g.write(line.strip("\n")+"::1\n")
	else:
		g.write(line.strip("\n")+"::0\n")

	rating = 5

	if (int(rating) < mode  and not sat(tup)):
		tn += 1
	elif (int(rating) >= mode and sat(tup)):
		tp += 1
	elif (int(rating) >= mode and not sat(tup)):
		fn += 1
	elif (int(rating) < mode and sat(tup)):
		fp += 1
print "Frac: " + str(float(tp)/float(tp+tn+fp+fn))
print "True Positive: " + str(tp)
print "False Positive: " + str(fp)
print "False Negative: " + str(fn)
print "True Negative: " + str(tn)
#precision = tp/(tp+fp)
#recall = tp/(tp+fn)
#f1 = 2*((precision*recall)/(precision+recall))
#mc = ((tp*tn)-(fp*fn))/(((tp+fp)*(tp+fn)*(tn+fp)*(tn+fn))**(0.5))
#print "f1: " + str(f1)
#print "mc: " + str(mc)
g.close()
f.close()



