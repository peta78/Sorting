using System;
using System.Collections.Generic;

public class HelloWorld
{
    public static int Sort(List<double> v)
    {
	if(v.Count < 150)
	{
		v.Sort();
		return 0;
	}

	int s = (int) Math.Sqrt(v.Count);

	List<double>[] x = new List<double>[s];
	for(int i=0;i<s;i++)
	{
		x[i] = new List<double>();
	}

	double min = 2.0;
	double max = -1.0;
	for(int i=0;i<v.Count;i++)
	{
		if(min>v[i])
		{
			min = v[i];
		}
		if(max<v[i])
		{
			max = v[i];
		}
	}
	max += 0.000001;
	//Console.WriteLine("{0},{1}",min,max);
	for(int i=0;i<v.Count;i++)
	{
		int p = (int)(((double)v[i]-min)/(max-min)*((double)s));
		x[p].Add(v[i]);
	}
	for(int i=0;i<s;i++)
	{
		Sort(x[i]);
	}

	v.Clear();
	for(int i=0;i<s;i++)
	{
		v.AddRange(x[i]);
	}

	return 1;
    }

    public static int Main()
    {
	Random r = new Random();
	List<double> v1, v2;
	int minsize = 1000;
	int maxsize = 10000000;
	int trials = 100;

	for(int q=0;q<trials;q++)
	{
	int size = minsize + (maxsize-minsize) * q / (trials-1);

	v1 = new List<double>();
	v2 = new List<double>();
	for(int i=0;i<size;i++)
	{
		double rn = r.NextDouble();
		v1.Add(rn);
		v2.Add(rn);
	}

	double t1 = DateTime.Now.Ticks / TimeSpan.TicksPerMillisecond;
	v1.Sort();
	double t2 = DateTime.Now.Ticks / TimeSpan.TicksPerMillisecond;
	Sort(v2);
	double t3 = DateTime.Now.Ticks / TimeSpan.TicksPerMillisecond;

	for(int i=0;i<v1.Count;i++)
	{
		if(v1[i]!=v2[i])
		{
			Console.WriteLine("Error");
			return -1;
		}
	}

	Console.WriteLine("{0},{1},{2}",v1.Count,(t2-t1)/1000.0,(t3-t2)/1000.0);

	}

	return 0;
    }
}