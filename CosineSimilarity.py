'''
Implementing the Cosine Similarity Algorithm on all text files existing in a given folder.
It returns the pairwise similarity score of the documents.
'''
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import glob

#..use the list to get the links for the list of files ...#
listofFiles=[]
#...Stores the data from the each text file in the form of a string in each index...#
documents=[]

#...gets the list of text files in a particular folder...#
fileList=glob.glob("C:/Users/IBM_ADMIN/Desktop/GBS/learning docs/Baxter/documents/*.txt")

#...Loop through the files and creates the correct absolute path of the files...#
for f in fileList:
    listofFiles.append(f.replace("\\","/"))

    #...Gets the contents of the file in a string and append it the list...#
    for doc in listofFiles:
        print doc
	    with open(doc, 'r') as myfile:
	            #...reads the contents of the file and stores in a string...#
		            data=myfile.read().replace('\n', '')
			            documents.append(data)

				    #...Applying the TFidfVectorizer...#
				    vectorizer = TfidfVectorizer()
				    tfidf = vectorizer.fit_transform(documents)
				    #....getting list of feature words from the documents...#
				    words = vectorizer.get_feature_names()
				    print words
				    #...Applying the cosine similarity algorithm which returns a matrix of the similarity score of all the documents...#
				    similarity_matrix = cosine_similarity(tfidf)
				    print similarity_matrix
