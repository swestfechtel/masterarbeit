import io

import pandas as pd

from PyPDF2 import PdfReader
from tqdm import tqdm


def pdf_to_dataframe():
    reader = PdfReader("H:/Masterarbeit/Rural college/ManhattanFullNetwork.pdf")
    df = pd.DataFrame(columns=['Source', 'Target', 'Weight'])
    for i, page in enumerate(tqdm(reader.pages)):
        text = page.extract_text()
        text = text.split('\n')
        if i == 0:
            text = text[1:]
        
        text = list(map(lambda x: x.split(' '), text))
        text = [[int(x) for x in y] for y in text]
        tmp = pd.DataFrame(text, columns=['Source', 'Target', 'Weight'])
        df = pd.concat([df, tmp])

    df.to_pickle('./Data/college_dataframe.pickle')