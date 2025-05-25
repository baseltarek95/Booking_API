# Booking_API 
Overview
This repository contains the complete deliverables for the technical assessment task. The objective was to validate the booking API endpoint for functionality, performance, and reliability under various test scenarios.

Folder Structure
The project is organized as follows:

1.Test_Plan: Contains API testing plans in Word and PDF documents.

2.Postman_Collection: Contains Postman Booking Tests.postman_collection (JSON file) and screenshots.

3.Load_Testing_Jmeter: Contains JMeter JMX test plan scripts and CSV data files (payloads) valid and invalid.

4.CSV_and_Results: Contains test result files in CSV and JTL formats, execution reports in word document, and JSON files.

5.Clean_API_codes: Contains JMX and Python files for clean API code implementation.

5.Bonus_Advanced_Testing: Includes Database_Testing and Test_Idempotency folders with advanced tests.
Test_Idempotency folder which Contains Test Idempotency.postman_collection for advanced idempotency tests and Database_Testing folder Contains JTL, Database payload.CSV, and JMX files related to database testing. 

Usage Instructions
1. Postman Collection
Import the Postman collection file (Booking Tests.postman_collection.json) located in the Postman_Collection folder into Postman.

Run the requests to validate API functionality.

Review assertions to ensure response codes (201, 400, 409) and response schemas are correctly verified.

Check the screenshots in the Postman_Collection/Screenshots folder for expected results.

2. JMeter Load Test
Open the Load testing.jmx script found in the Load_Testing_Jmeter folder using Apache JMeter.

Make sure the CSV data file (payloads.csv) is in the correct relative location as configured in the test plan.

Execute the test with 100 threads (virtual users), a 5-minute duration, and a 30-second ramp-up period.

After the run, review performance metrics such as average and percentile response times, throughput, and error rates using the reports and raw data in the CSV_and_Results folder (Load Test summary.csv, Load Test result.jtl).

3. Bonus Advanced Tests
Idempotency Testing:
Run the Postman collection in the Test_Idempotency folder to verify that duplicate booking requests result in a 409 Conflict response and do not create multiple entries.

Database Consistency Testing:
Use the JMeter test plan and payload files located in the Database_Testing folder to validate that the number of successful booking creations matches the total records retrieved (no lost or missed entries).

Test results and execution reports are available in the CSV_and_Results folder (Test Idempotency.postman_test_run.json, Database consistency result1.jtl, summary CSV files).
