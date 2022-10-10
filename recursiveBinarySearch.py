#binary search in python
#recursive binary search

def binarySearch(List,l,r,x):
 m=l+(r-l)//2
 if(r>=l):
 if(List[m]==x):
 return m
 elif(x<List[m]):
 return binarySearch(List,l,m-1,x)
 else:
 return binarySearch(List,m+1,r,x)
 return -1

List=[2,5,6,8,9]
search=int(input("enter the element you have to search:"))
res=binarySearch(List,0,(len(List)-1),search)
if(res!=-1):
 print("element found at index",res)
else:
 print("element not found")
