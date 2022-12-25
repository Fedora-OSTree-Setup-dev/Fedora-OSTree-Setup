#!/usr/bin/env bash

mypy --strict $(git ls-files "*.py")
