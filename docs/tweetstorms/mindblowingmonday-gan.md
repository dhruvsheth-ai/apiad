Hey, today is #MindblowingMonday 🤯!

A day to share with you amazing things from every corner of Computer Science.

Today I want to talk about Generative Adversarial Networks 👇

---

🍬 But let's begin with some eye candy. 

Take a look at this mind-blowing 2-minute video and, if you like it, then read on, I'll tell you a couple of things about it...

<iframe width="560" height="315" src="https://www.youtube.com/embed/9QuDh3W3lOY" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<!-- https://youtu.be/9QuDh3W3lOY -->

---

Generative Adversarial Networks (GAN) have taken by surprise the machine learning world with their uncanny ability to generate hyper-realistic examples of human faces, cars, landscapes, and a lot of other stuff, as you just saw.

Want to know how they work? 👇

---

There are many variants, but the core idea is to have 2️⃣ neural networks: 

- ⚙️ a generator network
- ⚖️ a discriminator network

Both networks are connected in a sort of adversarial game, where each is trying to outperform the other.

---

⚖️ The discriminator is a regular neural network whose job is to determine if a specific sample (say, an image of a face) is real or generated.

This network's architecture depends on the classification, as usual, e.g., lots of convolutions and pooling for images.

---

⚙️ The generator network is a decoder network, whose job is to transform an input of random values to whatever you want to generate.

In images, for example, you'll have deconvolution layers and upsampling, i.e., the "reverse" of an image classification network.

---

🎩 All the magic happens in the training.

You train the discriminator by alternatively showing it real and generated images, and minimizing some classification loss (e.g., binary cross-entropy).

---

The generator is trained to try and "fool" the discriminator. But this is not easy, so the trick involves letting it "see" the discriminator loss function.

💡 It's like showing you my brain while you perform a magic trick, so you can understand how I can be fooled best.

---

This is the basic idea, but the devil is in the details. Two common problems with GANs are:

1️⃣ The discriminator learns much faster, so the generator never gets a chance to catch up.

2️⃣ The generator gets complacent and just produces the same good examples over and over.

---

🤔 Finally, beyond the technical challenges, the possibility of suddenly creating very realistic content opens a can of worms of ethical issues such as disinformation.

But technology itself is neither good nor bad, it is just a tool. It's on ourselves what we do with it.

---

As usual, if you like this topic, have any questions, or just want to discuss, reply in this thread or @ me any time. I'll be listening.

This thread is available in plain format here, forever:
<https://apiad.net/tweetstorms/mindblowingmonday-gan/>

---

Stay curious:

- 🎥 <https://apiad.net/to/#gan-video>
- 🏫 <https://deepgenerativemodels.github.io/>
- 📘 <https://www.manning.com/books/gans-in-action>
- 📃 <https://arxiv.org/abs/1710.07035>
- 💻 <https://github.com/nightrome/really-awesome-gan>

---
