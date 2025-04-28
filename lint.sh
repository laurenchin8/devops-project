#!/bin/sh

echo "Installing pylint..."
sudo apt-get install -y -q pylint

echo "Linting mypl_error.py file..."
pylint ./mypl_error.py

echo "Linting mypl_iowrapper.py file..."
pylint ./mypl_iowrapper.py

echo "Linting mypl_lexer.py file..."
pylint ./mypl_lexer.py

echo "Linting mypl_token.py file..."
pylint ./mypl_token.py

echo "Linting mypl.py file..."
pylint ./mypl.py

echo "Done linting"
