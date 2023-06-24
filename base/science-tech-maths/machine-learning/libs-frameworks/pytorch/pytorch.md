# PyTorch

## Table of Contents

- [PyTorch](#pytorch)
  - [Table of Contents](#table-of-contents)
  - [Cheat Sheets](#cheat-sheets)
  - [Tutorials](#tutorials)
  - [General Functioning](#general-functioning)
  - [Tips/Tricks, code snippets](#tipstricks-code-snippets)
    - [Gradient accumulation](#gradient-accumulation)
    - [Freeze seeds for reproducibility](#freeze-seeds-for-reproducibility)
    - [Freeze layers](#freeze-layers)
    - [Save and load weights](#save-and-load-weights)
    - [Change last layer](#change-last-layer)
    - [Delete last layer](#delete-last-layer)
    - [Get number of parameters](#get-number-of-parameters)
    - [No grad and inference\_mode decorators](#no-grad-and-inference_mode-decorators)
    - [Gradient clipping](#gradient-clipping)
    - [Remove bias weight decay](#remove-bias-weight-decay)
    - [Test time augmentation (TTA)](#test-time-augmentation-tta)
    - [Intermediate gradients](#intermediate-gradients)
    - [Get intermediate layers values](#get-intermediate-layers-values)
    - [Weight init](#weight-init)
    - [Train/test/valid splits](#traintestvalid-splits)
  - [Common mistakes](#common-mistakes)
    - [Retained graphs](#retained-graphs)
    - [Copy an array](#copy-an-array)
  - [Maximizing performance](#maximizing-performance)
    - [Construct tensors directly on GPUs](#construct-tensors-directly-on-gpus)
    - [Avoid CPU to GPU transfers or vice-versa](#avoid-cpu-to-gpu-transfers-or-vice-versa)
    - [Workers in dataloader](#workers-in-dataloader)
    - [cuddn.benchmark](#cuddnbenchmark)
    - [Use inplace operations](#use-inplace-operations)
    - [Gradient checkpointing](#gradient-checkpointing)
    - [Pinned Memory](#pinned-memory)
    - [Use DistributedDataParallel not DataParallel](#use-distributeddataparallel-not-dataparallel)
    - [Profile your code](#profile-your-code)
    - [Use auto mixed precision](#use-auto-mixed-precision)
    - [Static graphs](#static-graphs)
    - [Lightning Fabric](#lightning-fabric)
    - [More tips](#more-tips)
  - [Torchmetrics](#torchmetrics)
  - [Visualize Layer Activations](#visualize-layer-activations)
  - [MultiGPU](#multigpu)
  - [PyTorch internals](#pytorch-internals)
  - [Debugging](#debugging)

## Cheat Sheets

- [PyTorch Cheat Sheet](https://pytorch.org/tutorials/beginner/ptcheat.html)
- [PyTorch - Basic operations](https://jhui.github.io/2018/02/09/PyTorch-Basic-operations/)

## Tutorials

- [Getting Started Tutorials](https://pytorch.org/tutorials/)
- [PyTorch Autograd Explained - In-depth Tutorial](https://www.youtube.com/watch?v=MswxJw-8PvE)
- [PyTorchZeroToAll](https://www.youtube.com/playlist?list=PLlMkM4tgfjnJ3I-dbhO9JTw7gNty6o_2m)
- [Neural Network Programming - Deep Learning with PyTorch](https://www.youtube.com/playlist?list=PLZbbT5o_s2xrfNyHZsM6ufI0iZENK9xgG)
- [Understanding PyTorch with an example: a step-by-step tutorial](https://towardsdatascience.com/understanding-pytorch-with-an-example-a-step-by-step-tutorial-81fc5f8c4e8e)
- <https://towardsdatascience.com/how-to-use-pytorch-hooks-5041d777f904>
- <https://leimao.github.io/blog/PyTorch-Benchmark/>
- <https://www.learnpytorch.io/#does-this-course-cover-pytorch-20>
- <https://github.com/srush/Tensor-Puzzles>

## General Functioning

Modern libraries like PyTorch are designed with 3 components:

1. a fast (C/CUDA) **general Tensor library** that implements basic mathematical operations over multi-dimensional tensors
2. an **autograd engine** that tracks the forward compute graph and can generate operations for the backward pass
3. a scriptable (Python) deep-learning-aware, **high-level API** of common deep learning operations, layers, architectures, optimizers, loss functions, etc.

Each tensor has a `.grad_fn` attribute that references a function that has created the Tensor (except for Tensors created by the user - their `grad_fn` is `None`).

The dynamic graph records the execution of the running program. The graph is being generated ON THE FLY.

Automatic differentiations is basically a pre-implementation of the most common functions and their local gradients.

Mathematically, if you have a vector valued function $\vec{y}=f(\vec{x})$, then the gradient of $\vec{y}$ with respect to $\vec{x}$ is a Jacobian matrix:

$$J=\left(\begin{array}{ccc}
   \frac{\partial y_{1}}{\partial x_{1}} & \cdots & \frac{\partial y_{1}}{\partial x_{n}}\\
   \vdots & \ddots & \vdots\\
   \frac{\partial y_{m}}{\partial x_{1}} & \cdots & \frac{\partial y_{m}}{\partial x_{n}}
   \end{array}\right)$$

Generally speaking, ``torch.autograd`` is an engine for computing
vector-Jacobian product. If $v$ happens to be
the gradient of a scalar function $L=g\left(\vec{y}\right)$,
that is,
$v=\left(\begin{array}{ccc}\frac{\partial L}{\partial y_{1}} & \cdots & \frac{\partial L}{\partial y_{m}}\end{array}\right)^{T}$,
then by the chain rule, the vector-Jacobian product would be the
gradient of $L$ with respect to $\vec{x}$:

$$J^{T}\cdot v=\left(\begin{array}{ccc}
   \frac{\partial y_{1}}{\partial x_{1}} & \cdots & \frac{\partial y_{m}}{\partial x_{1}}\\
   \vdots & \ddots & \vdots\\
   \frac{\partial y_{1}}{\partial x_{n}} & \cdots & \frac{\partial y_{m}}{\partial x_{n}}
   \end{array}\right)\left(\begin{array}{c}
   \frac{\partial L}{\partial y_{1}}\\
   \vdots\\
   \frac{\partial L}{\partial y_{m}}
   \end{array}\right)=\left(\begin{array}{c}
   \frac{\partial L}{\partial x_{1}}\\
   \vdots\\
   \frac{\partial L}{\partial x_{n}}
   \end{array}\right)$$

(Note that $v^{T}\cdot J$ gives a row vector which can be
treated as a column vector by taking $J^{T}\cdot v$)

This characteristic of vector-Jacobian product makes it very
convenient to feed external gradients into a model that has
non-scalar output.

## Tips/Tricks, code snippets

### Gradient accumulation

<https://kozodoi.me/python/deep%20learning/pytorch/tutorial/2021/02/19/gradient-accumulation.html>

```python
optimizer.zero_grad()
scaled_loss = 0
for accumulated_step_i in range(N_STEPS):
    out = model.forward()
    loss = ...
    loss.backward()
    scaled_loss += loss.item()
optimizer.step()
actual_loss = scaled_loss / N_STEPS
```

### Freeze seeds for reproducibility

```python
np.random.seed(1)
torch.manual_seed(1)
torch.cuda.manual_seed(1)
random.seed(seed)
torch.backends.cudnn.deterministic = True
torch.backends.cudnn.benchmark = False
```

### Freeze layers

```python
for child in model.children():
    for param in child.parameters():
        param.requires_grad = False

optimizer = torch.optim.Adam(
    filter(lambda p: p.requires_grad, model.parameters()), lr=...
)
```

### Save and load weights

```python
torch.save(model.state_dict(), MODEL_PATH)
model.load_state_dict(torch.load(MODEL_PATH))
```

### Change last layer

```python
num_final_in = model.fc.in_features
model.fc = nn.Linear(num_final_in, NUM_CLASSES)
```

### Delete last layer

```python
new_model = nn.Sequential(*list(model.children())[:-1])
```

### Get number of parameters

```python
num_params = sum(p.numel() for p in model.parameters())  # Total parameters
num_trainable_params = sum(
    p.numel() for p in model.parameters() if p.requires_grad
)  # Trainable parameters
```

### No grad and inference_mode decorators

```python
@torch.no_grad()
def eval(model, data):
    model.eval()


@torch.inference_mode()
def eval(model, data):
    model.eval()
```

### Gradient clipping

```python
torch.nn.utils.clip_grad_value_(parameters=model.parameters(), clip_value=1.0)
torch.nn.utils.clip_grad_norm_(parameters, max_norm, norm_type=2)
```

### Remove bias weight decay

```python
def add_weight_decay(net, l2_value, skip_list=()):
    decay, no_decay = [], []
    for name, param in net.named_parameters():
        if not param.requires_grad:
            continue  # frozen weights
        if len(param.shape) == 1 or name.endswith(".bias") or name in skip_list:
            no_decay.append(param)
        else:
            decay.append(param)
    return [
        {"params": no_decay, "weight_decay": 0.0},
        {"params": decay, "weight_decay": l2_value},
    ]


params = add_weight_decay(net, 2e-5)
sgd = torch.optim.SGD(params, lr=0.1)
```

### Test time augmentation (TTA)

```python
data = torch.stack([list_of_tensors])
batch_size, n_crops, c, h, w = data.size()
data = data.view(-1, c, h, w)
output = model(data)
output = output.view(batch_size, n_crops, -1).mean(1)
```

### Intermediate gradients

By default, PyTorch only stores the gradients of the leaf variables (e.g., the weights and biases) via their grad attribute to save memory. So, if we are interested in the intermediate results in a computational graph, we can use the `retain_grad` method to store gradients of non-leaf variables as follows:

```python
u = x * w
v = u + b
u.retain_grad()
v.backward()
print(u.grad)
```

### Get intermediate layers values

<https://pytorch.org/blog/FX-feature-extraction-torchvision/>

### Weight init

```python
def init_weights(net, init_type="normal", gain=0.02):
    def init_func(m):
        if isinstance(m, (nn.Conv2d, nn.Linear)):
            if init_type == "normal":
                nn.init.normal_(m.weight.data, 0.0, gain)
            elif init_type == "xavier":
                nn.init.xavier_normal_(m.weight.data, gain=gain)
            elif init_type == "kaiming":
                nn.init.kaiming_normal_(m.weight.data, a=0, mode="fan_in")
            elif init_type == "orthogonal":
                nn.init.orthogonal_(m.weight.data, gain=gain)
            else:
                raise NotImplementedError(
                    "initialization method [%s] is not implemented" % init_type
                )
            if hasattr(m, "bias") and m.bias is not None:
                nn.init.constant_(m.bias.data, 0.0)
        elif isinstance(m, nn.BatchNorm2d):
            nn.init.normal_(m.weight.data, 1.0, gain)
            nn.init.constant_(m.bias.data, 0.0)

    print("initialize network with %s" % init_type)
    net.apply(init_func)
```

### Train/test/valid splits

Use `from torch.utils.data.dataset import Subset`

## Common mistakes

### Retained graphs

```python
losses.append(loss)  # bad
losses.append(loss.item())  # good
```

### Copy an array

```python
a = torch.tensor([1.0, 2.0, 3.0])
b = a  # WRONG: same reference
b = a.clone()
```

## Maximizing performance

### Construct tensors directly on GPUs

```python
t = tensor.rand(2, 2).cuda()  # bad
t = tensor.rand(2, 2, device="cuda")  # good
```

### Avoid CPU to GPU transfers or vice-versa

Avoid usage of the .item() or .cpu() or .numpy() calls. This is really bad for performance because every one of these calls transfers data from GPU to CPU and dramatically slows your performance.

### Workers in dataloader

PyTorch allows loading data on multiple processes simultaneously.

Good rule of thumb:

- set the number of workers to the number of CPU cores.
- num_worker = 4 * num_GPU

### cuddn.benchmark

Set `torch.backends.cudnn.benchmark = True` Note that cudnn.benchmark will profile the kernels for each new input shape, so be careful if dynamic shapes are used.

### Use inplace operations

For example, if we perform x.cos().cos(), usually we need to perform 4 global reads and writes.

```python
x1 = x.cos()  # Read from x in global memory, write to x1
x2 = x1.cos()  # Read from x1 in global memory, write to x2
```

But, with operator fusion, we only need 2 global memory reads and writes! So operator fusion will speed it up by 2x.

```python
x2 = x.cos().cos()  # Read from x in global memory, write to x2
```

### Gradient checkpointing

[Deep Learning Memory Usage and Pytorch Optimization Tricks](https://www.sicara.fr/blog-technique/2019-28-10-deep-learning-memory-usage-and-pytorch-optimization-tricks)

### Pinned Memory

`pin_memory=True` in PyTorch's `DataLoader` class

Theoretically, pinning the memory should speed up the data transfer rate but minimizing the data transfer cost between CPU and the CUDA device; hence, enabling `pin_memory=True` should make the model training faster by some small margin.

`pin_memory=torch.cuda.is_available()`

When you enable pinned_memory in a DataLoader it “automatically puts the fetched data Tensors in pinned memory, and enables faster data transfer to CUDA-enabled GPUs”.

### Use DistributedDataParallel not DataParallel

PyTorch has two main models for training on multiple GPUs. The first, DataParallel (DP), splits a batch across multiple GPUs. But this also means that the model has to be copied to each GPU and once gradients are calculated on GPU 0, they must be synced to the other GPUs.

That’s a lot of GPU transfers which are expensive! Instead, DistributedDataParallel (DDP)creates a siloed copy of the model on each GPU (in its own process), and makes only a portion of the data available to that GPU. Then its like having N independent models training, except that once each one calculates the gradients, they all sync gradients across models… this means we only transfer data across GPUs once during each batch.

### Profile your code

Pytorch lightning has a profiler built in.

<https://pytorch.org/tutorials/recipes/recipes/profiler_recipe.html>

<https://zdevito.github.io/2022/12/09/memory-traces.html>

### Use auto mixed precision

Forward and backward pass in 16-bit precision, convert gradients to 16-bit and upgrade weights in 32-bit precision.

This is another way to speed up training which we don’t see many people using. In 16-bit training parts of your model and your data go from 32-bit numbers to 16-bit numbers. This has a few advantages:

- You use half the memory (which means you can double batch size and cut training time in half).
- Certain GPUs (V100, 2080Ti) give you automatic speed-ups (3x-8x faster) because they are optimized for 16-bit computations.

Can make your code run three times faster.

<https://pytorch.org/docs/stable/amp.html>

### Static graphs

Pytorch 2.0 added torch.compile()

```python
model = torch.compile(model)  # NEW
```

the compile API converts your model into an intermediate computation graph (an FX graph) which it then compiles into low-level compute kernels in a manner that is optimal for the underlying training accelerator, using techniques such as kernel fusion and out-of-order execution (see here for more details).

### Lightning Fabric

Lightning Fabric is a lightweight Pytorch Lightning extension: <https://lightning.ai/docs/fabric/stable/>

### More tips

- <https://efficientdl.com/faster-deep-learning-in-pytorch-a-guide/>

## Torchmetrics

Remove boilerplate code using torchmetrics to accumulate batch metrics over an epoch.

<https://sebastianraschka.com/blog/2022/torchmetrics.html>

## Visualize Layer Activations

- [How to visualize convolutional features in 40 lines of code](https://towardsdatascience.com/how-to-visualize-convolutional-features-in-40-lines-of-code-70b7d87b0030)

## MultiGPU

- [Training Neural Nets on Larger Batches: Practical Tips for 1-GPU, Multi-GPU & Distributed setups](https://medium.com/huggingface/training-larger-batches-practical-tips-on-1-gpu-multi-gpu-distributed-setups-ec88c3e51255)

## PyTorch internals

- [PyTorch internals](http://blog.ezyang.com/2019/05/pytorch-internals/)
- <http://blog.christianperone.com/2018/03/pytorch-internal-architecture-tour/>

## Debugging

Debugging PyTorch memory use with snapshots: <https://zdevito.github.io/2022/08/16/memory-snapshots.html>
