## Solsea NFT Explorer
[![Solsea NFT Explore](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/devincapriola/solsea-nft-explore/main/app.py)

## :package: Download and Setup
1. [Fork](https://help.github.com/articles/fork-a-repo/) this repository to your own GitHub account and then [clone](https://help.github.com/articles/cloning-a-repository/) it to your local device. <br /> 
`$ git clone https://github.com/devincapriola/SOLSEA-NFT-EXPLORE.git`

2. Go to [docs.docker.com/get-docker](https://docs.docker.com/get-docker/) and click on the installer that matches your operating system and follow the installation instructions. Docker is available for macOS, Windows, and Linux computers. 

## Quick Start
1. install the requirements. <br /> 
`$ python -m pip install -r requirements.txt`
2. running streamlit. <br /> 
`$ streamlit run app.py`

### Using Docker
Docker is an open platform for developing, shipping, and running applications. Docker enables you to separate your applications from your infrastructure so you can deliver software quickly. With Docker, you can manage your infrastructure in the same ways you manage your applications. By taking advantage of Docker’s methodologies for shipping, testing, and deploying code quickly, you can significantly reduce the delay between writing code and running it in production.

`$ docker build -t app:latest .`

`$ docker run -p 8501:8501 app:latest`

We supplied -p argument to specify what port on the host machine to map the port the app is listening on in the container. Now you can access the app from your browser on http://localhost:8501.
<br />

### :handshake: Contributing
Contributions, issues and feature requests are welcome!<br />Feel free to check [issues page](https://github.com/devincapriola/SOLSEA-NFT-EXPLORE/issues).

### Show your support
Give a :star: if this project helped you!
