from configparser import ConfigParser
from termcolor import colored
import numpy as np


changed_stanza = input("Enter stanza that you want to compare:")
config_old = ConfigParser()
config_new = ConfigParser()

config_old.read('indexes_old.conf')
config_new.read('indexes.conf')

stanzas_old = config_old.sections()
stanzas_new = config_new.sections()

#print(stanzas_old)
#print(stanzas_new)

if stanzas_old != stanzas_new:
    print("there are some stanza which is missing or extra added!!!")
    print("Diff stanzas as below")
    print(set(stanzas_old).symmetric_difference(set(stanzas_new)))
    print("if you want to contunue then press y\n\n")

stanzas = np.unique(stanzas_old + stanzas_new)

for stanza in stanzas:
    try:
        if config_old.get(stanza,changed_stanza) != config_new.get(stanza,changed_stanza):   
            print("Stanza " + colored(stanza,"yellow").rjust(75, " ") + "\tis changed from\t" + config_old.get(stanza,changed_stanza) + "\t--->>>\t" + config_new.get(stanza,changed_stanza))
    except Exception as e:
        print(colored(f"Exception !! {e}", "red"))
  
