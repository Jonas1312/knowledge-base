# Transformers

- [Transformers](#transformers)
  - [Introduction](#introduction)
  - [Architecture](#architecture)
    - [Transformer encoder](#transformer-encoder)
    - [Attention](#attention)
      - [Scaled dot product attention (or self-attention)](#scaled-dot-product-attention-or-self-attention)
      - [Interpretation](#interpretation)
      - [Computation](#computation)
      - [Multi head attention](#multi-head-attention)
      - [Self-attention vs global attention](#self-attention-vs-global-attention)
    - [Transformer decoder](#transformer-decoder)
      - [Stacked self-attention layers](#stacked-self-attention-layers)
      - [Masked self-attention](#masked-self-attention)
      - [Cross-attention (seq2seq tasks)](#cross-attention-seq2seq-tasks)
    - [Positional encoding](#positional-encoding)
      - [Different positional encodings](#different-positional-encodings)
    - [Layers](#layers)
      - [Layer normalization](#layer-normalization)
      - [Residual connections](#residual-connections)
  - [In a nutshell](#in-a-nutshell)
  - [Training](#training)
    - [Batch size and sequence length](#batch-size-and-sequence-length)
    - [Fixed or variable length?](#fixed-or-variable-length)
  - [Transformers in NLP](#transformers-in-nlp)
  - [Transformers in computer vision](#transformers-in-computer-vision)
    - [Adapting transformers to CV](#adapting-transformers-to-cv)
    - [Patch embeddings and tokenization](#patch-embeddings-and-tokenization)

## Introduction

<https://arxiv.org/abs/1706.03762>

Transformers are a type of neural network architecture that allow for parallelization while maintaining the ability to capture long-range dependencies.

They are based on the attention mechanism. Attention is a mechanism that allows a model to focus on certain parts of the input.

The transformer architecture is based on the encoder-decoder architecture. The encoder takes the input and produces a representation of it. The decoder takes that representation and produces the output.

Transformers are now SOTA for NLP tasks, since they can capture long-range dependencies and are parallelizable, unlike RNNs or LSTMs.

## Architecture

![](transformer-arch.png)

The transformer architecture is based on the encoder-decoder architecture.

The encoder takes an input sequence of symbol representations $(x_1, ..., x_n)$ and produces a sequence
of continuous representations $z = (z_1, ..., z_n)$.

Given $z$, the decoder then generates an output sequence $(y_1, ..., y_m)$ of symbols one element at a time.
The decoder takes that representation and produces the output.

![](seq2seq.png)

Input elements $x_1, x_2, etc$ are called **tokens**. They can be text representations, pixels, images in case of videos.

The input and predicted sequences can be of same or arbitrary length.

At each step the model is auto-regressive, consuming the previously generated symbols as additional input when generating the next.

The transformer is based solely on attention mechanisms, dispensing with recurrence and convolutions
entirely.

### Transformer encoder

The encoder is composed of a stack of $N=6$ identical layers.

![](transformer-encoder.png)

Each layer has two sub-layers:

- The first is a **multi-head self-attention** mechanism.
- The second is a simple, position-wise fully connected feed-forward network.

We employ a residual connection around each of the two sub-layers, followed by layer normalization .

That is, the output of each sub-layer is $LayerNorm(x + Sublayer(x))$, where *Sublayer(x)* is the function implemented by the sub-layer itself.

To facilitate these residual connections, all sub-layers in the model, as well as the embedding layers, produce outputs of dimension $dmodel=512$.

### Attention

Attention is a mechanism that allows a model to focus on certain parts of the input.

An attention function can be described as mapping **a query** and **a set of key-value pairs** to **an output**. The query, keys, values, and output are all vectors.

The output is computed as a weighted sum of the values, where the weight assigned to each value is computed by a compatibility function of the query with the corresponding key.

#### Scaled dot product attention (or self-attention)

![](./scaled-dot-prod-attention.png)

An input sequence $X \in \mathbb{R}^{n \times d}$ of $n$ tokens of dimensions $d=512$, is projected using three matrices of weights:

- $W_Q \in \mathbb{R}^{d \times d_q}$
- $W_K \in \mathbb{R}^{d \times d_k}$
- $W_V \in \mathbb{R}^{d \times d_v}$

to extract feature representations:

- $Q = XW_Q \in \mathbb{R}^{n \times d_q}$, the query matrix
- $K = XW_K \in \mathbb{R}^{n \times d_k}$, the key matrix
- $V = XW_V \in \mathbb{R}^{n \times d_v}$, the value matrix

$d_k$ and $d_v$ are hyperparameters, but they are often taken as $d_k=d_v=64$.

Note that the input $X \in \mathbb{R}^{n \times d}$ is a list of tokens, so each $n$ is a token, and each $d$ is the dimension of the token embedding, that is the vector that represents the token in the embedding space.

We compute the dot products of the query with all keys, divide each by $\sqrt d_k$, and apply a row-wise softmax function to obtain the weights on the values:

$$Attention(Q, K, V) = softmax \left( \frac{QK^T}{\sqrt d_k} \right) V$$

The dimensions of the matrices are:

- $QK^T \in \mathbb{R}^{n \times n}$
- $S = softmax \left( \frac{QK^T}{\sqrt d_k} \right) \in \mathbb{R}^{n \times n}$: it's the attention weights matrix:
  - The softmax is applied to each row, so the sum of the weights for each row is 1.
  - The i-th row of $S$ is the attention weights for the i-th token with respect to the other tokens.
- $O = S V \in \mathbb{R}^{n \times d_v}$: the output matrix:
  - Each row of $O$ is the weighted sum of the values for a token.

Note that the attention outout is $O \in \mathbb{R}^{n \times d_v}$, so it's different from the input $X \in \mathbb{R}^{n \times d}$.

Thus, a final weight matrix $W^O \in \mathbb{R}^{d_v \times d}$ can be applied to the output to obtain the final output $O' \in \mathbb{R}^{n \times d}$.

On the image below, we see the self-attention mechanism in action. The query is the word "it".

![](self-attention.png)

#### Interpretation

For sake of simplicity, we assume that the sequence length is one, that is $n=1$.

The query is a vector, for the current word, of dimensions $d_q$.

Key-value is the memory, it's the past, all the words that have been seen so far.

Attention takes the query, find the most similar key(s), and then get the value(s) that correspond to that/those similar key(s).

![](attention-as-database-query.png)

The encoder builds/discovers key-value pairs, it's the memory.
The decoder builds the queries, it's the question that is asked to the memory.

#### Computation

All-to-all comparison: Each layer is $O(n^2)$, where $n$ is the sequence length.

Note that we have only multiplied matrices so far, so the computation is parallelizable using GPUs.

In the softmax, we divide by $\sqrt d_k$. This is to avoid the softmax to be too peaked for large values of $d_k$. If the softmax is too peaked, the gradient might be too small.

#### Multi head attention

![](./multi-head-attention.png)

We perform the self-attention operation multiple times $h$ independently, in parallel, called **heads**.

Each head has different linear transformations, that is different $W_Q$, $W_K$, $W_V$.

The rational is that different heads can learn different relationships between words.

We thus have $h$ outputs $O_1, \dots, O_h$, where each $O_i \in \mathbb{R}^{n \times d_v}$.

We then concatenate them to obtain the attention output $O \in \mathbb{R}^{n \times hd_v}$.

Since the output should be of dimension $d$, we apply a final linear transformation $W^O \in \mathbb{R}^{hd_v \times d}$ to obtain the final output $O' \in \mathbb{R}^{n \times d}$.

$h$, the number of heads, is usually set to 8.