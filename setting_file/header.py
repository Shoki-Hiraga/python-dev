import re
import requests
from bs4 import BeautifulSoup
import concurrent.futures
import gspread
import sys
import random
import os
import csv
import time
import pandas as pd
import logging
import pytesseract
import pdfplumber
import base64
import difflib
# import whisper
import json
import calendar
from urllib.parse import urljoin
from datetime import datetime, timedelta
from datetime import datetime
from PIL import Image
from io import BytesIO
from google.cloud import vision
# from google.cloud.vision import types
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from google.cloud import storage
from googleapiclient.discovery import build
from google.oauth2 import service_account
from oauth2client.service_account import ServiceAccountCredentials
import google.auth.transport.requests
import google.oauth2.credentials
import google_auth_oauthlib.flow
from google.ads.googleads.client import GoogleAdsClient
from selenium.webdriver.common.action_chains import ActionChains
import setting_file.file_path as file_path
from playwright.sync_api import sync_playwright
from urllib.parse import urlparse
from setting_file.user_agent import user_agents  # ユーザーエージェントのリストをインポート
from setting_file import csv_output_path, gcp_api, api_json, api_yaml  # 設定ファイルからCSVの出力パスとAPIのJSONをインポート
os.chdir(os.path.dirname(os.path.abspath(__file__)))# スクリプトが存在するディレクトリを作業ディレクトリとして設定

