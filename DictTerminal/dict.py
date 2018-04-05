#!/Users/poudel/miniconda3/bin/python
# -*- coding: utf-8 -*-#
"""
Using MacOS Dictionary using pyobjc and colorama modules.
    
@author: Bhishan Poudel
    
@date: Apr 4, 2018

Requires:
pip install -U pyobjc
pip install -U colorama
    
"""
# Imports
import sys

try:
  from DictionaryServices import *
except:
  print("WARNING: The pyobjc Python library was not found. You can install it by typing: 'pip install -U pyobjc'")
  print("..................\n")


try:
  from colorama import Fore, Back, Style
except:
  print("WARNING: The colorama Python library was not found. You can install it by typing: 'pip install colorama'")
  print("..................\n")





def main():
  """
  define.py

  Access the default OSX dictionary
  """
  try:
    searchword = sys.argv[1].encode().decode('utf-8')
  except IndexError:
    errmsg = 'You did not enter any terms to look up in the Dictionary.'
    print(errmsg)
    sys.exit()
  wordrange = (0, len(searchword))
  dictresult = DCSCopyTextDefinition(None, searchword, wordrange)
  if not dictresult:
    errmsg = "'%s' not found in Dictionary." % (searchword)
    print(errmsg.encode('utf-8'))
  else:
    s = dictresult.encode("utf-8")
    
    s = s.replace(b'\xe2\x96\xb6', b"\n\n\xe2\x96\xb6 ")  # arrow
    s = s.replace(b'\xe2\x80\xa2', b"\n\n\xe2\x80\xa2 ")  # bullet

    phr =  Style.BRIGHT + "\n\nPHRASES\n" + Style.RESET_ALL
    s = s.replace(b'PHRASES', phr.encode())

    deri = Style.BRIGHT + "\n\nDERIVATIVES\n" + Style.RESET_ALL
    s = s.replace(b'DERIVATIVES', deri.encode())
    
    # make numbers green
    for n in list('123456789'):
      num = Fore.GREEN + '('+ n + ')' + Style.RESET_ALL
      n2 = b'. ' + n.encode() 
      n2replace = b'. ' + num.encode()
      s = s.replace(n2, n2replace)

    orig = Fore.GREEN + "\n\nORIGIN\n" + Style.RESET_ALL
    s = s.replace(b'ORIGIN', orig.encode( ))

    entry = Fore.RED + "Definition of : " + searchword + "\n" +  Style.RESET_ALL

    print(entry)
    print(s.decode())
    print("\n---------------------------------")

if __name__ == '__main__':
  main()
