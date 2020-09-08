file= input("Enter the file name to read:")
f= open(file,"r")
wordCount=0
for a in f:
    word= a.split()
    count= len(word)
    wordCount=wordCount+count
print("wordCount=",wordCount)