#!/bin/bash

set -e

function usage()
{
	bold=$(tput bold)
	normal=$(tput sgr0)
	echo "NAME"
	echo "    encrypt.sh -- encrypt all secret files in an env"
	echo "SYNOPSIS"
	echo "    ${bold}encrypt.sh${normal} <passphrase> <directory>"
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

function encrypt() {
    # Generate a random 16-byte IV and convert it to hexadecimal
    IV=$(openssl rand -hex 16)

    # Convert IV from hex to binary
    # IV_BIN=$(echo -n "$IV" | xxd -r -p)
    tmpfile_iv=$(mktemp ./iv.XXXXXX)
    echo -n "$IV" | xxd -r -p > $tmpfile_iv

    # Generate a 32-byte salt and convert it to hexadecimal
    SALT_HEX=$(openssl rand -hex 32)
    tmpfile_salt=$(mktemp ./salt.XXXXXX)
    echo -n "$SALT_HEX" > $tmpfile_salt

    # Your AES passphrase
    PASS="$1"
    # Derive the key using passphrase and salt
    KEY=$(echo -n "$PASS$SALT_HEX" | openssl dgst -binary -sha256 | xxd -p -c 256 | cut -c 1-32)

    HEX_KEY=$(echo -n $KEY | xxd -p -c 256)

    # Encrypt the file
    tmpfile_enc=$(mktemp ./enc.XXXXXX)
    openssl enc -aes-256-cbc -in $2 -out $tmpfile_enc -K "$HEX_KEY" -iv "$IV"

    # echo "IV $IV"
    # echo "hex key $HEX_KEY"
    # echo "salt $SALT_HEX"
    # echo $(cat $tmpfile_enc | xxd -p -c 256)

    # Prepend the binary salt and IV to the encrypted file
    if [ "$3" ]; then
        # openssl enc -aes-256-cbc -in $2 -K "$HEX_KEY" -iv "$IV"
        # echo -n "$SALT_HEX$IV_BIN$enc" > $3
        cat $tmpfile_salt $tmpfile_iv $tmpfile_enc > $3
    else
        cat $tmpfile_salt $tmpfile_iv $tmpfile_enc
    fi

    rm $tmpfile_enc $tmpfile_iv $tmpfile_salt
}


files=$(find "$2" -name "*.dec.yaml")
for file in "$files"
do
    name=${file%".dec.yaml"}
    out=$(echo "$name.yaml.enc")
    echo "encrypting $file to $out..."
    encrypt "$1" "$file" "$out"
    rm "$file"
    echo "done"
done