def graphColoring(graph,m,finalcolor):
	finalcolor[0]='R'
	tempcolor=[]

	for i in range(len(graph)):
		tempcolor=['R','G','B']
		if i !=0:
			for j in range(len(graph[i])):				
					if graph[i][j]==1 and finalcolor[j]!='':
						if tempcolor.count(finalcolor[j])>=1:		
							tempcolor.remove(finalcolor[j])				
			print("temp color for node {}: {}".format(i+1,tempcolor))			
			finalcolor[i]=tempcolor[0]
			print("final colors: {}".format(finalcolor))
		print("next row")
	for i in range(len(finalcolor)):
		print("node {} is given color : {}".format(i+1,finalcolor[i]))

if __name__ == '__main__':
	graph = [
		[ 0, 1, 1, 1 ],
		[ 1, 0, 1, 0 ],
		[ 1, 1, 0, 1 ],
		[ 1, 0, 1, 0 ],
	]
	m = 3

	finalcolor = ['' for i in range(4)]
	graphColoring(graph, m, finalcolor)