#PF-Prac-12
def generate_sentences(subjects,verbs,objects):
	#start writing your code here
	list=[]
	for i in subjects:
	    for j in verbs:
	        for k in objects:
	            list.append(i+" "+j+" "+k)
	return list 
	           
subjects=["I","You"]
verbs=["love", "play"]
objects=["Hockey","Football"]
print(generate_sentences(subjects,verbs,objects))

