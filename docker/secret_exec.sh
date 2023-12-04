#!/bin/bash

set -e

if [ -f /run/secrets/PYPI_USERNAME ]; then
    echo "file /run/secrets/PYPI_USERNAME is set, setting up env variable"
    PYPI_USERNAME=$(cat /run/secrets/PYPI_USERNAME)
fi
if [ -f /run/secrets/PYPI_PASSWORD ]; then
    echo "file /run/secrets/PYPI_PASSWORD is set, setting up env variable"
    PYPI_PASSWORD=$(cat /run/secrets/PYPI_PASSWORD)
fi

cat > $HOME/.netrc <<- EOM
machine pypiserver.itrcs3-app.intranet.chuv
    login ${PYPI_USERNAME}
    password ${PYPI_PASSWORD}
EOM

# Execute the command
"$@"
execution_status=$?

rm $HOME/.netrc
PYPI_USERNAME=""
PYPI_PASSWORD=""

exit $execution_status
