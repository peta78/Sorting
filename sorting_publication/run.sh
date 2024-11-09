rm main
rm *.png
rm *.csv
g++ main.cpp -o main -Ofast


./main uniform
python3 plotit.py uniform
mv log.csv log_uniform.csv

./main gauss
python3 plotit.py gauss
mv log.csv log_gauss.csv

./main weird
python3 plotit.py weird
mv log.csv log_weird.csv

