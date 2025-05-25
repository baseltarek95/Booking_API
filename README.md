# Booking_API 
Overview
This repository contains the complete deliverables for the technical assessment task. The objective was to validate the booking API endpoint for functionality, performance, and reliability under various test scenarios.

Folder Structure
The project is organized as follows:

1.Test_Plan: Contains API testing plans in Word and PDF documents.

2.Postman_Collection: Contains Postman request collection (JSON file) and screenshots.

3.Load_Testing_Jmeter: Contains JMeter JMX test plan and CSV data files (payloads).

4.CSV_and_Results: Contains test result files in CSV and JTL formats, execution reports, and JSON files.

5.Clean_API_codes: Contains JMX and Python files for clean API code implementation.

6.Test_Idempotency: Contains JSON files of Postman collections for advanced idempotency tests.

7.Database_Testing: Contains JTL, CSV, and JMX files related to database testing.

8.Bonus_Advanced_Testing: Includes Database_Testing and Test_Idempotency folders with advanced tests.

Usage Instructions
1. Postman Collection
Import the Postman collection file (Postman_collection.json) into Postman.
Observe the assertions and validate response codes and schemas.

2. JMeter Load Test
Open the load_test.jmx script in Apache JMeter.

Ensure the CSV data files (user_data.csv, place_data.csv) are in the correct relative path as configured.

Run the test with 100 threads, 5 minutes duration, and 30 seconds ramp-up.

Review aggregate report listeners for performance metrics. from the Load testing.jtl file with in the CSV_and_Results folder

3.Bonus Tests
Idempotency: Tests for ensuring duplicate booking requests do not create multiple entries.

Database Consistency: Validates that the total successful responses match the expected number of bookings.

