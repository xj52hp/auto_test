__author__ = 'Administrator'
import configparser
def read_email( Memail):

    config = configparser.ConfigParser()
    config.read(Memail.file, encoding='utf-8')
    Memail.report = "report.xlsx"
    Memail.to_addr = eval(config['DEFAULT']['to_addr'])
    Memail.mail_host = config['DEFAULT']['mail_host']
    Memail.mail_user = config['DEFAULT']['mail_user']
    Memail.mail_pass =  config['DEFAULT']['mail_pass']
    Memail.port = config['DEFAULT']['port']
    Memail.headerMsg = config['DEFAULT']['headerMsg']
    Memail.attach = config['DEFAULT']['attach']
    return Memail
