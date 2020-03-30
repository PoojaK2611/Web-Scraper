from django.shortcuts import render,redirect
from .models import ScrapData
from .forms import SimpleForm
from bs4 import BeautifulSoup
import requests

def web_scraper(request):
    if request.method == 'POST':
        form = SimpleForm(request.POST)
        if form.is_valid():
            #   url to scrap         # url = 'https://websites.co.in/sitemap'
            url = form.cleaned_data['url']
            numOfSites = form.cleaned_data['NumOfSites']
            plain_html_text = requests.get(url)     #   Load html's plain data into a variable
            soup = BeautifulSoup(plain_html_text.text, 'html.parser')   #   parse the data
            get_table = soup.find('table')
            for each_url in get_table.find_all('a')[0:numOfSites]:
                if each_url.has_attr('href'):
                    url1 = each_url.attrs['href']
                    get_url = 'http:' + url1
                    print("url", get_url)
                    data = requests.get(get_url)
                    website_soup = BeautifulSoup(data.text, 'html.parser')
                    # results = soup1.find_all('a')
                    phone = website_soup.find('a', {"data-type": "phone"})
                    email = website_soup.find('a', {"data-type": "email"})
                    ScrapData.objects.create(
                        phone=phone['href'],
                        email=email['href']
                    )
                    print("Phone Detail: ", phone['href'])
                    print("Email: ", email['href'])
            return redirect('web_scraper:home')
        else:
            return render(request,'home.html',{"form":form})
    else:
        form = SimpleForm()
        return render(request,'home.html',{"form": form})