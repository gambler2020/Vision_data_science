#The class starts when a certain number of students (5) have joined. Until then, we wait.

#Write Python code to simulate this scenario.


student_join=0
class_started=False
while(class_started==False):
    if(student_join==5):
        class_started=True
    else:
        print("Please Wait... Still joined student is", student_join)
        n=input("Do you want to join the Class Press y/n: ")
        if(n=="y" or n=="Y"):
            student_join+=1
        else:
            print("Sorry you didn't Join the class!!!")
            continue
print("Lets begin the class")
