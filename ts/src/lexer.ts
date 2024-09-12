import { Token, TokenType, ASSIGN, PLUS, LPAREN, RPAREN, LBRACE, RBRACE, COMMA, SEMICOLON, EOF } from './token';

export class Lexer {
  private input: string;
  private position: number = 0; // current position in input (points to current char)
  private readPosition: number = 0; // current reading position in input (after current char)
  private ch: string = ''; // current char under examination

  constructor(input: string) {
    this.input = input;
    this.readChar(); // Initialize the first character
  }

  private readChar(): void {
    if (this.readPosition >= this.input.length) {
      this.ch = '';
    } else {
      this.ch = this.input[this.readPosition];
    }
    this.position = this.readPosition;
    this.readPosition += 1;
  }
}