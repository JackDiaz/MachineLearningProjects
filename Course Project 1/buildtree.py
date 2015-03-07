import pickle
import sys
import math


sys.setrecursionlimit(10000)

opt = {}
maxDepth = 10
justFives = True
if justFives:
	mode = 5
else:
	mode = 4

spCons = ["Gender", "Age", "Occupation", "Year", "Action", "Adventure", "Animation", 
"Children's", "Comedy", "Crime", "Documentary", "Drama", "Fantasy", "Film-Noir", 
"Horror", "Musical", "Mystery", "Romance", "Sci-Fi", "Thriller", "War", "Western", "Zip", "LooseTime"]
#, "MovieID"] time loosetime decade zip zip2

class Node:
	def __init__(self, dataIn, depth):
		self.data = dataIn
		self.left = None
		self.right = None
		self.depth = depth

class DecisionTree:
	def __init__(self, rootIn):
		self.root = rootIn

def homogenous(tuples):
	global mode
	yes = 0.0
	no = 0.0
	for t in tuples:
		r = int(opt[t][8])
		if r < mode:
			no +=1.0
		else:
			yes+=1.0
	if yes == 0.0:
		return (True, '0')
	elif no == 0.0:
		return (True, '1')
	elif yes/(yes+no) >= 0.4:
		return (True, '1')
	else:
		return (False, '-1')

	#comp = 0
	#for t in tuples:
	#	r = int(t[7])
	#	if comp > 0:
	#		if r < mode:
	#			return False
	#	elif comp < 0:
	#		if r >= mode:
	#			return False
	#	elif comp == 0:
	#		if r >= mode:
	#			comp = 1
	#		else:
	#			comp = -1
	#return True

def gini(data):
	global mode
	if len(data) == 0:
		return 2
	else:
		C1 = []
		C2 = []
		for i in data:
			d = opt[i]
			if int(d[8]) < mode:
				C2.append(d)
			else:
				C1.append(d)
		return 1.0 - (math.pow((float(len(C1))/float(len(data))), 2.0) + math.pow((float(len(C2))/float(len(data))),2.0))
			

def divideSet(data, splitCon, val):
	N1 = []
	N2 = []
	if splitCon == "Gender":
		for i in data:
			d = opt[i]
			if d[0] == "F":
				N1.append(i)
			else:
				N2.append(i)
	elif splitCon == "Age":
		for i in data:
			d = opt[i]
			if int(d[1]) == val:
				N1.append(i)
			else:
				N2.append(i)
	elif splitCon == "Time":
		for i in data:
			d = opt[i]
			if int(math.floor(float(d[7])/10)) == val:
				N1.append(i)
			else:
				N2.append(i)
	elif splitCon == "LooseTime":
		for i in data:
			d = opt[i]
			if int(d[7]) == val:
				N1.append(i)
			else:
				N2.append(i)
	elif splitCon == "Occupation":
		for i in data:
			d = opt[i]
			if int(d[2]) == val:
				N1.append(i)
			else:
				N2.append(i)
	elif splitCon == "Zip":
		for i in data:
			d = opt[i]
			if int(d[3][0]) == val:# and int(d[3][1]) == (val[1]) and int(d[3][2]) == (val[2]):
				N1.append(i)
			else:
				N2.append(i)
	elif splitCon == "Year":
		for i in data:
			d = opt[i]
			if int(d[4]) == int(val):
				N1.append(i)
			else:
				N2.append(i)
	elif splitCon == "Decade":
		for i in data:
			d = opt[i]
			if int(d[4][0:3]) == int(val):
				N1.append(i)
			else:
				N2.append(i)
	elif splitCon == "MovieID":
		for i in data:
			d = opt[i]
			if int(d[6]) == val:
				N1.append(i)
			else:
				N2.append(i)
	elif splitCon == "Zip2":
		for i in data:
			d = opt[i]
			if int(d[3][0]) == val[0] and int(d[3][1]) == (val[1]):# and int(d[3][2]) == (val[2]):
				N1.append(i)
			else:
				N2.append(i)
	elif splitCon == "Zip3":
		for i in data:
			d = opt[i]
			if int(d[3][0]) == val[0] and int(d[3][1]) == (val[1]) and int(d[3][2]) == (val[2]):
				N1.append(i)
			else:
				N2.append(i)
	elif splitCon == "Zip4":
		for i in data:
			d = opt[i]
			if int(d[3][0]) == val[0] and int(d[3][1]) == (val[1]) and int(d[3][2]) == (val[2]) and int(d[3][3]) == val[3]:
				N1.append(i)
			else:
				N2.append(i)
	elif splitCon == "Zip5":
		for i in data:
			d = opt[i]
			if int(d[3][0]) == val[0] and int(d[3][1]) == (val[1]) and int(d[3][2]) == (val[2]) and int(d[3][3]) == val[3] and int(d[3][4]) == val[4]:
				N1.append(i)
			else:
				N2.append(i)
	else:
		for i in data:
			d = opt[i]
			if splitCon in d[5]:
				N1.append(i)
			else:
				N2.append(i)
	return (N1, N2)

