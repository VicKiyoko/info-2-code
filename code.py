import math as m

# als Listen von Zahlen wird K3 aus K1 und K2 gebildet
def resmerge(lispos0, lisneg0, elem):
	lispos = []
	lispos.extend(lispos0)
	lisneg = []
	lisneg.extend(lisneg0)
	del lispos[lispos.index(elem)]
	del lisneg[lisneg.index(-elem)]
	lispos.extend(lisneg)
	return lispos

# Uebertragung aller Aussagen als Zahlen in eine Menge (ohne Negation)
def fullset(K):
	allelems = []
	for alist in K:
		for elem in alist:
			if not m.fabs(elem) in allelems:
				allelems.append(m.fabs(elem))
	return allelems

# Anwendung von resmerge auf die entsprechenden Listen
def resmergeall(poslists, neglists, elem):
	morelists = []
	for alist in poslists:
		for aneglist in neglists:
			if not areidentical(alist, aneglist):
				morelists.append(resmerge(alist, aneglist, elem))
	return morelists

# Erweiterung mittels Hilfsfunktionen von Res^(n) zu Res^(n+1)
def addResolvent(K):
	allelems = fullset(K)
	out = []
	out.extend(K)
	for elem in allelems:
		poslists = []
		neglists = []
		for alist in K:
			if elem in alist:
				poslists.append(alist)
			if -elem in alist:
				neglists.append(alist)
		out.extend(resmergeall(poslists, neglists, elem))
	return cleanup(transSets(out))

# Menge / Zahlenlisten in Liste werden sortiert
def sortcontainedlists(S):
	for alist in S:
		alist.sort()

# Duplikate aus Liste (von Listen) entfernen
def cleanup(L):
	outL = []
	sortcontainedlists(L)
	for alist in L:
		if alist not in outL:
			outL.append(alist)
	return outL


# Komplement von S1 in S2
def removeSetinSet(S1, S2):
	if containslists(S1) and containslists(S2):
		S0 = []
		S0.extend(S2)
		for alist in S1:
			if alist in S0:
				del S0[S0.index(alist)]
		return S0

# Duplikate aus Zahlen- / Aussagenliste entfernen (umstaendlich)
def applySetproperties(L):
	lilS = set()
	newL = []
	for i in L:
		lilS.add(i)
	for j in lilS:
		newL.append(j)
	return newL

# Globale Anwendung von applySetproperties
def transSets(L):
	newL = []
	for alist in L:
		newl = applySetproperties(alist)
		newL.append(newl)
	return newL

# def len2(L):
# 	outL = []
# 	for alist in L:
# 		if len(alist) < 3:
# 			outL.append(alist)
# 	return outL


K = [[1,-2],[1,2,3],[-1,3],[-1,-2,-3],[2,-3]]
Res = K
i = 1
while not ([] in Res):
	print(i)
	i += 1
	Res = addResolvent(Res)
	print(Res)
	print()