#include <iostream>
#include <string>
#include <stdio.h>
#include <unistd.h>
#include <sys/ioctl.h>
#include <fstream>

using namespace std;

namespace lib  {
	void print(string text);
	string wrap(string text, size_t width);

	string loadChallengeData();
}
