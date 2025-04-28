#!/bin/sh

TEMP_DIR=temp

echo "Starting deb package build"

echo "Making temporary directory tree"
mkdir -p $TEMP_DIR
mkdir -p $TEMP_DIR/etc/systemd/system/
mkdir -p $TEMP_DIR/usr/local/bin/
mkdir -p $TEMP_DIR/DEBIAN

echo "Copying control file for DEBIAN/"
cp bin/DEBIAN/control $TEMP_DIR/DEBIAN/

# adding executable file permissions to preinst, postinst, prerm, postrm
chmod +x bin/DEBIAN/preinst
chmod +x bin/DEBIAN/postinst
chmod +x bin/DEBIAN/prerm
chmod +x bin/DEBIAN/postrm

echo "Copying preinst, postinst, prerm, and postrm for DEBIAN/"
cp bin/DEBIAN/preinst $TEMP_DIR/DEBIAN/
cp bin/DEBIAN/postinst $TEMP_DIR/DEBIAN/
cp bin/DEBIAN/prerm $TEMP_DIR/DEBIAN/
cp bin/DEBIAN/postrm $TEMP_DIR/DEBIAN/

echo "Copying python files and mypl file into place"
cp mypl.py $TEMP_DIR/usr/local/bin/
cp mypl_token.py $TEMP_DIR/usr/local/bin/
cp mypl_lexer.py $TEMP_DIR/usr/local/bin/
cp mypl_iowrapper.py $TEMP_DIR/usr/local/bin/
cp mypl_error.py $TEMP_DIR/usr/local/bin/
cp hw1_example.mypl $TEMP_DIR/usr/local/bin/

echo "Copying service file into place"
cp bin/mypl-hw1.service $TEMP_DIR/etc/systemd/system/

echo "Building deb file"
# if all good, outputs temp.deb
dpkg-deb --root-owner-group --build $TEMP_DIR
mv $TEMP_DIR.deb mypl-hw1-v2.0.0.deb


echo "Complete."