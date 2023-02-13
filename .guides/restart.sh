#!/usr/bin/env bash

#delete existing version
cd /home/codio/workspace/.guides
mysql < cleanup.sql

# instantiate database
cd /home/codio/workspace/data
mysql < w2la.sql