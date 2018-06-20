#!/bin/bash
date
out=$(ps aux | grep "[p]lant-water.py")
if [[ -z ${out} ]]
then
        echo "starting plant-water.py..."
        /home/pi/projects/raspberry/scripts/run.sh
else
        echo "plant-water.py already running!!!"
fi