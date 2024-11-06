rm main
rm *.csv
rm *.png
g++ main.cpp -o main -Ofast

./main Gauss
python3 plotit.py
