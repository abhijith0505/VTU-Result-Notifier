import os.path
import requests
import urllib2
from twilio.rest import TwilioRestClient
from lxml import etree, html

account_sid = " " # Your Account SID from www.twilio.com/console
auth_token  = " "  # Your Auth Token from www.twilio.com/console
usn = "" # Your USN

BASE_URL = 'http://results.vtu.ac.in'

	


if os.path.isfile('rctmp') == True:
	file = open('rctmp','r+')
	flag = file.read(1)
else:
	file = open('rctmp','w')
	file.write('0')
	file = open('rctmp','r+')
	flag = file.read(1)

if flag == "0":

	payload = {'rid': usn,'submit': 'SUBMIT'}
	
	headers = {
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:39.0) Gecko/20100101 Firefox/39.0',
		'X-Requested-With': 'XMLHttpRequest',
		'Host': 'results.vtu.ac.in',
		'Referer': 'http://results.vtu.ac.in/'
		}

    # xpath selector for subject name
	sub_xpath = '/html/body/table/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[2]/td[1]/table[2]/tbody/tr/td/table/tbody/tr[2]/td/table[2]/tr[{}]/td[{}]/i/text()'

    # xpath selector for subject external marks, internal marks and total marks
	sub_xpath2 = '/html/body/table/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[2]/td[1]/table[2]/tbody/tr/td/table/tbody/tr[2]/td/table[2]/tr[{}]/td[{}]/text()'

    # xpath selector for subject result
	sub_xpath3 = '/html/body/table/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[2]/td[1]/table[2]/tbody/tr/td/table/tbody/tr[2]/td/table[2]/tr[{}]/td[{}]/b/text()'


	response = requests.post(BASE_URL + '/vitavi.php', payload, headers=headers)
	tree = html.fromstring(response.content)
	print ("\n---------------------------------------\n")
	print ("Response code : ")
	print (response.status_code)

	# student details
	student_name_usn = tree.xpath('/html/body/table/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[2]/td[1]/table[2]/tbody/tr/td/table/tbody/tr[2]/td/b/text()')
	total_marks = tree.xpath('/html/body/table/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[2]/td[1]/table[2]/tbody/tr/td/table/tbody/tr[2]/td/table[3]/tr/td[4]/text()')
	semester = tree.xpath('/html/body/table/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[2]/td[1]/table[2]/tbody/tr/td/table/tbody/tr[2]/td/table[1]/tr/td[2]/b/text()')
	result = tree.xpath('/html/body/table/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[2]/td[1]/table[2]/tbody/tr/td/table/tbody/tr[2]/td/table[1]/tr/td[4]/b/text()')

	# subject details
	sub1 = tree.xpath(sub_xpath.format('2', '1'))
	sub1_external = tree.xpath(sub_xpath2.format('2', '2'))
	sub1_internal = tree.xpath(sub_xpath2.format('2', '3'))
	sub1_total = tree.xpath(sub_xpath2.format('2', '4'))
	sub1_result = tree.xpath(sub_xpath3.format('2', '5'))

	sub2 = tree.xpath(sub_xpath.format('3', '1'))
	sub2_external = tree.xpath(sub_xpath2.format('3', '2'))
	sub2_internal = tree.xpath(sub_xpath2.format('3', '3'))
	sub2_total = tree.xpath(sub_xpath2.format('3', '4'))
	sub2_result = tree.xpath(sub_xpath3.format('3', '5'))

	sub3 = tree.xpath(sub_xpath.format('4', '1'))
	sub3_external = tree.xpath(sub_xpath2.format('4', '2'))
	sub3_internal = tree.xpath(sub_xpath2.format('4', '3'))
	sub3_total = tree.xpath(sub_xpath2.format('4', '4'))
	sub3_result = tree.xpath(sub_xpath3.format('4', '5'))

	sub4 = tree.xpath(sub_xpath.format('5', '1'))
	sub4_external = tree.xpath(sub_xpath2.format('5', '2'))
	sub4_internal = tree.xpath(sub_xpath2.format('5', '3'))
	sub4_total = tree.xpath(sub_xpath2.format('5', '4'))
	sub4_result = tree.xpath(sub_xpath3.format('5', '5'))

	sub5 = tree.xpath(sub_xpath.format('6', '1'))
	sub5_external = tree.xpath(sub_xpath2.format('6', '2'))
	sub5_internal = tree.xpath(sub_xpath2.format('6', '3'))
	sub5_total = tree.xpath(sub_xpath2.format('6', '4'))
	sub5_result = tree.xpath(sub_xpath3.format('6', '5'))

	sub6 = tree.xpath(sub_xpath.format('7', '1'))
	sub6_external = tree.xpath(sub_xpath2.format('7', '2'))
	sub6_internal = tree.xpath(sub_xpath2.format('7', '3'))
	sub6_total = tree.xpath(sub_xpath2.format('7', '4'))
	sub6_result = tree.xpath(sub_xpath3.format('7', '5'))

	sub7 = tree.xpath(sub_xpath.format('8', '1'))
	sub7_external = tree.xpath(sub_xpath2.format('8', '2'))
	sub7_internal = tree.xpath(sub_xpath2.format('8', '3'))
	sub7_total = tree.xpath(sub_xpath2.format('8', '4'))
	sub7_result = tree.xpath(sub_xpath3.format('8', '5'))

	sub8 = tree.xpath(sub_xpath.format('9', '1'))
	sub8_external = tree.xpath(sub_xpath2.format('9', '2'))
	sub8_internal = tree.xpath(sub_xpath2.format('9', '3'))
	sub8_total = tree.xpath(sub_xpath2.format('9', '4'))
	sub8_result = tree.xpath(sub_xpath3.format('9', '5'))

	try:
		student_name_usn = student_name_usn[0].split('(')
		result = result[0].split()
		total_marks = total_marks[0].strip().replace(' ','')
		if len(result) == 5:
			result = result[1] + ' ' + result[2] + ' ' + result[3] + ' ' + result[4]
		elif len(result) == 3:
			result = result[1] + ' ' + result[2]
		elif len(result) == 2:
			result = result[1]  
				
		client = TwilioRestClient(account_sid, auth_token)

		message = client.messages.create(body="Res=" + result + ", " 
			+ sub1[0] + ":" + sub1_total[0] + ","
			+ sub2[0] + ":" + sub2_total[0] + ","
			+ sub3[0] + ":" + sub3_total[0] + ","
			+ sub4[0] + ":" + sub4_total[0] + ","
			+ sub5[0] + ":" + sub5_total[0] + ","
			+ sub6[0] + ":" + sub6_total[0] + ","
			+ sub7[0] + ":" + sub7_total[0] + ","
			+ sub8[0] + ":" + sub8_total[0] + ","
			+ "Total:" + total_marks,	#Messgage body you want to receive as SMS
			to=" ",   #Replace with your number to which you want to send the message
			from_=" ") # Replace with your Twilio number
		file = open('rctmp','w')
		file.write('1')

	except IndexError as e:
		donothing = 1