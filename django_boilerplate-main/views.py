from django.shortcuts import render
from bs4 import BeautifulSoup as bs
# Create your views here.


def index(request):
    return render(request, 'index.html')

def web_scrap(request):

    t_html = request.post("url")

    t_soup = bs(t_html.text,"html.parser")
    p_con = t_soup.findAll("div",{"class":"details"})
    brand_con = t_soup.findAll("span",{"class":"value"})
    price_con = t_soup.findAll("span",{"class":"price actual-price"})

    filename = "information.csv"

    f = open(filename, "w")

    headers = "Brand , Product_Name , Price \n"
    f.write(headers)

    Product_name=[]
    product_brand=[]
    product_price=[]

    for p_name in p_con:
        Product_name.append(p_name.h2.a.text)
    
    for p_brand in brand_con:
        product_brand.append(p_brand.text.strip())
    
    for p_price in price_con:
        product_price.append(p_price.text)
    

    for i,j,k in zip(Product_name, product_brand, product_price):
        f.write(j + "," + i.replace("," "|")+ "," +k+ "\n")
    
    
        
    f.close()

    return render(request,'result.html')