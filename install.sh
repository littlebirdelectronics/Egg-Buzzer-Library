#!/bin/bash

printf "Little Bird Electronics -- Egg Module\nEgg-Buzzer Python Installer"

if python --version 2>&1 | grep -q '^Python 3\.'; then
    printf "Found python"
    printf python --version
    python setup.py install
elif [ -f "/usr/bin/python3" ]; then
    printf "Found python3"
    printf python --version
    python setup.py install
else
    printf "This library requires python3, we could not find python3"
fi

printf "Done!\n\n"
