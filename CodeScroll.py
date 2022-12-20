# Program that reads all files in the ./Sources directory and picks one at random
# The program then reads the file and prints the contents to the screen
# the files contain programs and should be rendered as code with syntax highlighting

import os
import random
import time
import sys
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.lexers import CSharpLexer
from pygments.lexers import JavascriptLexer
from pygments.lexers import TextLexer
from pygments.formatters import TerminalFormatter

# class that reads the files and prints them to the screen
class CodeScroll:
    def __init__(self):
        self.cwd = os.getcwd()
        self.path = self.cwd + "/Sources/"
        if not os.path.exists(self.path):
            raise Exception("Sources directory does not exist")
        self.files = os.listdir(self.path)
        if len(self.files) == 0:
            raise Exception("No files in Sources directory")
        self.scrollSpeed = 20
        self.transitionSpeed = 10
        self.fileContents = ""
        
    # Set the scroll speed
    def setScrollSpeed(self, speed):
        self.scrollSpeed = speed
        
    # Set the transition speed
    def setTransitionSpeed(self, speed):
        self.transitionSpeed = speed
        
    # Get the scroll speed
    def getScrollSpeed(self):
        return self.scrollSpeed
    
    # Get the transition speed
    def getTransitionSpeed(self):
        return self.transitionSpeed
    
    # Get the file contents
    def getFileContents(self, file):
        with open(self.path + file, "r") as f:
            if file.endswith(".py"):
                self.fileContents = highlight(f.read(), PythonLexer(), TerminalFormatter())
            elif file.endswith(".cs"):
                self.fileContents = highlight(f.read(), CSharpLexer(), TerminalFormatter())
            elif file.endswith(".js"):
                self.fileContents = highlight(f.read(), JavascriptLexer(), TerminalFormatter())
            else:
                self.fileContents = highlight(f.read(), TextLexer(), TerminalFormatter())
            
    # Pick a random file
    def pickRandomFile(self):
        return random.choice(self.files)
    
    # Print the file contents to the screen
    def printFileContents(self):
        for line in self.fileContents:
            sys.stdout.write(line)
            sys.stdout.flush()
            time.sleep(1/self.scrollSpeed)
            
    # Clear the screen            
    def clearScreen(self):
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
        
    # Main loop
    def main(self):
        while True:
            self.clearScreen()
            self.getFileContents(self.pickRandomFile())
            self.printFileContents()
            time.sleep(self.transitionSpeed)
            
# Main
if __name__ == "__main__":
    cs = CodeScroll()
    cs.main()