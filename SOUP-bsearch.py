List1 = [0,1,2,3,4,5]
def Binary_Search (element, aList):
	StartPoint = 0
	EndPoint = len(aList)
	while StartPoint != EndPoint-1:
		MidPoint = (StartPoint + EndPoint) / 2
		if element > aList[MidPoint]:
			StartPoint = MidPoint
		elif element < aList[MidPoint]:
			EndPoint = MidPoint
		elif element == aList[MidPoint]:
			return MidPoint
	return -1
