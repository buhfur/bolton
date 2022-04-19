import sys 



#seeing if taking a file as input will read it line from line 
# while using the data as system arguments 

one = ""
two  = "" 
# sys.argv[0] is the name of the script 
if len(sys.argv) > 1 :
     one =  sys.argv[1]
     two = sys.argv[2]
 

print(f"one is : {} ", one ) 
print(f"two is : {} ", two ) 
