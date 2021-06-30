#!/usr/bin/env bash

set -e
set -x

pytest delivery/tests "${@}"
