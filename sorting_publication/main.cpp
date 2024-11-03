#include <iostream>
#include <algorithm>    // std::sort
#include <vector>       // std::vector
#include <chrono>
#include <ctime>
#include <iomanip>
#include <sstream>
#include <string>
#include <limits>
#include <cmath>

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

void statsort(vector<double> &vec)
{
    double min, max;

    min = std::numeric_limits<double>::max();
    max = std::numeric_limits<double>::lowest();

    for(long int i=0;i<vec.size();i++)
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

    int memsize = sqrt(vec.size());

    std::vector<double> *myvectors = new std::vector<double>[memsize];

    for(long int i=0;i<vec.size();i++)
    {
        long int where = (int)((vec[i]-min) * (memsize + 0.0) / (max-min));

        myvectors[where].push_back(vec[i]);
    }

    for(long int i=0;i<memsize;i++)
    {
        std::sort (myvectors[i].begin(), myvectors[i].end());
    }

    vec.clear();
    for(long int i=0;i<memsize;i++)
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
    long int min_size = 1000;
    long int max_size = 500000000;
    int num_sizes = 200;

    for(int j=0;j<num_sizes;j++)
    {
        long int size = min_size + (max_size-min_size) * j / (num_sizes-1);
        std::vector<double> myvector, myvector2;

        cout << j << "," << num_sizes << "," << size << ",";

        for(long int i=0;i<size;i++)
        {
            double f = (double)rand() / RAND_MAX;

            myvector.push_back(f);
            myvector2.push_back(f);
        }

        cout << time_in_HH_MM_SS_MMM() << ",";

        std::sort (myvector.begin(), myvector.end());

        cout << time_in_HH_MM_SS_MMM() << ",";

        statsort(myvector2);

        cout << time_in_HH_MM_SS_MMM() << ",";

        cout << "Verifying,";

        for(long int i=0;i<myvector.size();i++)
        {
            if(myvector[i] != myvector2[i])
            {
                cout << "ERROR,";
                exit(-1);
            }
        }
        cout << "\n" << std::flush;
    }

    cout << "Done\n";

    return 0;
}
