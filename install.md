# essential
```
sudo apt-get update && sudo apt-get upgrade  

sudo apt-get install \
make cmake build-essential ruby \
openjdk-11-jdk pkg-config libncurses-dev libncurses5 
ibusb-1.0-0-dev autotools-dev bc flex bison libssl-dev libelf-dev \
dwarves debhelper libxrender1 wget ca-certificates tar \
g++ git autogen graphviz libboost-dev libboost-test-dev libgtest-dev libtool \
python3-sip-dev doxygen python3-sphinx pkg-config python3-sphinx-rtd-theme
```

# arm-none-eabi compiler
```
# arm-none-eabi compiler install.sh
wget https://developer.arm.com/-/media/Files/downloads/gnu-rm/10.3-2021.10/gcc-arm-none-eabi-10.3-2021.10-x86_64-linux.tar.bz2

sudo tar xjf gcc-arm-none-eabi-10.3-2021.10-x86_64-linux.tar.bz2 -C /usr/share/

sudo ln -s /usr/share/gcc-arm-none-eabi-10.3-2021.10/bin/arm-none-eabi-gcc /usr/bin/arm-none-eabi-gcc
sudo ln -s /usr/share/gcc-arm-none-eabi-10.3-2021.10/bin/arm-none-eabi-g++ /usr/bin/arm-none-eabi-g++
sudo ln -s /usr/share/gcc-arm-none-eabi-10.3-2021.10/bin/arm-none-eabi-gdb /usr/bin/arm-none-eabi-gdb
sudo ln -s /usr/share/gcc-arm-none-eabi-10.3-2021.10/bin/arm-none-eabi-objcopy /usr/bin/arm-none-eabi-objcopy
sudo ln -s /usr/share/gcc-arm-none-eabi-10.3-2021.10/bin/arm-none-eabi-size /usr/bin/arm-none-eabi-size
sudo ln -s /usr/share/gcc-arm-none-eabi-10.3-2021.10/bin/arm-none-eabi-nm /usr/bin/arm-none-eabi-nm
sudo ln -s /usr/share/gcc-arm-none-eabi-10.3-2021.10/bin/arm-none-eabi-objdump /usr/bin/arm-none-eabi-objdump
```

# googletest
```
#google test install.sh

git clone https://github.com/google/googletest.git
cd googletest
cmake -Bbuild
make -C build
sudo make install -C build
cd ..
```

# cubemx
```
# download file : https://www.st.com/content/ccc/resource/technical/software/sw_development_suite/group0/20/84/df/4d/db/30/44/b3/stm32cubemx-lin-v6-8-1/files/stm32cubemx-lin-v6-8-1.zip/jcr:content/translations/en.stm32cubemx-lin-v6-8-1.zip

# cubemx install.sh
unzip en.stm32cubemx-lin-v6-8-1.zip
sudo ./SetupSTM32CubeMX-6.8.1
echo "alias cubemx='/usr/local/STMicroelectronics/STM32Cube/STM32CubeMX/STM32CubeMX'" >> ~/.bashrc
source ~/.bashrc
```

# cubeide (stlink)
```
# download file : https://www.st.com/content/ccc/resource/technical/software/sw_development_suite/group0/30/a8/7a/1c/24/19/42/c0/stm32cubeide-lnx/files/st-stm32cubeide_1.12.1_16088_20230420_1057_amd64.sh.zip/jcr:content/translations/en.st-stm32cubeide_1.12.1_16088_20230420_1057_amd64.sh.zip

# cubeide (stlink) install.sh
unzip en.st-stm32cubeide_1.12.1_16088_20230420_1057_amd64.sh.zip
sudo ./en.st-stm32cubeide_1.12.1_16088_20230420_1057_amd64.sh
echo "alias cubeide='/opt/st/stm32cubeide_1.12.1/stm32cubeide'" >> ~/.bashrc
source ~/.bashrc
```

# usbipd
## window
```
# download file : https://objects.githubusercontent.com/github-production-release-asset-2e65be/305202189/ef768600-9d7a-409f-bffc-fc3af041f45d?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIWNJYAX4CSVEH53A%2F20230511%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230511T070644Z&X-Amz-Expires=300&X-Amz-Signature=9c4d94dc8416773ef65df3f37eacc8d3b15b2c7ebd678f4b35d25963f3a90144&X-Amz-SignedHeaders=host&actor_id=84785986&key_id=0&repo_id=305202189&response-content-disposition=attachment%3B%20filename%3Dusbipd-win_2.4.1.msi&response-content-type=application%2Foctet-stream
```
## wsl
```
# wsl install.sh
sudo apt install linux-tools-generic hwdata
sudo update-alternatives --install /usr/local/bin/usbip usbip /usr/lib/linux-tools/*-generic/usbip 20
```

#  libserial
```
# download file
git clone https://github.com/crayzeewulf/libserial.git
```
## update CMakeLists.txt
```
update gtest version
   EXTERNALPROJECT_ADD(GTestExternal
     PREFIX             "${GTEST_PREFIX}"
     URL https://github.com/google/googletest/archive/refs/tags/v1.13.0.tar.gz
     URL_HASH SHA1=bfa4b5131b6eaac06962c251742c96aab3f7aa78
     INSTALL_COMMAND ""
     )
update GTEST_LOCATION
   SET(GTEST_LOCATION "${GTEST_PREFIX}/src/GTestExternal-build/lib")
```
```
# libserial install.sh
./compile
sudo make -C install
```