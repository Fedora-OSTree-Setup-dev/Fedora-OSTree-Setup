#!/usr/bin/env bash

command -v mypy >/dev/null 2>&1 || { echo -e "\033[1;31mmypy==0.991 is not installed!" && exit 1; }

mypy --install-types
mypy --strict $(git ls-files "*.py") --explicit-package-base
