#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <new>
#include <sstream> 
#include <cstdlib>
class compiler_errors{
public:
	enum class types{
		INVALID,
		FILE_FAILED_TO_OPEN,
		NON_ASCII_CHAR,
		SYNTAX_ERROR,
		UNSUPPORTTED
	};
private:
	types type;
	std::string value;
public:
	compiler_errors(types type,std::string value):type(type),value(value){}
	types get_type(){
		return this->type;
	}
	std::string get_value(){
		return this->value;
	}
};
std::string join(std::vector<std::string>& strs,char delim){
	if(delim>(char)127) throw compiler_errors(compiler_errors::types::NON_ASCII_CHAR,"");
	std::string out="";
	for(int i=0;i<(int)strs.size();i++) out+=(strs.at(i)+(((i+1)==(int)strs.size())?(char)0:delim));
	return out;
}
std::string read_file(std::string& name){
	std::ifstream input(name);
	if(!input.is_open()) throw compiler_errors(compiler_errors::types::FILE_FAILED_TO_OPEN,name);
	std::vector<std::string> lines;
	std::string temp;
	while(std::getline(input,temp)) lines.push_back(temp);
	return join(lines,'\n');
}
struct token{
	enum class token_type{
		INVALID,
		ADD_OP,
		SUB_OP,
		MUL_OP,
		DIV_OP,
		REM_OP,
		AND_BIT_OP,
		OR_BIT_OP,
		XOR_BIT_OP,
		NOT_BIT_OP,
		AND_LOG_OP,
		OR_LOG_OP,
		XOR_LOG_OP,
		NOT_LOG_OP,
		FUNCTION,
		OPEN_ARGS,
		CLOSE_ARGS,
		END_STATEMENT,
		LABEL,
		GOTO,
		IF,
		INT_LIT,
		CHAR_LIT,
		STR_LIT,
		ID,
		ASS,
		EQU_OP,
		GREAT_OP,
		LESS_OP,
		POINT_OP,
		PROGRAM,
		START_BLOCK,
		END_BLOCK,
		ARG_SEP,
		AS,
		RETURN
	} type;
	std::string value;
	unsigned line;
	unsigned pos;
	unsigned handle;
	token():type(token_type::INVALID),value(std::string("")),line(0),pos(0),handle(0){}
	token(token_type type):type(type),value(std::string("")),line(0),pos(0),handle(0){}
	token(token_type type,std::string value):type(type),value(value),line(0),pos(0),handle(0){}
	token(token_type type,unsigned handle):type(type),value(std::string("")),line(0),pos(0),handle(handle){}
	token(token_type type,std::string value,unsigned handle):type(type),value(value),line(0),pos(0),handle(handle){}
	token(token_type type,unsigned line,unsigned pos):type(type),value(std::string("")),line(line),pos(pos),handle(0){}
	token(token_type type,std::string value,unsigned line,unsigned pos):type(type),value(value),line(line),pos(pos),handle(0){}
	token(token_type type,unsigned line,unsigned pos,unsigned handle):type(type),value(std::string("")),line(line),pos(pos),handle(handle){}
	token(token_type type,std::string value,unsigned line,unsigned pos,unsigned handle):type(type),value(value),line(line),pos(pos),handle(handle){}
};
template<typename T> class tokenize_error{
	T err;
	unsigned line;
	unsigned pos;
	unsigned handle;
};
std::vector<token> tokenize(std::string& input){
	unsigned line=0;
	unsigned pos=0;
	bool in_str=false;
	bool in_chr=false;
	bool in_id=false;
	bool escape=false;
	bool in_comment=false;
	bool in_number=false;
	std::vector<token> tkns;
	for(unsigned handle=0;handle<input.size();handle++){
		if(in_comment){
			if(input.at(handle)=='}') in_comment=false;
		} else if(in_str&&(!((input.at(handle)=='"')||(input.at(handle)=='\\')))&&(!escape)) tkns.back().value.push_back(input.at(handle));
		else if(in_str&&(input.at(handle)=='\\')&&(!escape)) escape=true;
		else if(in_str&&(input.at(handle)=='\\')){
			for(int i=0;i<2;i++) tkns.back().value.push_back('\\');
			escape=false;
		} else if(in_str&&(input.at(handle)=='"'&&(!escape))) in_str=false;
		else if(in_str&&(input.at(handle)=='"')){
			tkns.back().value.push_back('\\');
			tkns.back().value.push_back('"');
			escape=false;
		} else if(in_str&&(input.at(handle)=='n')&&escape){
			tkns.back().value.push_back('\\');
			tkns.back().value.push_back('n');
			escape=false;
		} else if(in_chr&&(!(escape||(input.at(handle)=='\'')||(input.at(handle)=='\\')))) tkns.back().value.push_back(input.at(handle));
		else if(in_chr&&(input.at(handle)=='\\')&&(!escape)) escape=true;
		else if(in_chr&&(input.at(handle)=='\\')&&escape){
			for(int i=0;i<2;i++) tkns.back().value.push_back('\\');
			escape=false;
		} else if(in_chr&&(input.at(handle)=='n')&&escape){
			tkns.back().value.push_back('\\');
			tkns.back().value.push_back('n');
			escape=false;
		} else if(in_chr&&(input.at(handle)=='\'')&&(!escape)) in_chr=false;
		else if(in_chr&&(input.at(handle)=='\'')&&escape){
			tkns.back().value.push_back('\\');
			tkns.back().value.push_back('\'');
			escape=false;
		}
		else if(in_id){
			if(isalnum(input.at(handle))) tkns.back().value.push_back(input.at(handle));
			else if(input.at(handle)=='_') tkns.back().value.push_back('_');
			else{
				in_id=false;
				handle--;
				if(tkns.back().value=="program") tkns.back().type=token::token_type::PROGRAM;
				else if(tkns.back().value=="label") tkns.back().type=token::token_type::LABEL;
				else if(tkns.back().value=="function") tkns.back().type=token::token_type::FUNCTION;
				else if(tkns.back().value=="start") tkns.back().type=token::token_type::START_BLOCK;
				else if(tkns.back().value=="end") tkns.back().type=token::token_type::END_BLOCK;
				else if(tkns.back().value=="goto") tkns.back().type=token::token_type::GOTO;
				else if(tkns.back().value=="if") tkns.back().type=token::token_type::IF;
				else if(tkns.back().value=="as") tkns.back().type=token::token_type::AS;
				else if(tkns.back().value=="return") tkns.back().type=token::token_type::RETURN;
				goto after_pos;
			}
		} else if(isalpha(input.at(handle))){
			tkns.push_back(token(token::token_type::ID,line,pos,handle));
			tkns.back().value.push_back(input.at(handle));
			in_id=true;
		} else if(isdigit(input.at(handle))&&(!in_number)){
			tkns.push_back(token(token::token_type::INT_LIT,line,pos,handle));
			tkns.back().value.push_back(input.at(handle));
			in_number=true;
		} else if(in_number){
			if(isdigit(input.at(handle))) tkns.back().value.push_back(input.at(handle));
			else if(input.at(handle)=='.') throw compiler_errors(compiler_errors::types::UNSUPPORTTED,"Floating point number");
			else{
				in_number=false;
				handle--;
				goto after_pos;
			}
		} else{
			switch(input.at(handle)){
			case '+':
				tkns.push_back(token(token::token_type::ADD_OP,line,pos,handle));
				break;
			case '-':
				tkns.push_back(token(token::token_type::SUB_OP,line,pos,handle));
				break;
			case '*':
				if(tkns.back().type==token::token_type::AND_BIT_OP) tkns.back().type=token::token_type::POINT_OP;
				else tkns.push_back(token(token::token_type::MUL_OP,line,pos,handle));
				break;
			case '/':
				tkns.push_back(token(token::token_type::DIV_OP,line,pos,handle));
				break;
			case '%':
				tkns.push_back(token(token::token_type::REM_OP,line,pos,handle));
				break;
			case '>':
				tkns.push_back(token(token::token_type::GREAT_OP,line,pos,handle));
				break;
			case '<':
				tkns.push_back(token(token::token_type::LESS_OP,line,pos,handle));
				break;
			case '=':
				if(tkns.back().type==token::token_type::ASS) tkns.back().type=token::token_type::EQU_OP;
				else tkns.push_back(token(token::token_type::ASS,line,pos,handle));
			case ' ':
				break;
			case '&':
				if(tkns.back().type==token::token_type::AND_BIT_OP) tkns.back().type=token::token_type::AND_LOG_OP;
				else tkns.push_back(token(token::token_type::AND_BIT_OP,line,pos,handle));
				break;
			case '|':
				if(tkns.back().type==token::token_type::OR_BIT_OP) tkns.back().type=token::token_type::OR_LOG_OP;
				else tkns.push_back(token(token::token_type::OR_BIT_OP,line,pos,handle));
				break;
			case '^':
				if(tkns.back().type==token::token_type::XOR_BIT_OP) tkns.back().type=token::token_type::XOR_LOG_OP;
				else tkns.push_back(token(token::token_type::XOR_BIT_OP,line,pos,handle));
				break;
			case '~':
				tkns.push_back(token(token::token_type::NOT_BIT_OP,line,pos,handle));
				break;
			case '{':
				in_comment=true;
				break;
			case '!':
				if(tkns.back().type==token::token_type::AND_BIT_OP) tkns.back().type=token::token_type::NOT_LOG_OP;
				else throw compiler_errors(compiler_errors::types::UNSUPPORTTED,"Single-line comments");
				break;
			case '(':
				tkns.push_back(token(token::token_type::OPEN_ARGS,line,pos,handle));
				break;
			case ')':
				tkns.push_back(token(token::token_type::CLOSE_ARGS,line,pos,handle));
				break;
			case '"':
				tkns.push_back(token(token::token_type::STR_LIT,line,pos,handle));
				in_str=true;
				break;
			case ',':
				tkns.push_back(token(token::token_type::ARG_SEP,line,pos,handle)); 
				break;
			case ';':
				tkns.push_back(token(token::token_type::END_STATEMENT,line,pos,handle));
				break;
			case '\'':
				tkns.push_back(token(token::token_type::CHAR_LIT,line,pos,handle));
				in_chr=true;
				break;
			case '\n':
				line++;
				pos=0;
				goto after_pos;
			}
		}
		pos++;
	after_pos:
	}
	return tkns;
}
/*struct program{
	struct top_decl{
		enum class types{
			INVALID,
			FUNCTION,
			PROGRAM
		} type;
		union{
			struct decl{
				std::string name;
				std::string type;
			};
			struct instruction{
				enum class types{
				} type;
				;
			};
			std::vector<instruction> driver;
			struct{
				std::string name;
				std::string ret;
				std::vector<decl> args;
				std::vector<instruction> body;
			} function;
		} value;
	};
	std::vector<top_decl> decls;
};*/
struct declaration{
	std::string name;
	std::string type;
};
void compile(std::vector<token>& tkns){
	std::ofstream out("program.c");
	out<<"#include <stdint.h>"<<std::endl;
	out<<"typedef void u0;"<<std::endl;
	out<<"typedef uint8_t u8;"<<std::endl;
	out<<"typedef uint16_t u16;"<<std::endl;
	out<<"typedef uint32_t u32;"<<std::endl;
	out<<"typedef uint64_t u64;"<<std::endl;
	out<<"typedef void i0;"<<std::endl;
	out<<"typedef int8_t i8;"<<std::endl;
	out<<"typedef int16_t i16;"<<std::endl;
	out<<"typedef int32_t i32;"<<std::endl;
	out<<"typedef int64_t i64;"<<std::endl;
	out<<"extern u64 stdout;"<<std::endl;
	out<<"extern u64 stdin;"<<std::endl;
	out<<"extern u64 stderr;"<<std::endl;
	for(unsigned handle=0;handle<tkns.size();handle++){
		switch(tkns.at(handle).type){
		case token::token_type::INVALID:
			std::cerr<<"Invalid"<<std::endl;
			break;
		case token::token_type::FUNCTION:
			{
				std::stringstream str;
				str.clear();
				if(!((handle+1)<(unsigned)tkns.size())) return (void)(std::cerr<<"Expected Token to Exist"<<std::endl);
				if(!(tkns.at(handle+1).type==token::token_type::ID)) return (void)(std::cerr<<"Expected Id at ["<<tkns.at(handle+1).line<<"]["<<tkns.at(handle+1).pos<<"]["<<tkns.at(handle+1).handle<<']'<<std::endl);
				std::string name=tkns.at(handle+1).value;
				std::vector<declaration> decl;
				if(tkns.at(handle+3).type==token::token_type::CLOSE_ARGS) goto after_loop;
				for(int i=0;(i+handle+3)<tkns.size();i++){
					if(!((handle+5+i)<tkns.size())) return (void)(std::cerr<<"Expected tokens to exist in argument list declaration"<<std::endl);
					if(!((tkns.at(handle+3+i).type==token::token_type::ID)&&(tkns.at(handle+4+i).type==token::token_type::ID))) return (void)(std::cerr<<"Expected tokens to be of type:ID"<<std::endl);
					decl.push_back({tkns.at(handle+4+i).value,tkns.at(handle+3+i).value});
					if(tkns.at(handle+5+i).type==token::token_type::CLOSE_ARGS) break;
					i+=2;
				}
				after_loop:
				if(!((handle+3+decl.size()*3)<tkns.size())) return (void)(std::cerr<<"Expected Token to Exist"<<std::endl);
				if(!(tkns.at(handle+3+decl.size()*3).type==token::token_type::ID)) return (void)(std::cerr<<"Expected Id at["<<tkns.at(handle+3+decl.size()*3).line<<"]["<<tkns.at(handle+3+decl.size()*3).pos<<"]["<<tkns.at(handle+3+decl.size()*3).handle<<']'<<std::endl);
				out<<tkns.at(handle+3+decl.size()*3).value<<' '<<tkns.at(handle+1).value<<'(';
				for(int i=0;i<(int)decl.size();i++){
					if(i) out<<',';
					out<<decl.at(i).type<<' '<<decl.at(i).name;
				}
				out<<')';
				handle+=(3+decl.size()*3);
			}
			break;
		case token::token_type::START_BLOCK:
			out<<'{'<<std::endl;
			break;
		case token::token_type::END_BLOCK:
			out<<'}'<<std::endl;
			break;
		case token::token_type::LABEL:
			if(!((handle+1)<tkns.size())) return (void)(std::cerr<<"Expected Token to Exist"<<std::endl);
			if(!(tkns.at(handle+1).type==token::token_type::ID)) return (void)(std::cerr<<"Expected Id at["<<tkns.at(handle+1).line<<"]["<<tkns.at(handle+1).pos<<"]["<<tkns.at(handle+1).handle<<']'<<std::endl);
			out<<tkns.at(++handle).value<<":\n";
			if(!(tkns.at(handle+1).type==token::token_type::END_STATEMENT)) return (void)(std::cerr<<"Expected Semicolon at["<<tkns.at(handle+1).line<<"]["<<tkns.at(handle+1).pos<<"]["<<tkns.at(handle+1).handle<<']'<<std::endl);
			handle++;
			break;
		case token::token_type::IF:
			out<<"if";
			break;
		case token::token_type::GOTO:
			if(!((handle+1)<tkns.size())) return (void)(std::cerr<<"Expected Token to Exist"<<std::endl);
			if(!(tkns.at(handle+1).type==token::token_type::ID)) return (void)(std::cerr<<"Expected Id at["<<tkns.at(handle+1).line<<"]["<<tkns.at(handle+1).pos<<"]["<<tkns.at(handle+1).handle<<']'<<std::endl);
			out<<"goto "<<tkns.at(++handle).value;
			break;
		case token::token_type::END_STATEMENT:
			out<<';'<<std::endl;
			break;
		case token::token_type::OPEN_ARGS:
			{
				unsigned depth=1;
				unsigned jmp=0;
				for(unsigned i=1;(handle+i)<tkns.size();i++){
					if(tkns.at(handle+i).type==token::token_type::OPEN_ARGS) depth++;
					else if(tkns.at(handle+i).type==token::token_type::CLOSE_ARGS) depth--;
					if(!depth){
						jmp=i;
						break;
					}
				}
				if(!((handle+1+jmp)<tkns.size())) return (void)(std::cerr<<"Expected Token to exist"<<std::endl);
				if(tkns.at(handle+1+jmp).type==token::token_type::AS){
					if(!((handle+3+jmp)<tkns.size())) return (void)(std::cerr<<"Expected Tokens to exist"<<std::endl);
					if(!(tkns.at(handle+2+jmp).type==token::token_type::ID)) return (void)(std::cerr<<"Expected Id at["<<tkns.at(handle+2+jmp).line<<"]["<<tkns.at(handle+jmp+2).pos<<"]["<<tkns.at(handle+2+jmp).handle<<']'<<std::endl);
					out<<'('<<tkns.at(handle+2+jmp).value<<((tkns.at(handle+3+jmp).type==token::token_type::POINT_OP)?'*':' ')<<')';
				}
			}
			out<<'(';
			break;
		case token::token_type::AS:
			if(!((handle+2)<tkns.size())) return (void)(std::cerr<<"Expected Tokens to Exist"<<std::endl);
			if(!(tkns.at(handle+1).type==token::token_type::ID)) return (void)(std::cerr<<"Expected Id at["<<tkns.at(handle+1).line<<"]["<<tkns.at(handle+1).pos<<"]["<<tkns.at(handle+1).handle<<']'<<std::endl);
			if(tkns.at(handle+2).type==token::token_type::POINT_OP) handle++;
			handle++;
			break;
		case token::token_type::ADD_OP:
			out<<'+';
			break;
		case token::token_type::AND_BIT_OP:
			out<<'&';
			break;
		case token::token_type::AND_LOG_OP:
			out<<"&&";
			break;
		case token::token_type::ARG_SEP:
			out<<',';
			break;
		case token::token_type::ASS:
			out<<'=';
			break;
		case token::token_type::CHAR_LIT:
			out<<'\''<<tkns.at(handle).value<<'\'';
			break;
		case token::token_type::CLOSE_ARGS:
			out<<')';
			break;
		case token::token_type::DIV_OP:
			out<<'/';
			break;
		case token::token_type::EQU_OP:
			out<<"==";
			break;
		case token::token_type::GREAT_OP:
			out<<'>';
			break;
		case token::token_type::ID:
		case token::token_type::INT_LIT:
			out<<tkns.at(handle).value<<' ';
			break;
		case token::token_type::LESS_OP:
			out<<'<';
			break;
		case token::token_type::MUL_OP:
			out<<'*';
			break;
		case token::token_type::NOT_BIT_OP:
			out<<'~';
			break;
		case token::token_type::NOT_LOG_OP:
			out<<'!';
			break;
		case token::token_type::OR_BIT_OP:
			out<<'|';
			break;
		case token::token_type::OR_LOG_OP:
			out<<"||";
			break;
		case token::token_type::POINT_OP:
			out<<'*';
			break;
		case token::token_type::PROGRAM:
			out<<"int main(int argc,char** argv)";
			break;
		case token::token_type::REM_OP:
			out<<'%';
			break;
		case token::token_type::RETURN:
			out<<"return ";
			break;
		case token::token_type::STR_LIT:
			out<<'"'<<tkns.at(handle).value<<'"';
			break;
		case token::token_type::SUB_OP:
			out<<'-';
			break;
		case token::token_type::XOR_BIT_OP:
			out<<'^';
			break;
		case token::token_type::XOR_LOG_OP:
			out<<"^^";
			break;
		}
	}
	out.close();
	std::system("gcc -o program.out program.c");
}
int main(){
	std::string name;
	std::cin>>name;
	std::string value=read_file(name);
	std::vector<token> tkns=tokenize(value);
	compile(tkns);
}
