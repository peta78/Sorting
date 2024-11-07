rm main
rm *.png
g++ main.cpp -o main -Ofast

rm *.csv
./main norm
python3 plotit.py norm

rm *.csv
./main gauss
python3 plotit.py gauss


