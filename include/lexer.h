#ifndef AURUM_LEXER_FILE
#define AURUM_LEXER_FILE
#include "shared.h"
namespace aurum{
    namespace lexer{
		enum class token_type : shared::integers::byte {
			INVALID,
			ID,
			RETURN,
			INT_LIT,
			STR_LIT,
			END_STATEMENT,
			ADD_OP,
			SUB_OP,
			DIV_OP,
			MUL_OP,
			POINT_OP,
			NOT_OP,
			GET_ATTRIB,
			POINT_ATTRIB,
			SUB_ASS,
			AND_OP,
			DEC_OP,
			INC_OP,
			ADD_ASS,
			MUL_ASS,
			EXP_OP,
			AND_LOG,
			EXP_ASS,
			AND_ASS,
			LESS_LOG,
			LSH_OP,
			LSH_ASS,
			MORE_LOG,
			RSH_OP,
			RSH_ASS,
			OR_OP,
			OR_LOG,
			OR_ASS,
			XOR_OP,
			XOR_LOG,
			XOR_ASS,
			EQU_ASS,
			EQU_LOG,
			COMPILER_TAG,
			START,
			END,
			PROGRAM,
			CLASS,
			START_ARGS,
			END_ARGS,
			START_OFFSET,
			END_OFFSET,
			NOT_LOG,
			AUTO,
			LET,
			IF,
			ELF,
			ELSE,
			UNLESS,
			WHILE,
			UNTIL,
			FUNCTION,
			CLR,
			ARG_SEPERATOR,
			MEMBER,
			PROCEDURE,
			GET_THIS_TYPE,
			MOD_OP,
			CREATE,
			DESTROY,
			MOD_ASS,
			LETTER,
			EMBED,
			IMPORT,
			AS,
			OPEN_CLASS,
			STRUCT,
			_NULL,
			GET_TYPE,
			GET_SIZE,
			GET_LOC,
			FOREVER,
			PASS,
			SIGNED_TYPE,
			UNSIGNED_TYPE,
			DIV_ASS,
			CHAR_LIT,
			TYPEDEF,
			VARARGS,
			OPERATOR
		};
		struct token {
			token_type type;
			std::string val;
		};
		class lexer {
			std::string str;
			shared::integers::nat location;
			inline optional<char> peek();
			inline char consume();
		public:
			lexer();
			lexer(std::string);
			std::vector<token> tokenize();
			lexer& use(std::string);
			bool operator!();
			bool operator~();
		};
    };
};
#endif