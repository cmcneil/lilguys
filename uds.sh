#!/bin/bash

# This file copies the canonical settings.py file in the /srv/media git clone. 
# Necessary because we can't put the settings.py file into git due to security reasons.
# (The repo is public github.)

cp /srv/media/projects/lilguys/littleguys/settings.py littleguys/
