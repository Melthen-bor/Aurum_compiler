#ifndef AURUM_COMPILER_MAIN_FUNCTIONS
#define AURUM_COMPILER_MAIN_FUNCTIONS
#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <string>
void store_flags(unsigned char& flags, bool val, unsigned char loc) {
	switch (loc) {
	case 0:
		if (val) {
			flags |= 1;
		}
		else {
			flags &= 254;
		}
		break;
	case 1:
		if (val) {
			flags |= 2;
		}
		else {
			flags &= 253;
		}
		break;
	case 2:
		if (val) {
			flags |= 4;
		}
		else {
			flags &= 251;
		}
		break;
	case 3:
		if (val) {
			flags |= 8;
		}
		else {
			flags &= 247;
		}
		break;
	case 4:
		if (val) {
			flags |= 16;
		}
		else {
			flags &= 239;
		}
		break;
	case 5:
		if (val) {
			flags |= 32;
		}
		else {
			flags &= 223;
		}
		break;
	case 6:
		if (val) {
			flags |= 64;
		}
		else {
			flags *= 191;
		}
		break;
	case 7:
		if (val) {
			flags |= 128;
		}
		else {
			flags &= 127;
		}
		break;
	}
}
bool read_flag(unsigned char flags, unsigned char loc) {
	switch (loc) {
	case 0:
		return flags & 1;
	case 1:
		return flags & 2;
	case 2:
		return flags & 4;
	case 3:
		return flags & 8;
	case 4:
		return flags & 16;
	case 5:
		return flags & 32;
	case 6:
		return flags & 64;
	case 7:
		return flags & 128;
	}
}
std::string join(std::vector<std::string>& list, char connector) {
	std::string out = list.at(0);
	unsigned long long count = 1;
	while (count < list.size()) {
		out.push_back(connector);
		out += list.at(count);
		count++;
	}
	return out;
}
void split(std::vector<std::string>& out, std::string String, char delim) {
	std::string tempString;
	char tempChar;
	unsigned long long count = 0;
	while (count < String.size()) {
		tempChar = String.at(count);
		if (tempChar == delim) {
			out.push_back(tempString);
			tempString.clear();
		}
		else {
			tempString.push_back(tempChar);
		}
		count++;
	}
}
template<class A,class B> bool contains(std::vector<A>& list, B item) {
	unsigned long long count = 0;
	while (count < list.size()) {
		if (list.at(count) == item) {
			return true;
		}
	}
	return false;
}
template<class A,class B> unsigned long long indexOf(std::vector<A>& list, B item) {
	unsigned long long count = 0;
	while (count < list.size()) {
		if (list.at(count) == item) {
			return count;
		}
		count++;
	}
}
template<class T> T remove(std::vector<T>& list, unsigned long long index) {
	std::vector<T> out;
	T str;
	unsigned long long count = 0;
	while (count < list.size()) {
		if (!(count == index)) {
			out.push_back(list.at(count));
		}
		count++;
	}
	str = list.at(index);
	list = out;
	return str;
}
std::string load_file(std::string name) {
	std::ifstream file(name);
	if (!file.is_open()) {
		std::cerr << "\033[31mFile failed to open[Crashing program]\n\033[0m";
		std::exit(1);
	}
	std::vector<std::string> out;
	std::string temp;
	while (std::getline(file, temp)) {
		out.push_back(temp);
	}
	file.close();
	return join(out, '\n');
}
#endif
