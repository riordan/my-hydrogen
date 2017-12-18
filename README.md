# my-hydrogen
Personal configuration to use a consistent Hydrogen -> Atom environment with a Docker container

# Known Issues
Only works with Python3 kernels; not yet able to use kernels for Julia, R, Javascript.

# Instructions
1. Install Atom `$ brew cask install atom`
1. Install hydrogen `$ apm install hydrogen`
1. Install Docker `$ brew cask install docker`
1. Clone this repository `$ git clone git@github.com:riordan/my-hydrogen.git`
1. Set a new token for this machine. Copy `.env.sample` to `.env` and randomly generate a new token
1. Run the docker-compose `$ docker-compose up -d`
1. In Atom go to Settings->Hydrogen. Add this as a Gateway (but update the `token`): ```
[{
  "name": "Local jupyter-datascience-notebook",
  "options": {
    "baseUrl": "http://127.0.0.1:8855",
    "token": "my_secret_token"
  }
}]
```
1. In Atom go to Packages->Hydrogen->Connect to Remote Kernels and connect to this kernel.


To shut down, after the session's over, you can just destroy the kernel by switching to this folder and running `$ docker-compose down` or stop it by `$ docker-compose stop`.

# Background
This is just a Dockerfile for use with [Hydrogen's Remote Kernels](https://nteract.gitbooks.io/hydrogen/docs/Usage/RemoteKernelConnection.html) feature.
