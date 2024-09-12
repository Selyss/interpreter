// Importing the necessary modules and types
import { Lexer } from '../src/lexer'; // Assume you have a lexer.ts file that exports a Lexer class
import { TokenType, Token, ASSIGN, PLUS, LPAREN, RPAREN, LBRACE, RBRACE, COMMA, SEMICOLON, EOF } from '../src/token'; // Assume you have a token.ts file that exports TokenType enum and Token interface


describe('Lexer', () => {
  test('NextToken', () => {
    const input = '=+(){},;';
    const tests: { expectedType: TokenType; expectedLiteral: string }[] = [
      { expectedType: ASSIGN, expectedLiteral: '=' },
      { expectedType: PLUS, expectedLiteral: '+' },
      { expectedType: LPAREN, expectedLiteral: '(' },
      { expectedType: RPAREN, expectedLiteral: ')' },
      { expectedType: LBRACE, expectedLiteral: '{' },
      { expectedType: RBRACE, expectedLiteral: '}' },
      { expectedType: COMMA, expectedLiteral: ',' },
      { expectedType: SEMICOLON, expectedLiteral: ';' },
      { expectedType: EOF, expectedLiteral: '' },
    ];

    const lexer = new Lexer(input);

    tests.forEach((tt, i) => {
      const tok = lexer.nextToken();
      expect(tok.type).toBe(tt.expectedType);
      expect(tok.literal).toBe(tt.expectedLiteral);
    });
  });
});
