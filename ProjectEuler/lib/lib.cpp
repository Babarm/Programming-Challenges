#include "lib.h"

namespace lib {
	vector<string> loadData(int id) {

		vector<string> data;

		// String Format: xxx.txt
		string fileName = "";

		if (id < 10) {
			fileName += "00";
		} else if (id < 100) {
			fileName += "0";
		} 

		fileName += to_string(id);
		fileName += ".txt";
		
		data.push_back(fileName);
		return data;
	}
}
