#!bin/bash

echo "installing packages for dev environment"

package1="php5"

for package in package1; do
    dpkg -s "$package1" >/dev/null 2>&1 && {
        echo "$package1 is installed."
    } || {
          apt-get install $package1
    }
done

package2="npm"

for package in package2; do
    dpkg -s "$package2" >/dev/null 2>&1 && {
        echo "$package2 is installed."
    } || {
          apt-get install $package2
    }
done

package3="nodejs"

for package in package3; do
    dpkg -s "$package3" >/dev/null 2>&1 && {
        echo "$package3 is installed."
    } || {
         apt-get install $package3
    }
done

package4="mysql-server"

for package in package4; do
    dpkg -s "$package4" >/dev/null 2>&1 && {
        echo "$package4 is installed."
    } || {
         apt-get install $package4
    }
done

package5="postgresql"

for package in package5; do
    dpkg -s "$package5" >/dev/null 2>&1 && {
        echo "$package5 is installed."
    } || {
         apt-get install $package5
    }
done


