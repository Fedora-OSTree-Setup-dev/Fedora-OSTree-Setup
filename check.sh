#!/usr/bin/env bash

if [[ ! $(command -v mypy &> /dev/null) ]]; then
    echo -e "\033[1;31mmypy==0.991 is not installed!"
    exit 1
fi

mypy --install-types
mypy --strict $(git ls-files "*.py") --explicit-package-base
