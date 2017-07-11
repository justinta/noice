# noice
This is a working POC right now. There is some work to do to clean it up and make it not shit.

Local note log. Prints out notes to stdout

key value notes. call with key, get value printed to stdout

```bash
% noice get test
This is a test note

% noice get cmd
ls -lthr
```

Next steps:  
  1. Fix cli args to not use `--` 
  1. Clean up noice.py database calls
  1. Add more args like `get all` or `list all` or something of that nature

Future nice to haves:  
  1. webapp? 
