#!/bin/bash

echo "Starting Docker containers..."
docker-compose -f docker-compose-e2e.yml up -d

echo "Running tests..."
pytest automation/

echo "Tests completed."
