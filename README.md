
# AITU Campus Shuttle and Mobility Data
Assignment 1 — Python Fundamentals for Data Streaming

This project simulates the processing of AITU campus shuttle events using Python. 
It includes event parsing and validation, generator-based stream processing,
a FastAPI endpoint, data analysis and automated tests.

## Project Files

- `shuttle.py` - contains the main event parsing, validation, stream generator and occupancy calculation functions.
- `api.py` - contains the FastAPI application and POST `/events` endpoint.
- `events.json` - contains the supplied shuttle events in JSON format.
- `test_shuttle.py` - contains automated test cases.
- `assignment.ipynb` - demonstrates event processing, streaming simulation, and data analysis.
- `README.md` - contains instructions for running the project.

## Requirements

The project requires Python and the following packages:

- pandas
- fastapi
- uvicorn
- pytest
- jupyter

Install the required packages using:

pip install pandas fastapi uvicorn pytest jupyter

## How to Run the Notebook

Open the project folder in Visual Studio Code.

Open:

assignment.ipynb

Select a Python kernel and run the notebook cells from top to bottom.

The notebook demonstrates:
- loading shuttle events;
- parsing and validation;
- generator-based stream processing;
- occupancy categories;
- passenger statistics and analysis.

## How to Run the FastAPI Application

Open a terminal in the project folder and run:

uvicorn api:app --reload

After the server starts, open the FastAPI documentation in a browser:

http://127.0.0.1:8000

Find the POST/events endpoint, click **Try it out**, enter a shuttle event in JSON format
and click **Execute**.

The API validates the event and returns whether it was accepted or rejected.
For valid events, it also calculates the occupancy category.

## Occupancy Categories

Passenger occupancy is classified as:

- 0-10 passengers: LOW
- 11-20 passengers: MEDIUM
- 21-30 passengers: HIGH
- More than 30 passengers: OVER_CAPACITY

## How to Run the Tests

Open a terminal in the project folder and run:

pytest -v

The tests check different parts of the program, including:

- valid event processing;
- negative passenger validation;
- invalid speed validation;
- invalid status validation;
- occupancy category boundaries;

A test passes when the actual program result matches the expected result.

## Running the Complete Project

1. Open the project folder in Visual Studio Code.
2. Install the required packages.
3. Run `assignment.ipynb` to view the processing and analysis.
4. Run `uvicorn api:app --reload` to start the API.
5. Open `http://127.0.0.1:8000/docs` to test POST `/events`.
6. Run `pytest -v` to execute the automated tests.
