*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  bob  secretbob1

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  bo  secretbob1
    Output Should Contain  Username must be 3 or above characters

Register With Valid Username And Too Short Password
    Input Credentials  bob  s1
    Output Should Contain  Password must be 8 or above characters

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  bob  secretbob
    Output Should Contain  Password must characters other than letters

*** Keywords ***
Input New Command And Create User
    Input New Command
    Create User  kalle  kalle123