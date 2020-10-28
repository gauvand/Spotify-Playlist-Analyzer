from bs4 import BeautifulSoup
import requests
import dotenv
    
    
def link2uri(link):
    uri = link[link.rfind("/")+1:link.rfind("?")]
    uri = "spotify:playlist:" + uri
    return(uri)
def count_plot(data,column):
    fig=plt.figure(figsize = (12,12))
    sns.set(font_scale=5)
    sns.set_style("whitegrid")
    matplotlib.rcParams.update({'font.size': 8})
    sns.countplot(x=f"{column}",data=data.sort_values([f"{column}"]))
    plt.show()