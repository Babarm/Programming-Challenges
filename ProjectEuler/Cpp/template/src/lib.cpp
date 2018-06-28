#include "lib.h"

using namespace lib;

namespace lib  {

	void print(string text) {
		struct winsize w;
		ioctl(STDOUT_FILENO, TIOCGWINSZ, &w);
		
		text = wrap(text, w.ws_col);

		cout << text;

		return;
	}

	string wrap(string text, size_t width) {
		size_t curWidth = width;
		while(curWidth < text.length()) {
			string::size_type spacePos = text.rfind(' ', curWidth);
			if (spacePos == string::npos) {
				spacePos = text.find(' ', curWidth);
			} else {
				text[spacePos] = '\n';
				curWidth = spacePos + width + 1;
			}
		}
		text += '\n';
		return text;
	}

	string loadChallengeData() {
		ifstream infile("data.txt");
		string line;
		bool keepPrinting = true;
		string data;
		while(getline(infile, line)) {
			if(line == "[DATA]") {
				keepPrinting = false;
				continue;
			}

			if (keepPrinting) {
				print(line);
			} else {
				data += line;
			}
		}
		
		return data;
	}
}
