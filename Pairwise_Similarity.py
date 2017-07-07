'''
Implementing the Pairwise Similarity Algorithm on all text files existing in a given folder.
It returns the pairwise similarity score of the documents.
'''
from sklearn.feature_extraction.text import TfidfVectorizer
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
				    tfidf = TfidfVectorizer(tokenizer=lambda doc: doc, lowercase=False).fit_transform(documents)

				    #...Run the pairwise similarity algorithm...#
				    # no need to normalize, since Vectorizer will return normalized tf-idf
				    pairwise_similarity = tfidf * tfidf.T
				    print pairwise_similarity
