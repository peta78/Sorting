# Statistical Sorting

Did you know you can sort faster than [quick sort](https://en.wikipedia.org/wiki/Quicksort)?

This code was written just to inspire, not to be a production code... And there is even way better way (why to sort when you know where things approximately belong?) to do it (without using quicksort)...

Quick sort takes around ~31 seconds, "statistical" sorting took only ~8 seconds...

~/Code/Sorting>>>./run.sh

hello

2024-06-06 15:29:30.119

2024-06-06 15:30:01.407

2024-06-06 15:30:09.113

Verifying

Done



Simple idea behind this code is O(n log n) > O(n log (n/m)).
