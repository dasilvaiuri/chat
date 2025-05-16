{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMO6RgX31uUUE34QitBw+fU",
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
        "<a href=\"https://colab.research.google.com/github/dasilvaiuri/chat/blob/main/aluraimersao.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install google-genai"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "rb47I7buR8ED",
        "outputId": "f57eca11-2ae6-47c7-e03d-19d9eb24df00"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: google-genai in /usr/local/lib/python3.11/dist-packages (1.15.0)\n",
            "Requirement already satisfied: anyio<5.0.0,>=4.8.0 in /usr/local/lib/python3.11/dist-packages (from google-genai) (4.9.0)\n",
            "Requirement already satisfied: google-auth<3.0.0,>=2.14.1 in /usr/local/lib/python3.11/dist-packages (from google-genai) (2.38.0)\n",
            "Requirement already satisfied: httpx<1.0.0,>=0.28.1 in /usr/local/lib/python3.11/dist-packages (from google-genai) (0.28.1)\n",
            "Requirement already satisfied: pydantic<3.0.0,>=2.0.0 in /usr/local/lib/python3.11/dist-packages (from google-genai) (2.11.4)\n",
            "Requirement already satisfied: requests<3.0.0,>=2.28.1 in /usr/local/lib/python3.11/dist-packages (from google-genai) (2.32.3)\n",
            "Requirement already satisfied: websockets<15.1.0,>=13.0.0 in /usr/local/lib/python3.11/dist-packages (from google-genai) (15.0.1)\n",
            "Requirement already satisfied: typing-extensions<5.0.0,>=4.11.0 in /usr/local/lib/python3.11/dist-packages (from google-genai) (4.13.2)\n",
            "Requirement already satisfied: idna>=2.8 in /usr/local/lib/python3.11/dist-packages (from anyio<5.0.0,>=4.8.0->google-genai) (3.10)\n",
            "Requirement already satisfied: sniffio>=1.1 in /usr/local/lib/python3.11/dist-packages (from anyio<5.0.0,>=4.8.0->google-genai) (1.3.1)\n",
            "Requirement already satisfied: cachetools<6.0,>=2.0.0 in /usr/local/lib/python3.11/dist-packages (from google-auth<3.0.0,>=2.14.1->google-genai) (5.5.2)\n",
            "Requirement already satisfied: pyasn1-modules>=0.2.1 in /usr/local/lib/python3.11/dist-packages (from google-auth<3.0.0,>=2.14.1->google-genai) (0.4.2)\n",
            "Requirement already satisfied: rsa<5,>=3.1.4 in /usr/local/lib/python3.11/dist-packages (from google-auth<3.0.0,>=2.14.1->google-genai) (4.9.1)\n",
            "Requirement already satisfied: certifi in /usr/local/lib/python3.11/dist-packages (from httpx<1.0.0,>=0.28.1->google-genai) (2025.4.26)\n",
            "Requirement already satisfied: httpcore==1.* in /usr/local/lib/python3.11/dist-packages (from httpx<1.0.0,>=0.28.1->google-genai) (1.0.9)\n",
            "Requirement already satisfied: h11>=0.16 in /usr/local/lib/python3.11/dist-packages (from httpcore==1.*->httpx<1.0.0,>=0.28.1->google-genai) (0.16.0)\n",
            "Requirement already satisfied: annotated-types>=0.6.0 in /usr/local/lib/python3.11/dist-packages (from pydantic<3.0.0,>=2.0.0->google-genai) (0.7.0)\n",
            "Requirement already satisfied: pydantic-core==2.33.2 in /usr/local/lib/python3.11/dist-packages (from pydantic<3.0.0,>=2.0.0->google-genai) (2.33.2)\n",
            "Requirement already satisfied: typing-inspection>=0.4.0 in /usr/local/lib/python3.11/dist-packages (from pydantic<3.0.0,>=2.0.0->google-genai) (0.4.0)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.11/dist-packages (from requests<3.0.0,>=2.28.1->google-genai) (3.4.2)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.11/dist-packages (from requests<3.0.0,>=2.28.1->google-genai) (2.4.0)\n",
            "Requirement already satisfied: pyasn1<0.7.0,>=0.6.1 in /usr/local/lib/python3.11/dist-packages (from pyasn1-modules>=0.2.1->google-auth<3.0.0,>=2.14.1->google-genai) (0.6.1)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#importando a chave criada no google Ai Studio\n",
        "import os\n",
        "\n",
        "from google.colab import userdata\n",
        "os.environ[\"GOOGLE_API_KEY\"] = userdata.get('GOOGLE_API_KEY')"
      ],
      "metadata": {
        "id": "OviboelPSrp9"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from google import genai\n",
        "\n",
        "client = genai.Client()"
      ],
      "metadata": {
        "id": "xxpuM0lZTPjs"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "for model in client.models.list():\n",
        "  print(model.name)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "M9MlbaNMTqln",
        "outputId": "3bcc7bb3-5a5a-4e73-96bb-5174b2018aae"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "models/chat-bison-001\n",
            "models/text-bison-001\n",
            "models/embedding-gecko-001\n",
            "models/gemini-1.0-pro-vision-latest\n",
            "models/gemini-pro-vision\n",
            "models/gemini-1.5-pro-latest\n",
            "models/gemini-1.5-pro-001\n",
            "models/gemini-1.5-pro-002\n",
            "models/gemini-1.5-pro\n",
            "models/gemini-1.5-flash-latest\n",
            "models/gemini-1.5-flash-001\n",
            "models/gemini-1.5-flash-001-tuning\n",
            "models/gemini-1.5-flash\n",
            "models/gemini-1.5-flash-002\n",
            "models/gemini-1.5-flash-8b\n",
            "models/gemini-1.5-flash-8b-001\n",
            "models/gemini-1.5-flash-8b-latest\n",
            "models/gemini-1.5-flash-8b-exp-0827\n",
            "models/gemini-1.5-flash-8b-exp-0924\n",
            "models/gemini-2.5-pro-exp-03-25\n",
            "models/gemini-2.5-pro-preview-03-25\n",
            "models/gemini-2.5-flash-preview-04-17\n",
            "models/gemini-2.5-flash-preview-04-17-thinking\n",
            "models/gemini-2.5-pro-preview-05-06\n",
            "models/gemini-2.0-flash-exp\n",
            "models/gemini-2.0-flash\n",
            "models/gemini-2.0-flash-001\n",
            "models/gemini-2.0-flash-exp-image-generation\n",
            "models/gemini-2.0-flash-lite-001\n",
            "models/gemini-2.0-flash-lite\n",
            "models/gemini-2.0-flash-preview-image-generation\n",
            "models/gemini-2.0-flash-lite-preview-02-05\n",
            "models/gemini-2.0-flash-lite-preview\n",
            "models/gemini-2.0-pro-exp\n",
            "models/gemini-2.0-pro-exp-02-05\n",
            "models/gemini-exp-1206\n",
            "models/gemini-2.0-flash-thinking-exp-01-21\n",
            "models/gemini-2.0-flash-thinking-exp\n",
            "models/gemini-2.0-flash-thinking-exp-1219\n",
            "models/learnlm-2.0-flash-experimental\n",
            "models/gemma-3-1b-it\n",
            "models/gemma-3-4b-it\n",
            "models/gemma-3-12b-it\n",
            "models/gemma-3-27b-it\n",
            "models/embedding-001\n",
            "models/text-embedding-004\n",
            "models/gemini-embedding-exp-03-07\n",
            "models/gemini-embedding-exp\n",
            "models/aqa\n",
            "models/imagen-3.0-generate-002\n",
            "models/gemini-2.0-flash-live-001\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "modelo = \"models/gemini-2.0-flash\"\n",
        "response = client.models.generate_content(model=modelo, contents=\"Qual a empresa responsável pelo Gemini?\")"
      ],
      "metadata": {
        "id": "hK6KnT-NUO3D"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "response.text"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "id": "q8PA2ebSUpU2",
        "outputId": "84da5d8e-5c95-443a-8d2f-658ed64f309a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'A empresa responsável pelo Gemini é o **Google**. O Gemini é o modelo de linguagem multimodal mais recente e avançado do Google AI.\\n'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 17
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from google.genai import types\n",
        "\n",
        "chat_config = types.GenerateContentConfig(system_instruction=\"Você é um assistente pessoal e você sempre responde de forma sucinta.\")\n",
        "chat = client.chats.create(model=modelo, config=chat_config)\n",
        "#resposta = chat.send_message(\"Qual a empresa responsável pelo Gemini?\")\n",
        "#resposta.text"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "id": "xDtqbF5sV6L7",
        "outputId": "06d60688-47d5-4294-aebb-6873f414aabd"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'Google.'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 22
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "prompt = input(\"Digite sua pergunta: \")\n",
        "\n",
        "while prompt\t!= \"sair\":\n",
        "  resposta = chat.send_message(prompt)\n",
        "  print(resposta.text)\n",
        "  prompt = input(\"Digite sua pergunta: \")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "HyvPXAwbWrm0",
        "outputId": "3c4c80d5-9416-4196-ca7f-faf47f0ab297"
      },
      "execution_count": null,
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Digite sua pergunta: oi\n",
            "Olá!\n",
            "\n",
            "Digite sua pergunta: o que eu posso fazer?\n",
            "Como posso te ajudar hoje?\n",
            "\n",
            "Digite sua pergunta: o que você pode fazer?\n",
            "Posso responder a perguntas, gerar textos criativos, traduzir idiomas, resumir textos e muito mais.\n",
            "\n",
            "Digite sua pergunta: gosto de você\n",
            "Obrigado! Fico feliz em ajudar.\n",
            "\n",
            "Digite sua pergunta: fim\n",
            "OK. Até a próxima!\n",
            "\n",
            "Digite sua pergunta: sair\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "chat.get_history"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 186
        },
        "id": "HOEP5LF7XYDM",
        "outputId": "56c3df1d-5765-4c1f-9217-24214d980d59"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<bound method _BaseChat.get_history of <google.genai.chats.Chat object at 0x7afc87f031d0>>"
            ],
            "text/html": [
              "<div style=\"max-width:800px; border: 1px solid var(--colab-border-color);\"><style>\n",
              "      pre.function-repr-contents {\n",
              "        overflow-x: auto;\n",
              "        padding: 8px 12px;\n",
              "        max-height: 500px;\n",
              "      }\n",
              "\n",
              "      pre.function-repr-contents.function-repr-contents-collapsed {\n",
              "        cursor: pointer;\n",
              "        max-height: 100px;\n",
              "      }\n",
              "    </style>\n",
              "    <pre style=\"white-space: initial; background:\n",
              "         var(--colab-secondary-surface-color); padding: 8px 12px;\n",
              "         border-bottom: 1px solid var(--colab-border-color);\"><b>google.genai.chats._BaseChat.get_history</b><br/>def get_history(curated: bool=False) -&gt; list[Content]</pre><pre class=\"function-repr-contents function-repr-contents-collapsed\" style=\"\"><a class=\"filepath\" style=\"display:none\" href=\"#\">/usr/local/lib/python3.11/dist-packages/google/genai/chats.py</a>Returns the chat history.\n",
              "\n",
              "Args:\n",
              "    curated: A boolean flag indicating whether to return the curated (valid)\n",
              "      history or the comprehensive (all turns) history. Defaults to False\n",
              "      (returns the comprehensive history).\n",
              "\n",
              "Returns:\n",
              "    A list of `Content` objects representing the chat history.</pre>\n",
              "      <script>\n",
              "      if (google.colab.kernel.accessAllowed && google.colab.files && google.colab.files.view) {\n",
              "        for (const element of document.querySelectorAll('.filepath')) {\n",
              "          element.style.display = 'block'\n",
              "          element.onclick = (event) => {\n",
              "            event.preventDefault();\n",
              "            event.stopPropagation();\n",
              "            google.colab.files.view(element.textContent, 178);\n",
              "          };\n",
              "        }\n",
              "      }\n",
              "      for (const element of document.querySelectorAll('.function-repr-contents')) {\n",
              "        element.onclick = (event) => {\n",
              "          event.preventDefault();\n",
              "          event.stopPropagation();\n",
              "          element.classList.toggle('function-repr-contents-collapsed');\n",
              "        };\n",
              "      }\n",
              "      </script>\n",
              "      </div>"
            ]
          },
          "metadata": {},
          "execution_count": 25
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [],
      "metadata": {
        "id": "AVemEBKFV5_k"
      }
    }
  ]
}