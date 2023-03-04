#!/bin/bash
python downloadfile.py
gunicorn main:app