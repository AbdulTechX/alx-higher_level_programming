#!/bin/bash
# Define the POST data with email and subject variables
post_data="email=test@gmail.com&subject=I%20will%20always%20be%20here%20for%20PLD"
curl -s -d "$post_data" "$1"
