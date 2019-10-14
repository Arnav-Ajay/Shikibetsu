{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Shikibetsu.ipynb",
      "provenance": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Arnav-Ajay/Shikibetsu/blob/master/Shikibetsu.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "276Y4EA3UlFo",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "import torch\n",
        "import torchvision.models as models\n",
        "\n",
        "#Siamese(2 parallel networks) Network which will take a pair of input images for comparison and \n",
        "#identifying whether they are from the same person or not.\n",
        "\n",
        "#The base network is GoogLeNet pre-trained on Imagenet database.\n",
        "basenet1 = models.googlenet(pretrained=True)\n",
        "basenet2 = models.googlenet(pretrained=True)"
      ],
      "execution_count": 0,
      "outputs": []
    }
  ]
}