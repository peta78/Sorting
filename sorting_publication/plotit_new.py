from datetime import datetime
import math
import numpy as np
import sys

def compute_res_a0_a1(x,y):
    coefs = 0
    res = 0
    
    A = []
    B = []
    for i in range(len(x)):
        A.append([x[i]])
        B.append([y[i]])
        
    A = np.array(A)
    B = np.array(B)
    At = np.transpose(A)
    X = np.matmul(np.linalg.inv(np.matmul(At,A)),np.matmul(At,B))
    
    res = np.matmul(A,X)-B
    res = np.matmul(np.transpose(res), res)
    
    return X, res

def theory(x,y):
    x_n = x
    x_nlogn = x * np.log(x)
    x_nloglogn = x * np.log(np.log(x))

    print('-------------------')

    X = np.array(x_n)
    y = np.array(y)
    k1A, residualsA = compute_res_a0_a1(X,y)
    print("Residuals O(n):", residualsA)
    
    X = np.array(x_nlogn)
    y = np.array(y)
    k2A, residualsB = compute_res_a0_a1(X,y)
    print("Residuals O(n log n):", residualsB)

    X = np.array(x_nloglogn)
    y = np.array(y)
    k3A, residualsC = compute_res_a0_a1(X,y)
    print("Residuals O(n log log n):", residualsC)

    print('-------------------')

    return 0, ''

print(  )


