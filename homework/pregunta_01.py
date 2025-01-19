# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""


def pregunta_01():


    import os
    import pandas as pd

    def create_dataframe_from_directory(directory):
        data = []
        for sentiment in ['negative', 'neutral', 'positive']:
            sentiment_dir = os.path.join(directory, sentiment)
            if os.path.exists(sentiment_dir):
                for filename in os.listdir(sentiment_dir):
                    filepath = os.path.join(sentiment_dir, filename)
                    with open(filepath, 'r', encoding='utf-8') as file:
                        content = file.read()
                        data.append([content, sentiment])
            else:
                print(f"La carpeta {sentiment_dir} no existe.")
        return pd.DataFrame(data, columns=['content', 'sentiment'])

    # Ajusta estas rutas según la ubicación real de tus carpetas
    train_directory = r'D:\Unal\Analitica Descriptiva\Labs\2024-2-LAB-04-ingestion-de-texto-en-directorios-DanielOrozco09\files\input\train'
    test_directory = r'D:\Unal\Analitica Descriptiva\Labs\2024-2-LAB-04-ingestion-de-texto-en-directorios-DanielOrozco09\files\input\test'

    # Crear el DataFrame para la carpeta train
    train_df = create_dataframe_from_directory(train_directory)

    # Crear el DataFrame para la carpeta test
    test_df = create_dataframe_from_directory(test_directory)


    test_df = test_df.rename(columns = {'content': 'phrase', 'sentiment': 'target'})
    train_df = train_df.rename(columns = {'content': 'phrase', 'sentiment': 'target'})


    # Exportar los DataFrames a archivos CSV en el directorio actual
    train_df.to_csv(r'D:\Unal\Analitica Descriptiva\Labs\2024-2-LAB-04-ingestion-de-texto-en-directorios-DanielOrozco09\files\output\train_dataset.csv', index=False)
    test_df.to_csv(r'D:\Unal\Analitica Descriptiva\Labs\2024-2-LAB-04-ingestion-de-texto-en-directorios-DanielOrozco09\files\output\test_dataset.csv', index=False)

    print("Los DataFrames se han exportado a archivos CSV: 'train_data.csv' y 'test_data.csv'.")
    """
    La información requerida para este laboratio esta almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este archivo.

    Como resultado se creara la carpeta "input" en la raiz del
    repositorio, la cual contiene la siguiente estructura de archivos:


    ```
    train/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    test/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    ```

    A partir de esta informacion escriba el código que permita generar
    dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
    archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
    del repositorio.

    Estos archivos deben tener la siguiente estructura:

    * phrase: Texto de la frase. hay una frase por cada archivo de texto.
    * sentiment: Sentimiento de la frase. Puede ser "positive", "negative"
      o "neutral". Este corresponde al nombre del directorio donde se
      encuentra ubicado el archivo.

    Cada archivo tendria una estructura similar a la siguiente:

    ```
    |    | phrase                                                                                                                                                                 | target   |
    |---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
    |  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
    |  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
    |  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
    |  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
    |  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
    ```


    """
