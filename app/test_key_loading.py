from flask import Flask, render_template, url_for, session, request, redirect
import os, json, urllib.request


FMP_key = "";
Open_Weather_Map_key = "";
NYT_key = "";
Calendarific_key = "";


FMP = open("../keys/key_FMP.txt", "r");
FMP_key = FMP.read();
print("FMP LOADED")

NYT = open("../keys/key_NYT.txt", "r");
NYT_key = NYT.read();
print("NYT LOADED")

Calendarific = open("../keys/key_Calendarific.txt", "r");
Calendarific_key = Calendarific.read();
print("CALENDARIFIC LOADED")

Open_Weather_Map = open("../keys/key_Open_Weather_Map.txt", "r");
Open_Weather_Map_key = Open_Weather_Map.read();
print("OPEN WEATHER MAP LOADED")

print("\nFMP: " + FMP_key)
print("OWM: " + Open_Weather_Map_key)
print("NYT: " + NYT_key)
print("CAL: " + Calendarific_key)
