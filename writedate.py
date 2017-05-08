fh = open('date.txt','w')
for i in range(2000,2018):
    for j in range(1,13):
        fh.write(str(i)+'\t'+str(j)+'\n')

fh.close()