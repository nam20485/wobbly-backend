#! /bin/bash

usage() { echo "Usage: $0 [-d] for a development build, [-p] for a production build" 1>&2; exit 1; }

if [ $# == 0 ]; then usage; fi

while getopts ":dp" opt; do
    case "$opt" in
        d)
          docker-compose -f docker-compose-development.yml build
          ;;
        p)
          docker-compose build
          ;;
        *)
          usage
          ;;
    esac
done