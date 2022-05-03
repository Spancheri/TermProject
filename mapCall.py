#All packages that will need to be imported
import contextily as cx
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
from matplotlib_scalebar.scalebar import ScaleBar

# A choropleth map showing economic precarity across the island of Montreal, 
# in which case you will need to present aggregated data.

#Function Start)
def map_drawing(gdf,targetPlot,titleMap,subTitle,xlimfrom,xlimto,ylimfrom,ylimto,dataSource,authorName,fig1):

#gdf = your geodataframe to plot              DATAFRAME
#targetPlot = the feature to be plotted       STRING
#titleMap = The Main Title of your Map        STRING
#subTitle = The Subtitle of your Map          STRING
#xlimfrom = X Coordinate limit (lower value)  INTEGER
#xlimto = X Coordinate limit (upper value)    INTEGER
#ylimfrom = Y Coordinate limit (lower value)  INTEGER
#ylimto = Y Coordinate limit (upper value)    INTEGER
#dataSource = Your map source data            STRING
#authorName = The author name + date          STRING


    #Plot the geodataframe
    ax1 = gdf.plot(
    targetPlot
    ,figsize=(10,10)
    ,edgecolor="#fff"
    ,linewidth=0.3
    ,vmax=20
    ,vmin=0
    ,legend=True
    ,legend_kwds={'shrink': 0.4}
    ,cmap="cool")
    
    
    # Create scale bar
    scalebar = ScaleBar(100, "km", length_fraction=0.50)
    ax1.add_artist(scalebar)

    #Center map where you wish
    ax1.set_xlim(xlimfrom, xlimto)
    ax1.set_ylim(ylimfrom, ylimto);
    

    #Set up map title and subtitle
    ax1.annotate(
    titleMap,
    (0.5,1.05)
    ,xycoords = 'axes fraction'
    ,horizontalalignment='center'
    ,verticalalignment='bottom'
    ,fontsize = 20
    ,color='#000'
    ,fontstyle='normal')
    
    ax1.annotate(
    subTitle,
    (0.50,1.01)
    ,xycoords = 'axes fraction'
    ,horizontalalignment='center'
    ,verticalalignment='bottom'
    ,fontsize = 15
    ,color='#000'
    ,fontstyle='normal')
    
    #Name the X and Y axes
    ax1.annotate(
    "X Coordinate",
    (0.5,-0.095)
    ,xycoords = 'axes fraction'
    ,horizontalalignment='center'
    ,verticalalignment='bottom'
    ,fontsize = 15
    ,color='#000'
    ,fontstyle='normal')

    ax1.annotate(
    "Y Coordinate",
    (-0.1,0.35)
    ,xycoords = 'axes fraction'
    ,horizontalalignment='center'
    ,verticalalignment='bottom'
    ,rotation=90
    ,fontsize = 15
    ,color='#000'
    ,fontstyle='normal')
    
    # Insert North Arrow
    x, y, arrow_length = 0.95, 0.5, 0.1
    ax1.annotate('N'
            ,xy=(x, y)
            ,xytext=(x, y-arrow_length)
            ,arrowprops=dict(facecolor='black', width=5, headwidth=15)
            ,ha='center'
            ,va='center'
            ,fontsize=20
            ,xycoords=ax1.transAxes)
    
    #Set up Data Source and Author Name/Date
    ax1.annotate(
    dataSource,
    (0.9,-0.095)
    ,xycoords = 'axes fraction'
    ,horizontalalignment='center'
    ,verticalalignment='bottom'
    ,fontsize = 9
    ,color='grey'
    ,fontstyle='normal')
    
    ax1.annotate(
    authorName,
    (1,1)
    ,xycoords = 'axes fraction'
    ,horizontalalignment='center'
    ,verticalalignment='bottom'
    ,fontsize = 9
    ,color='#000'
    ,fontstyle='normal')

    fig1 = fig1.figure
    fig1.savefig('MapOutput.png', dpi=300)
    
