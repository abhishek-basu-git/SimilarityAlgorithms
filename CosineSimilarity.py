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

	'''This function runs the cosine similarity algorithm between 2 files or 2 directories depeding on the input
	   @input: path1: File or directory path
	   @input: path2: File or directory path
	'''
	def cosineSimilarity(self,path1,path2):
		#..use the list to get the links for the list of files ...#
		listofFiles=[]
		#...Stores the data from the each text file in the form of a string in each index...#
		documents=[]
		documents1=[]
		documents2=[]

		#...gets the list of text files in a particular folder...#
		#fileList=glob.glob("C:/Users/IBM_ADMIN/Desktop/GBS/learning docs/Baxter/documents/*.txt")

		#Check if the path provided is a dir
		if os.path.isdir(path1):
			documents1=self.getListDocs(path1)
		else:
			with open(path1, 'r') as myfile:
				#...reads the contents of the file and stores in a string...#
				data=myfile.read().replace('\n', '').decode('utf-8')
				documents1.append(data)

		#Check if the path provided is a dir
		if os.path.isdir(path2):
			documents2=self.getListDocs(path2)
		else:
			with open(path2, 'r') as myfile:
				#...reads the contents of the file and stores in a string...#
				data=myfile.read().replace('\n', '').decode('utf-8')
				documents2.append(data)
		
		#stores all the documents in a list to be compared for similarity
		documents=documents1+documents2
		#print documents


		#...Applying the TFidfVectorizer...#
		vectorizer = TfidfVectorizer()
		tfidf = vectorizer.fit_transform(documents)
		#....getting list of feature words from the documents...#
		words = vectorizer.get_feature_names()
		#print words
		#...Applying the cosine similarity algorithm which returns a matrix of the similarity score of all the documents...#
		similarity_matrix = cosine_similarity(tfidf)
		print similarity_matrix

	'''This function gets the path of a dir and parses through the directory to find all the text files in that path.
	   It then gets the contents of each file and adds it to the list and returns that list
	   @input: path: directory path provided
	   @return: documentDetails: Python list containing every file content in each index
	'''
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


	'''This is the controller function
	   @input: path1: file or directory path
	   @input: path2: file or directory path
	'''
	def run(self,path1,path2):
		self.cosineSimilarity(path1,path2)


'''This is the main method of this script
   It takes input of the file paths and pass the inputs to the controller function
'''
if __name__ == "__main__":
	path1="C:/Users/IBM_ADMIN/Desktop/GBS/learning docs/Baxter/testdocuments"
	path2="C:/Users/IBM_ADMIN/Desktop/GBS/learning docs/Baxter/documents/HBR training.txt"
	CosineSimilarity().run(path1,path2)
