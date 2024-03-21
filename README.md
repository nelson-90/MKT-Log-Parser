# MKT-Log-Parser
Tool to parse Mikrotik firewall logs (Spanish)

## Use
Export your mikrotik firewall log as log.txt. 
Replace log.txt with the fresh export
Execute the program

```bash
python3 filter.py
```

Select one of the menu options:

* 1- Parses the entire log.txt as ***DATE | SRC_IP | DST_IP | PROTOCOL | DST_PORT | OCURRENCES***
            Generates 2 files: filtered_log.txt and result.txt
* 2- Parses the entire log.txt as ***SRC_IP | DST_IP | PROTOCOL | DST_PORTS***
            Generates 2 files: filtered_log.txt and mapeo.txt
* 3- Parses log.txt entrys that match with a keyword as ***DATE | SRC_IP | DST_IP | PROTOCOL | DST_PORT | OCURRENCES***
            Generates 2 files: filtered_log.txt and result{keyword}.txt
* 4- Parses log.txt entrys that match with a keyword as ***SRC_IP | DST_IP | PROTOCOL | DST_PORTS***
            Generates 2 files: filtered_log.txt and mapeo{keyword}.txt
* 5- Shows help in spanish
* 0- Closes the program
