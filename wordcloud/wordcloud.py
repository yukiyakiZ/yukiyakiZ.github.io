from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import os
import click

def return_stopwords():
    stopwords = set(STOPWORDS)
    with open('custom_list.txt') as lines:
        for word in lines:
            stopwords.add(word.rstrip('\n'))
    return stopwords

# text = text.replace("a's", "a")

def plt_wordcloud(cloud):
    plt.imshow(cloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()

@click.group()
def cli():
    pass

@cli.command()
@click.option(
    '--source',
    prompt='Source file',
    help='Relative path of source file to be analysed.')
@click.option('--savefig', default=False,
              help='Save the fig or not.')
@click.option('--imagepath', default='temp.png',
              help='Full path of the image path to be stored.')
def single(source, imagepath, savefig):
    d = os.path.dirname(__file__)
    text = open(os.path.join(d, source)).read()
    cloud = WordCloud(
        width=480,
        height=480,
        # background_color="white",
        max_words=2000,
        # contour_width=3,
        colormap="Blues",
        # contour_color='steelblue',
        stopwords=return_stopwords()).generate(text)

    plt_wordcloud(cloud)
    if savefig:
        cloud.to_file(imagepath)

@cli.command()
@click.option('--source', help='Root dir to be analysed.')
@click.option('--imagepath', default='temp.png',
              help='Full path of the image path to be stored.')
def cluster(source, imagepath):
    pass


if __name__ == '__main__':
    cli()