def findGiniIndex(data, splitCon, val):
	(N1, N2) = divideSet(data,splitCon,val)
	a = float(len(N1))/float(len(data))
	b = float(len(N2))/float(len(data))
	if a == 0 or b == 0:
		return (4, 3)
	return (a*gini(N1)+b*gini(N2), (N1, N2))


def findSplitCon(data):
	currSmallest = 2.0
	splitCon = "Cannot find a proper splitting condition"
	value = -1.0
	val = -1.0
	split = None
	for sc in spCons:
		print sc
		if sc == "Age":
			for val in [1, 18, 25, 35, 45, 50, 56]:
				temp = findGiniIndex(data, sc, val)
				if temp[0] <= currSmallest:
					currSmallest = temp[0]
					splitCon = sc
					value = val
					split = temp[1]
		elif sc == "Occupation":
			for val in range(21):
				temp = findGiniIndex(data, sc, val)
				if temp[0] <= currSmallest:
					currSmallest = temp[0]
					splitCon = sc
					value = val
					split = temp[1]
		elif sc == "Zip":
			for val in range(10):
				#for val2 in range(10):
					#for val3 in range(10):
						temp = findGiniIndex(data, sc, val)#(val, val2, val3))
						if temp[0] < currSmallest:
							currSmallest = temp[0]
							splitCon = sc
							value = val
							split = temp[1]
		elif sc == "Decade":
			for val in ['191', '192', '193', '194','195', '196', '197', '198', '199', '200']:
				temp = findGiniIndex(data, sc, val)
				if temp[0] < currSmallest:
					currSmallest = temp[0]
					splitCon = sc
					value = val
					split = temp[1]
		elif sc == "Time":
			for val in range(303,332):
				temp = findGiniIndex(data, sc, val)
				if temp[0] < currSmallest:
					currSmallest = temp[0]
					splitCon = sc
					value = val
					split = temp[1]
		elif sc == "Year":
			for val in ['1919', '1920', '1921', '1922', '1923', '1924', '1925', '1926', '1927', '1928', '1929', '1930', '1931', '1932', '1933', '1934', '1935', '1936', '1937', '1938', '1939', '1940', '1941', '1942', '1943', '1944', '1945', '1946', '1947', '1948', '1949', '1950', '1951', '1952', '1953', '1954', '1955', '1956', '1957', '1958', '1959', '1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000']:
				temp = findGiniIndex(data, sc, val)
				if temp[0] < currSmallest:
					currSmallest = temp[0]
					splitCon = sc
					value = val
					split = temp[1]
		elif sc == "Zip2":
			for val in range(10):
				for val2 in range(10):
					#for val3 in range(10):
					temp = findGiniIndex(data, sc, (val, val2))
					if temp[0] < currSmallest:
						currSmallest = temp[0]
						splitCon = sc
						split = temp[1]
						value = (val,val2)
		elif sc == "LooseTime":
			for val in range(30,34):
				temp = findGiniIndex(data, sc, val)
				if temp[0] < currSmallest:
					currSmallest = temp[0]
					splitCon = sc
					value = val
					split = temp[1]
		else:
			temp = findGiniIndex(data, sc, val)
			if temp[0] <= currSmallest:
				currSmallest = temp[0]
				splitCon = sc
				value = -1
				split = temp[1]

	if splitCon == " Cannot find a proper splitting condition":
		sc = "MovieID"
		for val in range(4000):
			temp = findGiniIndex(data, sc, val)
			if temp < currSmallest:
				currSmallest = temp
				splitCon = sc
				value = val
	if splitCon == " Cannot find a proper splitting condition":
		sc = "Zip3"
		for val in range(10):
			for val2 in range(10):
				for val3 in range(10):
					temp = findGiniIndex(data, sc, (val, val2, val3))
					if temp < currSmallest:
						currSmallest = temp
						splitCon = sc
						value = (val,val2,val3)
	if splitCon == " Cannot find a proper splitting condition":
		sc = "Zip4"
		for val in range(10):
			for val2 in range(10):
				for val3 in range(10):
					for val4 in range(10):
							temp = findGiniIndex(data, sc, (val, val2, val3, val4))
							if temp < currSmallest:
								currSmallest = temp
								splitCon = sc
								value = (val,val2,val3, val4)
	if splitCon == " Cannot find a proper splitting condition":
		sc = "Zip5"
		for val in range(10):
			for val2 in range(10):
				for val3 in range(10):
					for val4 in range(10):
						for val5 in range(10):
							temp = findGiniIndex(data, sc, (val, val2, val3, val4, val5))
							if temp < currSmallest:
								currSmallest = temp
								splitCon = sc
								value = (val,val2,val3, val4, val5)

	return (splitCon, value, split)

