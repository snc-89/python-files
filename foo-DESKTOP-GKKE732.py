import re
import csv

f = open('tweets_GroundTruth.txt','r')
lines = f.readlines()

    # keep_list = ". "
    # lines[i] = re.sub(r'[^\w'+keep_list+']', '', lines[i][14:])




#write_file = "scores.csv"
# with open(write_file, "w") as output:
#     for line in lines:
#         output.write(line + ',\n')

print(lines[990][:14])