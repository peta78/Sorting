# Statistical Sorting

Did you know you can sort faster than [quick sort](https://en.wikipedia.org/wiki/Quicksort)?

This code was written just to inspire, not to be a production code... And there is even way better way (why to sort when you know where things approximately belong?) to do it (without using quicksort)...

Quick sort takes around ~20.262 seconds, "statistical" sorting took only ~12.487 seconds with [AMD Ryzen™ 7 8845HS](https://www.amd.com/en/products/processors/laptop/ryzen/8000-series/amd-ryzen-7-8845hs.html) on [linux](https://kernel.org/) [Manjaro](https://manjaro.org/) on a [Lenovo](https://www.lenovo.com/) [IdeaPad](https://www.lenovo.com/us/en/c/laptops/ideapad/)... And if you use multi-threading, it can get to ~4.415 seconds on 16-threads already mentioned AMD processor.

~/Code/Sorting>>>./run.sh

hello

2024-06-08 14:48:03.562

2024-06-08 14:48:23.824

2024-06-08 14:48:36.311

Number of Threads 16

2024-06-08 14:48:40.726

Verifying

Done



Simple idea behind this code for single-thread execution is O(n log n) > O(n log (n/m)) = O(m (n/m log(n/m))). (Yes, if you do a good job without quicksort you can get close to O(n)... But there are obstacles ;) )
