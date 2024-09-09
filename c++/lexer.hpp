#ifndef AURUM_COMPILER_LEXER
#define AURUM_COMPILER_LEXER
#include "main_functions.hpp"
struct token {
	unsigned long long type;
	std::string val = "";
};
typedef std::vector<token> Tokens;
struct Char {
	bool exist;
	char val;
};
class lexer {
	unsigned long long index;
	std::string src;
	Char peek(unsigned long long ahead = 1) {
		if ((index + ahead) < (src.size() - 1)) {
			return Char{ true, this->src.at(index + ahead) };
		}
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
	Tokens tokenize() {
		Tokens tkns;
		std::string buf;
		while (peek().exist) {
			if (isalpha(peek().val)) {
				buf.push_back(consume());
				while (peek().exist && isalnum(peek().val)) {
					buf.push_back(consume());
				}
				if (buf == "return") {
					tkns.push_back(token{ 1 });
				}
				else if (buf == "start") {
					tkns.push_back(token{ 38 });
				}
				else if (buf == "end") {
					tkns.push_back(token{ 39 });
				}
				else if (buf == "program") {
					tkns.push_back(token{ 40 });
				}
				else if (buf == "class") {
					tkns.push_back(token{ 41 });
				}
				else if (buf == "auto") {
					tkns.push_back(token{ 47 });
				}
				else if (buf == "let") {
					tkns.push_back(token{ 48 });
				}
				else if (buf == "if") {
					tkns.push_back(token{ 49 });
				}
				else if (buf == "elf") {
					tkns.push_back(token{ 50 });
				}
				else if (buf == "else") {
					tkns.push_back(token{ 51 });
				}
				else if (buf == "unless") {
					tkns.push_back(token{ 52 });
				}
				else if (buf == "while") {
					tkns.push_back(token{ 53 });
				}
				else if (buf == "until") {
					tkns.push_back(token{ 54 });
				}
				else if (buf == "function") {
					tkns.push_back(token{ 55 });
				}
				else {
					tkns.push_back(token{ 0,buf });
				}
				buf.clear();
			}
			else if (isdigit(peek().val)) {
				buf.push_back(consume());
				while (peek().exist && isdigit(peek().val)) {
					buf.push_back(consume());
				}
				tkns.push_back(token{ 2,buf });
				buf.clear();
			}
			else if (isspace(peek().val) || peek().val == '\n') {
				consume();
			}
			else if (peek().val == '"') {
				buf.push_back(consume());
				while (peek().exist && !peek().val == '"') {
					buf.push_back(consume());
				}
				consume();
				buf.push_back('"');
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
				while (peek().val != ' ' && peek().val != '\n') {
					buf.push_back(consume());
				}
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
		}
	}
};
#endif
