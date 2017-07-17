'''
Implementing the Cosine Similarity Algorithm on all text files existing in a given folder.
It returns the pairwise similarity score of the documents.
'''
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import glob
import numpy as np
import os


np.set_printoptions(threshold='nan')

class CosineSimilarity(object):

	def cosineSimilarity(self,path1,path2):
		#..use the list to get the links for the list of files ...#
		listofFiles=[]
		#...Stores the data from the each text file in the form of a string in each index...#
		documents=[]
		documents1=[]
		documents2=[]

		#...gets the list of text files in a particular folder...#
		#fileList=glob.glob("C:/Users/IBM_ADMIN/Desktop/GBS/learning docs/Baxter/documents/*.txt")

		if os.path.isdir(path1):
			documents1=self.getListDocs(path1)
		else:
			with open(path1, 'r') as myfile:
				#...reads the contents of the file and stores in a string...#
				data=myfile.read().replace('\n', '').decode('utf-8')
				documents1.append(data)
		if os.path.isdir(path2):
			documents2=self.getListDocs(path1)
		else:
			with open(path2, 'r') as myfile:
				#...reads the contents of the file and stores in a string...#
				data=myfile.read().replace('\n', '').decode('utf-8')
				documents2.append(data)

		documents=documents1+documents2


		#...Applying the TFidfVectorizer...#
		vectorizer = TfidfVectorizer()
		tfidf = vectorizer.fit_transform(documents)
		#....getting list of feature words from the documents...#
		words = vectorizer.get_feature_names()
		#print words
		#...Applying the cosine similarity algorithm which returns a matrix of the similarity score of all the documents...#
		similarity_matrix = cosine_similarity(tfidf)
		print similarity_matrix


	def getListDocs(self,path):
		documentsDetails=[]
		listofFiles=[]
		fileList=glob.glob(path+"/*.txt")
		#...Loop through the files and creates the correct absolute path of the files...#
		for f in fileList:
			listofFiles.append(f.replace("\\","/"))
		for doc in listofFiles:
			print doc
			with open(doc, 'r') as myfile:
				#...reads the contents of the file and stores in a string...#
				data=myfile.read().replace('\n', '').decode('utf-8')
				documentsDetails.append(data)
		return documentsDetails


	
	def run(self,path1,path2):
		self.cosineSimilarity(path1,path2)



if __name__ == "__main__":
	path1="C:/Users/IBM_ADMIN/Desktop/GBS/learning docs/Baxter/documents/HBR training.txt"
	path2="C:/Users/IBM_ADMIN/Desktop/GBS/learning docs/Baxter/documents"
	CosineSimilarity().run(path1,path2)
