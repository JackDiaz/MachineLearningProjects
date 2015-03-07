import math
import itertools


def buildIt(it):
	it.append(('gen','F'))
	it.append(('gen','M'))

	for val in [1, 18, 25, 35, 45, 50, 56]:
		it.append(('age',val))

	for val in range(21):
		it.append(('occ',val))

	for val in range(10):
		it.append(('zip',val))

	for val in ['191', '192', '193', '194','195', '196', '197', '198', '199', '200']:
	#for val in ['1919', '1920', '1921', '1922', '1923', '1924', '1925', '1926', '1927', '1928', '1929', '1930', '1931', '1932', '1933', '1934', '1935', '1936', '1937', '1938', '1939', '1940', '1941', '1942', '1943', '1944', '1945', '1946', '1947', '1948', '1949', '1950', '1951', '1952', '1953', '1954', '1955', '1956', '1957', '1958', '1959', '1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000']:
		it.append(('year',val))

	for val in ["Action", "Adventure", "Animation", "Children's", "Comedy", "Crime", "Documentary", "Drama", "Fantasy", "Film-Noir", "Horror", "Musical", "Mystery", "Romance", "Sci-Fi", "Thriller", "War", "Western"]:
		it.append(('genre',val))

	for val in range(30,34):
		it.append(('time',val))

rules = []
buildIt(rules)

def findsubsets(S,m):
	ret = []
	for i in set(itertools.combinations(S, m)):
		ret.append(i[0])
	return ret

def join(L, j):
	count = 0
	rulesin = L[j-1]
	print rulesin
	out = []
	for r1 in rulesin:
		for r2 in rulesin:
			r3 = [r1]+[r2]
			r3 = list(set(r3)) #remove dups
			if len(r3) == j:
				tot = []
				count = 0
				for h in range(1,len(r3)):
					tot = tot+list(findsubsets(r3, h))
				for t in tot:
					for i in range(1,j):
						if t in L[i]:
							count += 1
				if count == len(tot):
					out.append(r3)
	return out



# [gen,age,occ,zipc,year,genres,mid,time,rating]

def sat(rulesin, tup):

	for r in rulesin:
		if r[0] == 'gen' and tup[0] != r[1]:
			return False
		elif r[0] == 'age' and tup[1] != str(r[1]):
			return False
		elif r[0] == 'occ' and tup[2] != str(r[1]):
			return False
		elif r[0] == 'zip' and tup[3][0] != str(r[1]):
			return False
		elif r[0] == 'year' and tup[4][0:3] != r[1]:
			return False
		elif r[0] == 'genre':
			if r[1] not in tup[5]:
				return False
		elif r[0] == 'time' and tup[7] != str(r[1]):
			return False
	return True



def support(rulesin):
	a = 0.0
	b = 0.0
	for p in pos:
		if sat(rulesin, pos[p]):
			a += 1.0

	for n in neg:
		if sat(rulesin, neg[n]):
			b += 1.0
	if a+b == 0:
		return False
	con = a/(a+b)
	if con >= 0.65:
		print con, rulesin
		if a/(len(pos)+len(neg)) >= 0.01:
			return True
	return False



users = {}
movies = {}
pos = {}
neg = {}
inp = 'data.dat'
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

f = open(inp, 'r')
i = 0
totalRows = 0.0
tuples = []
n = 0
p = 0
for line in f:
	totalRows += 1.0
	(uid,mid,rating,time) = line.strip('\n').split("::")
	time = math.floor(float(time)/(31556900.0))
	(gen,age,occ,zipc) = users[uid]
	(year, genres, mid) = movies[mid]
	yoyo = 0.0
	if int(rating) >= 4:
		pos[p] = users[uid]+movies[mid]+[time, rating]
		p += 1
	else:
		neg[n] = users[uid]+movies[mid]+[time, rating]
		n += 1
L = {}
L[1] = []
for r in rules:
	if support([r]):
		L[1].append(r)
print len(L[1])

j = 1
while(len(L[j]) != 0):
	j += 1
	C = join(L, j)
	L[j] = []
	for x in C:
		if support(x):
			L[j].append(x)

print L

 


