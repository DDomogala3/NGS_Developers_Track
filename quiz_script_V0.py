#quiz 
class Questions:
   # attr1 = "Question 1"
  
    attr1 = "question"

    def __init__(self,name):
        self.name = name
    
    def question_announcement(self,f):
        print("Please answer the following:\n {}".format(self.name))
        f = open(f,'a')
        f.write(input("")+"\n")
        
        

Q1 = Questions("What are ways to process a BAM file for variant calling?: \n")
Q2 = Questions("Extra Credit:\n Please examine this script, please explain how object oriented programming is a core tenent of bioinformatics.:")
#output = "answer.txt"
output = input("please provide your name: ") + ".txt"
Q1.question_announcement(output)
Q2.question_announcement(output)
