#!/bin/bash

git clone https://github.com/arobito/arobito.git ../arobito
pip install -q -r ../arobito/src/requirements.txt
pip install -q -r requirements.txt