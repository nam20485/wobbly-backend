#! /bin/bash

usage() { echo "Usage: $0 [-d] for a development build, [-p] for a production build, [-b] for a development shell" 1>&2; exit 1; }

if [ $# == 0 ]; then usage; fi

while getopts ":dpb" opt; do
    case "$opt" in
        d)
          docker-compose -f docker-compose-development.yml up
          ;;
        p)
          docker run -it $DOCKER_IMAGE:latest -p 8000:8000 bin/docker-entrypoint.sh
          ;;
        b)
          docker-compose -f docker-compose-development.yml run --entrypoint bash -p 8000:8000 $DOCKER_SERVICE
          ;;
        *)
          usage
          ;;
    esac
done

# fix ownership on created files
echo "Fixing ownership on created files"
if [ `uname -s` = "Linux" ]
then
  echo "sudo chown -R `id -u $USER`:`id -g $USER` ."
  sudo chown -R `id -u $USER`:`id -g $USER` .
  ls -l
fi