import sys

# option = sys.argv[1]

# if option == '-a':
#     memo = sys.argv[2]
#     f = open('memo.txt','a')
#     f.write(memo)
#     f.write('\n')
#     f.close()
# elif option == '-v':
#     f = open('memo.txt')
#     memo = f.read()
#     f.close()
#     print(memo)

src = sys.argv[1]
dst = sys.argv[2]

f = open(src)
tab_content = f.read()
f.close()

space_content = tab_content.replace("a", "bb")
# print(space_content)

f = open(dst,'w')
f.write(space_content)
f.close()



