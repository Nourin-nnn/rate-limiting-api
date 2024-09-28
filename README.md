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
