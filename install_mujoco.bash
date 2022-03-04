#!/bin/bash
wget https://github.com/deepmind/mujoco/releases/download/2.1.1/mujoco-2.1.1-linux-x86_64.tar.gz
tar -xf mujoco-2.1.1-linux-x86_64.tar.gz
mv mujoco-2.1.1 .mujoco
mv .mujoco ~
rm mujoco-2.1.1-linux-x86_64.tar.gz
