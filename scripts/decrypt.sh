#!/bin/bash

set -e

function usage()
{
	bold=$(tput bold)
	normal=$(tput sgr0)
	echo "NAME"
	echo "    decrypt.sh -- decrypt all secret files in an env"
	echo "SYNOPSIS"
	echo "    ${bold}decrypt.sh${normal} <passphrase> <directory>"
}

if [ "$#" -ne 2 ]; then
    usage
    exit 1
fi

if [ ! -d "$2" ] && [ ! -f "$2" ]; then
    echo "Error: no file or directory $2"
    usage
    exit 1
fi

function decrypt() {
    SALT_HEX=$(head -c 64 "$2" | tr -d '\n')
    IV_AND_ENC_HEX=$(cat $2 | xxd -p -c 256 | tr -d '\n' | cut -z -c 129- | tr -d '\0')

    IV=$(echo -n "$IV_AND_ENC_HEX" | cut -c 1-32)
    REST_FILE_HEX=$(echo -n "$IV_AND_ENC_HEX" | cut -c 33-)

    # Your AES passphrase
    PASS="$1"
    KEY=$(echo -n "$PASS$SALT_HEX" | openssl dgst -binary -sha256 | xxd -p -c 256 | cut -c 1-32)

    HEX_KEY=$(echo -n $KEY | xxd -p -c 256)

    # echo "IV $IV"
    # echo "hex key $HEX_KEY"
    # echo "salt $SALT_HEX"
    # echo "REST_FILE_HEX $(echo $REST_FILE_HEX)"

    # Decryption command
    if [ "$3" ]; then
        echo -n "$REST_FILE_HEX" | xxd -r -p | openssl enc -d -aes-256-cbc -out $3 -K "$HEX_KEY" -iv "$IV"
    else
        echo -n "$REST_FILE_HEX" | xxd -r -p | openssl enc -d -aes-256-cbc -K "$HEX_KEY" -iv "$IV"
    fi
}

files=$(find "$2" -name "*.yaml.enc")
for file in "$files"
do
    name=${file%".yaml.enc"}
    out=$(echo "$name.dec.yaml")
    echo "decrypting $file to $out..."
    decrypt "$1" "$file" "$out"
    rm "$file"
    echo "done"
done

