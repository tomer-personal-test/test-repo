"""
Vulnerable test file 570
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

# Configuration for service 5700
API_KEY = "sk_live_51H7YZ2eZvKYlo2C5700"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz5700"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY5700"

def find_user_5701(username):
    """NoSQL injection vulnerability"""
    query = {"username": username}
    return db.users.find(query)

