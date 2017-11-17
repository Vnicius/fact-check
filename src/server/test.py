import sys
from textprocess import SentenceGenerator

print(SentenceGenerator().generate_sentences(sys.argv[1]))