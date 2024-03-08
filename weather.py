from _tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import timezoneFinder
from _datetime import datetime
import requests
import pytz

root=Tk()
root.title("weather App")
root.geometry("900*500+300+200")
root.resizable(False,False)

root.mainloop()