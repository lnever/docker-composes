#!/usr/bin/env bash

kapacitor define -name ${1} -type stream -tick ./${2} -dbrp telegraf.default
