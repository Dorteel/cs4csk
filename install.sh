#!/bin/bash

# This script sets up a virtual environment and installs requirements.

# Exit immediately if something goes wrong
set -e

# Name of the virtual environment directory
VENV_DIR=".venv"

# Check for Python 3
if ! command -v python3 &> /dev/null; then
    echo "Python 3 not found. Please install it."
    exit 1
fi

# Create virtual environment
echo "Creating virtual environment in $VENV_DIR..."
python3 -m venv $VENV_DIR

# Activate virtual environment
echo "Activating virtual environment..."
source $VENV_DIR/bin/activate

# Upgrade pip, just in case you're using something from 2013
echo "Upgrading pip..."
pip install --upgrade pip

# Install requirements
if [ -f "requirements.txt" ]; then
    echo "Installing dependencies from requirements.txt..."
    pip install -r requirements.txt
else
    echo "No requirements.txt found."
    exit 1
fi

echo "Setup complete."