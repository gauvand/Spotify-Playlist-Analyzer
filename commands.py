from bs4 import BeautifulSoup
import requests
import dotenvimport osimport spotipyfrom spotipy.oauth2 import SpotifyClientCredentialsimport jsonimport numpy as npimport pandas as pdimport seaborn as snsfrom matplotlib import pyplot as pltimport matplotlibdef analysis_chart(features):        fig=plt.figure(figsize = (30,30))    sns.set("poster")    sns.set_style("whitegrid")    sns.set(rc={'axes.facecolor':'white','grid.color':"black",'grid.alpha':0.9})    labels = features.columns    # Setting up angles for thetagrid    x=np.linspace(0, 2*np.pi, len(labels), endpoint=False)    x = np.concatenate((x,[x[0]])) #  for continuous plot    y = features.mean()    y = np.concatenate((y,[y[0]])) #  for continuous plot    ax = fig.add_subplot(221, polar=True)    ax.set_thetagrids(x * 180/np.pi,                      labels,                      fontsize = 16,                      position=[-0.1]*len(labels))    plt.yticks([0.2 , 0.4 , 0.6 , 0.8], color="grey", size=10)    print(len(y))    # Plotting results    ax.plot(x, y,"o-" , label = "Average", color= 'black')    ax.fill(x, y, alpha=0.5, facecolor='purple')    # Chart background color    # fig.patch.set_facecolor("violet")    # fig.patch.set_alpha(0.1)        def count_plot(data,column):    fig=plt.figure(figsize = (15,15))    sns.set(font_scale=5)    sns.set_style("whitegrid")    matplotlib.rcParams.update({'font.size': 16})    sns.countplot(x=f"{column}",data=data.sort_values([f"{column}"]))
    
    
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
