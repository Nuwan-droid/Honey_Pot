#libraries
import logging 
from logging.handlers import RotatingFileHandler
from flask import Flask, render_template, redirect, request, url_for


#Logging format
logging_format = logging.Formatter('%(asctime)s %(message)s')

#HTTP logger

funnel_logger = logging.getLogger('http_logger')
funnel_logger.setLevel(logging.INFO)
funnel_handler = RotatingFileHandler('http_audits.log', maxBytes=2000, backupCount=5)
funnel_handler.setFormatter(logging_format)
funnel_logger.addHandler(funnel_handler)
 

#baseline honeypot
