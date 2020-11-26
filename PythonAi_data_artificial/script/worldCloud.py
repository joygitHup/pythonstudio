import jieba
import numpy
from PIL import Image
from wordcloud import WordCloud
from   matplotlib import pyplot as plt

def product_word_clould(word_file, mask_file):
    text = open(word_file, 'r', encoding='utf-8').read()
    dispose_text = jieba.cut(text)
    result = ''.join(dispose_text)
    pick_imag=numpy.array(Image.open(mask_file))
    WC = WordCloud(font_path='simhei.ttf', background_color='white', width=1000,
                   height=600, max_font_size=50, min_font_size=10,
                   mask=pick_imag, max_words=1000)
    WC.generate(result)
    WC.to_file('wc_img.jpg')
    plt.figure('wc_img')
    plt.imshow(WC)
    plt.axis('off')
    plt.show()
if __name__ == "__main__":
    product_word_clould(word_file='E:\\DevWorkSpace\\pythonstudio\\PythonAi_data_artificial\\file\\word_txt\\woldtxt',
                        mask_file='E:\\DevWorkSpace\\pythonstudio\\PythonAi_data_artificial\\file\\img\\17.jpg')