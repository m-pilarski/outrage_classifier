# *DOC*: Digital Outrage Classifier

> Developed by members of the Crockett Lab at Yale University in the Psychology and Statistics and Data Science department, `DOC` is a Python package that allows researchers to predict the probability that tweets contain moral outrage. 

> The details of the development of the code and materials in this repository are described in detail in the paper, "[How social learning amplifies moral outrage expression in online social networks](https://psyarxiv.com/gf7t5) (2021).

[![made-with-python][made-with-python]](https://www.python.org/)
[![Outrageclf version][outrage-image]](www.google.com)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](www.google.com)
[![CC NC-SA 4.0](https://img.shields.io/badge/License-CC--NC--SA%202.0-lightgrey)](www.google.com)


## Repository Contributors
* William Brady | Postdoctoral Fellow | Yale University | william.brady@yale.edu | [Website](http://williamjbrady.com)
* Killian McLoughlin | Ph.D. Student | Yale University | killian.mcloughlin@yale.edu | [LinkedIn](www.linkedin.com/in/killian-mc-loughlin-5a151032)
* Tuan Nguyen Doan | Data Scientist | Quora | tuan.nguyen.doan@aya.yale.edu | [LinkedIn](https://www.linkedin.com/in/tuan-nguyen-doan)


## Installation

The first step is to clone the repo into a local directory on you computer. Using the terminal, navigate to the location where you want to store the package and run the following command:

```sh
git clone "https://github.com/CrockettLab/outrage_classifier"
```

Then run the command below. The package is compatible with both Python2 and Python3.
```sh
python setup.py install 
```

## Importing
The package can be imported using the following code:

```python
import outrageclf as oclf
from outrageclf.preprocessing import WordEmbed, get_lemmatize_hashtag
from outrageclf.classifier import _load_crockett_model
```

For those using macOS, a runtime error (described [here](https://stackoverflow.com/questions/53014306/error-15-initializing-libiomp5-dylib-but-found-libiomp5-dylib-already-initial)) may prevent the package from being successfully imported. If you experience this issue, setting the environment varibale `KMP_DUPLICATE_LIB_OK` to `TRUE` should solve the problem:

```python
import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'
```

## Usage
The current version of `outrageclf` allows users to predict moral outrage using a pre-trained deep gated recurrent unit (GRU) model as described in detail in [this](www.google.com) article. 

To run the pre-trained model used in the article, you will need **model files that are NOT hosted in this repository**. If you would like access to these files, see 'Accessing Model Files' below. The omited files are:

- [x] A pre-trained embedding model, stored in a `.joblib` format
- [x] A pre-trained GRU model, stored in a `.h5` format 

In order to predict the probability a tweet contains moral outrage we use the following pipeline:

```mermaid
Load pretrained models -> Preprocess text -> Embed text -> Make prediction 
```

Below is a complete coded instance of the pipeline. Note that this example **assumes the presence of either our pretrained-model files or similar files generated by the user**:

```python

tweets = [
          "This topic infuriates me because it violates my moral stance",
          "This is just a super-normal topic #normal"
         ]

# loading our pre-trained models
word_embed = WordEmbed()
word_embed._get_pretrained_tokenizer(embedding_url)
model = _load_crockett_model(model_url)

# the text are lemmatized and embedded into 50-d space
lemmatized_text = get_lemmatize_hashtag(text_vector)
embedded_vector = word_embed._get_embedded_vector(lemmatized_text)
predict = model.predict(embedded_vector)
```

Alternatively, classifications can be generated using the package's model wrapper function, stored in the `classifier` module. This step bypasses the need to lemmatize and embed text input:

```python
from outrageclf.classifier import pretrained_model_predict
pretrained_model_predict(tweets, embedding_url, model_url)
```
## Accessing Model Files
In order to access pre-trained model files please fill out [this form](https://forms.gle/sRDbmtGK1dW6z6ff6). The form will ask for your email and a brief description of your use case. We will then email you the model files. Note that the classifier is for use in academic research only. See the license for more information.

## Example Notebook
`example.ipynb` demonstrates examples of these two use cases.

## Citation
Brady, W.J., McLoughlin, K.L., Doan, T.N., & Crockett, M.J. (2021). How social learning amplifies moral outrage expression in online social networks. [PsyArXiv](https://psyarxiv.com/gf7t5). doi: 10.31234/osf.io/gf7t5

## License
This work is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 2.0 Generic License][cc-nc-sa].

[![CC NC-SA 4.0][cc-nc-sa-image]][cc-nc-sa]

## Release History
* 0.1.0
    * Initial release

<!-- Markdown link & img dfn's -->
[made-with-python]: https://img.shields.io/badge/Made%20with-Python-FF0000.svg
[outrage-image]: https://img.shields.io/badge/DOC-v0.1.4-orange.svg
[cc-nc-sa]: https://creativecommons.org/licenses/by-nc-sa/2.0/
[cc-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/2.0/88x31.png
[cc-nc-sa-shield]: https://img.shields.io/badge/License-CC--NC--SA%202.0-lightgrey
[travis-image]: https://img.shields.io/travis/dbader/node-datadog-metrics/master.svg?style=flat-square
[travis-url]: https://travis-ci.org/dbader/node-datadog-metrics
