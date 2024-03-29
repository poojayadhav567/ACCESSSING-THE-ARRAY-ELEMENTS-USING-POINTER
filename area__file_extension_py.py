{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "area _file_extension.py",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyPUnKM5K2yZOoliw7FMzdcL",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
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
        "<a href=\"https://colab.research.google.com/github/poojayadhav567/ACCESSSING-THE-ARRAY-ELEMENTS-USING-POINTER/blob/main/area__file_extension_py.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "FmS_RhKohFxt",
        "outputId": "0db612cf-83fd-405b-9017-957c277e0592"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "computing the area of the circle\n",
            "enter the radius of the circle :3\n",
            "The radius of the circle is : 3.0\n",
            "The area of the circle is:  28.274333882308138\n"
          ]
        }
      ],
      "source": [
        "import math as m\n",
        "print(\"computing the area of the circle\")\n",
        "rad=float(input(\"Enter the radius of the circle :\" ))\n",
        "area=m.pi*rad*rad\n",
        "print(\"The radius of the circle is :\",rad)\n",
        "print(\"The area of the circle is: \",area)"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "filename = input(\"Input the Filename: \")\n",
        "f_extns = filename.split(\".\")\n",
        "print (\"The extension of the file is : \" + repr(f_extns[-1]))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "QErxkSlJD_ze",
        "outputId": "a5e5bb84-d715-4f84-9136-4f57b21f597d"
      },
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Input the Filename: abc.py\n",
            "The extension of the file is : 'py'\n"
          ]
        }
      ]
    }
  ]
}