def processNode(nodeIn):
	global totalUnHomo
	global mode
	global totalHomo
	print totalHomo+totalUnHomo
	if nodeIn.depth >= maxDepth:
		totalUnHomo += 1
		yes = 0.0
		no = 0.0
		for t in nodeIn.data:
			r = int(opt[t][8])
			if r < mode:
				no +=1.0
			else:
				yes+=1.0
		if yes/(yes+no) >= 0.4:
			nodeIn.label = "1"
		else:
			nodeIn.label = "0"
		return nodeIn
	if len(nodeIn.data) == 0:
		nodeIn.label = "0"
		return nodeIn
	(bl, lbl) = homogenous(nodeIn.data)
	if bl:
		totalHomo += 1
		nodeIn.label = lbl
		return nodeIn
	else:
		(sc, val, split) = findSplitCon(nodeIn.data)
		if sc == "Cannot find a proper splitting condition":
			totalUnHomo += 1
			yes = 0.0
			no = 0.0
			for t in nodeIn.data:
				r = int(opt[t][8])
				if r < mode:
					no +=1.0
				else:
					yes+=1.0
			if yes/(yes+no) >= 0.4:
				nodeIn.label = "1"
			else:
				nodeIn.label = "0"
			return nodeIn
		(N1, N2) = split
		#(N1, N2) = divideSet(nodeIn.data, sc, val)
		nodeIn.sc = sc
		nodeIn.val = val
		nodeIn.left = processNode(Node(N1, (nodeIn.depth+1)))
		nodeIn.right = processNode(Node(N2, (nodeIn.depth+1)))
		return nodeIn

def buildTree(treeIn):
	processNode(treeIn.root)

f = open('users.dat', 'r')
users = {}
for line in f:
	(uid,gen,age,occ,zipc) = line.strip('\n').split("::")
	users[uid] = [gen,age,occ,zipc]
f.close()

f = open('movies.dat', 'r')
movies = {}
for line in f:
	(mid, nameyear, genres) = line.strip('\n').split("::")
	genres = genres.split('|')
	gen = ["Action", "Adventure", "Animation", "Children's", "Comedy", "Crime", "Documentary", "Drama", "Fantasy", "Film-Noir", 
	"Horror", "Musical", "Mystery", "Romance", "Sci-Fi", "Thriller", "War", "Western"]
	x = 0
	#gfinal = []
	#for g in gen:
	#	if g in genres:
#			gfinal.append(True)
#		else:
#			gfinal.append(False)
#		x += 1
	year = nameyear[len(nameyear)-5:len(nameyear)-1]
	name = nameyear[0:len(nameyear)-7]
	movies[mid] = [year]+[genres]+[mid]
f.close()

inp = 'randtrain7' #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

f = open(inp, 'r')
tuples = []
i = 0
for line in f:
	(uid,mid,rating,time) = line.strip('\n').split("::")
	time = math.floor(float(time)/(31556900.0))
	tup = users[uid]+movies[mid]+[time, rating]
	opt[i] = tup
	tuples.append(i)
	i += 1
totalUnHomo = 0
totalHomo = 0
tree = DecisionTree(Node(tuples, 0))
buildTree(tree)

name = "tree555.p" #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

pickle.dump(tree, open(name, "wb" ))
pickle.dump(users, open("users.p", "wb"))
pickle.dump(movies, open("movies.p", "wb"))
print "Pickled"
print totalHomo

print "Input: "+str(inp)
print "Tree: "+str(name)



#print tree.root.left.right.right.left.sc
#print tree.root.left.right.right.left.val
#print "Right: "
#print tree.root.left.right.right.left.left.right.data
#print "Left:"
#print tree.root.left.right.right.left.left.left.data


#print tree.root.left

#so now we figure out the best splitting conditions right?


