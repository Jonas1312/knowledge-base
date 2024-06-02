# Diffusion models

Succession of layers that try to predict the input in one step less noisy.

What we are trying to do is find the distribution that maximizes the likelihood of the data.

What we do in practice is to minimize the negative ELBO.

The important part about diffusion models is that this objective becomes tenable because of (1) the Markov assumption and (2) the fact that transitions are conditional Gaussians

if you forward diffuse and image and then reverse diffuse the result, you will very probably get a different image than the one you started at.

GANs are slower than diffusion models:

- False during inference
- True during training. Because the min max game is complex with the discriminator, it's hard to reach the equilibrium. For diffusion models, the output is straigthforward to learn and objective is obvious and clear.

What conditions do diffusion model architectures need to fulfill?

- Input dimension == output dimension

## More

- <https://keras.io/guides/keras_cv/generate_images_with_stable_diffusion/>
- <https://lilianweng.github.io/posts/2021-07-11-diffusion-models/>
- <https://old.reddit.com/r/MachineLearning/comments/u7lv35/d_why_is_the_diffution_model_so_powerful_but_the/>
- <https://towardsdatascience.com/diffusion-models-made-easy-8414298ce4da>
- <https://yang-song.github.io/blog/2021/score/>
- <https://www.assemblyai.com/blog/diffusion-models-for-machine-learning-introduction/>
- <https://benanne.github.io/2022/01/31/diffusion.html>
- <https://benanne.github.io/2022/05/26/guidance.html>
- <https://www.chenyang.co/diffusion.html>
- <https://andrewkchan.dev/posts/diffusion.html>
