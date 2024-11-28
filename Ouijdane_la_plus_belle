-- Initial exploration and mind mapping of the data schema.
-- Checking the bakery security logs for activity on the morning of the theft.
-- Goal: Narrow down the timeline and identify potential suspects.
SELECT *
FROM bakery_security_logs
WHERE day = 28 AND month = 7 AND year = 2023;

-- No exact time for the theft yet, so following Eugene's lead in interview 161. (Didn't read crimescene reports)
-- Hypothesis: Eugene's words might reveal when the thief withdrew money.
SELECT *
FROM bakery_security_logs
JOIN people ON people.license_plate = bakery_security_logs.license_plate
WHERE name = 'Eugene';

-- Discovery: Eugene didn’t go to the bakery that day,I assume he walked there (im so stupid he literally didn't say he went there).
-- Moving on to check ATM transactions for withdrawals on Leggett Street.
SELECT *
FROM atm_transactions
WHERE day = 28
  AND month = 7
  AND year = 2023
  AND atm_location = 'Leggett Street'
  AND transaction_type = 'withdraw';

-- Create an initial list of suspects based on ATM withdrawals.
SELECT name
FROM people
JOIN bank_accounts ON bank_accounts.person_id = people.id
JOIN atm_transactions ON atm_transactions.account_number = bank_accounts.account_number
WHERE day = 28
  AND atm_location = 'Leggett Street'
  AND transaction_type = 'withdraw';

-- Cross-reference suspects with those who exited the bakery on July 28.
SELECT people.name, bakery_security_logs.*
FROM bakery_security_logs
JOIN people ON people.license_plate = bakery_security_logs.license_plate
JOIN bank_accounts ON bank_accounts.person_id = people.id
JOIN atm_transactions ON atm_transactions.account_number = bank_accounts.account_number
WHERE atm_transactions.day = 28
  AND atm_transactions.atm_location = 'Leggett Street'
  AND atm_transactions.transaction_type = 'withdraw'
ORDER BY hour;

-- Check for short phone calls made right after leaving the bakery.
-- From interview (162): The thief might’ve contacted an accomplice to coordinate the escape.
SELECT phone_calls.*, people.name
FROM bakery_security_logs
JOIN phone_calls ON phone_calls.caller = people.phone_number
JOIN people ON people.license_plate = bakery_security_logs.license_plate
JOIN bank_accounts ON bank_accounts.person_id = people.id
JOIN atm_transactions ON atm_transactions.account_number = bank_accounts.account_number
WHERE atm_transactions.day = 28
  AND atm_transactions.atm_location = 'Leggett Street'
  AND atm_transactions.transaction_type = 'withdraw'
  AND phone_calls.month = 7
  AND phone_calls.day = 28
  AND phone_calls.duration < 60
ORDER BY people.name;

-- Narrowing the suspect list further to three individuals.
-- Cross-referencing with flight records to identify anyone who fled town the next day.
SELECT DISTINCT people.name, flights.*
FROM bakery_security_logs
JOIN flights ON flights.id = passengers.flight_id
JOIN passengers ON passengers.passport_number = people.passport_number
JOIN phone_calls ON phone_calls.caller = people.phone_number
JOIN people ON people.license_plate = bakery_security_logs.license_plate
JOIN bank_accounts ON bank_accounts.person_id = people.id
JOIN atm_transactions ON atm_transactions.account_number = bank_accounts.account_number
WHERE atm_transactions.day = 28
  AND atm_transactions.atm_location = 'Leggett Street'
  AND atm_transactions.transaction_type = 'withdraw'
  AND bakery_security_logs.activity = 'exit'
  AND bakery_security_logs.day = 28
  AND phone_calls.month = 7
  AND phone_calls.day = 28
  AND phone_calls.duration < 60
  AND flights.day = 29
ORDER BY flights.hour;

-- My stupid ass finally reads the crimescene reports.
-- Discovery: The crime occurred at 10:15 AM.
-- Refining the queries to include this key detail and pinpoint the thief.
SELECT DISTINCT people.name, flights.*
FROM bakery_security_logs
JOIN flights ON flights.id = passengers.flight_id
JOIN passengers ON passengers.passport_number = people.passport_number
JOIN phone_calls ON phone_calls.caller = people.phone_number
JOIN people ON people.license_plate = bakery_security_logs.license_plate
JOIN bank_accounts ON bank_accounts.person_id = people.id
JOIN atm_transactions ON atm_transactions.account_number = bank_accounts.account_number
WHERE atm_transactions.day = 28
  AND atm_transactions.atm_location = 'Leggett Street'
  AND atm_transactions.transaction_type = 'withdraw'
  AND bakery_security_logs.activity = 'exit'
  AND bakery_security_logs.hour = 10
  AND bakery_security_logs.minute < 25
  AND bakery_security_logs.day = 28
  AND phone_calls.month = 7
  AND phone_calls.day = 28
  AND phone_calls.duration < 60
  AND flights.day = 29
ORDER BY flights.hour;

-- Consolidating all evidence to reveal the thief and accomplice, and their escape plan.
SELECT DISTINCT people.name, flights.*
FROM bakery_security_logs
JOIN flights
    ON flights.id = passengers.flight_id
JOIN passengers
    ON passengers.passport_number = people.passport_number
JOIN phone_calls
    ON phone_calls.caller = people.phone_number
JOIN people
    ON people.license_plate = bakery_security_logs.license_plate
JOIN bank_accounts
    ON bank_accounts.person_id = people.id
JOIN atm_transactions
    ON atm_transactions.account_number = bank_accounts.account_number
WHERE atm_transactions.day = 28
  AND atm_transactions.atm_location = 'Leggett Street'
  AND atm_transactions.transaction_type = 'withdraw'
  AND bakery_security_logs.activity = 'exit'
  AND bakery_security_logs.hour = 10
  AND bakery_security_logs.minute < 25
  AND bakery_security_logs.day = 28
  AND phone_calls.month = 7
  AND phone_calls.day = 28
  AND phone_calls.duration < 60
  AND flights.day = 29
ORDER BY flights.hour LIMIT 1;

-- Identify who Bruce called after leaving the bakery.
-- Hypothesis: The thief contacted an accomplice for coordination.
SELECT phone_calls.receiver, called_person.name AS call_receiver_name
FROM phone_calls
JOIN people AS caller ON phone_calls.caller = caller.phone_number
JOIN people AS called_person ON phone_calls.receiver = called_person.phone_number
WHERE caller.name = 'Bruce'
  AND phone_calls.day = 28
  AND phone_calls.month = 7
  AND phone_calls.year = 2023
  AND phone_calls.duration < 60;

-- Determine Bruce’s flight destination by linking to the destination airport.
-- Goal: Identify where Bruce fled to after committing the theft.
SELECT flights.id, airports.city AS destination_city
FROM flights
JOIN airports ON flights.destination_airport_id = airports.id
JOIN passengers ON flights.id = passengers.flight_id
JOIN people ON passengers.passport_number = people.passport_number
WHERE people.name = 'Bruce'
  AND flights.day = 29
  AND flights.month = 7
  AND flights.year = 2023
ORDER BY flights.hour, flights.minute
LIMIT 1;
