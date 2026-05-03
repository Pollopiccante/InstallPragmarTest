
# build package wheel, and use it while building container
echo "BUILD PACKAGE WHEEL"
cd .. && pip install --no-index --find-links=wheels hatchling build && python3 -m build --no-isolation

echo "INSTALL"
pip uninstall -y PRAGMAR
pip install --find-links=dist --no-index PRAGMAR

echo "CLEAR WHEEL FILES"
cd dist && rm ./*
