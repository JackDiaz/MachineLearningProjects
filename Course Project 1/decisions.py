import pickle
import math

mode = 4

class Node:
	def __init__(self, dataIn):
		self.data = dataIn
		self.left = None
		self.right = None

class DecisionTree:
	def __init__(self, rootIn):
		self.root = rootIn



def traverseTree(nodeIn, d):
	if nodeIn.left is None:
		if nodeIn.right is None:
			return nodeIn.label
	splitCon = nodeIn.sc
	N1 = []
	N2 = []
	if splitCon == "Gender":
			if d[0] == "F":
				return traverseTree(nodeIn.left, d)
			else:
				return traverseTree(nodeIn.right, d)
	elif splitCon == "Age":
			if int(d[1]) == nodeIn.val:
				return traverseTree(nodeIn.left, d)
			else:
				return traverseTree(nodeIn.right, d)
	elif splitCon == "Time":
			if int(math.floor(float(d[7])/10)) == nodeIn.val:
				return traverseTree(nodeIn.left, d)
			else:
				return traverseTree(nodeIn.right, d)
	elif splitCon == "LooseTime":
			if int(d[7]) == nodeIn.val:
				return traverseTree(nodeIn.left, d)
			else:
				return traverseTree(nodeIn.right, d)
	elif splitCon == "Occupation":
			if int(d[2]) == nodeIn.val:
				return traverseTree(nodeIn.left, d)
			else:
				return traverseTree(nodeIn.right, d)
	elif splitCon == "Zip":
			if int(d[3][0]) == nodeIn.val:# and int(d[3][1]) == (val[1]) and int(d[3][2]) == (val[2]):
				return traverseTree(nodeIn.left, d)
			else:
				return traverseTree(nodeIn.right, d)
	elif splitCon == "Year":
			if int(d[4]) == int(nodeIn.val):
				return traverseTree(nodeIn.left, d)
			else:
				return traverseTree(nodeIn.right, d)
	elif splitCon == "Decade":
			if int(d[4][0:3]) == int(nodeIn.val):
				return traverseTree(nodeIn.left, d)
			else:
				return traverseTree(nodeIn.right, d)
	elif splitCon == "MovieID":
			if int(d[6]) == nodeIn.val:
				return traverseTree(nodeIn.left, d)
			else:
				return traverseTree(nodeIn.right, d)
	elif splitCon == "Zip2":
			if int(d[3][0]) == nodeIn.val[0] and int(d[3][1]) == (nodeIn.val[1]):# and int(d[3][2]) == (val[2]):
				return traverseTree(nodeIn.left, d)
			else:
				return traverseTree(nodeIn.right, d)
	elif splitCon == "Zip3":
			if int(d[3][0]) == nodeIn.val[0] and int(d[3][1]) == (nodeIn.val[1]) and int(d[3][2]) == (nodeIn.val[2]):
				return traverseTree(nodeIn.left, d)
			else:
				return traverseTree(nodeIn.right, d)
	elif splitCon == "Zip4":
			if int(d[3][0]) == nodeIn.val[0] and int(d[3][1]) == (nodeIn.val[1]) and int(d[3][2]) == (nodeIn.val[2]) and int(d[3][3]) == nodeIn.val[3]:
				return traverseTree(nodeIn.left, d)
			else:
				return traverseTree(nodeIn.right, d)
	elif splitCon == "Zip5":
			if int(d[3][0]) == nodeIn.val[0] and int(d[3][1]) == (nodeIn.val[1]) and int(d[3][2]) == (nodeIn.val[2]) and int(d[3][3]) == nodeIn.val[3] and int(d[3][4]) == nodeIn.val[4]:
				return traverseTree(nodeIn.left, d)
			else:
				return traverseTree(nodeIn.right, d)
	else:
			if splitCon in d[5]:
				return traverseTree(nodeIn.left, d)
			else:
				return traverseTree(nodeIn.right, d)




tree = pickle.load(open("tree420.p", "rb" ))
users = pickle.load(open("users.p", "rb"))
movies = pickle.load(open("movies.p", "rb"))
spCons = ["Gender", "Age", "Occupation", "Zip", "Year", "Action", "Adventure", "Animation", 
"Children's", "Comedy", "Crime", "Documentary", "Drama", "Fantasy", "Film-Noir", 
"Horror", "Musical", "Mystery", "Romance", "Sci-Fi", "Thriller", "War", "Western", "MovieID"]

f = open('testing3.dat', 'r')
g = open('output32.dat', 'w')
#h = open('out2', 'w')
tuples = []
tp = 0.0
tn = 0.0
fp = 0.0
fn = 0.0
for line in f:
	(uid,mid,time) = line.strip('\n').split("::")
	time = math.floor(float(time)/(31556900.0))
	tup = users[uid]+movies[mid]+[time]
	out = traverseTree(tree.root, tup)
	if int(out) < 1:
		print out
	g.write(line.strip('\n')+'::'+out+'\n')

g.close()
f.close()



