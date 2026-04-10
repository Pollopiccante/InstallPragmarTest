
# build package wheel, and use it while building container
echo "BUILD PACKAGE WHEEL"
cd .. && python3 -m build

echo "INSTALL"
pip uninstall -y PRAGMAR
ls
pip install --find-links=dist --no-index PRAGMAR

echo "CLEAR WHEEL FILES"
cd dist && rm ./*
