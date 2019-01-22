import urllib

def read_text():
	#FILE-LOCATION:
	#example LINUX: /home/USER/Desktop/file.txt
	#example Windows: C:\file.txt

	#Please change the path here 
	quotes = open(r"FILE-LOCATION")
	contents_of_file = quotes.read()
	quotes.close()
	check_profanity(contents_of_file)

def check_profanity(text_to_check):
	connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
	output = connection.read()
	if "false" in output:
		print("No curse words found!")
	elif "true" in output:
		print("Profanity Alert!")	
	else:
		print("can't scan the doc.")
	connection.close()

read_text()	
