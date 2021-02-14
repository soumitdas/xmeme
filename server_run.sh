#!/bin/bash

# Run Server
cd backend
source env/bin/activate
cd app
PORT=8081
uvicorn main:app --host 0.0.0.0 --port $PORT --log-level error
