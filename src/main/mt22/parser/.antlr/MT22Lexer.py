# Generated from d:\Documents\OISP\PPL\assignment3\src\main\mt22\parser\MT22.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2<")
        buf.write("\u01d3\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\3\2\3\2\3\2")
        buf.write("\3\2\7\2\u0088\n\2\f\2\16\2\u008b\13\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\3\3\3\3\3\3\3\7\3\u0096\n\3\f\3\16\3\u0099\13\3")
        buf.write("\3\3\3\3\3\4\3\4\3\4\7\4\u00a0\n\4\f\4\16\4\u00a3\13\4")
        buf.write("\3\4\3\4\6\4\u00a7\n\4\r\4\16\4\u00a8\7\4\u00ab\n\4\f")
        buf.write("\4\16\4\u00ae\13\4\5\4\u00b0\n\4\3\4\3\4\3\5\3\5\7\5\u00b6")
        buf.write("\n\5\f\5\16\5\u00b9\13\5\3\6\3\6\5\6\u00bd\n\6\3\6\6\6")
        buf.write("\u00c0\n\6\r\6\16\6\u00c1\3\7\3\7\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\5\7\u00d1\n\7\3\7\3\7\3\b\3\b")
        buf.write("\5\b\u00d7\n\b\3\t\3\t\3\t\3\n\3\n\3\n\7\n\u00df\n\n\f")
        buf.write("\n\16\n\u00e2\13\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3")
        buf.write("\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3")
        buf.write("\16\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3 \3 \3!\3!\3\"\3")
        buf.write("\"\3#\3#\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3")
        buf.write("+\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3")
        buf.write("\62\3\62\3\62\3\63\3\63\3\63\3\64\3\64\3\64\3\65\3\65")
        buf.write("\3\65\3\66\3\66\3\67\3\67\3\67\38\38\39\39\39\3:\3:\3")
        buf.write(";\3;\3<\3<\3=\3=\5=\u01a6\n=\3=\3=\3=\7=\u01ab\n=\f=\16")
        buf.write("=\u01ae\13=\3>\6>\u01b1\n>\r>\16>\u01b2\3>\3>\3?\3?\3")
        buf.write("?\3?\7?\u01bb\n?\f?\16?\u01be\13?\3?\3?\3?\3?\3@\3@\3")
        buf.write("@\7@\u01c7\n@\f@\16@\u01ca\13@\3@\5@\u01cd\n@\3@\3@\3")
        buf.write("A\3A\3A\4\u0089\u00e0\2B\3\3\5\4\7\5\t\2\13\2\r\6\17\7")
        buf.write("\21\2\23\b\25\t\27\n\31\13\33\f\35\r\37\16!\17#\20%\21")
        buf.write("\'\22)\23+\24-\25/\26\61\27\63\30\65\31\67\329\33;\34")
        buf.write("=\35?\36A\37C E!G\"I#K$M%O&Q\'S(U)W*Y+[,]-_.a/c\60e\61")
        buf.write("g\62i\63k\64m\65o\66q\67s\2u\2w\2y8{9}:\177;\u0081<\3")
        buf.write("\2\26\4\2\f\f\17\17\3\2\62\62\3\2\63;\3\2aa\3\2\60\60")
        buf.write("\4\2GGgg\4\2--//\3\2^^\n\2$$))^^ddhhppttvv\3\2$$\5\2$")
        buf.write("$))^^\3\2--\3\2//\3\2,,\3\2\61\61\3\2\'\'\4\2C\\c|\3\2")
        buf.write("\62;\5\2\13\f\17\17\"\"\3\3\f\f\2\u01e4\2\3\3\2\2\2\2")
        buf.write("\5\3\2\2\2\2\7\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2")
        buf.write("%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3")
        buf.write("\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q")
        buf.write("\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2")
        buf.write("\2\2\u0081\3\2\2\2\3\u0083\3\2\2\2\5\u0091\3\2\2\2\7\u00af")
        buf.write("\3\2\2\2\t\u00b3\3\2\2\2\13\u00ba\3\2\2\2\r\u00d0\3\2")
        buf.write("\2\2\17\u00d6\3\2\2\2\21\u00d8\3\2\2\2\23\u00db\3\2\2")
        buf.write("\2\25\u00e7\3\2\2\2\27\u00ef\3\2\2\2\31\u00f5\3\2\2\2")
        buf.write("\33\u00fd\3\2\2\2\35\u0104\3\2\2\2\37\u010a\3\2\2\2!\u010f")
        buf.write("\3\2\2\2#\u0114\3\2\2\2%\u011a\3\2\2\2\'\u011f\3\2\2\2")
        buf.write(")\u0123\3\2\2\2+\u0129\3\2\2\2-\u012c\3\2\2\2/\u0132\3")
        buf.write("\2\2\2\61\u013b\3\2\2\2\63\u013e\3\2\2\2\65\u0143\3\2")
        buf.write("\2\2\67\u014a\3\2\2\29\u014e\3\2\2\2;\u0157\3\2\2\2=\u015a")
        buf.write("\3\2\2\2?\u0162\3\2\2\2A\u0164\3\2\2\2C\u0166\3\2\2\2")
        buf.write("E\u0168\3\2\2\2G\u016a\3\2\2\2I\u016c\3\2\2\2K\u016e\3")
        buf.write("\2\2\2M\u0170\3\2\2\2O\u0172\3\2\2\2Q\u0174\3\2\2\2S\u0176")
        buf.write("\3\2\2\2U\u0178\3\2\2\2W\u017b\3\2\2\2Y\u017d\3\2\2\2")
        buf.write("[\u017f\3\2\2\2]\u0181\3\2\2\2_\u0183\3\2\2\2a\u0185\3")
        buf.write("\2\2\2c\u0187\3\2\2\2e\u018a\3\2\2\2g\u018d\3\2\2\2i\u0190")
        buf.write("\3\2\2\2k\u0193\3\2\2\2m\u0195\3\2\2\2o\u0198\3\2\2\2")
        buf.write("q\u019a\3\2\2\2s\u019d\3\2\2\2u\u019f\3\2\2\2w\u01a1\3")
        buf.write("\2\2\2y\u01a5\3\2\2\2{\u01b0\3\2\2\2}\u01b6\3\2\2\2\177")
        buf.write("\u01c3\3\2\2\2\u0081\u01d0\3\2\2\2\u0083\u0084\7\61\2")
        buf.write("\2\u0084\u0085\7,\2\2\u0085\u0089\3\2\2\2\u0086\u0088")
        buf.write("\13\2\2\2\u0087\u0086\3\2\2\2\u0088\u008b\3\2\2\2\u0089")
        buf.write("\u008a\3\2\2\2\u0089\u0087\3\2\2\2\u008a\u008c\3\2\2\2")
        buf.write("\u008b\u0089\3\2\2\2\u008c\u008d\7,\2\2\u008d\u008e\7")
        buf.write("\61\2\2\u008e\u008f\3\2\2\2\u008f\u0090\b\2\2\2\u0090")
        buf.write("\4\3\2\2\2\u0091\u0092\7\61\2\2\u0092\u0093\7\61\2\2\u0093")
        buf.write("\u0097\3\2\2\2\u0094\u0096\n\2\2\2\u0095\u0094\3\2\2\2")
        buf.write("\u0096\u0099\3\2\2\2\u0097\u0095\3\2\2\2\u0097\u0098\3")
        buf.write("\2\2\2\u0098\u009a\3\2\2\2\u0099\u0097\3\2\2\2\u009a\u009b")
        buf.write("\b\3\2\2\u009b\6\3\2\2\2\u009c\u00b0\t\3\2\2\u009d\u00a1")
        buf.write("\t\4\2\2\u009e\u00a0\5w<\2\u009f\u009e\3\2\2\2\u00a0\u00a3")
        buf.write("\3\2\2\2\u00a1\u009f\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2")
        buf.write("\u00ac\3\2\2\2\u00a3\u00a1\3\2\2\2\u00a4\u00a6\t\5\2\2")
        buf.write("\u00a5\u00a7\5w<\2\u00a6\u00a5\3\2\2\2\u00a7\u00a8\3\2")
        buf.write("\2\2\u00a8\u00a6\3\2\2\2\u00a8\u00a9\3\2\2\2\u00a9\u00ab")
        buf.write("\3\2\2\2\u00aa\u00a4\3\2\2\2\u00ab\u00ae\3\2\2\2\u00ac")
        buf.write("\u00aa\3\2\2\2\u00ac\u00ad\3\2\2\2\u00ad\u00b0\3\2\2\2")
        buf.write("\u00ae\u00ac\3\2\2\2\u00af\u009c\3\2\2\2\u00af\u009d\3")
        buf.write("\2\2\2\u00b0\u00b1\3\2\2\2\u00b1\u00b2\b\4\3\2\u00b2\b")
        buf.write("\3\2\2\2\u00b3\u00b7\t\6\2\2\u00b4\u00b6\5w<\2\u00b5\u00b4")
        buf.write("\3\2\2\2\u00b6\u00b9\3\2\2\2\u00b7\u00b5\3\2\2\2\u00b7")
        buf.write("\u00b8\3\2\2\2\u00b8\n\3\2\2\2\u00b9\u00b7\3\2\2\2\u00ba")
        buf.write("\u00bc\t\7\2\2\u00bb\u00bd\t\b\2\2\u00bc\u00bb\3\2\2\2")
        buf.write("\u00bc\u00bd\3\2\2\2\u00bd\u00bf\3\2\2\2\u00be\u00c0\5")
        buf.write("w<\2\u00bf\u00be\3\2\2\2\u00c0\u00c1\3\2\2\2\u00c1\u00bf")
        buf.write("\3\2\2\2\u00c1\u00c2\3\2\2\2\u00c2\f\3\2\2\2\u00c3\u00c4")
        buf.write("\5\7\4\2\u00c4\u00c5\5\t\5\2\u00c5\u00c6\5\13\6\2\u00c6")
        buf.write("\u00d1\3\2\2\2\u00c7\u00c8\5\7\4\2\u00c8\u00c9\5\13\6")
        buf.write("\2\u00c9\u00d1\3\2\2\2\u00ca\u00cb\5\t\5\2\u00cb\u00cc")
        buf.write("\5\13\6\2\u00cc\u00d1\3\2\2\2\u00cd\u00ce\5\7\4\2\u00ce")
        buf.write("\u00cf\5\t\5\2\u00cf\u00d1\3\2\2\2\u00d0\u00c3\3\2\2\2")
        buf.write("\u00d0\u00c7\3\2\2\2\u00d0\u00ca\3\2\2\2\u00d0\u00cd\3")
        buf.write("\2\2\2\u00d1\u00d2\3\2\2\2\u00d2\u00d3\b\7\4\2\u00d3\16")
        buf.write("\3\2\2\2\u00d4\u00d7\5%\23\2\u00d5\u00d7\5#\22\2\u00d6")
        buf.write("\u00d4\3\2\2\2\u00d6\u00d5\3\2\2\2\u00d7\20\3\2\2\2\u00d8")
        buf.write("\u00d9\t\t\2\2\u00d9\u00da\t\n\2\2\u00da\22\3\2\2\2\u00db")
        buf.write("\u00e0\t\13\2\2\u00dc\u00df\5\21\t\2\u00dd\u00df\n\f\2")
        buf.write("\2\u00de\u00dc\3\2\2\2\u00de\u00dd\3\2\2\2\u00df\u00e2")
        buf.write("\3\2\2\2\u00e0\u00e1\3\2\2\2\u00e0\u00de\3\2\2\2\u00e1")
        buf.write("\u00e3\3\2\2\2\u00e2\u00e0\3\2\2\2\u00e3\u00e4\t\13\2")
        buf.write("\2\u00e4\u00e5\3\2\2\2\u00e5\u00e6\b\n\5\2\u00e6\24\3")
        buf.write("\2\2\2\u00e7\u00e8\7k\2\2\u00e8\u00e9\7p\2\2\u00e9\u00ea")
        buf.write("\7v\2\2\u00ea\u00eb\7g\2\2\u00eb\u00ec\7i\2\2\u00ec\u00ed")
        buf.write("\7g\2\2\u00ed\u00ee\7t\2\2\u00ee\26\3\2\2\2\u00ef\u00f0")
        buf.write("\7h\2\2\u00f0\u00f1\7n\2\2\u00f1\u00f2\7q\2\2\u00f2\u00f3")
        buf.write("\7c\2\2\u00f3\u00f4\7v\2\2\u00f4\30\3\2\2\2\u00f5\u00f6")
        buf.write("\7d\2\2\u00f6\u00f7\7q\2\2\u00f7\u00f8\7q\2\2\u00f8\u00f9")
        buf.write("\7n\2\2\u00f9\u00fa\7g\2\2\u00fa\u00fb\7c\2\2\u00fb\u00fc")
        buf.write("\7p\2\2\u00fc\32\3\2\2\2\u00fd\u00fe\7u\2\2\u00fe\u00ff")
        buf.write("\7v\2\2\u00ff\u0100\7t\2\2\u0100\u0101\7k\2\2\u0101\u0102")
        buf.write("\7p\2\2\u0102\u0103\7i\2\2\u0103\34\3\2\2\2\u0104\u0105")
        buf.write("\7c\2\2\u0105\u0106\7t\2\2\u0106\u0107\7t\2\2\u0107\u0108")
        buf.write("\7c\2\2\u0108\u0109\7{\2\2\u0109\36\3\2\2\2\u010a\u010b")
        buf.write("\7x\2\2\u010b\u010c\7q\2\2\u010c\u010d\7k\2\2\u010d\u010e")
        buf.write("\7f\2\2\u010e \3\2\2\2\u010f\u0110\7c\2\2\u0110\u0111")
        buf.write("\7w\2\2\u0111\u0112\7v\2\2\u0112\u0113\7q\2\2\u0113\"")
        buf.write("\3\2\2\2\u0114\u0115\7h\2\2\u0115\u0116\7c\2\2\u0116\u0117")
        buf.write("\7n\2\2\u0117\u0118\7u\2\2\u0118\u0119\7g\2\2\u0119$\3")
        buf.write("\2\2\2\u011a\u011b\7v\2\2\u011b\u011c\7t\2\2\u011c\u011d")
        buf.write("\7w\2\2\u011d\u011e\7g\2\2\u011e&\3\2\2\2\u011f\u0120")
        buf.write("\7h\2\2\u0120\u0121\7q\2\2\u0121\u0122\7t\2\2\u0122(\3")
        buf.write("\2\2\2\u0123\u0124\7y\2\2\u0124\u0125\7j\2\2\u0125\u0126")
        buf.write("\7k\2\2\u0126\u0127\7n\2\2\u0127\u0128\7g\2\2\u0128*\3")
        buf.write("\2\2\2\u0129\u012a\7f\2\2\u012a\u012b\7q\2\2\u012b,\3")
        buf.write("\2\2\2\u012c\u012d\7d\2\2\u012d\u012e\7t\2\2\u012e\u012f")
        buf.write("\7g\2\2\u012f\u0130\7c\2\2\u0130\u0131\7m\2\2\u0131.\3")
        buf.write("\2\2\2\u0132\u0133\7e\2\2\u0133\u0134\7q\2\2\u0134\u0135")
        buf.write("\7p\2\2\u0135\u0136\7v\2\2\u0136\u0137\7k\2\2\u0137\u0138")
        buf.write("\7p\2\2\u0138\u0139\7w\2\2\u0139\u013a\7g\2\2\u013a\60")
        buf.write("\3\2\2\2\u013b\u013c\7k\2\2\u013c\u013d\7h\2\2\u013d\62")
        buf.write("\3\2\2\2\u013e\u013f\7g\2\2\u013f\u0140\7n\2\2\u0140\u0141")
        buf.write("\7u\2\2\u0141\u0142\7g\2\2\u0142\64\3\2\2\2\u0143\u0144")
        buf.write("\7t\2\2\u0144\u0145\7g\2\2\u0145\u0146\7v\2\2\u0146\u0147")
        buf.write("\7w\2\2\u0147\u0148\7t\2\2\u0148\u0149\7p\2\2\u0149\66")
        buf.write("\3\2\2\2\u014a\u014b\7q\2\2\u014b\u014c\7w\2\2\u014c\u014d")
        buf.write("\7v\2\2\u014d8\3\2\2\2\u014e\u014f\7h\2\2\u014f\u0150")
        buf.write("\7w\2\2\u0150\u0151\7p\2\2\u0151\u0152\7e\2\2\u0152\u0153")
        buf.write("\7v\2\2\u0153\u0154\7k\2\2\u0154\u0155\7q\2\2\u0155\u0156")
        buf.write("\7p\2\2\u0156:\3\2\2\2\u0157\u0158\7q\2\2\u0158\u0159")
        buf.write("\7h\2\2\u0159<\3\2\2\2\u015a\u015b\7k\2\2\u015b\u015c")
        buf.write("\7p\2\2\u015c\u015d\7j\2\2\u015d\u015e\7g\2\2\u015e\u015f")
        buf.write("\7t\2\2\u015f\u0160\7k\2\2\u0160\u0161\7v\2\2\u0161>\3")
        buf.write("\2\2\2\u0162\u0163\7*\2\2\u0163@\3\2\2\2\u0164\u0165\7")
        buf.write("+\2\2\u0165B\3\2\2\2\u0166\u0167\7]\2\2\u0167D\3\2\2\2")
        buf.write("\u0168\u0169\7_\2\2\u0169F\3\2\2\2\u016a\u016b\7}\2\2")
        buf.write("\u016bH\3\2\2\2\u016c\u016d\7\177\2\2\u016dJ\3\2\2\2\u016e")
        buf.write("\u016f\7\60\2\2\u016fL\3\2\2\2\u0170\u0171\7.\2\2\u0171")
        buf.write("N\3\2\2\2\u0172\u0173\7=\2\2\u0173P\3\2\2\2\u0174\u0175")
        buf.write("\7<\2\2\u0175R\3\2\2\2\u0176\u0177\7?\2\2\u0177T\3\2\2")
        buf.write("\2\u0178\u0179\7<\2\2\u0179\u017a\7<\2\2\u017aV\3\2\2")
        buf.write("\2\u017b\u017c\t\r\2\2\u017cX\3\2\2\2\u017d\u017e\t\16")
        buf.write("\2\2\u017eZ\3\2\2\2\u017f\u0180\t\17\2\2\u0180\\\3\2\2")
        buf.write("\2\u0181\u0182\t\20\2\2\u0182^\3\2\2\2\u0183\u0184\t\21")
        buf.write("\2\2\u0184`\3\2\2\2\u0185\u0186\7#\2\2\u0186b\3\2\2\2")
        buf.write("\u0187\u0188\7(\2\2\u0188\u0189\7(\2\2\u0189d\3\2\2\2")
        buf.write("\u018a\u018b\7~\2\2\u018b\u018c\7~\2\2\u018cf\3\2\2\2")
        buf.write("\u018d\u018e\7?\2\2\u018e\u018f\7?\2\2\u018fh\3\2\2\2")
        buf.write("\u0190\u0191\7#\2\2\u0191\u0192\7?\2\2\u0192j\3\2\2\2")
        buf.write("\u0193\u0194\7@\2\2\u0194l\3\2\2\2\u0195\u0196\7@\2\2")
        buf.write("\u0196\u0197\7?\2\2\u0197n\3\2\2\2\u0198\u0199\7>\2\2")
        buf.write("\u0199p\3\2\2\2\u019a\u019b\7>\2\2\u019b\u019c\7?\2\2")
        buf.write("\u019cr\3\2\2\2\u019d\u019e\t\22\2\2\u019et\3\2\2\2\u019f")
        buf.write("\u01a0\t\5\2\2\u01a0v\3\2\2\2\u01a1\u01a2\t\23\2\2\u01a2")
        buf.write("x\3\2\2\2\u01a3\u01a6\5s:\2\u01a4\u01a6\5u;\2\u01a5\u01a3")
        buf.write("\3\2\2\2\u01a5\u01a4\3\2\2\2\u01a6\u01ac\3\2\2\2\u01a7")
        buf.write("\u01ab\5s:\2\u01a8\u01ab\5u;\2\u01a9\u01ab\5w<\2\u01aa")
        buf.write("\u01a7\3\2\2\2\u01aa\u01a8\3\2\2\2\u01aa\u01a9\3\2\2\2")
        buf.write("\u01ab\u01ae\3\2\2\2\u01ac\u01aa\3\2\2\2\u01ac\u01ad\3")
        buf.write("\2\2\2\u01adz\3\2\2\2\u01ae\u01ac\3\2\2\2\u01af\u01b1")
        buf.write("\t\24\2\2\u01b0\u01af\3\2\2\2\u01b1\u01b2\3\2\2\2\u01b2")
        buf.write("\u01b0\3\2\2\2\u01b2\u01b3\3\2\2\2\u01b3\u01b4\3\2\2\2")
        buf.write("\u01b4\u01b5\b>\2\2\u01b5|\3\2\2\2\u01b6\u01bc\7$\2\2")
        buf.write("\u01b7\u01bb\n\13\2\2\u01b8\u01b9\7^\2\2\u01b9\u01bb\7")
        buf.write("$\2\2\u01ba\u01b7\3\2\2\2\u01ba\u01b8\3\2\2\2\u01bb\u01be")
        buf.write("\3\2\2\2\u01bc\u01ba\3\2\2\2\u01bc\u01bd\3\2\2\2\u01bd")
        buf.write("\u01bf\3\2\2\2\u01be\u01bc\3\2\2\2\u01bf\u01c0\t\t\2\2")
        buf.write("\u01c0\u01c1\n\n\2\2\u01c1\u01c2\b?\6\2\u01c2~\3\2\2\2")
        buf.write("\u01c3\u01c8\t\13\2\2\u01c4\u01c7\5\21\t\2\u01c5\u01c7")
        buf.write("\n\f\2\2\u01c6\u01c4\3\2\2\2\u01c6\u01c5\3\2\2\2\u01c7")
        buf.write("\u01ca\3\2\2\2\u01c8\u01c6\3\2\2\2\u01c8\u01c9\3\2\2\2")
        buf.write("\u01c9\u01cc\3\2\2\2\u01ca\u01c8\3\2\2\2\u01cb\u01cd\t")
        buf.write("\25\2\2\u01cc\u01cb\3\2\2\2\u01cd\u01ce\3\2\2\2\u01ce")
        buf.write("\u01cf\b@\7\2\u01cf\u0080\3\2\2\2\u01d0\u01d1\13\2\2\2")
        buf.write("\u01d1\u01d2\bA\b\2\u01d2\u0082\3\2\2\2\31\2\u0089\u0097")
        buf.write("\u00a1\u00a8\u00ac\u00af\u00b7\u00bc\u00c1\u00d0\u00d6")
        buf.write("\u00de\u00e0\u01a5\u01aa\u01ac\u01b2\u01ba\u01bc\u01c6")
        buf.write("\u01c8\u01cc\t\b\2\2\3\4\2\3\7\3\3\n\4\3?\5\3@\6\3A\7")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    C_COMMENT = 1
    CPP_COMMENT = 2
    INTLIT = 3
    FLOATLIT = 4
    BOOLLIT = 5
    STRINGLIT = 6
    INTEGER = 7
    FLOAT = 8
    BOOLEAN = 9
    STRING = 10
    ARRAY = 11
    VOID = 12
    AUTO = 13
    FALSE = 14
    TRUE = 15
    FOR = 16
    WHILE = 17
    DO = 18
    BREAK = 19
    CONTINUE = 20
    IF = 21
    ELSE = 22
    RETURN = 23
    OUT = 24
    FUNCTION = 25
    OF = 26
    INHERIT = 27
    LRB = 28
    RRB = 29
    LSB = 30
    RSB = 31
    LCB = 32
    RCB = 33
    DOT = 34
    COMMA = 35
    SM_COLON = 36
    COLONS = 37
    ASSIGN = 38
    STRING_CONCAT = 39
    ADD_OP = 40
    MIN_OP = 41
    MUL_OP = 42
    DIV_OP = 43
    MOD_OP = 44
    NOT = 45
    AND = 46
    OR = 47
    EQUAL = 48
    NEQ = 49
    GRT = 50
    GEQ = 51
    LWT = 52
    LEQ = 53
    ID = 54
    WS = 55
    ILLEGAL_ESCAPE = 56
    UNCLOSE_STRING = 57
    ERROR_CHAR = 58

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'integer'", "'float'", "'boolean'", "'string'", "'array'", 
            "'void'", "'auto'", "'false'", "'true'", "'for'", "'while'", 
            "'do'", "'break'", "'continue'", "'if'", "'else'", "'return'", 
            "'out'", "'function'", "'of'", "'inherit'", "'('", "')'", "'['", 
            "']'", "'{'", "'}'", "'.'", "','", "';'", "':'", "'='", "'::'", 
            "'!'", "'&&'", "'||'", "'=='", "'!='", "'>'", "'>='", "'<'", 
            "'<='" ]

    symbolicNames = [ "<INVALID>",
            "C_COMMENT", "CPP_COMMENT", "INTLIT", "FLOATLIT", "BOOLLIT", 
            "STRINGLIT", "INTEGER", "FLOAT", "BOOLEAN", "STRING", "ARRAY", 
            "VOID", "AUTO", "FALSE", "TRUE", "FOR", "WHILE", "DO", "BREAK", 
            "CONTINUE", "IF", "ELSE", "RETURN", "OUT", "FUNCTION", "OF", 
            "INHERIT", "LRB", "RRB", "LSB", "RSB", "LCB", "RCB", "DOT", 
            "COMMA", "SM_COLON", "COLONS", "ASSIGN", "STRING_CONCAT", "ADD_OP", 
            "MIN_OP", "MUL_OP", "DIV_OP", "MOD_OP", "NOT", "AND", "OR", 
            "EQUAL", "NEQ", "GRT", "GEQ", "LWT", "LEQ", "ID", "WS", "ILLEGAL_ESCAPE", 
            "UNCLOSE_STRING", "ERROR_CHAR" ]

    ruleNames = [ "C_COMMENT", "CPP_COMMENT", "INTLIT", "DEC_PART", "EXP_PART", 
                  "FLOATLIT", "BOOLLIT", "ESCAPE_SEQUENCE", "STRINGLIT", 
                  "INTEGER", "FLOAT", "BOOLEAN", "STRING", "ARRAY", "VOID", 
                  "AUTO", "FALSE", "TRUE", "FOR", "WHILE", "DO", "BREAK", 
                  "CONTINUE", "IF", "ELSE", "RETURN", "OUT", "FUNCTION", 
                  "OF", "INHERIT", "LRB", "RRB", "LSB", "RSB", "LCB", "RCB", 
                  "DOT", "COMMA", "SM_COLON", "COLONS", "ASSIGN", "STRING_CONCAT", 
                  "ADD_OP", "MIN_OP", "MUL_OP", "DIV_OP", "MOD_OP", "NOT", 
                  "AND", "OR", "EQUAL", "NEQ", "GRT", "GEQ", "LWT", "LEQ", 
                  "LETTER", "UNDERSCORE", "DIGIT", "ID", "WS", "ILLEGAL_ESCAPE", 
                  "UNCLOSE_STRING", "ERROR_CHAR" ]

    grammarFileName = "MT22.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[2] = self.INTLIT_action 
            actions[5] = self.FLOATLIT_action 
            actions[8] = self.STRINGLIT_action 
            actions[61] = self.ILLEGAL_ESCAPE_action 
            actions[62] = self.UNCLOSE_STRING_action 
            actions[63] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INTLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace('_','')
     

    def FLOATLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text.replace('_','')
     

    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            self.text = self.text[1:-1]
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

            	string_error = str(self.text)
            	raise IllegalEscape(string_error[1:])

     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

            	string_error = str(self.text)
            	escape = '\n'
            	if string_error[-1] == escape:
            		raise UncloseString(self.text[1:-2])
            	else:
            		raise UncloseString(self.text[1:])

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:
            raise ErrorToken(self.text)
     


