#include "lexer.h"
aurum::lexer::lexer::lexer() {
	this->str = std::string();
	this->location = -1;
}
aurum::lexer::lexer::lexer(std::string str) {
	this->str = str;
	this->location = 0;
}
aurum::lexer::lexer& aurum::lexer::lexer::use(std::string str){
	this->str = str;
	this->location = 0;
	return *this;
}
bool aurum::lexer::lexer::operator!() {
	return !(this->location == -1);
}
bool aurum::lexer::lexer::operator~() {
	return this->location == this->str.size();
}
inline aurum::shared::optional<char> aurum::lexer::lexer::peek() {
	return ((!!(*this)) || (~(*this))) ? shared::optional<char>() : shared::optional<char>(this->str.at(this->location));
}
inline char aurum::lexer::lexer::consume() {
	return this->str.at(this->location++);
}
std::vector<aurum::lexer::token> aurum::lexer::lexer::tokenize() {
	std::vector<token> out = std::vector<token>();
	if (!!(*this)) shared::utils::crash(shared::internals::errors,0);
	char small_buffer;
	std::string buffer;
	while(!~(*this)){
		small_buffer=this->consume();
		buffer=std::string();
		if(std::isalpha(small_buffer)){
			buffer.push_back(small_buffer);
			while((!this->peek())&&std::isalnum(this->peek.val)) buffer.push_back(this->consume());
			if(buffer=="return") out.push_back({token_type::RETURN,std::string()});
			else if(buffer=="start") out.push_back({token_type::START,std::string()});
			else if(buffer=="end") out.push_back({token_type::END,std::string()});
			else if(buffer=="program") out.push_back({token_type::PROGRAM,std::string()});
			else if(buffer=="class") out.push_back({token_type::CLASS,std::string()});
			else if(buffer=="auto") out.push_back({token_type::AUTO,std::string()});
			else if(buffer=="let") out.push_back({token_type::LET,std::string()});
			else if(buffer=="if") out.push_back({token_type::IF,std::string()});
			else if(buffer=="elf") out.push_back({token_type::ELF,std::string()});
			else if(buffer=="else") out.push_back({token_type::ELSE,std::string()});
			else if(buffer=="unless") out.push_back({token_type::UNLESS,std::string()});
			else if(buffer=="while") out.push_back({token_type::WHILE,std::string()});
			else if(buffer=="until") out.push_back({token_type::UNTIL,std::string()});
			else if(buffer=="function") out.push_back({token_type::FUNCTION,std::string()});
			else if(buffer=="clr") out.push_back({token_type::CLR,std::string()});
			else if(buffer=="member") out.push_back({token_type::MEMBER,std::string()});
			else if(buffer=="sysout") out.push_back({token_type::SYSOUT,std::string()});
			else if(buffer=="procedure") out.push_back({token_type::PROCEDURE,std::string()});
			else if(buffer=="create") out.push_back({token_type::CREATE,std::string()});
			else if(buffer=="destroy") out.push_back({token_type::DESTROY,std::string()});
			else if(buffer=="letter") out.push_back({token_type::LETTER,std::string()});
			else if(buffer=="embed") out.push_back({token_type::EMBED,std::string()});
			else if(buffer=="import") out.push_back({token_type::IMPORT,std::string()});
			else if(buffer=="as") out.push_back({token_type::AS,std::string()});
			else if(buffer=="open_class") out.push_back({token_type::OPEN_CLASS,std::string()});
			else if(buffer=="struct") out.push_back({token_type::STRUCT,std::string()});
			else if(buffer=="null") out.push_back({token_type::_NULL,std::string()});
			else if(buffer=="forever") out.push_back({token_type::FOREVER,std::string()});
			else if(buffer=="pass") out.push_back({token_type::PASS,std::string()});
			else if(buffer=="typedef") out.push_back({token_type::TYPEDEF,std::string()});
			else if(buffer=="varargs") out.push_back({token_type::VARARGS,std::string()});
			else if(buffer=="operator") out.push_back({token_type::OPERATOR,std::string()});
			else out.push_back({token_type::ID,buffer});
		} else if(std::isdigit(small_buffer)){
			buffer.push_back(small_buffer);
			while((!this->peek())&&std::isdigit(this->peek.val)) buffer.push_back(this->consume());
			out.push_back({token_type::INT_LIT,buffer});
		} else{
			switch(small_buffer){
			case ';':
				out.push_back({token_type::END_STATEMENT,std::string()});
				break;
			case '+':
				if(this->peek()=='+') {out.push_back({token_type::INC_OP,std::string()});this->consume()}
				else if(this->peek()=='=') {out.push_back({token_type::ADD_ASS,std::string()});this->consume();}
				else out.push_back({token_type::ADD_OP,std::string()});
				break;
			case '-':
				if(this->peek()=='-') {out.push_back({token_type::DEC_OP,std::string()});this->consume()}
				else if(this->peek()=='=') {out.push_back({token_type::SUB_ASS,std::string()});this->consume()}
				else if(this->peek()=='>') {out.push_back({token_type::POINT_ATTRIB,std::string()});this->consume()}
				else out.push_back({token_type::SUB_OP,std::string()});
				break;
			case '/':
				if(this->peek()=='=') {out.push_back({token_type::DIV_ASS,std::string()});this->consume();}
				else out.push_back({token_type::DIV_OP,std::string()});
				break;
			case '*':
				if(this->peek()=='*') { 
					this->consume();
					if(this->peek()=='=') {out.push_back({token_type::EXP_ASS,std::string()});this->consume();}
					else out.push_back({token_type::EXP_OP,std::string()});
				}
				else if(this->peek()=='=') {out.push_back({token_type::MUL_ASS,std::string()});this->consume();}
				else out.push_back({token_type::MUL_OP,std::string()});
				break;
			case '&':
				if(this->peek()=='*') {out.push_back({token_type::POINT_OP,std::string()});this->consume();}
				else if(this->peek()=='!') {out.push_back({token_type::NOT_OP,std::string()});this->consume();}
				else if(this->peek()=='>') {out.push_back({token_type::GET_ATTRIB,std::string()});this->consume();}
				else if(this->peek()=='&') {out.push_back({token_type::AND_LOG,std::string()});this->consume();}
				else if(this->peek()=='=') {out.push_back({token_type::AND_ASS,std::string()});this->consume();}
				else out.push_back({token_type::AND_OP,std::string()});
				break;
			case '<':
				if(this->peek()=='<'){
					this->consume();
					if(this->peek()=='=') {out.push_back({token_type::LSH_ASS,std::string()});this->consume();}
					else out.push_back({token_type::LSH_OP,std::string()});
				}
				else out.push_back({token_type::LESS_LOG,std::string()});
				break;
			case '>':
				if(this->peek()=='>'){
					this->consume();
					if(this->peek()=='=') {out.push_back({token_type::RSH_ASS,std::string()});this->consume();}
					else out.push_back({token_type::RSH_OP,std::string()});
				}
				else out.push_back({token_type::MORE_LOG,std::string()});
				break;
			case '^':
				if(this->peek()=='^') {out.push_back({token_type::XOR_LOG,std::string()});this->consume();}
				else if(this->peek()=='=') {out.push_back({token_type::XOR_ASS,std::string()});this->consume();}
				else out.push_back({token_type::XOR_OP,std::string()});
				break;
			case '|':
				if(this->peek()=='|') {out.push_back({token_type::OR_LOG,std::string()});this->consume();}
				else if(this->peek()=='=') {out.push_back({token_type::OR_ASS,std::string()});this->consume();}
				else out.push_back({token_type::OR_OP,std::string()});
				break;
			case '=':
				if(this->peek()=='=') {out.push_back({token_type::EQU_LOG,std::string()});this->consume();}
				else out.push_back({token_type::EQU_ASS,std::string()});
				break;
			case '@':
				while(!this->peek()&&isalnum(this->peek().val)) buffer.push_back(this->consume());
				out.push_back({token_type::COMPILER_TAG,buffer});
				break;
			case '%':
				if(this->peek()=='%') {out.push_back({token_type::GET_SIZE,std::string()});this->consume();}
				else if(this->peek()=='&') {out.push_back({token_type::GET_LOC,std::string()});this->consume();}
				else if(this->peek()=='^') {out.push_back({token_type::GET_TYPE,std::string()});this->consume();}
				else if(this->peek()=='=') {out.push_back({token_type::MOD_ASS,std::string()});this->consume();}
				else if(this->peek()=='>') {out.push_back({token_type::GET_THIS_TYPE,std::string()});this->consume();}
				else out.push_back({token_type::MOD_OP,std::string()});
				break;
			case ',':
				out.push_back({token_type::ARG_SEPERATOR,std::string()});
				break;
			case '$':
				out.push_back({token_type::NOT_LOG,std::string()});
				break;
			case '[':
				out.push_back({token_type::START_OFFSET,std::string()});
				break;
			case ']':
				out.push_back({token_type::END_OFFSET,std::string()});
				break;
			case '(':
				out.push_back({token_type::START_ARGS,std::string()});
				break;
			case ')':
				out.push_back({token_type::END_ARGS,std::string()});
				break;
			case '"':
				while(!(this->peek()=='"')) buffer.push_back(this->consume());
				this->consume();
				out.push_back({token_type::STR_LIT,buffer});
				break;
			case 39:
				if(!(this->peek()==39)) buffer.push_back(this->consume());
				this->consume();
				out.push_back({token_type::CHAR_LIT,buffer});
            case '{':
                while(!this->peek()&&(!((this->peek()==10)||(this->peek()=='}'))) this->consume();
                this->consume();
                break;
			case '!':
				while(!(this->peek()==10)) this->consume();
			case 10:
			case 32:
                this->consume();
				break;
			default:
				shared::utils::crash(shared::internals::errors,1);
			}
		}
	}
	return out;
}