#!/bin/bash
set -euxo pipefail

export DEBIAN_FRONTEND=noninteractive

apt-get update -y
apt-get upgrade -y
apt-get install -y curl git tmux ufw unzip build-essential ca-certificates

# Node.js 20 LTS (needed for the Codex CLI)
curl -fsSL https://deb.nodesource.com/setup_20.x | bash -
apt-get install -y nodejs

# OpenAI Codex CLI
npm install -g @openai/codex

# Firewall: SSH only, deny everything else by default
ufw allow OpenSSH
ufw --force enable

# Convenience: make the default user's shell start tmux-friendly
echo 'alias ll="ls -la"' >> /home/ubuntu/.bashrc

touch /home/ubuntu/.codex-remote-ready
chown ubuntu:ubuntu /home/ubuntu/.codex-remote-ready
