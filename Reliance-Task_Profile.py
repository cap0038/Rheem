import ast
profile = publicWebServiceProfilesManager.getRESTfulProfile("ECONET_D")
search = profile.getOperation("getAllRecords")
response = search.invoke()
raw_data = response.getAsString()
#Rutilities.debug("test")
#Rutilities.debug(raw_data)
output = raw_data.split('"output" : {\r\n    "c" :')[1]
#lastName = output['c']
#Rutilities.debug(output)
i = 0
myFullArray = []
for name in output.split(','):
 #Rutilities.debug(name.trim())
 newStr = name.replace("' ", "")
 newStr1 = newStr.replace("'", "")
 newStr2 = newStr1.replace("}", "")
 newStr3 = newStr2.replace("\r\n  \r\n", "")
 Rutilities.debug(newStr3)
 myFullArray.append(newStr3.strip())

 #if '}' in name:
 # break
 #else:
 # query = "Select ECONET_DATA_ID FROM VACATION7.ECONET_DATA WHERE ID_4 = '" + name + "'"
 # documents = thisUser.getApplication("VACATION7").getDocumentKeysByQuery("ECONET_DATA_D", query)
 # if len(documents) == 0:
 #  doc = thisUser.getApplication("VACATION7").newDocument("ECONET_DATA_D", "ACTIVE_13_D")
 #  doc.setFieldValue("NAME_20_D", name)
 #  doc.getPhase().reassign([6465], [], false)
 #  doc.save()
 #  doc.close()
 # else:
 #  for doc in documents:
 #   doc = thisUser.getApplication("VACATION7").getDocumentInEditMode(doc)
 #   doc.save()
 #   doc.close()
Rutilities.debug(myFullArray)
Rutilities.debug(len(myFullArray)/7)
for rowNum in range(0,len(myFullArray)/7):
 Rutilities.debug("KEY" + myFullArray[(rowNum*7) + 0])
 query = "Select ECONET_DATA_ID FROM VACATION7.ECONET_DATA WHERE ID_4 = '" + myFullArray[(rowNum*7) + 0] + "'"
 documents = thisUser.getApplication("VACATION7").getDocumentKeysByQuery("ECONET_DATA_D", query)
 if len(documents) == 0:
  doc = thisUser.getApplication("VACATION7").newDocument("ECONET_DATA_D", "ACTIVE_13_D")
  doc.setFieldValue("ID_4_D", int(myFullArray[(rowNum*7) + 0]))
  doc.setFieldValue("NAME_20_D", myFullArray[(rowNum*7) + 1])
  doc.setFieldValue("USER_ID_1_D", int(myFullArray[(rowNum*7) + 2]))
  doc.setFieldValue("CITY_6_D", myFullArray[(rowNum*7) + 3])
  doc.setFieldValue("STATE_15_D", myFullArray[(rowNum*7) + 4])
  doc.setFieldValue("TIMEZONE_GMT_OFFSET_D", myFullArray[(rowNum*7) + 5])
  doc.setFieldValue("ZIP_CODE_6_D", myFullArray[(rowNum*7) + 6])
  doc.getPhase().reassign([6465], [], false)
  doc.save()
  doc.close()
 else:
  for doc in documents:
   doc = thisUser.getApplication("VACATION7").getDocumentInEditMode(doc)
   doc.save()
   doc.close()