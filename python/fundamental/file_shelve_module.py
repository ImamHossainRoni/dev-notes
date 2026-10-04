import shelve
var = shelve.open('/home/roni/Desktop/file/myfile.txt','a')
cats = ['lol','cool','fool']
var['cats'] = cats
var.close()
