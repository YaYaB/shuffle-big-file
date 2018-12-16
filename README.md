# Shuffle big file
> Simply shuffle a big file that does not fit in memory


This tool helps you shuffle by line a big file that does not fit in memory.
Given the *batch_size* that your machine can put in memory it will shuffle the whole file by
reading as many times as necessary.

## Installation

OS X, Linux & Windows:
No specific requirements except python3 (3.4 and later).

```sh
pip install git+https://github.com/YaYaB/shuffle-big-file
```


## Usage example

```sh
usage: Shuffle a huge file without loading in fully in RAM [-h]
                                                           [--input_file INPUT_FILE]
                                                           [--batch_size BATCH_SIZE]
                                                           [--output_file OUTPUT_FILE]

optional arguments:
  -h, --help            show this help message and exit
  --input_file INPUT_FILE
                        Path to input file
  --batch_size BATCH_SIZE
                        Batch size that can fit in memory
  --output_file OUTPUT_FILE
                        Path to output shuffled file

```

Please refer to [here](https://github.com/YaYaB/shuffle-big-file/examples) for examples.

## Benchmark
The machine used has the following specs:

```sh
cpu: i7-6700HQ CPU @ 2.60GHz × 8
ram: 16Gb
Os: Ubuntu 18.04
SSD: 512Gb Toshiba M.2 2280 THNSN5512GPUK 
```

The benchmark is the following:
| Size  | Batch size | Time |
| ------------- | ------------- | ------------- |
| 100M (100K lines) | 1K | 35s |
| 100M (100K lines) | 10K | 4s |
| 1G (1M lines) | 10K | 5min 13s |
| 1G (1M lines) | 100K | 32s |
| 11G (10M lines) | 100K | 55min |
| 11G (10M lines) | 1M | 8min 4s |

## Meta

YaYaB

Distributed under the Apache license v2.0. See ``LICENSE`` for more information.

[https://github.com/YaYaB/shuffle-big-file](https://github.com/YaYaB/shuffle-big-file)
