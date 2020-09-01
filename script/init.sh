#!/bin/bash
current_path=`pwd`
project_path=`dirname ${current_path}`
export PYTHONPATH=${project_path}/tools:${project_path}:utils:${project_path}:/cores:${PYTHONPATH}