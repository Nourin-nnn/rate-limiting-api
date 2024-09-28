# Rate Limiting API

This is a FastAPI application that implements a simple rate limiting mechanism using Redis. The API allows clients to fetch data while limiting the number of requests that can be made in a given time frame.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup](#setup)
  - [Set Up Virtual Environment](#set-up-virtual-environment)
  - [Install Dependencies](#install-dependencies)
  - [Configuration](#configuration)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [Screenshots](#screenshots)
- [License](#license)

## Features

- Rate limiting for IP addresses
- Simple RESTful API
- Built using FastAPI and Redis

## Technologies Used

- FastAPI
- Redis
- Python

## Setup

### Set Up Virtual Environment

Create the Virtual Environment:

```bash
python -m venv venv
```

This command creates a directory named venv in the project folder, which will contain the necessary files for the virtual environment.

Activate the Virtual Environment:

For Git Bash (MINGW64) on Windows:

```bash
source venv/Scripts/activate
```
For Command Prompt (CMD) on Windows:

```bash
venv\Scripts\activate
```
For PowerShell on Windows:

```bash
.\venv\Scripts\Activate
```
For macOS or Linux:

```bash
source venv/bin/activate
```
After activation, terminal prompt will change to show the virtual environment's name, indicating that we are now working inside it.

### Install Dependencies

With the virtual environment activated, run:

```bash
pip install -r requirements.txt
```
### Configuration

Before running the application, we have to make sure to configure the Redis client in main.py:

```python
redis_client = redis.StrictRedis(host='your-redis-host', port=your-redis-port, db=0, decode_responses=True)
# Replace your-redis-host and your-redis-port with the appropriate values for your Redis instance.
```

## Running the Application

To start the FastAPI application, run:

```bash
uvicorn main:app --reload
```
We can access the API at http://localhost:8000.

## API Endpoints

GET /data: Fetches data and checks the rate limit for the IP address.
GET /: Welcome message.

## Screenshots

- Welcome Message Example ![Welcome Message](Images/1.png)
- API Response Example ![API Response](Images/2.png)
- Rate Limit Exceeded Example ![Rate Limit Exceeded](Images/3.png)

## License

This project does not have a specific license. Feel free to use and modify it as you wish.


### Instructions to Update the README

1. **Replace** the `path/to/your/screenshotX.png` with the actual paths to your screenshot files.
2. Make sure to provide any necessary instructions regarding the Redis configuration.

