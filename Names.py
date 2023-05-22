
#Display names only with length 5 or more than 5
n=int(input("Enter how many names u want to enter :"))
names=[]
for i in range(n):
    name=input("Enter name: ")
    names.append(name)

print("Entered names are:",names)

print("Names which are greater than or equal to 5 are :")
for i in names:
    if len(i)>=5:
        print(i)

#list comprehension
# res=[i for i in names if len(i)>=5]
# for i in res:
#     print(i)


### output ###
C:\Users\Madhav\PycharmProjects\pythonProject\venv\Scripts\python.exe C:\Users\Madhav\PycharmProjects\pythonProject\main.py 
Enter how many names u want to enter :10
Enter name: madhav
Enter name: ram
Enter name: python
Enter name: java
Enter name: cpp
Enter name: docker
Enter name: john
Enter name: pradeep
Enter name: vishwa
Enter name: rockey
Entered names are: ['madhav', 'ram', 'python', 'java', 'cpp', 'docker', 'john', 'pradeep', 'vishwa', 'rockey']
Names which are greater than or equal to 5 are :
madhav  length is 6
python  length is 6
docker  length is 6
pradeep  length is 7
vishwa  length is 6
rockey  length is 6

Process finished with exit code 0

