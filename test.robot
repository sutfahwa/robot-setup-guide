*** Settings ***
Library    SeleniumLibrary
Library    common.py

*** Test Cases ***
Test Run robot
  Log  success
  ${driver_path}=    Get Driver Path With Browser    Chrome
  Open Browser    www.google.com    Chrome    executable_path=${driver_path}
