inp=raw_input()
my_inp=['a','e','i','o','u']
my_inp1=['q','w','r','t','y','u','i','p','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
if(inp in my_inp):
	print "Vowel"
elif(inp in my_inp1):
	print "Consonant"
else:
	print "invalid input"
