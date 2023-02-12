

# general

# print('hello world,welcome',100)
# name='tim'
# print(name,'is a boy')
# print(name[2])
# name=input('input ur name: ')
# print(name,'is a boy')
# ch=input('input ur ch: ')
# w1=input('input ur w1: ')
# w2=input('input ur w2: ')
# print(ch.replace(w1,w2))


# lists

# djihene = ['djo', 'bari', 'hbs']
# print(djihene)
# print(len(djihene)) #we can mix different data type
# djihene2 = ['djo', 'bari', 'hbs']
# djihene.extend(djihene2)
# print(djihene)
# djihene.insert(1,'hh')
# print(djihene)
# djihene.remove('hh')
# print(djihene)
# list=[1,2,4,2,6,8]
# list.sort()
# print(list)
# list.pop()
# print(list)
# del list[2]
# print(list)

# def djihene(*name):
#     print(name[1])

# djihene('djihene','djihene','djihene')


# def djihene2(*name):
#     return 23

# print(djihene2())


# if 2>3:
#     print('djihene')
# elif 4<5 and 8<9:
#     print('hhh')
# else:
#     print('bahri')


# dic={
#     'djihene':'bahri'
# }
# print(dic)

# i=0
# while i<6 or i == 10:
#     print(i)
#     i=i+1


# for letter in 'hello':
#     print(letter)

#     list=['djihene','djihene']
# for values in list:
#     if values=='djihene':
#         break
#     print(values)


# for x in range(3,5):
#     print(x)
# else:
#     print('fin')


# try:
#     x=int(input('input an int'))
#     print(x)
# except:
#     print('fin')
# else:
#     print('done')


#file = open('djihene.txt','w')

# for lines in file.readlines():
#    print(lines)

# file.write('djihene')

# object oriented programming
# constructor
# class Myclass:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

# p1=Myclass('djihene',12)
# print(p1.name)

# inheritance
# from student import student

# class person(student):
#     pass

# p1=person()
# print(p1.name)

import student
student.say()



