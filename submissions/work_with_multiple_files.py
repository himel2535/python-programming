

# import os
# files=os.listdir("submissions")

# list_extensions=[]
# for file in files:
#     extensions=file.split(".")
#     ext=extensions[-1]
#     list_extensions.append(ext)
  
## print(list_extensions)

#####find count without library:

# unique_ext=list(set((list_extensions)))
# # print(unique_ext)

# count_total={}
# for ex in unique_ext:
#     count=list_extensions.count(ex)
#     # print(f"for extnsns {ex} the total in count {count}")
#     count_total[ex]=count
# print(count_total)


##### find count with library:
import os
files=os.listdir("submissions")

list_extensions=[]
for file in files:
    extensions=file.split(".")
    ext=extensions[-1]
    list_extensions.append(ext)

from collections import Counter
count_using_library=Counter(list_extensions)
print(count_using_library)
