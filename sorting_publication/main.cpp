#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <chrono>
#include <ctime>
#include <iomanip>
#include <sstream>
#include <string>
#include <limits>
#include <cmath>
#include <cstring>

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

double randomUniform()
{
    return (double)rand() / RAND_MAX;
}

// https://stackoverflow.com/questions/75677/converting-a-uniform-distribution-to-a-normal-distribution
double gaussRandom()
{
    double u = 2.0*randomUniform()-1.0;
    double v = 2.0*randomUniform()-1.0;
    double r = u*u + v*v;

    if(r <= 0.0 || r >= 1.0) return gaussRandom();

    double c = sqrt(-2.0*log(r)/r);
    return u*c;
}

void statsort(vector<double> &vec, double min, double max)
{
    int memsize = sqrt(vec.size());
    std::vector<double> *myvectors = new std::vector<double>[memsize];

    for(long int i=0;i<vec.size();i++)
    {
        long int where = (int)((vec[i]-min) * (memsize + 0.0) / (max-min));

        myvectors[where].push_back(vec[i]);
    }

    for(long int i=0;i<memsize;i++)
    {
        if(myvectors[i].size()>10)
        {
            statsort(myvectors[i], min+(i+0.0)*(max-min)/memsize, min+(i+1.0)*(max-min)/memsize);
        }
        else
        {
            std::sort (myvectors[i].begin(), myvectors[i].end());
        }
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
    statsort(vec, min, max);
}

enum Distribution {
    Uniform,
    Gauss,
    Weird
};

int main(int argc, char **argv)
{
    long int min_size = 10000;
    long int max_size = 500000000;
    int num_sizes = 200;

    cout << argc << ",";
    for(int i=0;i<argc;i++)
    {
        cout << argv[i] << ",";
    }
    cout << "\n";

    enum Distribution dist;
    if(argc==1 || strcmp(argv[1],"uniform")==0)
    {
        dist = Uniform;
    }
    else if(strcmp(argv[1],"gauss")==0)
    {
        dist = Gauss;
    }
    else
    {
        dist = Weird;
    }

    ofstream logfile, distfile;
    logfile.open ("log.csv");
    distfile.open ("dist.csv");


    for(int j=0;j<num_sizes;j++)
    {
        long int size = min_size + (max_size-min_size) * j / (num_sizes-1);
        std::vector<double> myvector, myvector2;

        cout << j << "," << num_sizes << "," << size << "," << std::flush;
        logfile << j << "," << num_sizes << "," << size << "," << std::flush;

        for(long int i=0;i<size;i++)
        {
            double f;

            if(dist == Uniform)
            {
                f = randomUniform();
            }
            else if(dist == Gauss)
            {
                f = gaussRandom();
            }
            else
            {
                f = randomUniform();
                f = f * f;
            }

            myvector.push_back(f);
            myvector2.push_back(f);

            if(j==num_sizes-1 && i < 10000000)
            {
                distfile << f << "\n";
            }
        }

        logfile << time_in_HH_MM_SS_MMM() << "," << std::flush;
        cout << time_in_HH_MM_SS_MMM() << "," << std::flush;

        std::sort (myvector.begin(), myvector.end());

        logfile << time_in_HH_MM_SS_MMM() << "," << std::flush;
        cout << time_in_HH_MM_SS_MMM() << "," << std::flush;

        statsort(myvector2);

        logfile << time_in_HH_MM_SS_MMM() << "," << std::flush;
        cout << time_in_HH_MM_SS_MMM() << "," << std::flush;

        cout << "Verifying," << std::flush;

        for(long int i=0;i<myvector.size();i++)
        {
            if(myvector[i] != myvector2[i])
            {
                cout << "ERROR," << std::flush;
                exit(-1);
            }
        }
        logfile << "\n" << std::flush;
        cout << "\n" << std::flush;
    }

    cout << "Done\n" << std::flush;
    logfile.close();
    distfile.close();

    return 0;
}
