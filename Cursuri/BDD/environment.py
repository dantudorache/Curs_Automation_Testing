from browser import Browser
from pages.ebay_homepage import Home_page

# context este ca o cutiuta in care vom stoca toate atributele ce pot fi folosite in alte fisiere
# before_all este o metoda recunoscuta de libraria behave si care se va executa inainte de toate testele
# after_all este o metoda recunoscuta de libraria behave si care se va executa dupa de toate testele

def before_all(context):
    context.browser = Browser()
    context.home_page_object = Home_page()

def after_all(context):
    context.browser.close()























