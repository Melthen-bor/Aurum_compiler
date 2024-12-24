#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <filesystem>
#define USER_ERROR "Ic forhealde the!\n"
unsigned char pass() {
	return 0;
}
struct token {
	unsigned long long type;
	std::string val = "";
};
typedef std::vector<token> Tokens;
struct Type {
	std::string name;
	char start_character;
};
typedef std::vector<Type> Types;
unsigned find_type(Types& types, std::string name) {
	unsigned handle = 0;
	while (handle < types.size()) {
		if (types.at(handle).name == name) break;
		handle++;
	}
	return handle;
}
bool does_type_exist(Types& types, std::string name){
	return !(find_type(types, name) == types.size());
}
unsigned find_type_with_char(Types& types, char start_char) {
	unsigned handle = 0;
	while (handle < types.size()) {
		if (types.at(handle).start_character == start_char) break;
		handle++;
	}
	return handle;
}
bool does_type_exist_with_char(Types& types, char start_char) {
	return !(find_type_with_char(types, start_char) == types.size());
}
struct Char {
	bool exist;
	char val;
	void print() {
		if (exist) std::cout << "true,";
		else std::cout << "false,";
		std::cout << (int)val << '\n';
	}
};
class lexer {
	unsigned long long index;
	std::string src;
	Char peek(unsigned long long ahead = 0) {
		if ((index + ahead) < src.size()) return Char{ true, this->src.at(index + ahead) };
		return Char{ false,'\0' };
	}
	char consume() {
		return this->src.at(this->index++);
	}
public:
	lexer(std::string source) {
		src = source;
		index = 0;
	}
	void reset(std::string source) {
		src = source;
		index = 0;
	}
	Tokens tokenize() {
		Tokens tkns;
		std::string buf;
		Char prev = { 0,0 };
		while (peek().exist) {
			if (isalpha(peek().val)) {
				buf.push_back(consume());
				while ((peek().exist && isalnum(peek().val))||peek().val=='_') buf.push_back(consume());
				if (buf == "return") tkns.push_back(token{ 1 });
				else if (buf == "start") tkns.push_back(token{ 38 });
				else if (buf == "end") tkns.push_back(token{ 39 });
				else if (buf == "program") tkns.push_back(token{ 40 });
				else if (buf == "class") tkns.push_back(token{ 41 });
				else if (buf == "auto") tkns.push_back(token{ 47 });
				else if (buf == "let") tkns.push_back(token{ 48 });
				else if (buf == "if") tkns.push_back(token{ 49 });
				else if (buf == "elf") tkns.push_back(token{ 50 });
				else if (buf == "else") tkns.push_back(token{ 51 });
				else if (buf == "unless") tkns.push_back(token{ 52 });
				else if (buf == "while") tkns.push_back(token{ 53 });
				else if (buf == "until") tkns.push_back(token{ 54 });
				else if (buf == "function") tkns.push_back(token{ 55 });
				else if (buf == "clr") tkns.push_back(token{ 56 });
				else if (buf == "member") tkns.push_back(token{ 58 });
				else if (buf == "sysout") tkns.push_back(token{ 59 });
				else if (buf == "procedure") tkns.push_back(token{ 60 });
				else if (buf == "sysin") tkns.push_back(token{ 61 });
				else if (buf == "create") tkns.push_back(token{ 64 });
				else if (buf == "destroy") tkns.push_back(token{ 65 });
				else if (buf == "letter") tkns.push_back(token{ 67 });
				else tkns.push_back(token{ 0,buf });
				buf.clear();
			}
			else if (isdigit(peek().val)) {
				buf.push_back(consume());
				while (peek().exist && isdigit(peek().val)) buf.push_back(consume());
				tkns.push_back(token{ 2,buf });
				buf.clear();
			}
			else if (peek().val == '"') {
				consume();
				while (peek().exist && !(peek().val == '"')) buf.push_back(consume());
				consume();
				tkns.push_back(token{ 3,buf });
				buf.clear();
			}
			else if (peek().val == ';') {
				consume();
				tkns.push_back(token{ 4 });
			}
			else if (peek().val == '+') {
				consume();
				switch (peek().val) {
				case 43:
					consume();
					tkns.push_back(token{ 16 });
					break;
				case 61:
					consume();
					tkns.push_back(token{ 17 });
					break;
				default:
					tkns.push_back(token{ 5 });
				}
			}
			else if (peek().val == '-') {
				consume();
				switch (peek().val) {
				case 62:
					consume();
					tkns.push_back(token{ 12 });
					break;
				case 61:
					consume();
					tkns.push_back(token{ 13 });
					break;
				case 45:
					consume();
					tkns.push_back(token{ 15 });
					break;
				default:
					tkns.push_back(token{ 6 });
				}
			}
			else if (peek().val == '/') {
				consume();
				tkns.push_back(token{ 7 });
			}
			else if (peek().val == '*') {
				consume();
				switch (peek().val) {
				case 61:
					consume();
					tkns.push_back(token{ 18 });
					break;
				case 42:
					consume();
					switch (peek().val) {
					case 61:
						consume();
						tkns.push_back(token{ 21 });
					default:
						tkns.push_back(token{ 19 });
					}
					break;
				default:
					tkns.push_back(token{ 8 });
				}
			}
			else if (peek().val == '&') {
				consume();
				switch (peek().val) {
				case 42:
					consume();
					tkns.push_back(token{ 9 });
					break;
				case 33:
					consume();
					tkns.push_back(token{ 10 });
					break;
				case 62:
					consume();
					tkns.push_back(token{ 11 });
					break;
				case 38:
					consume();
					tkns.push_back(token{ 20 });
					break;
				case 61:
					consume();
					tkns.push_back(token{ 22 });
					break;
				default:
					tkns.push_back(token{ 14 });
				}
			}
			else if (peek().val == '<') {
				consume();
				switch (peek().val) {
				case 60:
					consume();
					switch (peek().val) {
					case 61:
						consume();
						tkns.push_back(token{ 25 });
						break;
					default:
						tkns.push_back(token{ 24 });
					}
					break;
				default:
					tkns.push_back(token{ 23 });
				}
			}
			else if (peek().val == '>') {
				consume();
				switch (peek().val) {
				case 62:
					consume();
					switch (peek().val) {
					case 61:
						consume();
						tkns.push_back(token{ 28 });
						break;
					default:
						tkns.push_back(token{ 27 });
					}
					break;
				default:
					tkns.push_back(token{ 26 });
				}
			}
			else if (peek().val == '|') {
				consume();
				switch (peek().val) {
				case 61:
					consume();
					tkns.push_back(token{ 31 });
					break;
				case 124:
					consume();
					tkns.push_back(token{ 30 });
					break;
				default:
					tkns.push_back(token{ 29 });
				}
			}
			else if (peek().val == '^') {
				consume();
				switch (peek().val) {
				case 61:
					consume();
					tkns.push_back(token{ 34 });
					break;
				case 94:
					consume();
					tkns.push_back(token{ 33 });
					break;
				default:
					tkns.push_back(token{ 32 });
				}
			}
			else if (peek().val == '=') {
				consume();
				switch (peek().val) {
				case '=':
					consume();
					tkns.push_back(token{ 36 });
					break;
				default:
					tkns.push_back(token{ 35 });
				}
			}
			else if (peek().val == '[') {
				consume();
				while (peek().val != ']') {
					consume();
				}
				consume();
			}
			else if (peek().val == '@') {
				consume();
				while (peek().val != ' ' && peek().val != '\n') buf.push_back(consume());
				tkns.push_back(token{ 37,buf });
			}
			else if (peek().val == '{') {
				consume();
				tkns.push_back(token{ 42 });
			}
			else if (peek().val == '}') {
				consume();
				tkns.push_back(token{ 43 });
			}
			else if (peek().val == '(') {
				consume();
				tkns.push_back(token{ 44 });
			}
			else if (peek().val == ')') {
				consume();
				tkns.push_back(token{ 45 });
			}
			else if (peek().val == '$') {
				consume();
				tkns.push_back(token{ 47 });
			}
			else if (peek().val == ',') {
				consume();
				tkns.push_back(token{ 57 });
			}
			else if (peek().val == '%') {
				consume();
				switch (peek().val) {
				case 61:
					consume();
					tkns.push_back(token{ 66 });
					break;
				case 62:
					consume();
					tkns.push_back(token{ 62 });
					break;
				default:
					tkns.push_back(token{ 63 });
				}
			}
			else {
				consume();
			}
		}
		return tkns;
	}
};
struct flags {
	unsigned char val;
	flags() {
		this->val = 0;
	}
	bool get(unsigned char loc) {
		return this->val & (1 << loc);
	}
	void store(unsigned char loc, bool val) {
		if (val) this->val |= (1 << loc);
		else this->val &= 255 - (1 << loc);
	}
};
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
		else tempString.push_back(tempChar);
		count++;
	}
	out.push_back(tempString);
}
template<class A,class B> bool contains(std::vector<A>& list, B item) {
	unsigned long long count = 0;
	while (count < list.size()) if (list.at(count++) == item) return true;
	return false;
}
template<class A,class B> unsigned long long indexOf(std::vector<A>& list, B item) {
	unsigned long long count = 0;
	while (count < list.size()) if (list.at(count++) == item) return count-1;
	return list.size();
}
template<class T> T remove(std::vector<T>& list, unsigned long long index) {
	std::vector<T> out;
	T str;
	unsigned long long count = 0;
	while (count < list.size()) if (!(count == index)) out.push_back(list.at(count++));
	str = list.at(index);
	list = out;
	return str;
}
class macro {
	std::vector<std::string> lines;
	std::vector<std::string> arguments;
	std::string name;
public:
	macro() {
		pass();
	}
	macro(std::string name,std::vector<std::string> args) {
		this->name = name;
		this->lines = std::vector<std::string>();
		this->arguments = args;
	}
	void add_line(std::string line) {
		this->lines.push_back(line);
	}
	std::string format_line(std::vector<std::string>& values,unsigned long long line) {
		std::vector<std::string> tokens;
		split(tokens, this->lines.at(line), ' ');
		unsigned long long count = 0;
		while (count < tokens.size()) if (contains<std::string,std::string>(this->arguments, tokens.at(count))) tokens[count] = values.at(indexOf<std::string,std::string>(this->arguments, tokens.at(count++)));
		return join(tokens, ' ');
	}
	void insert(std::vector<std::string>& lines, unsigned long long line,std::vector<std::string>& values) {
		std::vector<std::string> format_lines;
		unsigned long long count = 0;
		while (count < this->lines.size()) format_lines.push_back(this->format_line(values, count++));
		lines[line] = join(format_lines, '\n');
	}
	bool operator ==(std::string name) {
		return this->name == name;
	}
	std::string operator --(int amount) {
		return remove<std::string>(this->lines, this->lines.size() - 1);
	}
	std::string operator [](int line) {
		return this->lines.at(line);
	}
	int size() {
		return this->lines.size();
	}
};
std::string load_file(std::string name) {
	std::ifstream file(name);
	if (!file.is_open()) {
		std::cerr << "\033[31mFile failed to open[Crashing program]\n\033[0m";
		std::exit(1);
	}
	std::vector<std::string> out;
	std::string temp;
	while (std::getline(file, temp)) out.push_back(temp);
	file.close();
	return join(out, '\n');
}
unsigned char preprocess_run(std::vector<std::string>& lines, std::vector<macro>& macros,std::vector<std::string>& files) {
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
							if (!contains<macro, std::string>(macros, temp.at(1))) return 2;
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
											if (!contains<std::string, std::string>(files, temp.at(1) + ".header")) {
												lines[count] = load_file(temp.at(1) + ".header");
												files.push_back(temp.at(1) + ".header");
												split(lines, join(lines, '\n'), '\n');
											}
											else remove<std::string>(lines, count);
											return 0;
										}
										else if (line.at(8) == '_') {
											if (line.at(9) == 'e') {
												if (line.at(10) == 'x') {
													if (line.at(11) == ' ') {
														split(temp, line, ' ');
														if (!contains<std::string, std::string>(files,temp.at(1))) {
															lines[count] = load_file(temp.at(1));
															files.push_back(temp.at(1));
															split(lines, join(lines, '\n'), '\n');
														}
														else remove<std::string>(lines, count);
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
								if (!(contains<macro, std::string>(macros, temp.at(1)))) return 2;
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
									if (line.at(7) == ' ') lines.at(count) = "sysout << \"testing+\";";
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
									if (!(contains<macro, std::string>(macros, temp.at(1)))) return 2;
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
std::string preprocess(std::string name) {
	std::vector<std::string> lines;
	std::vector<macro> macros;
	std::vector<std::string> files;
	split(lines, load_file(name), '\n');
	unsigned char err;
	bool flag = true;
	while (flag) {
		err = preprocess_run(lines, macros, files);
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
	return join(lines, '\n');
}
void load_flags(std::vector<std::string>& flags, char* argv[], int argc) {
	int count = 0;
	if (argc < 2) {
		std::cout << USER_ERROR;
		std::exit(1);
	}
	while (count < argc) flags.push_back(argv[count++]);
}
struct Variable {
	unsigned long long type;
	unsigned char ptr_type;
	std::string name;
};
typedef std::vector<Variable> Variables;
unsigned find_variable(Variables& variables, std::string name) {
	unsigned count = 0;
	while (count < variables.size()) {
		if (variables.at(count).name == name) break;
		count++;
	}
	return count;
}
bool does_variable_exist(Variables& variables, std::string name) {
	return !(find_variable(variables, name) == variables.size());
}
struct Argument {
	unsigned long long value_type;
	unsigned char type_of_argument;
	std::string name;
};
typedef std::vector<Argument> Arguments;
unsigned find_argument(Arguments& args, std::string name) {
	unsigned count = 0;
	while (count < args.size()) {
		if (args.at(count).name == name) break;
		count++;
	}
	return count;
}
bool does_argument_exist(Arguments& args, std::string name) {
	return !(find_argument(args, name) == args.size());
}
struct Args {
	Arguments args;
	unsigned char flags;
};
struct Function {
	std::string name;
	Arguments args;
	unsigned long long Rtype;
	unsigned char ptr_type;
	bool no_discard;
};
typedef std::vector<Function> Functions;
unsigned find_function(Functions& functions, std::string name) {
	unsigned count = 0;
	while (count < functions.size()) {
		if (functions.at(count).name == name) break;
		count++;
	}
	return count;
}
bool does_function_exist(Functions& functions, std::string name) {
	return !(find_function(functions, name) == functions.size());
}
struct Procedure {
	std::string name;
	Arguments args;
};
typedef std::vector<Procedure> Procedures;
unsigned find_procedure(Procedures& procedures, std::string name) {
	unsigned count = 0;
	while (count < procedures.size()) {
		if (procedures.at(count).name == name) break;
		count++;
	}
	return count;
}
bool does_procedure_exist(Procedures& procedures, std::string name) {
	return !(find_procedure(procedures, name) == procedures.size());
}
struct Class {
	std::string name;
	Functions methods;
	Variables members;
	Procedures procedures;
	bool doth_arg_exist(std::string name) {
		return does_argument_exist(methods.at(methods.size() - 1).args, name);
	}
	bool doth_proc_arg_exist(std::string name) {
		return does_argument_exist(procedures.at(procedures.size() - 1).args, name);
	}
	Argument& get_arg(std::string name) {
		return methods.at(methods.size() - 1).args.at(find_argument(methods.at(methods.size() - 1).args, name));
	}
	Argument& get_proc_arg(std::string name) {
		return procedures.at(procedures.size() - 1).args.at(find_argument(procedures.at(procedures.size() - 1).args, name));
	}
};
typedef std::vector<Class> Classes;
unsigned find_class(Classes& classes, std::string name) {
	unsigned count = 0;
	while (count < classes.size()) {
		if (classes.at(count).name == name) break;
		count++;
	}
	return count;
}
struct Constant {
	std::string name;
	std::string value;
};
typedef std::vector<Constant> Constants;
unsigned find_constant(Constants& constants, std::string name) {
	unsigned count = 0;
	while (count < constants.size()) {
		if (constants.at(count).name == name) break;
		count++;
	}
	return count;
}
bool does_constant_exist(Constants& constants, std::string name) {
	return !(find_constant(constants, name) == constants.size());
}
unsigned char is_what(Types& types, Functions& functions, Variables& variables,Constants& constants,std::string name) {
	if (does_type_exist(types, name)) return 1;
	if (does_function_exist(functions, name)) return 2;
	if (does_variable_exist(variables, name)) return 3;
	if (does_constant_exist(constants, name)) return 4;
	return 0;
}
struct node {
	unsigned char type;
	token tkn;
	node* nd_one;
	node* nd_two;
	node(token tkn) {
		this->type = 1;
		this->tkn = tkn;
		this->nd_one = nullptr;
		this->nd_two = nullptr;
	}
	node(node* one, node* two) {
		this->type = 2;
		this->nd_one = one;
		this->nd_two = two;
	}
	unsigned long long level() {
		if (this->type < 2) return this->type;
		if (this->nd_one->level() > this->nd_two->level()) return this->nd_one->level() + 1;
		return this->nd_two->level() + 1;
	}
};
class parse_tree {
	std::vector<node*> nodes;
	unsigned long long current_level;
public:
	parse_tree(Tokens tkns) {
		unsigned long long index = 0;
		while (index < tkns.size()) {
			nodes.push_back(new node(tkns.at(index)));
			index++;
		}
		this->current_level = 1;
	}
	void collapse() {
		unsigned long long index = 0;
		while (index < this->nodes.size()) {
			if (this->nodes[index]->level() == this->current_level) {

			}
			index++;
		}
	}
	node* get_tree() {
		return this->nodes[0];
	}
};
struct scope {
	Variables variables;
	Constants constants;
	bool is_class=false;
	bool is_function = false;
};
typedef std::vector<scope> Scopes;
typedef unsigned char language_type;
typedef unsigned char system_type;
void print(Tokens& tkns) {
	unsigned long long index = 0;
	while (index < tkns.size()) {
		std::cout << tkns.at(index).type << ':' << tkns.at(index).val << '\n';
		index++;
	}
}
void print(Tokens& tkns,unsigned long long& index) {
	std::cout << index << ':' << tkns.at(index).type << ':' << tkns.at(index).val << '\n';
}
class compiler {
	Types types;
	Classes classes;
	Functions functions;
	Procedures procedures;
	Scopes scopes;
	flags mode;
	unsigned long long index;
public:
	compiler() {
		types = Types();
		types.push_back(Type{ "byte",'b' });
		types.push_back(Type{ "char",'c' });
		types.push_back(Type{ "Sbyte",'B' });
		types.push_back(Type{ "Umini",'m' });
		types.push_back(Type{ "mini",'M' });
		types.push_back(Type{ "Ucint",'t' });
		types.push_back(Type{ "cint",'T' });
		types.push_back(Type{ "Ulong",'i' });
		types.push_back(Type{ "long",'I' });
		types.push_back(Type{ "Ullong",'l' });
		types.push_back(Type{ "llong",'L' });
		types.push_back(Type{ "str",'s' });
		scopes.push_back({});
	}
	Args get_args(std::ofstream& file,Tokens& tkns) {
		Arguments args;
		unsigned char loop = 1;
		file << '(';
		while (loop) {
			if (index == tkns.size()) {
				std::cout << USER_ERROR;
				std::exit(1);
			}
			print(tkns, index);
			switch (tkns.at(index).type) {
			case 0:
				switch (tkns.at(index + 1).type) {
				case 0:
					file << tkns.at(index).val << ' ' << tkns.at(index + 1).val;
					args.push_back({ find_type(types,tkns.at(index).val),0,tkns.at(index + 1).val });
					index++;
					break;
				case 9:
					if (!tkns.at(index + 2).type) return { args,1 };
					file << tkns.at(index).val << "* " << tkns.at(index + 1).val;
					if (mode.get(0)) args.push_back({ find_type(types,tkns.at(index).val),2,tkns.at(index + 2).val });
					else args.push_back({ find_type(types,tkns.at(index).val),1,tkns.at(index + 2).val });
					mode.store(0, 0);
					index += 2;
					break;
				default:
					std::cout << "Args:thing doth not exist\n";
					return { args,1 };
				}
				break;
			case 37:
				if (tkns.at(index).val == "ARRAY_POINTER") mode.store(0, 1);
				break;
			case 42:
				file << '(';
				loop++;
				break;
			case 43:
				file << ')';
				loop--;
				break;
			case 47:
				switch (tkns.at(index + 1).type) {
				case 0:
					file << types.at(find_type_with_char(types, tkns.at(index + 1).val[0])).name << ' ' << tkns.at(index + 1).val;
					args.push_back({ find_type_with_char(types,tkns.at(index+1).val[0]),0,tkns.at(index + 1).val});
					index++;
					break;
				case 9:
					if (!tkns.at(index + 2).type) return { args,1 };
					file << types.at(find_type_with_char(types, tkns.at(index + 1).val[0])).name << "* " << tkns.at(index + 1).val;
					args.push_back({ find_type_with_char(types,tkns.at(index + 2).val[0]),1,tkns.at(index + 2).val });
					index += 2;
					break;
				default:

					return { args,1 };
				}
				break;
			case 57:
				file << ',';
				break;
			default:
				std::cout << "Args:token type not recognized\n";
				return { args,1 };
			}
			index++;
		}
		return { args,0 };
	}
	std::string indent(unsigned long long amount) {
		std::string out;
		while (amount > 0) {
			out.push_back(9);
			amount--;
		}
		return out;
	}
	void setup_cpp(std::ofstream& file) {
		file << "#include <string>\n";
		file << "#include <iostream>\n";
		file << "typedef std::string str;\n";
		//file << "struct byte{\n";
		//file << "unsigned char data;\n";
		//file << "byte(unsigned char);\n";
		//file << "byte add(byte other);\n";
		//file << "void ass(byte other);\n"
		//file << "};\n";
		file << "typedef unsigned char byte;\n";
		file << "typedef signed char Sbyte;\ntypedef unsigned short Umini;\ntypedef short mini;\ntypedef unsigned Ucint;\ntypedef int cint;\n";
		file << "typedef unsigned long Ulong;\ntypedef unsigned long long Ullong;\ntypedef long long llong;";
		//std::ofstream Lfile("defaults.cpp");
		//Lfile << "#include <declarations.hpp>\n";
		//Lfile << "byte::byte(unsigned char value){\n";
		//Lfile << "  this->data=value;\n";
		//Lfile << "}\n";
		//Lfile << "byte byte::add(byte other){\n";
		//Lfile << "  return this->data+other.data;\n";
		//Lfile << "}\n";
		//Lfile << "void byte::ass(byte other){\n";
		//Lfile << " this->data=other.data;\n";
		//Lfile << "}\n";
		//Lfile.close();
	}
	void setup_c() {
		std::ofstream Lfile("language_defaults.h");
		Lfile << "#ifndef LANGUAGE_DEFAULTS\n#define LANGUAGE_DEFAULTS\n#include <stdio.h>\n#include <stdlib.h>\ntypedef unsigned char byte;\n";
		Lfile << "typedef signed char Sbyte;\ntypedef unsigned short Umini;\ntypedef short mini;\ntypedef unsigned Ucint;\ntypedef int cint;\n";
		Lfile << "typedef unsigned long Ulong;\ntypedef unsigned long long Ullong;\ntypedef long long llong;\n#endif";
		Lfile.close();
	}
	bool doth_constant_exist(std::string name) {
		unsigned index = 0;
		while (index < scopes.size()) if (does_constant_exist(scopes.at(index++).constants, name)) return 1;
		return 0;
	}
	unsigned get_constant_scope(std::string name) {
		unsigned index = scopes.size();
		while (index > 0) if (does_constant_exist(scopes.at(--index).constants, name)) break;
		return index;
	}
	bool doth_variable_exist(std::string name){
		unsigned index = 0;
		while (index < scopes.size()) if (does_variable_exist(scopes.at(index++).variables, name)) return 1;
		return 0;
	}
	unsigned get_variable_scope(std::string name) {
		unsigned index = scopes.size();
		while (index > 0) if (does_variable_exist(scopes.at(--index).variables, name)) break;
		return index;
	}
	bool doth_argument_exist(std::string name) {
		if (!functions.size()) return 0;
		return does_argument_exist(functions.at(functions.size() - 1).args, name);
	}
	Argument& get_argument(std::string name) {
		return functions.at(functions.size() - 1).args.at(find_argument(functions.at(functions.size() - 1).args, name));
	}
	Argument& get_proc_argument(std::string name) {
		return procedures.at(procedures.size() - 1).args.at(find_argument(procedures.at(procedures.size() - 1).args, name));
	}
	bool doth_proc_argument_exist(std::string name) {
		if (!procedures.size()) return 0;
		return does_argument_exist(procedures.at(procedures.size() - 1).args, name);
	}
	unsigned long long compile_cpp(Tokens tkns,std::string& name,flags& values,system_type sys) {
		index = 0;
		bool inClass = false;
		bool isMember = false;
		bool inFunction = false;
		bool inProgram = false;
		bool is_last_varPointer = false;
		bool afterAssignment = false;
		bool afterReturn = false;
		bool inProcedure = false;
		//bool afterOperation = false;
		print(tkns);
		unsigned char stream_type = 0;
		unsigned long long last_var_type = 0;
		std::ofstream file(name + ".cpp");
		if (!file.is_open()) {
			std::cout << USER_ERROR;
			return 2;
		}
		file << "#include <declarations.hpp>\n";
		while (index < tkns.size()) {
			print(tkns, index);
			switch (tkns[index].type) {
			case 0:
				switch (tkns.at(index + 1).type) {
				case 0:
					{
						unsigned long long type = find_type(types, tkns.at(index).val);
						if (type == types.size()) return 1;
						if (isMember) classes.at(classes.size() - 1).members.push_back({ type,0,tkns.at(index + 1).val });
						else {
							file << types.at(type).name << ' ' << tkns.at(index + 1).val;
							scopes.at(scopes.size() - 1).variables.push_back({ type,0,tkns.at(index + 1).val });
						}
						index++;
					}
					break;
				case 9:
					if (!tkns.at(index + 2).type) return 1;
					{
						unsigned long long type = find_type(types, tkns.at(index).val);
						unsigned char ptr_type = 1;
						if (mode.get(2)) ptr_type = 3;
						else if (mode.get(0)) ptr_type = 2;
						if (type == types.size()) return 1;
						if (isMember) classes.at(classes.size() - 1).members.push_back({type,1,tkns.at(index+2).val});
						else {
							file << types.at(type).name << "* " << tkns.at(index + 2).val;
							scopes.at(scopes.size() - 1).variables.push_back({ type,1,tkns.at(index + 2).val });
						}
						index+=2;
					}
					break;
				default:
					if (doth_constant_exist(tkns.at(index).val)) file << scopes.at(get_constant_scope(tkns.at(index).val)).constants.at(find_constant(scopes.at(get_constant_scope(tkns.at(index).val)).constants, tkns.at(index).val)).value;
					else if (doth_variable_exist(tkns.at(index).val)) {
						last_var_type = scopes.at(get_variable_scope(tkns.at(index).val)).variables.at(find_variable(scopes.at(get_variable_scope(tkns.at(index).val)).variables, tkns.at(index).val)).type;
						is_last_varPointer = scopes.at(get_variable_scope(tkns.at(index).val)).variables.at(find_variable(scopes.at(get_variable_scope(tkns.at(index).val)).variables, tkns.at(index).val)).ptr_type;
						file << tkns.at(index).val;
					}
					else if (inFunction && doth_argument_exist(tkns.at(index).val)&&!inClass) {
						last_var_type = get_argument(tkns.at(index).val).value_type;
						is_last_varPointer = get_argument(tkns.at(index).val).type_of_argument;
						file << tkns.at(index).val;
					}
					else if (inProcedure && doth_proc_argument_exist(tkns.at(index).val)&&!inClass) {
						last_var_type = get_proc_argument(tkns.at(index).val).value_type;
						is_last_varPointer = get_proc_argument(tkns.at(index).val).type_of_argument;
						file << tkns.at(index).val;
					}
					else if (inFunction && inClass && classes.at(classes.size() - 1).doth_arg_exist(tkns.at(index).val)) {
						last_var_type = classes.at(classes.size() - 1).get_arg(tkns.at(index).val).value_type;
						is_last_varPointer = classes.at(classes.size() - 1).get_arg(tkns.at(index).val).type_of_argument;
						file << tkns.at(index).val;
					}
					else if (inProcedure && inClass && classes.at(classes.size() - 1).doth_proc_arg_exist(tkns.at(index).val)) {
						last_var_type = classes.at(classes.size() - 1).get_proc_arg(tkns.at(index).val).value_type;
						is_last_varPointer = classes.at(classes.size() - 1).get_proc_arg(tkns.at(index).val).type_of_argument;
						file << tkns.at(index).val;
					}
					else if (does_function_exist(functions, tkns.at(index).val)) {
						last_var_type = functions.at(find_function(functions, tkns.at(index).val)).Rtype;
						is_last_varPointer = functions.at(find_function(functions, tkns.at(index).val)).ptr_type;
						if (functions.at(find_function(functions, tkns.at(index).val)).no_discard && !afterAssignment) return 1;
						file << tkns.at(index).val;
					}
					else if (does_procedure_exist(procedures, tkns.at(index).val)) file << tkns.at(index).val;
					else if (inProgram) {
						if (tkns.at(index).val == "argc") file << "argc";
						else if (tkns.at(index).val == "argv") {
							file << "argv";
							if (tkns.at(index + 1).type == 1) {
								file << '[' << tkns.at(index + 1).val << ']';
								index++;
							}
						}
					}
					else return 1;
				}
				break;
			case 1:
			if(!mode.get(4)){
				unsigned var_index = 0;
				unsigned scope_index = 1;
				while (!scopes.at(scopes.size()-scope_index).is_function) {
					var_index = 0;
					while (var_index < scopes[scopes.size() - scope_index].variables.size()) {
						switch (scopes[scopes.size() - scope_index].variables[var_index].ptr_type) {
						case 1:
							file << indent(scopes.size()) << "delete " << scopes[scopes.size() - scope_index].variables[var_index].name << ";\n";
							break;
						case 2:
							file << indent(scopes.size()) << "delete[] " << scopes[scopes.size() - scope_index].variables[var_index].name << ";\n";
							break;
						}
						index++;
					}
					scope_index++;
				}
			}
			file << "return ";
			if ((tkns.at(index + 1).type == 0) || (tkns.at(index + 1).type == 2) || (tkns.at(index + 1).type == 3)) {
				index++;
				file << tkns.at(index).val;
			}
			afterReturn = true;
			break;
			case 2:
				file << tkns.at(index).val;
				break;
			case 3:
				file << '"' << tkns.at(index).val << '"';
				break;
			case 4:
				last_var_type = 0;
				is_last_varPointer = 0;
				[[unlikely]] if (stream_type) stream_type = 0;
				if (inClass) {
					if (tkns.at(index + 1).type == 39) file << ";\n" << indent(scopes.size() - 3);
					else if (!isMember) file << ";\n" << indent(scopes.size() - 2);
				}
				else if (tkns.at(index + 1).type == 39) file << ";\n" << indent(scopes.size() - 2);
				else file << ";\n" << indent(scopes.size() - 1);
				isMember = false;
				break;
			case 5:
				/*if (!tkns.at(index - 1).type) {
					file << ".add(";
					index++;
					if (tkns.at(index).type == 9) {
						file << '*';
						index++;
					}
					if (tkns.at(index).type) return 1;
					else file << tkns.at(index).val << ')';
				}
				else file << '+';*/
				file << '+';
				break;
			case 6:
				file << '-';
				break;
			case 7:
				file << '*';
				break;
			case 8:
				file << '/';
				break;
			case 9:
				index++;
				[[unlikely]] if (tkns.at(index).type) return 1;
				[[likely]] if (!(doth_variable_exist(tkns.at(index).val))) return 1;
				[[unlikely]] if (!(scopes.at(get_variable_scope(tkns.at(index).val)).variables.at(find_variable(scopes.at(get_variable_scope(tkns.at(index).val)).variables, tkns.at(index).val)).ptr_type)) return 1;
				file << "(*" << tkns.at(index).val << ')';
				break;
			case 10:
				file << '~';
				break;
			case 11:
				index++;
				[[unlikely]] if (!inClass) {
					std::cout << "not in class\n";
					return 1;
				}
				[[unlikely]] if (tkns.at(index).type) {
					std::cout << "non-identifier after symbol[&>]\n";
					return 1;
				}
				[[unlikely]] if (does_variable_exist(classes.at(classes.size() - 1).members, tkns.at(index).val)) last_var_type = classes.at(classes.size() - 1).members.at(find_variable(classes.at(classes.size() - 1).members, tkns.at(index).val)).type;
				else if (does_function_exist(classes.at(index).methods, tkns.at(index).val)) {
					last_var_type = classes.at(classes.size() - 1).methods.at(find_function(classes.at(classes.size() - 1).methods, tkns.at(index).val)).Rtype;
					if (classes.at(classes.size() - 1).methods.at(find_function(classes.at(classes.size() - 1).methods, tkns.at(index).val)).no_discard && !afterAssignment) return 1;
				}
				else if (does_procedure_exist(classes.at(index).procedures, tkns.at(index).val)) pass();
				else {
					std::cout << "unrecognized\n";
					return 1;
				}
				file << "this->" << tkns.at(index).val;
				break;
			case 12:
				index++;
				[[unlikely]] if (tkns.at(index).type) return 1;
				[[likely]] if ((!(does_function_exist(classes.at(find_class(classes, types.at(last_var_type).name)).methods, tkns.at(index).val)))&&(!(does_procedure_exist(classes.at(find_class(classes,types.at(last_var_type).name)).procedures,tkns.at(index).val)))) return 1;
				if (is_last_varPointer) file << "->" << tkns.at(index).val;
				else file << '.' << tkns.at(index).val;
				if (does_function_exist(classes.at(find_class(classes, types.at(last_var_type).name)).methods, tkns.at(index).val)) {
					if (classes.at(find_class(classes, types.at(last_var_type).name)).methods.at(find_function(classes.at(find_class(classes, types.at(last_var_type).name)).methods, tkns.at(index).val)).no_discard && !afterAssignment) return 1;
					last_var_type = classes.at(find_class(classes, types.at(last_var_type).name)).methods.at(find_function(classes.at(find_class(classes, types.at(last_var_type).name)).methods, tkns.at(index).val)).Rtype;
				}
				break;
			case 13:
				file << "-=";
				afterAssignment = true;
				break;
			case 14:
				file << '&';
				break;
			case 15:
				file << "--";
				break;
			case 16:
				file << "++";
				break;
			case 17:
				file << "+=";
				afterAssignment = true;
				break;
			case 18:
				file << "*=";
				afterAssignment = true;
				break;
			case 19:
				std::cout << "Not yet implemented!\n";
				break;
			case 20:
				file << "&&";
				break;
			case 21:
				std::cout << "Not yet implemented!\n";
				break;
			case 22:
				file << "&=";
				afterAssignment = true;
				break;
			case 23:
				file << '<';
				break;
			case 24:
				if (!(stream_type == 2)) file << "<<";
				else return 1;
				break;
			case 25:
				file << "<<=";
				afterAssignment = true;
				break;
			case 26:
				file << '>';
				break;
			case 27:
				if (!(stream_type == 1)) file << ">>";
				else return 1;
				break;
			case 28:
				file << ">>=";
				afterAssignment = true;
				break;
			case 29:
				file << '|';
				break;
			case 30:
				file << "||";
				break;
			case 31:
				file << "|=";
				afterAssignment = true;
				break;
			case 32:
				file << '^';
				break;
			case 33:
				std::cout << "Not yet implemented!\n";
				break;
			case 34:
				file << "^=";
				afterAssignment = true;
				break;
			case 35:
				//file << ".ass(";
				//index++;
				//if (tkns.at(index).type == 9) {
				//	file << '*';
				//	index++;
				//}
				file << '=';
				afterAssignment = true;
				break;
			case 36:
				file << "==";
				break;
			case 37:
				if (tkns.at(index).val == "ARRAY_POINTER") mode.store(0, 1);
				else if (tkns.at(index).val == "POINTER_FUNCTION") mode.store(1, 1);
				else if (tkns.at(index).val == "RETURN_POINTER") mode.store(2, 1);
				else if (tkns.at(index).val == "NO_DISCARD") mode.store(3, 1);
				else if (tkns.at(index).val == "AUTO") mode.store(4, 0);
				else if (tkns.at(index).val == "MANUAL") mode.store(4, 1);
				else if (tkns.at(index).val == "VARS") {
					unsigned scope_index = 0;
					unsigned var_index;
					Variable temp;
					while (scope_index < scopes.size()) {
						var_index = 0;
						while (var_index < scopes.at(scope_index).variables.size()) {
							temp = scopes.at(scope_index).variables.at(var_index);
							std::cout << scope_index << ',' << temp.name << ',' << temp.type << ',' << temp.ptr_type << '\n';
							var_index++;
						}
						scope_index++;
					}
				}
				else if (tkns.at(index).val == "CONSTS") {
					unsigned scope_index = 0;
					unsigned var_index;
					Constant temp;
					while (scope_index < scopes.size()) {
						var_index = 0;
						while (var_index < scopes.at(scope_index).constants.size()) {
							temp = scopes.at(scope_index).constants.at(var_index);
							std::cout << scope_index << ',' << temp.name << ',' << temp.value << '\n';
							var_index++;
						}
						scope_index++;
					}
				}
				else if (tkns.at(index).val == "TYPE") {
					index++;
					if (tkns.at(index).type) return 1;
					std::cout << types.at(scopes.at(get_variable_scope(tkns.at(index).val)).variables.at(find_variable(scopes.at(get_variable_scope(tkns.at(index).val)).variables, tkns.at(index).val)).type).name;
				}
				break;
			case 38:
				if (inClass) file << "{\n" << indent(scopes.size() - 1);
				else file << "{\n" << indent(scopes.size());
				scopes.push_back({});
				break;
			case 39:
				if ((!mode.get(4))&&(!afterReturn)) {
					while (scopes[scopes.size() - 1].variables.size() > 0) {
						switch (scopes[scopes.size() - 1].variables[scopes[scopes.size()-1].variables.size()-1].ptr_type) {
						case 1:
							if(inClass) file << indent(scopes.size() - 2) << "delete " << scopes[scopes.size() - 1].variables[scopes[scopes.size() - 1].variables.size() - 1].name << ";\n";
							else file << indent(scopes.size()-1) << "delete " << scopes[scopes.size() - 1].variables[scopes[scopes.size() - 1].variables.size() - 1].name << ";\n";
							break;
						case 2:
							if(inClass) file << indent(scopes.size() - 2) << "delete[] " << scopes[scopes.size() - 1].variables[scopes[scopes.size() - 1].variables.size() - 1].name << ";\n";
							else file << indent(scopes.size()-1) << "delete[] " << scopes[scopes.size() - 1].variables[scopes[scopes.size() - 1].variables.size() - 1].name << ";\n";
							break;
						}
						scopes[scopes.size() - 1].variables.pop_back();
					}
				}
				if (scopes.at(scopes.size() - 1).is_class) {
					inClass = false;
				}
				else file << "}\n";
				if (scopes.at(scopes.size() - 1).is_function) {
					inFunction = false;
					inProcedure = false;
				}
				scopes.pop_back();
				afterReturn = false;
				break;
			case 40:
				file << "int main(int argc,char** argv)";
				inProgram = true;
				break;
			case 41:
				inClass = true;
				index++;
				switch (tkns.at(index).type) {
				case 0:
					classes.push_back({ tkns.at(index).val });
					break;
				case 42:
					{
						std::string name = "";
						bool test = true;
						while (test) {
							index++;
							switch (tkns.at(index).type) {
							case 0:
								name+=tkns.at(index).val;
								break;
							case 43:
								test = false;
								break;
							}
						}
						classes.push_back({ tkns.at(index).val });
					}
					break;
				}
				index++;
				types.push_back({ classes.at(classes.size() - 1).name });
				if (!(tkns.at(index).type == 38)) return 1;
				scopes.push_back({ .is_class = true });
				break;
			case 42:
				file << '(';
				break;
			case 43:
				file << ')';
				break;
			case 44:
				file << '[';
				break;
			case 45:
				file << ']';
				break;
			case 46:
				file << '!';
				break;
			case 47:
				index++;
				[[unlikely]] if (tkns.at(index).type == 9) {
					index++;
					[[unlikely]] if (tkns.at(index).type) return 1;
					else {
						unsigned long long type = find_type_with_char(types, tkns.at(index).val[0]);
						if (type == types.size()) return 1;
						if (isMember) classes.at(classes.size() - 1).members.push_back({ type,3,tkns.at(index).val });
						else {
							file << types.at(type).name << "* " << tkns.at(index).val;
							scopes.at(scopes.size() - 1).variables.push_back({ type,3,tkns.at(index).val });
						}
					}
				}
				else if (tkns.at(index).type) return 1;
				else {
					unsigned long long type = find_type_with_char(types, tkns.at(index).val[0]);
					if (type == types.size()) return 1;
					if (isMember) classes.at(classes.size() - 1).members.push_back({ type,0,tkns.at(index).val });
					else {
						file << types.at(type).name << ' ' << tkns.at(index).val;
						scopes.at(scopes.size() - 1).variables.push_back({ type,0,tkns.at(index).val });
					}
				}
				break;
			case 48:
				if (doth_constant_exist(tkns.at(index + 1).val)) {
					{
						Constant& contst = scopes.at(get_constant_scope(tkns.at(index + 1).val)).constants.at(find_constant(scopes.at(get_constant_scope(tkns.at(index + 1).val)).constants, tkns.at(index + 1).val));
						switch (tkns.at(index + 2).type) {
						case 0:
							if (doth_constant_exist(tkns.at(index + 2).val)) contst.value = scopes.at(get_constant_scope(tkns.at(index + 2).val)).constants.at(find_constant(scopes.at(get_constant_scope(tkns.at(index + 1).val)).constants, tkns.at(index + 1).val)).value;
							else contst.value = tkns.at(index + 2).val;
							break;
						case 16:
							contst.value = std::to_string(std::stoi(contst.value) + 1);
							break;
						}
					}
				}
				else scopes[scopes.size() - 1].constants.push_back({ tkns[index + 1].val,tkns[index + 2].val });
				index += 2;
				break;
			case 49:
				file << "if";
				break;
			case 50:
				file << "else if";
				break;
			case 51:
				file << "else";
				break;
			case 52:
				file << "if(";
				if (!(tkns.at(index + 1).type == 42)) return 1;
				index++;
				break;
			case 53:
				file << "while";
				break;
			case 54:
				file << "while(!";
				if (!(tkns.at(index + 1).type == 42)) return 1;
				index++;
				break;
			case 55:
				index++;
				if (!(!tkns.at(index).type)&&(!tkns.at(index+1).type)) return 1;
				{
					token ret = tkns.at(index);
					token name = tkns.at(index + 1);
					index+=3;
					Arguments args;
					unsigned char pointer_type = 0;
					if (inClass) file << ret.val << ' ' << classes.at(classes.size() - 1).name << "::" << name.val;
					else file << ret.val << ' ' << name.val;
					{
						Args temp = get_args(file, tkns);
						if (temp.flags) return 1;
						args = temp.args;
					}
					if (mode.get(1)) {
						if (mode.get(0)) pointer_type = 2;
						else pointer_type = 1;
						mode.store(0, 0);
						mode.store(1, 0);
					}
					if (inClass) classes.at(classes.size() - 1).methods.push_back({ name.val, args, find_type(types, ret.val),pointer_type,mode.get(3) });
					else functions.push_back({ name.val,args,find_type(types,ret.val),pointer_type,mode.get(3) });
					mode.store(3, 0);
				}
				inFunction = true;
				if (!(tkns.at(index).type == 38)) return 1;
				if (inClass) file << "{\n" << indent(scopes.size() - 1);
				else file << "{\n" << indent(scopes.size());
				scopes.push_back({ .is_function = true });
				break;
			case 56:
				switch (sys) {
				case 0:
					file << "cls";
					break;
				}
				break;
			case 57:
				file << ',';
				break;
			case 58:
				isMember = true;
				break;
			case 59:
				file << "std::cout";
				stream_type = 1;
				break;
			case 60:
				index++;
				if (tkns.at(index).type) return 1;
				{
					token name = tkns.at(index);
					index+=2;
					Arguments args;
					unsigned char pointer_type = 0;
					if (inClass) file << "void " << classes.at(classes.size() - 1).name << "::" << name.val;
					else file << "void " << name.val;
					{
						Args temp = get_args(file, tkns);
						if (temp.flags) return 1;
						args = temp.args;
					}
					if (inClass) classes.at(classes.size() - 1).procedures.push_back({ name.val,args });
					else procedures.push_back({ name.val,args });
				}
				inProcedure = true;
				if (!(tkns.at(index).type == 38)) return 1;
				if (inClass) file << "{\n" << indent(scopes.size() - 1);
				else file << "{\n" << indent(scopes.size());
				scopes.push_back({ .is_function = true });
				break;
			case 61:
				file << "std::cin";
				stream_type = 2;
				break;
			case 62:
				[[unlikely]] if (!inClass) return 1;
				file << find_type(types, classes.at(classes.size() - 1).name);
				break;
			case 63:
				file << '%';
				break;
			case 64:
				index++;
				switch (tkns.at(index).type) {
				case 0:
					if (tkns.at(index).type) return 1;
					if (!doth_variable_exist(tkns.at(index).val)) return 1;
					file << tkns.at(index).type << "=new " << types.at(scopes.at(get_variable_scope(tkns.at(index).val)).variables.at(find_variable(scopes.at(get_variable_scope(tkns.at(index).val)).variables, tkns.at(index).val)).type).name;
					switch (scopes.at(get_variable_scope(tkns.at(index).val)).variables.at(find_variable(scopes.at(get_variable_scope(tkns.at(index).val)).variables, tkns.at(index).val)).ptr_type) {
					case 1:
						if ((tkns.at(index + 1).type == 0) || (tkns.at(index + 1).type == 2)) {
							index++;
							file << '{' << tkns.at(index).val << '}';
						}
						else if (tkns.at(index + 1).type == 3) {
							index++;
							file << "{\"" << tkns.at(index).val << "\"}";
						}
						break;
					case 2:
						index++;
						file << '[' << tkns.at(index).val << ']';
						mode.store(0, 0);
						if ((tkns.at(index + 1).type == 0) || (tkns.at(index + 1).type == 2)) {
							index++;
							file << '{' << tkns.at(index).val << '}';
						}
						else if (tkns.at(index + 1).type == 3) {
							index++;
							file << "{\"" << tkns.at(index).val << "\"}";
						}
						break;
					case 3:
						if (mode.get(0)) {
							index++;
							if (!((tkns.at(index).type == 0) || (tkns.at(index).type == 2))) return 1;
							file << '[' << tkns.at(index).val << ']';
							mode.store(0, 0);
						}
						if ((tkns.at(index + 1).type == 0) || (tkns.at(index + 1).type == 2)) {
							index++;
							file << '{' << tkns.at(index).val << '}';
						}
						else if (tkns.at(index + 1).type == 3) {
							index++;
							file << "{\"" << tkns.at(index).val << "\"}";
						}
						break;
					default:
						return 1;
					}
					break;
				case 11:
					index++;
					if (tkns.at(index).type) return 1;
					if (!does_variable_exist(classes.at(classes.size() - 1).members, tkns.at(index).val)) return 1;
					file << "this->" << tkns.at(index).type << "=new " << types.at(classes.at(classes.size() - 1).members.at(find_variable(classes.at(classes.size() - 1).members, tkns.at(index).val)).type).name;
					switch (classes.at(classes.size()-1).members.at(find_variable(classes.at(classes.size()-1).members,tkns.at(index).val)).ptr_type) {
					case 1:
						if ((tkns.at(index + 1).type==0)||(tkns.at(index+1).type==2)) {
							index++;
							file << '{' << tkns.at(index).val << '}';
						}
						else if (tkns.at(index + 1).type == 3) {
							index++;
							file << "{\"" << tkns.at(index).val << "\"}";
						}
						break;
					case 2:
						index++;
						if (!((tkns.at(index).type == 0) || (tkns.at(index).type == 2))) return 1;
						file << '[' << tkns.at(index).val << ']';
						mode.store(0, 0);
						if ((tkns.at(index + 1).type == 0) || (tkns.at(index + 1).type == 2)) {
							index++;
							file << '{' << tkns.at(index).val << '}';
						}
						else if (tkns.at(index + 1).type == 3) {
							index++;
							file << "{\"" << tkns.at(index).val << "\"}";
						}
						break;
					case 3:
						if (mode.get(0)) {
							index++;
							if (!((tkns.at(index).type == 0) || (tkns.at(index).type == 2))) return 1;
							file << '[' << tkns.at(index).val << ']';
							mode.store(0, 0);
						}
						if ((tkns.at(index + 1).type == 0) || (tkns.at(index + 1).type == 2)) {
							index++;
							file << '{' << tkns.at(index).val << '}';
						}
						else if (tkns.at(index + 1).type == 3) {
							index++;
							file << "{\"" << tkns.at(index).val << "\"}";
						}
						break;
					default:
						return 1;
					}
					break;
				default:
					return 1;
				}
				break;
			case 65:
				index++;
				switch (tkns.at(index).type) {
				case 0:
					if (!doth_variable_exist(tkns.at(index).val)) return 1;
					switch (scopes.at(get_variable_scope(tkns.at(index).val)).variables.at(find_variable(scopes.at(get_variable_scope(tkns.at(index).val)).variables, tkns.at(index).val)).ptr_type) {
					case 1:
						file << "delete ";
						break;
					case 2:
						file << "delete[] ";
						break;
					case 3:
						if (mode.get(0)) file << "delete[] ";
						else file << "delete ";
						mode.store(0, 0);
						break;
					default:
						return 1;
					}
					file << tkns.at(index).val;
					break;
				case 11:
					index++;
					if (tkns.at(index).type) return 1;
					if (!does_variable_exist(classes.at(classes.size() - 1).members, tkns.at(index).val)) return 1;
					switch (classes.at(classes.size() - 1).members.at(find_variable(classes.at(classes.size() - 1).members, tkns.at(index).val)).ptr_type) {
					case 1:
						file << "delete ";
						break;
					case 2:
						file << "delete[] ";
						break;
					case 3:
						if (mode.get(0)) file << "delete[] ";
						else file << "delete ";
						mode.store(0, 0);
						break;
					default:
						return 1;
					}
					file << tkns.at(index).val;
					break;
				default:
					return 1;
				}
				break;
			case 66:
				file << "%=";
				break;
			case 67:
				index++;
				if (tkns.at(index).type) return 1;
				types.at(types.size() - 1).start_character = tkns.at(index).val.at(0);
				index++;
				if (!(tkns.at(index).type == 4)) return 1;
				break;
			}
			index++;
		}
		file.close();
		return 0;
	}
	unsigned long long compile_asm(node* base_node) {
		return pass();
	}
	unsigned long long compile_java() {
		return pass();
	}
	unsigned long long compile_c() {
		return pass();
	}
	void compile_arguments(std::ofstream& file, Arguments& args) {
		unsigned index = 0;
		file << '(';
		while (index < args.size()) {
			if (index > 0) file << ',';
			file << types.at(args.at(index).value_type).name;
			if (args.at(index).type_of_argument) file << '*';
			file << ' ';
			file << args.at(index).name;
			index++;
		}
		file << ')';
	}
	void compile_class_cpp(std::ofstream& file,unsigned class_index) {
		file << "\nclass " << classes.at(class_index).name << '{';
		unsigned index = 0;
		while (index < classes.at(class_index).members.size()) {
			file << '\n' << indent(1) << types.at(classes.at(class_index).members.at(index).type).name;
			if (classes.at(class_index).members.at(index).ptr_type) file << '*';
			file << ' ' << classes.at(class_index).members.at(index).name << ';';
			index++;
		}
		file << "\npublic:";
		index = 0;
		while (index < classes.at(class_index).methods.size()) {
			file << '\n' << indent(1) << types.at(classes.at(class_index).methods.at(index).Rtype).name;
			if (classes.at(class_index).methods.at(index).ptr_type) file << '*';
			file << ' ' << classes.at(class_index).methods.at(index).name;
			compile_arguments(file, classes.at(class_index).methods.at(index).args);
			file << ';';
			index++;
		}
		index = 0;
		while (index < classes.at(class_index).procedures.size()) {
			file << '\n' << indent(1) << "void " << classes.at(class_index).procedures.at(index).name;
			compile_arguments(file, classes.at(class_index).procedures.at(index).args);
			file << ';';
			index++;
		}
		file << "\n}";
	}
	void create_hpp() {
		std::ofstream file("declarations.hpp");
		setup_cpp(file);
		unsigned index = 0;
		while (index < classes.size()) {
			compile_class_cpp(file, index);
			index++;
		}
		index = 0;
		while (index < functions.size()) {
			file << '\n' << types.at(functions.at(index).Rtype).name;
			if (functions.at(index).ptr_type) {
				file << '*';
			}
			file << ' ' << functions.at(index).name;
			compile_arguments(file, functions.at(index).args);
			file << ';';
			index++;
		}
		index = 0;
		while (index < procedures.size()) {
			file << "\nvoid " << procedures.at(index).name;
			compile_arguments(file, procedures.at(index).args);
			file << ';';
			index++;
		}
	}
	void compile_class_c(std::ofstream& file, unsigned class_index) {
		file << "\ntypedef struct " << classes.at(class_index).name << "{";
		unsigned index = 0;
		while (index < classes.at(class_index).members.size()) {
			file << '\n' << indent(1) << classes.at(class_index).members.at(index).type;
			if (classes.at(class_index).members.at(index).ptr_type) file << '*';
			file << ' ' << classes.at(class_index).members.at(index).name << ";";
			index++;
		}
		file << "\n};";
		index = 0;

	}
};
template<class T> void put_in_vector(std::vector<T>& des, std::vector<T> loc) {
	unsigned index = 0;
	while (index < loc.size()) {
		des.push_back(loc.at(index));
		index++;
	}
}
template<class T> void put_in_vector(std::vector<T>& des, std::vector<T> loc, T addition) {
	unsigned index = 0;
	while (index < loc.size()) {
		des.push_back(addition + loc.at(index));
		index++;
	}
}
std::vector<std::string> get_files_in_path(std::filesystem::path path,std::error_code& what) {
	std::vector<std::string> out;
	std::filesystem::directory_iterator dirs{path};
	while (1) {
		if (dirs._At_end()) return out;
		dirs.increment(what);
		if ((*dirs).is_directory()) put_in_vector(out, get_files_in_path((*dirs).path(), what), std::filesystem::relative((*dirs).path(), path).string());
		else out.push_back((*dirs).path().filename().string());
	}
}
std::vector<std::string> get_files_in_path_with_ext(std::filesystem::path path, std::string ext, std::error_code& what) {
	std::vector<std::string> out;
	std::filesystem::directory_iterator dirs{path};
	while (1) {
		if (dirs._At_end()) return out;
		dirs.increment(what);
		if ((*dirs).is_directory()) put_in_vector(out, get_files_in_path_with_ext((*dirs).path(), ext, what), std::filesystem::relative((*dirs).path(), path).string());
		else if ((*dirs).path().extension() == ext) out.push_back((*dirs).path().stem().string());
	}
}
void compile(language_type lang, system_type os, flags& values,std::vector<std::string>& files) {
	compiler stuff;
	unsigned index = 0;
	lexer lex("");
	while (index < files.size()) {
		lex.reset(preprocess(files.at(index)+".aur"));
		switch (lang) {
		case 0:
			if (stuff.compile_cpp(lex.tokenize(), files.at(index), values, os)) std::cout << "Failed to compile:" << files.at(index) + ".aur\n";
			break;
		}
		index++;
	}
	switch (lang) {
	case 0:
		stuff.create_hpp();
		break;
	}
}
int main(int argc, char* argv[]) {
	language_type lang = 0;
	system_type operating = 0;
	std::string temp;
	std::vector<std::string> arguments;
	if (argc < 2) {
		std::cout << USER_ERROR;
		return 1;
	}
	load_flags(arguments, argv, argc);
	std::vector<std::string> files;
	flags values;
	unsigned long long count = 1;
	while (count < arguments.size()) {
		temp = arguments.at(count);
		if (temp == "-java") lang = 1;
		else if (temp == "-cpp") lang = 0;
		else if (temp == "-new") values.store(0, true);
		else if (temp == "-old") values.store(0, false);
		else if (temp == "-update") values.store(1, true);
		else if (temp == "-complete") values.store(1, false);
		else if (temp == "-package") values.store(2, true);
		else if (temp == "-project") values.store(2, false);
		else if (temp == "-show") values.store(3, true);
		else if (temp == "-hide") values.store(3, false);
		else if (temp == "-kernel") values.store(4, true);
		else if (temp == "-app") values.store(4, false);
		else if (temp == "-test") values.store(5, true);
		else if (temp == "-stable") values.store(5, false);
		else if (temp == "-debug") values.store(6, true);
		else if (temp == "-release") values.store(6, false);
		else if (temp == "-header") values.store(7, true);
		else if (temp == "-source") values.store(7, false);
		else if (temp == "-linux") operating = 1;
		else if (temp == "-windows") operating = 0;
		else files.push_back(temp);
		count++;
	}
	if (!files.size()) {
		std::cout << USER_ERROR;
		return 1;
	}
	compile(lang, operating, values, files);
}