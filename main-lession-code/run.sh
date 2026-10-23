#!/usr/bin/env bash
# run.sh — bien dich va chay mot file C++
# Dung:  ./run.sh            -> chay main.cpp
#        ./run.sh bai01.cpp  -> chay bai01.cpp

set -e                                  # gap loi la dung ngay

SRC="${1:-main.cpp}"                    # khong truyen gi thi lay main.cpp

if [ ! -f "$SRC" ]; then
    echo "Not fould file: $SRC"
    exit 1
fi

OUT="${SRC%.cpp}"                       # bo duoi .cpp de lam ten file chay

g++ -std=c++20 -Wall -Wextra -g "$SRC" -o "$OUT"

echo "--- result ---"
"./$OUT"
