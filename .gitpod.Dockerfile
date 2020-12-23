FROM gitpod/workspace-full

# Install custom tools, runtimes, etc.
# For example "bastet", a command-line tetris clone:
# RUN brew install bastet
#
# More information: https://www.gitpod.io/docs/config-docker/

RUN apt-add-repository -y ppa:rael-gc/rvm
RUN apt-get update
RUN apt-get install rvm
RUN rvm install ruby-2.7.1
