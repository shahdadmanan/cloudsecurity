

# PART 1
def unique_words(file):
	
	text_file = open(file, 'r')
	text = text_file.read()

	#cleaning
	text = text.lower()
	words = text.split()
	words = [word.strip('.,!;()[]" ') for word in words]
	words = [word.replace("'s", '') for word in words]
	words = ["".join(c for c in string if c.isalnum()) for string in words]

	#finding unique
	unique = []
	for word in words:
   	 	if word not in unique:
       			unique.append(word)

	#sort
	unique.sort()

	#print
        return(unique)



def count_the_articles(file):
	text_file = open(file, 'r')
        text = text_file.read()
        #cleaning
        text = text.lower()
        all_words = text.split() 
	articles= ["a", "the", "at", "run", "to","and","are","or","for","an","this"]
	count=0
	for i in all_words:
		for y in articles:
			if i==y:
				count=count +1
	print("count is: ", count)


def character_word_count(words):
	count={}
	for word in words:
		count[word] = len(word)
	return count

def starts_with_vow(words):
	count=0
	for word in words:
		if word != "":	
			if word[0] in "aeiou":
				count +=1
     	print(count)


def rare_words(words, file):
	text_file = open(file, 'r')
        text = text_file.read()

        #cleaning
        text = text.lower()
        ref = text.split()
        ref = [word.strip('.,!;()[]" ') for word in ref]
        ref = [word.replace("'s", '') for word in ref]
        ref = ["".join(c for c in string if c.isalnum()) for string in ref]
        print(ref)
	mylist =[]
	for i in words:
		if i not in ref:
			mylist.append(i)
	print(mylist)

def unused_words(ref,unique_words1, unique_words2,unique_words3):
	text_file = open(ref, 'r')
        text = text_file.read()

        #cleaning
        text = text.lower()
        ref = text.split()
        ref = [word.strip('.,!;()[]" ') for word in ref]
        ref = [word.replace("'s", '') for word in ref]
        ref = ["".join(c for c in string if c.isalnum()) for string in ref]
	#print(ref)
	print(len(ref))
	mylist=[]
	for i in ref:
		if i in unique_words1:
			if i not in unique_words2:
				if i not in unique_words3:
					mylist.append(i)
				
	print(mylist)
	print(len(mylist))
 

file= "/home/madhatter/midterm/Book1.txt"
unique_words(file)
l1= unique_words(file)
#print(l1)

#count_the_articles(file)
#print(sorted(l1, key=len))
#x=character_word_count(l)
#print(x)
#starts_with_vow(l1)
fileref= "/home/madhatter/midterm/20k.txt"
#rare_words(l1,fileref)
file2= "/home/madhatter/midterm/Book2.txt"
l2=unique_words(file2)
#count_the_articles(file)
file3= "/home/madhatter/midterm/Book3.txt"
l3=unique_words(file3)
unused_words(fileref,l1,l2,l3)
#count_the_articles(file)

