#!/bin/bash

set -exo pipefail

readonly PACKAGES=$(/usr/share/google/get_metadata_value attributes/PIP_PACKAGES || true)
readonly REQUIREMENTS=$(/usr/share/google/get_metadata_value attributes/REQUIREMENTS_FILE || true)

function err() {
  echo "[$(date +'%Y-%m-%dT%H:%M:%S%z')]: $*" >&2
  exit 1
}

function run_with_retry() {
  local -r cmd=("$@")
  for ((i = 0; i < 10; i++)); do
    if "${cmd[@]}"; then
      return 0
    fi
    sleep 5
  done
  err "Failed to run command: ${cmd[*]}"
}

function install_pip() {
  if command -v pip >/dev/null; then
    echo "pip is already installed."
    return 0
  fi

  if command -v easy_install >/dev/null; then
    echo "Installing pip with easy_install..."
    run_with_retry easy_install pip
    return 0
  fi

  echo "Installing python-pip..."
  run_with_retry apt update
  run_with_retry apt install python-pip -y
}


function main() {
  if [[ -z $PACKAGES && -z $REQUIREMENTS ]]; then
    echo "ERROR: Must specify PIP_PACKAGES or REQUIREMENTS_FILE metadata key"
    exit(1)
  fi

  if [[ -n $PACKAGES && -n $REQUIREMENTS ]]; then
    echo "ERROR: Only one of metadata key (PIP_PACKAGES / REQUIREMENTS_FILE) should be specified"
    exit(1)
  fi


  install_pip

  if [[ -n $PACKAGES ]];
  then
    echo "Install packages from PIP_PACKAGES"
    run_with_retry pip install --upgrade ${PACKAGES}
  else
    echo "Install packages from REQUIREMENTS_FILE"
    run_with_retry pip install `gsutil cat ${REQUIREMENTS}`
  fi
}

main
