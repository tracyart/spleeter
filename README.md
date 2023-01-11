<img src="https://github.com/deezer/spleeter/raw/master/images/spleeter_logo.png" height="80" />

[![Github actions](https://github.com/deezer/spleeter/workflows/pytest/badge.svg)](https://github.com/deezer/spleeter/actions) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/spleeter) [![PyPI version](https://badge.fury.io/py/spleeter.svg)](https://badge.fury.io/py/spleeter) [![Conda](https://img.shields.io/conda/vn/deezer-research/spleeter)](https://anaconda.org/deezer-research/spleeter) [![Docker Pulls](https://img.shields.io/docker/pulls/deezer/spleeter)](https://hub.docker.com/r/deezer/spleeter) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/deezer/spleeter/blob/master/spleeter.ipynb) [![Gitter chat](https://badges.gitter.im/gitterHQ/gitter.png)](https://gitter.im/spleeter/community) [![status](https://joss.theoj.org/papers/259e5efe669945a343bad6eccb89018b/status.svg)](https://joss.theoj.org/papers/259e5efe669945a343bad6eccb89018b)

> :warning: [Spleeter 2.1.0](https://pypi.org/project/spleeter/) release introduces some breaking changes, including new CLI option naming for input, and the drop
> of dedicated GPU package. Please read [CHANGELOG](CHANGELOG.md) for more details.

## About

**Spleeter** is [Deezer](https://www.deezer.com/) source separation library with pretrained models
written in [Python](https://www.python.org/) and uses [Tensorflow](https://tensorflow.org/). It makes it easy
to train source separation model (assuming you have a dataset of isolated sources), and provides
already trained state of the art model for performing various flavour of separation :

* Vocals (singing voice) / accompaniment separation ([2 stems](https://github.com/deezer/spleeter/wiki/2.-Getting-started#using-2stems-model))
* Vocals / drums / bass / other separation ([4 stems](https://github.com/deezer/spleeter/wiki/2.-Getting-started#using-4stems-model))
* Vocals / drums / bass / piano / other separation ([5 stems](https://github.com/deezer/spleeter/wiki/2.-Getting-started#using-5stems-model))

2 stems and 4 stems models have [high performances](https://github.com/deezer/spleeter/wiki/Separation-Performances) on the [musdb](https://sigsep.github.io/datasets/musdb.html) dataset. **Spleeter** is also very fast as it can perform separation of audio files to 4 stems 100x faster than real-time when run on a GPU.

We designed **Spleeter** so you can use it straight from [command line](https://github.com/deezer/spleeter/wiki/2.-Getting-started#usage)
as well as directly in your own development pipeline as a [Python library](https://github.com/deezer/spleeter/wiki/4.-API-Reference#separator). It can be installed with [pip](https://github.com/deezer/spleeter/wiki/1.-Installation#using-pip) or be used with
[Docker](https://github.com/deezer/spleeter/wiki/2.-Getting-started#using-docker-image).

## Environment

Device `MacBook Air (M1, 2020)`

Operating System `MacOS 12.6`

Python `3.9.0`

Anaconda `22.11.1`

FFMPEG `5.1.2`

libsndfile `2.1.0`


## Installation

install dependencies

```
brew install ffmpeg libsndfile
```

```
conda create -n py38 python=3.8

conda activate py38

conda install -c apple tensorflow-deps==2.9.0
```

clone
```
git clone --depth 1 --branch tf_2.9_m1 https://github.com/tracyart/spleeter.git
```

install spleeter from local file
```
python -m pip install ./spleeter
```

check spleeter version
```
spleeter --version
```

`Spleeter Version: 2.3.2`

pretrained model [download page](https://github.com/deezer/spleeter/releases/tag/v1.4.0)

dir 
`pretrained_model/2stems` 
`pretrained_model/4stems` 
`pretrained_model/5stems`

