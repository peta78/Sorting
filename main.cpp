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

#define MEMSIZE 100000

int main(void)
{
    cout << "hello\n";

    std::vector<double> myvector, myvector_orig;

    for(int i=0;i<100000000;i++)
    {
        double f = (double)rand() / RAND_MAX;
        myvector.push_back(f);
        myvector_orig.push_back(f);
    }

    cout << time_in_HH_MM_SS_MMM() << "\n";

    std::sort (myvector.begin(), myvector.end());

    cout << time_in_HH_MM_SS_MMM() << "\n";

    std::vector<double>* myvectors = new std::vector<double>[MEMSIZE];

    for(int i=0;i<myvector_orig.size();i++)
    {
        int where = (int)(myvector_orig[i] * (MEMSIZE + 0.0));

        myvectors[where].push_back(myvector_orig[i]);
    }

    for(int i=0;i<MEMSIZE;i++)
    {
        std::sort (myvectors[i].begin(), myvectors[i].end());
    }

    cout << time_in_HH_MM_SS_MMM() << "\n";

    cout << "Verifying\n";

    int pos = 0;
    int loc = 0;
    for(int i=0;i<myvector.size();i++)
    {
        if(myvector[i] != myvectors[loc][pos])
        {
            cout << "Error!!!\n";
        }
        pos++;
        if(pos==myvectors[loc].size())
        {
            loc++;
            pos = 0;
        }
    }
    delete[] myvectors;

    cout << "Done\n";

    return 0;
}
