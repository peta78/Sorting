#include <iostream>
#include <algorithm>    // std::sort
#include <vector>       // std::vector
#include <iterator>
#include <map>
#include <chrono>
#include <ctime>
#include <iomanip>
#include <sstream>
#include <string>
#include <limits>
#include <pthread.h>
#include <thread>
#include "math.h"

// better implementation than main.cpp, but still could use some work

using namespace std;

// https://stackoverflow.com/questions/24686846/get-current-time-in-milliseconds-or-hhmmssmmm-format
std::string time_in_HH_MM_SS_MMM()
{
    using namespace std::chrono;
    auto now = system_clock::now();
    auto ms = duration_cast<milliseconds>(now.time_since_epoch()) % 1000;
    auto timer = system_clock::to_time_t(now);
    std::tm bt = *std::localtime(&timer);
    std::ostringstream oss;
    oss << std::put_time(&bt, "%Y-%m-%d %H:%M:%S"); // HH:MM:SS
    oss << '.' << std::setfill('0') << std::setw(3) << ms.count();

    return oss.str();
}

std::vector<double>* myvectors;
int num_myvectors;
int numThreads = 1;

void *thread_sort(void *t) {
    int tid;

    tid = (long)t;

    for(int tt=tid;tt<num_myvectors;tt+=numThreads)
    {
        if(myvectors[tt].size() > 1)
        {
            int num_vecs = myvectors[tt].size();
            vector<double> vectors[num_vecs];

            double min, max;

            min = std::numeric_limits<double>::max();
            max = std::numeric_limits<double>::lowest();

            for(int i=0;i<myvectors[tt].size();i++)
            {
                if(min>myvectors[tt][i])
                {
                    min = myvectors[tt][i];
                }
                if(max<myvectors[tt][i])
                {
                    max = myvectors[tt][i];
                }
            }

            if(min!=max)
            {
                max += 0.0001 * (max-min);
            }
            else
            {
                max += 0.0001 * max;
            }

            for(int i=0;i<myvectors[tt].size();i++)
            {
                int pos = (int)((myvectors[tt][i]-min) * num_vecs / (max-min));
                vectors[pos].push_back(myvectors[tt][i]);
            }

            myvectors[tt].clear();
            for(int i=0;i<num_vecs;i++)
            {
                if(vectors[i].size()>0)
                {
                    sort(vectors[i].begin(), vectors[i].end());
                    for(int j=0;j<vectors[i].size();j++)
                    {
                        myvectors[tt].push_back(vectors[i][j]);
                    }
                }
            }
        }
    }

    pthread_exit(NULL);
}

void statsort(vector<double> &vec, int _numThreads)
{
    numThreads = _numThreads;

    int num_vecs = (int)sqrt(vec.size());
    vector<double> vectors[num_vecs];

    double min, max;

    min = std::numeric_limits<double>::max();
    max = std::numeric_limits<double>::lowest();

    for(int i=0;i<vec.size();i++)
    {
        if(min>vec[i])
        {
            min = vec[i];
        }
        if(max<vec[i])
        {
            max = vec[i];
        }
    }

    max += 0.0001 * (max-min);

    for(int i=0;i<vec.size();i++)
    {
        int pos = (int)((vec[i]-min) * num_vecs / (max-min));
        vectors[pos].push_back(vec[i]);
    }

    pthread_t *threads = new pthread_t[numThreads];
    pthread_attr_t attr;
    void *status;
    int rc;

    myvectors = vectors;
    num_myvectors = num_vecs;

    pthread_attr_init(&attr);
    pthread_attr_setdetachstate(&attr, PTHREAD_CREATE_JOINABLE);

    for(int i = 0; i < numThreads; i++ ) {
        rc = pthread_create(&threads[i], &attr, thread_sort, (void *)((long)i));
        if (rc) {
            cout << "Error:unable to create thread," << rc << endl;
            exit(-1);
        }
    }

    // free attribute and wait for the other threads
    pthread_attr_destroy(&attr);
    for(int i = 0; i < numThreads; i++ ) {
        rc = pthread_join(threads[i], &status);
        if (rc) {
            cout << "Error:unable to join," << rc << endl;
            exit(-1);
        }
    }

    vec.clear();
    for(int i=0;i<num_vecs;i++)
    {
        for(int j=0;j<vectors[i].size();j++)
        {
            vec.push_back(vectors[i][j]);
        }
    }
}

int main(void)
{
    cout << "Hello\n";

    vector<double> vec, vec2, vec3;

    for(int i=0;i<250000000;i++)
    {
        double f = (double)rand() / RAND_MAX;

        vec.push_back(f);
        vec2.push_back(f);
        vec3.push_back(f);
    }

    cout << time_in_HH_MM_SS_MMM() << "\n";

    std::sort (vec.begin(), vec.end());

    cout << time_in_HH_MM_SS_MMM() << "\n";

    statsort(vec2, 1);

    cout << time_in_HH_MM_SS_MMM() << "\n";

    statsort(vec3, std::thread::hardware_concurrency());

    cout << time_in_HH_MM_SS_MMM() << "\n";

    cout << "Verifying\n";

    for(int i=0;i<vec.size();i++)
    {
        if(vec[i] != vec2[i] || vec[i] != vec3[i])
        {
            cout << "ERROR\n";
            exit(-1);
        }
    }

    cout << "Done\n";

    return 0;
}
