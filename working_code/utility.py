#!/usr/bin/env python2.7

from bs4 import BeautifulSoup as BS
import urllib2
import json

def get_class_schedule(class_code, semester="Spring 2019"):
	URL = "http://cs.slu.edu/academics/courses/csci" + str(class_code)
	
	req = urllib2.Request(url=URL)
	html = urllib2.urlopen(req)
	soup = BS(html)
	
	professor = ""
	days = ""
	hours = ""
	idx = 0
	for string in soup.stripped_strings:
		if idx == 3:
			break
		if idx == 2:
			days_and_hours = string.split()
			days = days_and_hours[0]
			hours = days_and_hours[1]
			idx += 1
		if idx == 1:
			professor = string
			idx += 1
		if string == semester:
			idx += 1
	data = {}
	if idx == 3:
		days = days.replace("M", "Monday ")
		days = days.replace("T", "Tuesday ")
		days = days.replace("W", "Wednesday ")
		days = days.replace("R", "Thursday ")
		days = days.replace("F", "Friday ")
		days = days.strip()

		hours = hours.replace("-", " to ")
		hours = hours.replace(":00", "")
		
		data['professor'] = professor
		data['days'] = days
		data['hours'] = hours
	json_string = json.dumps(data)

	return data

if __name__ == "__main__":		
	print(get_class_schedule(1020))
