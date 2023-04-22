v2 seeks to improve upon v1 in the following ways:

- implementing the use of a virtual environment to run the application within (largely just for 
  upholding general best practices; I'm not actually concerned about 

- breaking the program into separate files for better comprehensibility. 
  This is my first time refactoring an application from one file into multiple files.

- restructuring the application code to be more eloquent and modular (trying to improve on DRY). 
  The current code base feels too hard-coded, and not modular enough (or just isn't intelligently written).
  For example, I currently run move validation through separate methods in each Piece class which share
  identical naming conventions. This is way too prone to error (what happens if one of the Piece's move validation 
  class names is accidentally - or intentionally - changed?). In this scenario, v2 will try to migrate the 
  fragmented move validation methods local to each piece class to a single universal move validation method
  local to the Game class which contains the appropriate logic for ALL pieces. 