#!/usr/bin/env python
# coding: utf8

""" Unit testing for Separator class. """

__email__ = 'spleeter@deezer.com'
__author__ = 'Deezer Research'
__license__ = 'MIT License'

import filecmp
import itertools
from os import makedirs
from os.path import splitext, basename, exists, join
from tempfile import TemporaryDirectory

import pytest
import numpy as np

import tensorflow as tf

from spleeter.audio.adapter import get_default_audio_adapter
from spleeter.commands import create_argument_parser

from spleeter.commands import evaluate

from spleeter.utils.configuration import load_configuration

BACKENDS = ["tensorflow", "librosa"]
TEST_CONFIGURATIONS = {el:el for el in BACKENDS}

res_4stems = {
                "librosa": {
                    "vocals": {
                        "SDR": -0.007,
                        "SAR": -19.231,
                        "SIR": -4.528,
                        "ISR": 0.000
                    },
                    "drums": {
                        "SDR": -0.071,
                        "SAR": -14.496,
                        "SIR": -4.987,
                        "ISR": 0.001
                    },
                    "bass":{
                        "SDR": -0.001,
                        "SAR": -12.426,
                        "SIR": -7.198,
                        "ISR": -0.001
                    },
                    "other":{
                        "SDR": -1.453,
                        "SAR": -14.899,
                        "SIR": -4.678,
                        "ISR": -0.015
                    }
                },
                "tensorflow": {
                    "vocals": {
                        "SDR": 3.25e-05,
                        "SAR": -11.153575,
                        "SIR": -1.3849,
                        "ISR": 2.75e-05
                    },
                    "drums": {
                        "SDR": -0.079505,
                        "SAR": -15.7073575,
                        "SIR": -4.972755,
                        "ISR": 0.0013575
                    },
                    "bass":{
                        "SDR": 2.5e-06,
                        "SAR": -10.3520575,
                        "SIR": -4.272325,
                        "ISR": 2.5e-06
                    },
                    "other":{
                        "SDR": -1.359175,
                        "SAR": -14.7076775,
                        "SIR": -4.761505,
                        "ISR": -0.01528
                    }
                }
            }

def generate_fake_eval_dataset(path):
    aa = get_default_audio_adapter()
    n_songs = 2
    fs = 44100
    duration = 3
    n_channels = 2
    rng = np.random.RandomState(seed=0)
    for song in range(n_songs):
        song_path = join(path, "test", f"song{song}")
        makedirs(song_path, exist_ok=True)
        for instr in ["mixture", "vocals", "bass", "drums", "other"]:
            filename = join(song_path, f"{instr}.wav")
            data = rng.rand(duration*fs, n_channels)-0.5
            aa.save(filename, data, fs)


def test_evaluate(path="FAKE_MUSDB_DIR"):
    generate_fake_eval_dataset(path)
    p = create_argument_parser()
    arguments = p.parse_args(["evaluate", "-p", "spleeter:4stems", "--mus_dir", path])
    params = load_configuration(arguments.configuration)
    metrics = evaluate.entrypoint(arguments, params)
    for instrument, metric in metrics.items():
        for m, value in metric.items():
            assert np.allclose(np.median(value), res_4stems[instrument][m], atol=1e-3)