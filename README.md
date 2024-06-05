# LSTM for Trajectory Prediction (Mac Edition)

This repository is a fork of the original [LSTM-for-Trajectory-Prediction](https://github.com/DengyuanWang/LSTM-for-Trajectory-Prediction) project, modified to improve compatibility with Mac systems and PyTorch. 

#### Make sure your Apple Silicon can accelerate PyTorch Training on Mac !!!

## Introduction

This project implements Long Short-Term Memory (LSTM) neural networks to predict trajectories. The primary improvements in this version include compatibility with macOS in PyTorch training. 

## Features

- LSTM-based trajectory prediction
- Mac compatibility
- Data preparation scripts included

## Running Environment

> [!NOTE]
>
> My Repository is running on **Apple Mac M2** (Please make sure your Mac chips is <u>Apple Silicon</u>)
>
> Still can run on **Windows**

> [!CAUTION]
>
> **Don't support Apple Mac Intel**

#### Python Version

- Python==3.11

#### **Apple Mac M2 install the pytorch:**

```bash
pip3 install torch torchvision torchaudio
```

or

```bash
conda install pytorch::pytorch torchvision torchaudio -c pytorch
```

## Install

1. Clone the repository:

    ```bash
    git clone https://github.com/Raymond1030/LSTM-for-Trajectory-Prediction_Mac-Edition.git
    cd LSTM-for-Trajectory-Prediction_Mac-Edition
    ```

2. Install the required packages on your environment:
    ```bash
    pip install -r requirements.txt
    ```

## Test your PyTorch Environment on Mac

1. Run the test script that make sure your pytorch environment can be run with Apple Silicon GPU:

   ```bash
   python MacPytorchTest.py
   ```

2. Success if print this, make sure the device is **MPS** model:

   ```
   True
   Device:mps
   tensor([[1, 2, 3],
           [4, 5, 8],
           [9, 8, 7]], device='mps:0')
   ```

## Usage

Train the model using the provided training script (Auto prepare the data):
```bash
python LSTM.py
```

You can change the TRAN_TAG depend on whether you have train the model.

## LICENSE

MIT