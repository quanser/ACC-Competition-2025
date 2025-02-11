#!/bin/sh

#
# Script to add the Quanser repository to the APT sources list.
#
# Copyright (c) 2022 Quanser Inc.

# Get the public key
wget --no-cache https://qrepoprivate.blob.core.windows.net/keys/Quanser.pub

# Get the configuration files
wget --no-cache https://qrepoprivate.blob.core.windows.net/debian/prerelease/config/99-quanser -O /etc/apt/preferences.d/99-quanser
wget --no-cache https://qrepoprivate.blob.core.windows.net/debian/prerelease/config/quanser.sources -O /etc/apt/sources.list.d/quanser.sources

# Add the public key for the repository
gpg --dearmor --homedir /root --output /usr/share/keyrings/Quanser.gpg Quanser.pub
rm Quanser.pub