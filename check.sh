#!/usr/bin/env bash

mypy --install-types
mypy --strict $(git ls-files "*.py") --explicit-package-base
