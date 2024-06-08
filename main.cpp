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
int numThreads = 1;

#define MEMSIZE 100000
void *wait(void *t) {
    int tid;

    tid = (long)t;

    for(int i=tid;i<MEMSIZE;i += numThreads)
    {
        std::sort (myvectors[i].begin(), myvectors[i].end());
    }

    pthread_exit(NULL);
}

void statsort(vector<double> &vec, int _numThreads)
{
    double min, max;

    numThreads = _numThreads;

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

    myvectors = new std::vector<double>[MEMSIZE];

    for(int i=0;i<vec.size();i++)
    {
        int where = (int)((vec[i]-min) * (MEMSIZE + 0.0) / (max-min));

        myvectors[where].push_back(vec[i]);
    }

    pthread_t *threads = new pthread_t[numThreads];
    pthread_attr_t attr;
    void *status;
    int rc;

    pthread_attr_init(&attr);
    pthread_attr_setdetachstate(&attr, PTHREAD_CREATE_JOINABLE);

    for(int i = 0; i < numThreads; i++ ) {
        rc = pthread_create(&threads[i], &attr, wait, (void *)((long)i));
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
    for(int i=0;i<MEMSIZE;i++)
    {
        for(int j=0;j<myvectors[i].size();j++)
        {
            vec.push_back(myvectors[i][j]);
        }
    }
    delete[] myvectors;
}

int main(void)
{
    cout << "hello\n";

    std::vector<double> myvector, myvector2, myvector3;

    for(int i=0;i<250000000;i++)
    {
        double f = (double)rand() / RAND_MAX;

        myvector.push_back(f);
        myvector2.push_back(f);
        myvector3.push_back(f);
    }

    cout << time_in_HH_MM_SS_MMM() << "\n";

    std::sort (myvector.begin(), myvector.end());

    cout << time_in_HH_MM_SS_MMM() << "\n";

    statsort(myvector2, 1);

    cout << time_in_HH_MM_SS_MMM() << "\n";

    cout << "Number of Threads " << std::thread::hardware_concurrency() << "\n";

    statsort(myvector3, std::thread::hardware_concurrency());

    cout << time_in_HH_MM_SS_MMM() << "\n";

    cout << "Verifying\n";

    for(int i=0;i<myvector.size();i++)
    {
        if(myvector[i] != myvector2[i] || myvector[i] != myvector3[i])
        {
            cout << "ERROR\n";
            exit(-1);
        }
    }

    cout << "Done\n";

    return 0;
}
