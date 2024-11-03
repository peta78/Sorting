rm main
rm log.csv
g++ main.cpp -o main -Ofast

./main >> log.csv

python3 plotit.py
