[![build status](
  http://img.shields.io/travis/collinpikeusa/repo/master.svg?style=flat)](
 https://travis-ci.org/username/Rheem)

Version: 1.0
Description:The system implemented currently is more of a proof of concept rather than an official system that will be deployed into production use.
	    Features that have been implemented is the automation of data migration from an S3 Bucket.
	    As soon as a new file is uploaded into the bucket it triggers the entire pipeline that causes the file to be moved into Redshift via Lambda code.
	    Then, from Redshift there is an API Gateway that triggers another Lambda code that queries data into the Reliance platform for further analytics
Features: S3 Bucket, Lambda, Redshift, and API Gateway implementation
Known bugs/issues: No implementation with EcoNet or Twilio text service
Source code: myPythonFile-API, myPythonFile-S3toRedshift, Reliance-Task_Profile, StartingOffPythonScript
