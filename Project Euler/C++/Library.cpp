#include "Library.h"

namespace library {
	bool is_prime(int val) {
		if(val < 2 || val % 2 == 0) return false;
		else if(val == 2) return true;
		else {
			for(int i = 3; i * i <= val; i += 2) {
				if(val % i == 0) return false;
			}
		}
		return true;
	};
}
