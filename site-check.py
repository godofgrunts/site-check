#!/usr/bin/env python

import urllib, smtplib, email
from datetime import datetime
from email.mime.text import MIMEText

websites = [INSERT WEBSITES] #FORMAT ["http://www.google.com", "http://www.facebook.com"]



for site in websites:
	try:
		status = urllib.urlopen(site).getcode()
		if status == 200:
			filename = /path/to/uptime.txt"
			currentTime = str(datetime.now())
			msg = "%s Reported up at %s" % (site, currentTime)
			f = open(filename, 'a')
			f.write(str(msg) + "\n")
			f.close()
			
		else:
			#print "Error! Sending email!"
			subjectline = "Subject:Error! %s Status is being reported as %s" % (site, status)
			fromaddr = "EXAMPLE@GMAIL.COM" #change this
			tos = ["ADMIN@EXAMPLE.COM", "ADMIN2@EXAMPLE.COM"] #change these
			toaddr = ", ".join(tos)
			header = 'To:' + toaddr + '\n' + 'From:' + fromaddr + '\n' + subjectline + '\n'
			errors = """


*****************************************************************************

4xx Client Error
The 4xx class of status code is intended for cases in which the client seems to have erred. Except when responding to a HEAD request, the server should include an entity containing an explanation of the error situation, and whether it is a temporary or permanent condition. These status codes are applicable to any request method. User agents should display any included entity to the user.

400 Bad Request
401 Unauthorized (RFC 7235)
403 Forbidden
404 Not Found
405 Method Not Allowed
406 Not Acceptable
407 Proxy Authentication Required (RFC 7235)
408 Request Timeout
409 Conflict
410 Gone
411 Length Required
412 Precondition Failed (RFC 7232)
413 Payload Too Large (RFC 7231)
414 Request-URI Too Long
415 Unsupported Media Type
416 Requested Range Not Satisfiable (RFC 7233)
417 Expectation Failed
421 Misdirected Request (RFC 7540)
422 Unprocessable Entity (WebDAV; RFC 4918)
423 Locked (WebDAV; RFC 4918)
424 Failed Dependency (WebDAV; RFC 4918)
426 Upgrade Required
428 Precondition Required (RFC 6585)
429 Too Many Requests (RFC 6585)
431 Request Header Fields Too Large (RFC 6585)
440 Login Timeout (Microsoft)
444 No Response (Nginx)
449 Retry With (Microsoft)
450 Blocked by Windows Parental Controls (Microsoft)
451 Unavailable For Legal Reasons (Internet draft)
451 Redirect (Microsoft)
494 Request Header Too Large (Nginx)
495 Cert Error (Nginx)
496 No Cert (Nginx)
497 HTTP to HTTPS (Nginx)
498 Token expired/invalid (Esri)
499 Client Closed Request (Nginx)
499 Token required (Esri)

*****************************************************************************

5xx Server Error
The server failed to fulfill an apparently valid request.
Response status codes beginning with the digit "5" indicate cases in which the server is aware that it has encountered an error or is otherwise incapable of performing the request. Except when responding to a HEAD request, the server should include an entity containing an explanation of the error situation, and indicate whether it is a temporary or permanent condition. Likewise, user agents should display any included entity to the user. These response codes are applicable to any request method.

500 Internal Server Error
501 Not Implemented
502 Bad Gateway
503 Service Unavailable
504 Gateway Timeout
505 HTTP Version Not Supported
506 Variant Also Negotiates (RFC 2295)
507 Insufficient Storage (WebDAV; RFC 4918)
508 Loop Detected (WebDAV; RFC 5842)
509 Bandwidth Limit Exceeded (Apache bw/limited extension)
510 Not Extended (RFC 2774)
511 Network Authentication Required (RFC 6585)
520 Unknown Error
522 Origin Connection Time-out
598 Network read timeout error (Unknown)
599 Network connect timeout error (Unknown)

*****************************************************************************
"""
			msg = header + '\n Please manually check the website!\n ' + errors
			s = smtplib.SMTP('smtp.gmail.com:587') #change this if not using gmail
			s.starttls()
			s.login("EXAMPLE@GMAIL.COM", "PASSWORD") #change these
			s.sendmail(fromaddr, tos, msg)
			s.quit()
			filename = "/path/to/down.txt"
			currentTime = str(datetime.now())
			msg1 = "%s was reported down at %s!" % (site, currentTime)
			f = open(filename, 'a')
			f.write(str(msg2) + "\n")
			f.close()
			
	except Exception as e:
		subjectline = "Subject:Script Failed while checking %s!" % site
		fromaddr = "EXAMPLE@GMAIL.COM"
		toaddr = "ADMIN1@EXAMPLE.COM"
		header = 'To:' + toaddr + '\n' + 'From:' + fromaddr + '\n' + subjectline + '\n'
		msg = header + str(e)
		s = smtplib.SMTP('smtp.gmail.com:587') #change if not using gmail
		s.starttls()
		s.login("EXAMPLE@GMAIL.COM", "PASSWORD")
		s.sendmail(fromaddr, toaddr, msg)
		s.quit()
		filename = "/path/to/errors.txt"
		currentTime = str(datetime.now())
		msg1 = "%s threw an error at %s error message was " % (site, currentTime)
		msg2 = msg1 + str(e)
		f = open(filename, 'a')
		f.write(str(msg2) + "\n")
		f.close()
