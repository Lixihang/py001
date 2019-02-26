import shutil
#encoing
# file = open('地怨虞角都','w')
# file.write('你们的战斗经验和我差太远了')
# file.close()
# file = open('地怨虞角都','r')
# content = file.read()
# print(content)
# file.close()

# file = open('03.jpg','rb+')
# file2 = open('副本.jpg','wb+')
# content = file.read()
# file2.write(content)
# file.close()
# file2.close()

img1 = '03.jpg'
img2 = '03_1.jpg'
shutil.copyfile(img1,img2)

# file1 = open('03.jpg','rb+')
# file2 = open('副本.jpg','wb+')
# content = file1.read()
# file2.write(content)
# file1.close()
# file2.close()