lines = """0,200,10000,2024-11-08 05:33:37.860,2024-11-08 05:33:37.861,2024-11-08 05:33:37.861,
1,200,2522512,2024-11-08 05:33:37.884,2024-11-08 05:33:38.046,2024-11-08 05:33:38.154,
2,200,5035025,2024-11-08 05:33:38.204,2024-11-08 05:33:38.548,2024-11-08 05:33:38.774,
3,200,7547537,2024-11-08 05:33:38.838,2024-11-08 05:33:39.356,2024-11-08 05:33:39.704,
4,200,10060050,2024-11-08 05:33:39.793,2024-11-08 05:33:40.508,2024-11-08 05:33:40.951,
5,200,12572562,2024-11-08 05:33:41.051,2024-11-08 05:33:41.926,2024-11-08 05:33:42.463,
6,200,15085075,2024-11-08 05:33:42.585,2024-11-08 05:33:43.648,2024-11-08 05:33:44.304,
7,200,17597587,2024-11-08 05:33:44.464,2024-11-08 05:33:45.712,2024-11-08 05:33:46.504,
8,200,20110100,2024-11-08 05:33:46.678,2024-11-08 05:33:48.167,2024-11-08 05:33:49.098,
9,200,22622613,2024-11-08 05:33:49.290,2024-11-08 05:33:50.917,2024-11-08 05:33:51.936,
10,200,25135125,2024-11-08 05:33:52.139,2024-11-08 05:33:53.982,2024-11-08 05:33:55.115,
11,200,27647638,2024-11-08 05:33:55.336,2024-11-08 05:33:57.341,2024-11-08 05:33:58.567,
12,200,30160150,2024-11-08 05:33:58.806,2024-11-08 05:34:01.046,2024-11-08 05:34:02.417,
13,200,32672663,2024-11-08 05:34:02.672,2024-11-08 05:34:05.061,2024-11-08 05:34:06.555,
14,200,35185175,2024-11-08 05:34:06.869,2024-11-08 05:34:09.494,2024-11-08 05:34:11.115,
15,200,37697688,2024-11-08 05:34:11.448,2024-11-08 05:34:14.276,2024-11-08 05:34:15.995,
16,200,40210201,2024-11-08 05:34:16.346,2024-11-08 05:34:19.397,2024-11-08 05:34:21.232,
17,200,42722713,2024-11-08 05:34:21.602,2024-11-08 05:34:24.857,2024-11-08 05:34:26.826,
18,200,45235226,2024-11-08 05:34:27.198,2024-11-08 05:34:30.628,2024-11-08 05:34:32.710,
19,200,47747738,2024-11-08 05:34:33.101,2024-11-08 05:34:36.736,2024-11-08 05:34:38.943,
20,200,50260251,2024-11-08 05:34:39.357,2024-11-08 05:34:43.186,2024-11-08 05:34:45.530,
21,200,52772763,2024-11-08 05:34:45.959,2024-11-08 05:34:50.033,2024-11-08 05:34:52.486,
22,200,55285276,2024-11-08 05:34:52.924,2024-11-08 05:34:57.223,2024-11-08 05:34:59.820,
23,200,57797788,2024-11-08 05:35:00.276,2024-11-08 05:35:04.776,2024-11-08 05:35:07.500,
24,200,60310301,2024-11-08 05:35:07.983,2024-11-08 05:35:12.730,2024-11-08 05:35:15.566,
25,200,62822814,2024-11-08 05:35:16.058,2024-11-08 05:35:20.968,2024-11-08 05:35:23.891,
26,200,65335326,2024-11-08 05:35:24.381,2024-11-08 05:35:29.457,2024-11-08 05:35:32.552,
27,200,67847839,2024-11-08 05:35:33.181,2024-11-08 05:35:38.476,2024-11-08 05:35:41.711,
28,200,70360351,2024-11-08 05:35:42.345,2024-11-08 05:35:47.761,2024-11-08 05:35:51.113,
29,200,72872864,2024-11-08 05:35:51.756,2024-11-08 05:35:57.409,2024-11-08 05:36:00.841,
30,200,75385376,2024-11-08 05:36:01.513,2024-11-08 05:36:07.414,2024-11-08 05:36:10.948,
31,200,77897889,2024-11-08 05:36:11.636,2024-11-08 05:36:17.696,2024-11-08 05:36:21.374,
32,200,80410402,2024-11-08 05:36:22.060,2024-11-08 05:36:28.361,2024-11-08 05:36:32.187,
33,200,82922914,2024-11-08 05:36:32.896,2024-11-08 05:36:39.394,2024-11-08 05:36:43.345,
34,200,85435427,2024-11-08 05:36:44.044,2024-11-08 05:36:50.708,2024-11-08 05:36:54.779,
35,200,87947939,2024-11-08 05:36:55.497,2024-11-08 05:37:02.498,2024-11-08 05:37:06.722,
36,200,90460452,2024-11-08 05:37:07.479,2024-11-08 05:37:14.552,2024-11-08 05:37:18.803,
37,200,92972964,2024-11-08 05:37:19.570,2024-11-08 05:37:26.947,2024-11-08 05:37:31.343,
38,200,95485477,2024-11-08 05:37:32.142,2024-11-08 05:37:39.625,2024-11-08 05:37:44.130,
39,200,97997989,2024-11-08 05:37:44.925,2024-11-08 05:37:52.662,2024-11-08 05:37:57.344,
40,200,100510502,2024-11-08 05:37:58.145,2024-11-08 05:38:06.100,2024-11-08 05:38:10.894,
41,200,103023015,2024-11-08 05:38:11.727,2024-11-08 05:38:19.923,2024-11-08 05:38:24.813,
42,200,105535527,2024-11-08 05:38:25.644,2024-11-08 05:38:33.949,2024-11-08 05:38:39.068,
43,200,108048040,2024-11-08 05:38:39.908,2024-11-08 05:38:48.500,2024-11-08 05:38:53.693,
44,200,110560552,2024-11-08 05:38:54.531,2024-11-08 05:39:03.292,2024-11-08 05:39:08.596,
45,200,113073065,2024-11-08 05:39:09.472,2024-11-08 05:39:18.531,2024-11-08 05:39:23.914,
46,200,115585577,2024-11-08 05:39:24.814,2024-11-08 05:39:34.001,2024-11-08 05:39:39.555,
47,200,118098090,2024-11-08 05:39:40.457,2024-11-08 05:39:49.798,2024-11-08 05:39:55.383,
48,200,120610603,2024-11-08 05:39:56.309,2024-11-08 05:40:05.848,2024-11-08 05:40:11.563,
49,200,123123115,2024-11-08 05:40:12.479,2024-11-08 05:40:22.341,2024-11-08 05:40:28.358,
50,200,125635628,2024-11-08 05:40:29.302,2024-11-08 05:40:39.281,2024-11-08 05:40:45.291,
51,200,128148140,2024-11-08 05:40:46.254,2024-11-08 05:40:56.445,2024-11-08 05:41:02.514,
52,200,130660653,2024-11-08 05:41:03.491,2024-11-08 05:41:13.954,2024-11-08 05:41:20.186,
53,200,133173165,2024-11-08 05:41:21.173,2024-11-08 05:41:31.997,2024-11-08 05:41:38.388,
54,200,135685678,2024-11-08 05:41:39.589,2024-11-08 05:41:50.437,2024-11-08 05:41:56.941,
55,200,138198190,2024-11-08 05:41:58.175,2024-11-08 05:42:09.208,2024-11-08 05:42:15.784,
56,200,140710703,2024-11-08 05:42:17.040,2024-11-08 05:42:28.405,2024-11-08 05:42:35.162,
57,200,143223216,2024-11-08 05:42:36.423,2024-11-08 05:42:47.901,2024-11-08 05:42:54.679,
58,200,145735728,2024-11-08 05:42:55.967,2024-11-08 05:43:07.610,2024-11-08 05:43:14.620,
59,200,148248241,2024-11-08 05:43:15.908,2024-11-08 05:43:27.995,2024-11-08 05:43:35.159,
60,200,150760753,2024-11-08 05:43:36.445,2024-11-08 05:43:48.644,2024-11-08 05:43:55.855,
61,200,153273266,2024-11-08 05:43:57.160,2024-11-08 05:44:09.587,2024-11-08 05:44:16.997,
62,200,155785778,2024-11-08 05:44:18.315,2024-11-08 05:44:30.928,2024-11-08 05:44:38.440,
63,200,158298291,2024-11-08 05:44:39.791,2024-11-08 05:44:52.511,2024-11-08 05:45:00.088,
64,200,160810804,2024-11-08 05:45:01.455,2024-11-08 05:45:14.412,2024-11-08 05:45:22.112,
65,200,163323316,2024-11-08 05:45:23.466,2024-11-08 05:45:36.757,2024-11-08 05:45:44.639,
66,200,165835829,2024-11-08 05:45:46.028,2024-11-08 05:45:59.426,2024-11-08 05:46:07.427,
67,200,168348341,2024-11-08 05:46:08.811,2024-11-08 05:46:22.516,2024-11-08 05:46:30.522,
68,200,170860854,2024-11-08 05:46:31.950,2024-11-08 05:46:45.922,2024-11-08 05:46:54.145,
69,200,173373366,2024-11-08 05:46:55.610,2024-11-08 05:47:09.745,2024-11-08 05:47:18.155,
70,200,175885879,2024-11-08 05:47:19.577,2024-11-08 05:47:33.831,2024-11-08 05:47:42.247,
71,200,178398391,2024-11-08 05:47:43.726,2024-11-08 05:47:58.305,2024-11-08 05:48:06.865,
72,200,180910904,2024-11-08 05:48:08.358,2024-11-08 05:48:23.115,2024-11-08 05:48:31.922,
73,200,183423417,2024-11-08 05:48:33.431,2024-11-08 05:48:48.446,2024-11-08 05:48:57.198,
74,200,185935929,2024-11-08 05:48:58.724,2024-11-08 05:49:13.614,2024-11-08 05:49:22.433,
75,200,188448442,2024-11-08 05:49:23.940,2024-11-08 05:49:39.413,2024-11-08 05:49:48.450,
76,200,190960954,2024-11-08 05:49:49.988,2024-11-08 05:50:05.503,2024-11-08 05:50:14.679,
77,200,193473467,2024-11-08 05:50:16.217,2024-11-08 05:50:32.096,2024-11-08 05:50:41.379,
78,200,195985979,2024-11-08 05:50:42.962,2024-11-08 05:50:58.971,2024-11-08 05:51:08.409,
79,200,198498492,2024-11-08 05:51:10.002,2024-11-08 05:51:26.148,2024-11-08 05:51:35.757,
80,200,201011005,2024-11-08 05:51:37.371,2024-11-08 05:51:53.867,2024-11-08 05:52:03.373,
81,200,203523517,2024-11-08 05:52:04.982,2024-11-08 05:52:21.658,2024-11-08 05:52:31.434,
82,200,206036030,2024-11-08 05:52:33.029,2024-11-08 05:52:49.993,2024-11-08 05:52:59.843,
83,200,208548542,2024-11-08 05:53:01.486,2024-11-08 05:53:18.550,2024-11-08 05:53:28.571,
84,200,211061055,2024-11-08 05:53:30.244,2024-11-08 05:53:47.469,2024-11-08 05:53:57.631,
85,200,213573567,2024-11-08 05:53:59.291,2024-11-08 05:54:16.873,2024-11-08 05:54:27.116,
86,200,216086080,2024-11-08 05:54:28.815,2024-11-08 05:54:46.683,2024-11-08 05:54:56.980,
87,200,218598592,2024-11-08 05:54:58.663,2024-11-08 05:55:16.620,2024-11-08 05:55:26.998,
88,200,221111105,2024-11-08 05:55:28.692,2024-11-08 05:55:46.919,2024-11-08 05:55:57.585,
89,200,223623618,2024-11-08 05:55:59.303,2024-11-08 05:56:17.572,2024-11-08 05:56:28.151,
90,200,226136130,2024-11-08 05:56:29.884,2024-11-08 05:56:48.459,2024-11-08 05:56:59.359,
91,200,228648643,2024-11-08 05:57:01.094,2024-11-08 05:57:20.049,2024-11-08 05:57:30.962,
92,200,231161155,2024-11-08 05:57:32.735,2024-11-08 05:57:51.924,2024-11-08 05:58:02.975,
93,200,233673668,2024-11-08 05:58:04.743,2024-11-08 05:58:24.100,2024-11-08 05:58:35.200,
94,200,236186180,2024-11-08 05:58:37.019,2024-11-08 05:58:56.648,2024-11-08 05:59:07.954,
95,200,238698693,2024-11-08 05:59:09.784,2024-11-08 05:59:29.512,2024-11-08 05:59:41.071,
96,200,241211206,2024-11-08 05:59:42.888,2024-11-08 06:00:02.756,2024-11-08 06:00:14.467,
97,200,243723718,2024-11-08 06:00:16.285,2024-11-08 06:00:36.476,2024-11-08 06:00:48.086,
98,200,246236231,2024-11-08 06:00:49.949,2024-11-08 06:01:10.313,2024-11-08 06:01:22.059,
99,200,248748743,2024-11-08 06:01:23.969,2024-11-08 06:01:44.362,2024-11-08 06:01:56.385,
100,200,251261256,2024-11-08 06:01:58.260,2024-11-08 06:02:19.153,2024-11-08 06:02:31.220,
101,200,253773768,2024-11-08 06:02:33.142,2024-11-08 06:02:54.137,2024-11-08 06:03:06.344,
102,200,256286281,2024-11-08 06:03:08.255,2024-11-08 06:03:29.654,2024-11-08 06:03:42.016,
103,200,258798793,2024-11-08 06:03:43.974,2024-11-08 06:04:05.350,2024-11-08 06:04:17.835,
104,200,261311306,2024-11-08 06:04:19.797,2024-11-08 06:04:41.488,2024-11-08 06:04:54.021,
105,200,263823819,2024-11-08 06:04:55.992,2024-11-08 06:05:17.991,2024-11-08 06:05:30.723,
106,200,266336331,2024-11-08 06:05:32.684,2024-11-08 06:05:54.636,2024-11-08 06:06:07.579,
107,200,268848844,2024-11-08 06:06:10.012,2024-11-08 06:06:32.451,2024-11-08 06:06:45.639,
108,200,271361356,2024-11-08 06:06:48.040,2024-11-08 06:07:10.563,2024-11-08 06:07:23.935,
109,200,273873869,2024-11-08 06:07:26.332,2024-11-08 06:07:48.958,2024-11-08 06:08:02.611,
110,200,276386381,2024-11-08 06:08:05.053,2024-11-08 06:08:28.049,2024-11-08 06:08:41.471,
111,200,278898894,2024-11-08 06:08:43.899,2024-11-08 06:09:06.973,2024-11-08 06:09:21.088,
112,200,281411407,2024-11-08 06:09:23.543,2024-11-08 06:09:47.013,2024-11-08 06:10:00.868,
113,200,283923919,2024-11-08 06:10:03.315,2024-11-08 06:10:26.855,2024-11-08 06:10:40.851,
114,200,286436432,2024-11-08 06:10:43.320,2024-11-08 06:11:07.132,2024-11-08 06:11:21.190,
115,200,288948944,2024-11-08 06:11:23.711,2024-11-08 06:11:47.943,2024-11-08 06:12:02.406,
116,200,291461457,2024-11-08 06:12:04.919,2024-11-08 06:12:29.171,2024-11-08 06:12:43.210,
117,200,293973969,2024-11-08 06:12:45.716,2024-11-08 06:13:10.112,2024-11-08 06:13:24.305,
118,200,296486482,2024-11-08 06:13:26.867,2024-11-08 06:13:51.542,2024-11-08 06:14:05.994,
119,200,298998994,2024-11-08 06:14:08.508,2024-11-08 06:14:33.316,2024-11-08 06:14:48.031,
120,200,301511507,2024-11-08 06:14:50.559,2024-11-08 06:15:15.620,2024-11-08 06:15:30.452,
121,200,304024020,2024-11-08 06:15:33.053,2024-11-08 06:15:58.332,2024-11-08 06:16:13.393,
122,200,306536532,2024-11-08 06:16:16.004,2024-11-08 06:16:41.528,2024-11-08 06:16:56.466,
123,200,309049045,2024-11-08 06:16:59.086,2024-11-08 06:17:24.837,2024-11-08 06:17:39.768,
124,200,311561557,2024-11-08 06:17:42.415,2024-11-08 06:18:08.421,2024-11-08 06:18:23.569,
125,200,314074070,2024-11-08 06:18:26.177,2024-11-08 06:18:52.513,2024-11-08 06:19:07.736,
126,200,316586582,2024-11-08 06:19:10.346,2024-11-08 06:19:36.652,2024-11-08 06:19:52.020,
127,200,319099095,2024-11-08 06:19:54.709,2024-11-08 06:20:21.417,2024-11-08 06:20:36.856,
128,200,321611608,2024-11-08 06:20:39.590,2024-11-08 06:21:06.439,2024-11-08 06:21:22.190,
129,200,324124120,2024-11-08 06:21:25.153,2024-11-08 06:21:52.358,2024-11-08 06:22:08.335,
130,200,326636633,2024-11-08 06:22:11.110,2024-11-08 06:22:38.495,2024-11-08 06:22:54.555,
131,200,329149145,2024-11-08 06:22:57.306,2024-11-08 06:23:24.901,2024-11-08 06:23:40.754,
132,200,331661658,2024-11-08 06:23:43.519,2024-11-08 06:24:11.360,2024-11-08 06:24:27.591,
133,200,334174170,2024-11-08 06:24:30.375,2024-11-08 06:24:58.383,2024-11-08 06:25:14.670,
134,200,336686683,2024-11-08 06:25:17.477,2024-11-08 06:25:45.269,2024-11-08 06:26:01.652,
135,200,339199195,2024-11-08 06:26:04.424,2024-11-08 06:26:32.655,2024-11-08 06:26:49.280,
136,200,341711708,2024-11-08 06:26:52.096,2024-11-08 06:27:20.903,2024-11-08 06:27:37.788,
137,200,344224221,2024-11-08 06:27:40.616,2024-11-08 06:28:09.685,2024-11-08 06:28:26.355,
138,200,346736733,2024-11-08 06:28:29.219,2024-11-08 06:28:58.270,2024-11-08 06:29:14.946,
139,200,349249246,2024-11-08 06:29:17.780,2024-11-08 06:29:47.194,2024-11-08 06:30:04.411,
140,200,351761758,2024-11-08 06:30:07.343,2024-11-08 06:30:36.893,2024-11-08 06:30:54.444,
141,200,354274271,2024-11-08 06:30:57.295,2024-11-08 06:31:26.826,2024-11-08 06:31:44.048,
142,200,356786783,2024-11-08 06:31:47.016,2024-11-08 06:32:17.143,2024-11-08 06:32:34.661,
143,200,359299296,2024-11-08 06:32:37.568,2024-11-08 06:33:07.598,2024-11-08 06:33:24.934,
144,200,361811809,2024-11-08 06:33:27.869,2024-11-08 06:33:58.086,2024-11-08 06:34:15.915,
145,200,364324321,2024-11-08 06:34:18.873,2024-11-08 06:34:49.359,2024-11-08 06:35:07.409,
146,200,366836834,2024-11-08 06:35:10.339,2024-11-08 06:35:41.018,2024-11-08 06:35:58.718,
147,200,369349346,2024-11-08 06:36:01.719,2024-11-08 06:36:32.889,2024-11-08 06:36:51.029,
148,200,371861859,2024-11-08 06:36:54.065,2024-11-08 06:37:25.541,2024-11-08 06:37:43.894,
149,200,374374371,2024-11-08 06:37:46.868,2024-11-08 06:38:18.603,2024-11-08 06:38:36.956,
150,200,376886884,2024-11-08 06:38:40.268,2024-11-08 06:39:12.433,2024-11-08 06:39:31.295,
151,200,379399396,2024-11-08 06:39:34.342,2024-11-08 06:40:06.841,2024-11-08 06:40:25.730,
152,200,381911909,2024-11-08 06:40:28.839,2024-11-08 06:41:01.428,2024-11-08 06:41:20.512,
153,200,384424422,2024-11-08 06:41:23.607,2024-11-08 06:41:56.470,2024-11-08 06:42:15.703,
154,200,386936934,2024-11-08 06:42:18.794,2024-11-08 06:42:51.487,2024-11-08 06:43:10.783,
155,200,389449447,2024-11-08 06:43:13.918,2024-11-08 06:43:47.047,2024-11-08 06:44:06.399,
156,200,391961959,2024-11-08 06:44:09.577,2024-11-08 06:44:43.348,2024-11-08 06:45:03.072,
157,200,394474472,2024-11-08 06:45:06.182,2024-11-08 06:45:39.755,2024-11-08 06:45:59.354,
158,200,396986984,2024-11-08 06:46:02.513,2024-11-08 06:46:36.348,2024-11-08 06:46:55.854,
159,200,399499497,2024-11-08 06:46:59.071,2024-11-08 06:47:33.055,2024-11-08 06:47:53.125,
160,200,402012010,2024-11-08 06:47:56.347,2024-11-08 06:48:30.728,2024-11-08 06:48:50.844,
161,200,404524522,2024-11-08 06:48:54.051,2024-11-08 06:49:28.391,2024-11-08 06:49:48.675,
162,200,407037035,2024-11-08 06:49:51.903,2024-11-08 06:50:26.641,2024-11-08 06:50:46.736,
163,200,409549547,2024-11-08 06:50:50.056,2024-11-08 06:51:24.925,2024-11-08 06:51:45.252,
164,200,412062060,2024-11-08 06:51:48.563,2024-11-08 06:52:23.242,2024-11-08 06:52:43.587,
165,200,414574572,2024-11-08 06:52:46.853,2024-11-08 06:53:22.245,2024-11-08 06:53:43.015,
166,200,417087085,2024-11-08 06:53:46.327,2024-11-08 06:54:22.131,2024-11-08 06:54:42.609,
167,200,419599597,2024-11-08 06:54:45.928,2024-11-08 06:55:21.711,2024-11-08 06:55:42.550,
168,200,422112110,2024-11-08 06:55:45.885,2024-11-08 06:56:22.085,2024-11-08 06:56:42.897,
169,200,424624623,2024-11-08 06:56:46.215,2024-11-08 06:57:22.639,2024-11-08 06:57:43.787,
170,200,427137135,2024-11-08 06:57:47.156,2024-11-08 06:58:23.306,2024-11-08 06:58:44.223,
171,200,429649648,2024-11-08 06:58:47.562,2024-11-08 06:59:23.503,2024-11-08 06:59:44.577,
172,200,432162160,2024-11-08 06:59:47.860,2024-11-08 07:00:24.024,2024-11-08 07:00:44.989,
173,200,434674673,2024-11-08 07:00:48.365,2024-11-08 07:01:24.603,2024-11-08 07:01:45.823,
174,200,437187185,2024-11-08 07:01:49.226,2024-11-08 07:02:25.338,2024-11-08 07:02:46.534,
175,200,439699698,2024-11-08 07:02:49.933,2024-11-08 07:03:27.018,2024-11-08 07:03:48.593,
176,200,442212211,2024-11-08 07:03:51.975,2024-11-08 07:04:28.918,2024-11-08 07:04:50.579,
177,200,444724723,2024-11-08 07:04:54.049,2024-11-08 07:05:31.046,2024-11-08 07:05:52.725,
178,200,447237236,2024-11-08 07:05:56.180,2024-11-08 07:06:33.594,2024-11-08 07:06:55.460,
179,200,449749748,2024-11-08 07:06:58.927,2024-11-08 07:07:36.432,2024-11-08 07:07:58.458,
180,200,452262261,2024-11-08 07:08:01.897,2024-11-08 07:08:39.806,2024-11-08 07:09:01.801,
181,200,454774773,2024-11-08 07:09:05.244,2024-11-08 07:09:43.377,2024-11-08 07:10:05.760,
182,200,457287286,2024-11-08 07:10:09.496,2024-11-08 07:10:48.010,2024-11-08 07:11:10.746,
183,200,459799798,2024-11-08 07:11:14.177,2024-11-08 07:11:53.081,2024-11-08 07:12:15.398,
184,200,462312311,2024-11-08 07:12:18.846,2024-11-08 07:12:57.251,2024-11-08 07:13:19.775,
185,200,464824824,2024-11-08 07:13:23.266,2024-11-08 07:14:02.450,2024-11-08 07:14:24.780,
186,200,467337336,2024-11-08 07:14:28.291,2024-11-08 07:15:07.849,2024-11-08 07:15:30.326,
187,200,469849849,2024-11-08 07:15:33.900,2024-11-08 07:16:13.175,2024-11-08 07:16:35.849,
188,200,472362361,2024-11-08 07:16:39.359,2024-11-08 07:17:19.136,2024-11-08 07:17:42.492,
189,200,474874874,2024-11-08 07:17:46.074,2024-11-08 07:18:25.865,2024-11-08 07:18:49.008,
190,200,477387386,2024-11-08 07:18:52.538,2024-11-08 07:19:32.281,2024-11-08 07:19:55.612,
191,200,479899899,2024-11-08 07:19:59.268,2024-11-08 07:20:39.550,2024-11-08 07:21:03.163,
192,200,482412412,2024-11-08 07:21:06.853,2024-11-08 07:21:47.691,2024-11-08 07:22:11.019,
193,200,484924924,2024-11-08 07:22:14.636,2024-11-08 07:22:55.706,2024-11-08 07:23:19.187,
194,200,487437437,2024-11-08 07:23:22.817,2024-11-08 07:24:04.100,2024-11-08 07:24:27.821,
195,200,489949949,2024-11-08 07:24:31.515,2024-11-08 07:25:12.676,2024-11-08 07:25:36.261,
196,200,492462462,2024-11-08 07:25:39.975,2024-11-08 07:26:21.276,2024-11-08 07:26:45.223,
197,200,494974974,2024-11-08 07:26:48.991,2024-11-08 07:27:30.450,2024-11-08 07:27:54.979,
198,200,497487487,2024-11-08 07:27:58.712,2024-11-08 07:28:40.673,2024-11-08 07:29:04.907,
199,200,500000000,2024-11-08 07:29:09.787,2024-11-08 07:29:52.201,2024-11-08 07:30:16.561,"""

lines = lines.split('\n')

x = []
y1 = []
y2 = []
for line in lines:
    parts = line.split(',')
    if len(parts) != 7:
        break

    s1 = datetime.strptime(parts[3], "%Y-%m-%d %H:%M:%S.%f")
    s2 = datetime.strptime(parts[4], "%Y-%m-%d %H:%M:%S.%f")
    s3 = datetime.strptime(parts[5], "%Y-%m-%d %H:%M:%S.%f")

    x.append(int(parts[2]))
    y1.append((s2-s1).total_seconds())
    y2.append((s3-s2).total_seconds())

x = np.array(x)
y1 = np.array(y1)
y2 = np.array(y2)

y1t, y1name = theory(x, y1)
y2t, y2name = theory(x, y2)
