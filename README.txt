v2 seeks to improve upon v1 in the following ways:

- implementing the use of a virtual environment to run the application within (largely just for 
  upholding general best practices; I'm not actually concerned about issues with dependencies in 
  different projects (yet). 

- breaking the program into separate files for better comprehensibility. 
  This is my first time refactoring an application from one file into multiple files.

- restructuring the application code to be more eloquent and modular (trying to improve on DRY). 
  The current code base feels too hard-coded, and not modular enough (or just isn't intelligently written).

Note: all files root to application.py