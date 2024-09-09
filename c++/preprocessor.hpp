#ifndef AURUM_COMPILER_PREPROCESSOR
#define AURUM_COMPILER_PREPROCESSOR
#include "main_functions.hpp"
unsigned char preprocess_run(std::vector<std::string>& lines, std::vector<macro>& macros,std::vector<std::string>& files,std::string& direct) {
	unsigned long long count = 0;
	std::string line;
	std::vector<std::string> temp;
	std::vector<std::string> args;
	while (count < lines.size()) {
		line = lines.at(count);
		if (line.at(0) == '#') {
			if (line.at(1) == 'p') {
				if (line.at(2) == 'u') {
					if (line.at(3) == 't') {
						if (line.at(4) == ' ') {
							split(temp, line, ' ');
							if (!contains<macro, std::string>(macros, temp.at(1))) {
								return 2;
							}
							args = temp;
							remove<std::string>(args, 0);
							remove<std::string>(args, 0);
							macros.at(indexOf<macro, std::string>(macros, temp.at(1))).insert(lines, count, args);
							split(lines, join(lines, '\n'), '\n');
							return 0;
						}
					}
				}
			}
			else if (line.at(1) == 'i') {
				if (line.at(2) == 'n') {
					if (line.at(3) == 'c'){
						if (line.at(4) == 'l') {
							if (line.at(5) == 'u') {
								if (line.at(6) == 'd') {
									if (line.at(7) == 'e') {
										if (line.at(8) == ' ') {
											split(temp, line, ' ');
											if (!contains<std::string, std::string>(files, direct + temp.at(1) + ".header")) {
												lines[count] = load_file(direct + temp.at(1) + ".header");
												files.push_back(direct + temp.at(1) + ".header");
												split(lines, join(lines, '\n'), '\n');
											}
											else {
												remove<std::string>(lines, count);
											}
											return 0;
										}
										else if (line.at(8) == '_') {
											if (line.at(9) == 'e') {
												if (line.at(10) == 'x') {
													if (line.at(11) == ' ') {
														split(temp, line, ' ');
														if (!contains<std::string, std::string>(files, direct + temp.at(1))) {
															lines[count] = load_file(direct + temp.at(1));
															files.push_back(direct + temp.at(1));
															split(lines, join(lines, '\n'), '\n');
														}
														else {
															remove<std::string>(lines, count);
														}
														return 0;
													}
												}
											}
										}
									}
								}
							}
						}
					}
				}
			}
			else if (line.at(1) == 's') {
				if (line.at(2) == 't') {
					if (line.at(3) == 'a') {
						if (line.at(4) == 'r') {
							if (line.at(5) == 't') {
								if (line.at(6) == '_') {
									if (line.at(7) == 'd') {
										if (line.at(8) == 'e') {
											if (line.at(9) == 'f') {
												if (line.at(10) == ' ') {
													split(temp, line, ' ');
													args = temp;
													remove<std::string>(args, 0);
													remove<std::string>(args, 0);
													remove<std::string>(lines, count);
													macros.push_back(macro{ temp.at(1),args });
													while (true) {
														macros.at(macros.size() - 1).add_line(remove<std::string>(lines, count));
														if (macros.at(macros.size()-1)[macros.at(macros.size()-1).size() - 1] == "#end_def") {
															macros.at(macros.size() - 1)--;
															break;
														}
													}
													return 0;
												}
											}
										}
									}
								}
							}
						}
					}
				}
			}
			else if (line.at(1) == 'm') {
				if (line.at(2) == 'o') {
					if (line.at(3) == 'v') {
						if (line.at(4) == 'e') {
							if (line.at(5) == ' ') {
								split(temp, line, ' ');
								if (!(contains<macro, std::string>(macros, temp.at(1)))) {
									return 2;
								}
								args = temp;
								remove<std::string>(args, 0);
								remove<std::string>(args, 0);
								macros.at(indexOf<macro, std::string>(macros, temp.at(1))).insert(lines, count, args);
								remove<macro>(macros, indexOf<macro, std::string>(macros, temp.at(1)));
								split(lines, join(lines, '\n'), '\n');
								return 0;
							}
						}
					}
				}
			}
			else if (line.at(1) == 'z') {
				if (line.at(2) == 'd') {
					if (line.at(3) == 'r') {
						if (line.at(4) == 'i') {
							if (line.at(5) == 'n') {
								if (line.at(6) == 'g') {
									if (line.at(7) == ' ') {
										lines.at(count) = "sysout << \" testing \" ;";
									}
								}
							}
						}
					}
				}
			}
			else if (line.at(1) == 'u') {
				if (line.at(2) == 'n') {
					if (line.at(3) == 'd') {
						if (line.at(4) == 'e') {
							if (line.at(5) == 'f') {
								if (line.at(6) == ' ') {
									split(temp, line, ' ');
									if (!(contains<macro, std::string>(macros, temp.at(1)))) {
										return 2;
									}
									remove<macro>(macros, indexOf<macro, std::string>(macros, temp.at(1)));
									remove(lines, count);
									return 0;
								}
							}
						}
					}
				}
			}
		}
		else if (line.at(0) == '!') {
			remove<std::string>(lines, count);
			return 0;
		}
		count++;
	}
	return 1;
}
void preprocess(std::string name, std::string direct) {
	std::fstream file;
	std::vector<std::string> lines;
	std::vector<macro> macros;
	std::vector<std::string> files;
	split(lines, load_file(name), '\n');
	unsigned char err;
	bool flag = true;
	while (flag) {
		err = preprocess_run(lines, macros, files, direct);
		switch (err) {
		case 0:
			break;
		case 1:
			flag = 0;
			break;
		case 2:
			std::cerr << "\033[31mMacro does not exist[Crashing program]\n\033[0m";
			std::exit(1);
		default:
			std::cerr << "\033[31mMemory corrupted[Crashing program]\n\033[0m";
			std::exit(1);
		}
	}
	file.open(direct + name + ".aur_gold", std::ios::out);
	if (!file.is_open()) {
		std::cerr << "\033[31mFile failed to open[Crashing program]\n\033[0m";
		std::exit(1);
	}
	file << join(lines, '\n');
	file.close();
}
#endif
