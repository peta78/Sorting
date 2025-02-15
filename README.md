# Statistical Sorting
## Why would you sort when you know where things approximately belong?

[Eight draft of the publication](./sorting_publication/Sorting/sorting8.pdf)

Also available on & cite as: Peter Taraba. [Why would you sort when you know where things approximately belong?](https://doi.org/10.22541/au.173145007.70152282/v1). Authorea. November 12, 2024.

[Code for Statistical sorting in O(n log log n) publication](./sorting_publication/)

## Previously... (publication is based on these previous experiments)

Did you know you can sort faster than [quick sort](https://en.wikipedia.org/wiki/Quicksort) - [C++ sort implementation in O(n log(n))](https://cplusplus.com/reference/algorithm/sort/)?

This code was written just to inspire, not to be a production code... And there is even way better way (why to sort when you know where things approximately belong?) to do it (without using quicksort)...

Quick sort takes around ~20.262 seconds, "statistical" sorting took only ~12.487 seconds with [AMD Ryzen™ 7 8845HS](https://www.amd.com/en/products/processors/laptop/ryzen/8000-series/amd-ryzen-7-8845hs.html) on [linux](https://kernel.org/) on a [Lenovo](https://www.lenovo.com/) [IdeaPad](https://www.lenovo.com/us/en/c/laptops/ideapad/)... And if you use multi-threading, it can get to ~4.415 seconds on 16-threads already mentioned AMD processor.

```
~/Code/Sorting>./run.sh
hello
2024-06-08 14:48:03.562
2024-06-08 14:48:23.824
2024-06-08 14:48:36.311
Number of Threads 16
2024-06-08 14:48:40.726
Verifying
Done
```


Simple idea behind this code for single-threaded execution is O(n log n) > O(n log (n/m)) = O(m (n/m log(n/m))). (Yes, if you do a great job without quicksort you can get close to O(n)...)

main_statsort.cpp is a bit improved implementation, which can be further improved?

quicksort ~ 21.478s

stat sort ~ 13.198s

stat sort multi threaded ~ 3.331s

```
./run.sh
Hello
2024-06-14 09:51:03.131
2024-06-14 09:51:24.609
2024-06-14 09:51:37.807
2024-06-14 09:51:41.138
Verifying
Done
```



```
~/Code/Sorting main*
base ❯ ./run.sh                                                                                           (base) 
hello
2024-12-11 18:06:29.669
2024-12-11 18:06:50.230
2024-12-11 18:07:02.851
Number of Threads 16
2024-12-11 18:07:07.235
Verifying
Done

~/Code/Sorting main* 42s
base ❯ neofetch                                                                                           (base) 
           .-------------------------:                   pepe@cachyos-x8664 
          .+=========================.                   ------------------ 
         :++===++==================-       :++-          OS: CachyOS x86_64 
        :*++====+++++=============-        .==:          Host: LENOVO LNVNB161216 
       -*+++=====+***++==========:                       Kernel: 6.12.4-2-cachyos 
      =*++++========------------:                        Uptime: 4 mins 
     =*+++++=====-                     ...               Packages: 1109 (pacman) 
   .+*+++++=-===:                    .=+++=:             Shell: fish 3.7.1 
  :++++=====-==:                     -*****+             Resolution: 1920x1200 
 :++========-=.                      .=+**+.             DE: Plasma 6.2.4 (Wayland) 
.+==========-.                          .                Theme: Breeze-Dark [GTK2], Breeze [GTK3] 
 :+++++++====-                                .--==-.    Icons: breeze-dark [GTK2/3] 
  :++==========.                             :+++++++:   Terminal: konsole 
   .-===========.                            =*****+*+   CPU: AMD Ryzen 7 8845HS w/ Radeon 780M Graphics (16) @  
    .-===========:                           .+*****+:   GPU: AMD ATI Phoenix3 
      -=======++++:::::::::::::::::::::::::-:  .---:     Memory: 2205MiB / 13731MiB 
       :======++++====+++******************=.
        :=====+++==========++++++++++++++*-                                      
         .====++==============++++++++++*-                                       
          .===+==================+++++++:
           .-=======================+++:
             ..........................


~/Code/Sorting main*
```
